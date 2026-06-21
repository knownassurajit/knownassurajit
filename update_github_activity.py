"""
Refreshes the profile README with live GitHub data and regenerates the
token-driven "Profile Overview" stat card.

  * PushEvent payloads from /events/public carry no `commits`/`size` array,
    so the old "Pushed N commit(s)" always printed 0. We now derive the
    branch from `ref` and use payload `size` only when present.
  * Handles Delete/Create/Release/Fork/Issue-comment events instead of
    silently dropping them.
  * De-noises the feed: collapses consecutive identical actions on the same
    repo (automation tends to fire many near-identical events).
  * Emits assets/stat-overview.svg and assets/stat-languages.svg with live
    counts from the GitHub API.
"""

import json
import os
import re
import ssl
import urllib.request
from collections import Counter
from datetime import datetime, timezone

from design_tokens import layout, token

from design_tokens import token

# Bypass SSL certificate verification issues on macOS python
ssl._create_default_https_context = ssl._create_unverified_context

USERNAME = "knownassurajit"
TOKEN = os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"

# ---- Shared profile design tokens ---------------------------------------
# These semantic aliases keep the stat card readable while sourcing every color
# from design_tokens.py, the profile asset source of truth.
SURFACE = token("surface")
SURFACE_VARIANT = token("surface_variant")
BORDER = token("outline")
TEXT = token("on_surface")
TEXT_SUBTLE = token("on_surface_variant")
TEXT_FAINT = token("on_surface_variant")
ACCENT = token("primary")
ACCENT_TEXT = token("primary")


def _request(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", f"{USERNAME}-profile-bot")
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def short_repo(full_name):
    return full_name.split("/", 1)[-1]


def describe(event):
    """Return action text for a public event, or None to skip it."""
    etype = event.get("type")
    payload = event.get("payload", {})
    repo = short_repo(event.get("repo", {}).get("name", ""))

    if etype == "PushEvent":
        branch = payload.get("ref", "").replace("refs/heads/", "") or "default"
        size = payload.get("size") or payload.get("distinct_size")
        if size:
            label = f"Pushed {size} commit{'s' if size != 1 else ''} to"
        else:
            label = "Pushed to"
        return f"{label} <code>{branch}</code> on <b>{repo}</b>"

    if etype == "PullRequestEvent":
        action = payload.get("action", "opened")
        num = payload.get("number")
        ref = f" #{num}" if num else ""
        return f"{action.capitalize()} pull request{ref} in <b>{repo}</b>"

    if etype == "IssuesEvent":
        action = payload.get("action", "opened")
        return f"{action.capitalize()} issue in <b>{repo}</b>"

    if etype == "IssueCommentEvent":
        return f"Commented on an issue in <b>{repo}</b>"

    if etype == "CreateEvent":
        ref_type = payload.get("ref_type", "repository")
        return f"Created {ref_type} in <b>{repo}</b>"

    if etype == "DeleteEvent":
        ref_type = payload.get("ref_type", "branch")
        return f"Deleted {ref_type} in <b>{repo}</b>"

    if etype == "ReleaseEvent":
        tag = payload.get("release", {}).get("tag_name", "")
        return f"Released {tag} on <b>{repo}</b>".strip()

    if etype == "ForkEvent":
        return f"Forked <b>{repo}</b>"

    if etype == "WatchEvent":
        return f"Starred <b>{repo}</b>"

    return None


def fetch_contributions(limit=5):
    try:
        data = _request(f"{API}/users/{USERNAME}/events/public")
    except Exception as e:
        print(f"Error fetching contributions: {e}")
        return []

    out, seen = [], None
    for event in data:
        text = describe(event)
        if not text:
            continue
        key = (event.get("type"), event.get("repo", {}).get("name"), text)
        if key == seen:
            continue
        seen = key

        dt = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        out.append({
            "text": text,
            "date": dt.strftime("%b %d, %Y"),
            "repo_url": f"https://github.com/{event['repo']['name']}",
        })
        if len(out) >= limit:
            break
    return out


def fetch_repos():
    try:
        return _request(f"{API}/users/{USERNAME}/repos?per_page=100&sort=updated")
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []


def top_languages(repos, n=5):
    counts = Counter(
        repo.get("language") for repo in repos if repo.get("language")
    )
    total = sum(counts.values()) or 1
    return [
        {"name": lang, "count": count, "pct": round(count / total * 100)}
        for lang, count in counts.most_common(n)
    ]


def fetch_extended_stats():
    try:
        user = _request(f"{API}/users/{USERNAME}")
        repos = fetch_repos()
        return {
            "repos": user.get("public_repos", 0),
            "followers": user.get("followers", 0),
            "following": user.get("following", 0),
            "stars": sum(r.get("stargazers_count", 0) for r in repos),
            "languages": top_languages(repos),
        }
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return {}


def _card_frame(w, h, title, aria_label):
    updated = datetime.now(timezone.utc).strftime("%d %b %Y")
    right = w - INSET
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" '
        f'viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid meet" '
        f'role="img" aria-label="{aria_label}">',
        f"<title>{title}</title>",
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" '
        f'rx="{CARD_RADIUS}" fill="{SURFACE}" stroke="{BORDER}"/>',
        f'<rect x="0.5" y="0.5" width="{layout("accent_rail_width")}" '
        f'height="{h - 1}" rx="2" fill="{ACCENT_RAIL}"/>',
        f'<circle cx="{INSET}" cy="32" r="4" fill="{ACCENT}"/>',
        f'<text x="{INSET + 16}" y="36" font-family="{SANS}" font-size="13" '
        f'font-weight="600" letter-spacing="2" fill="{TEXT_SUBTLE}">{title}</text>',
        f'<text x="{right}" y="36" text-anchor="end" font-family="{MONO}" '
        f'font-size="11" fill="{TEXT_SUBTLE}">@{USERNAME}</text>',
        f'<line x1="{INSET}" y1="56" x2="{right}" y2="56" stroke="{BORDER}"/>',
    ], right, updated


def build_stat_card(stats):
    """Token-driven 'Profile Overview' card with the live counts."""
    cols = [
        (stats.get("repos", 0), "REPOSITORIES"),
        (stats.get("followers", 0), "FOLLOWERS"),
        (stats.get("stars", 0), "STARS"),
        (stats.get("following", 0), "FOLLOWING"),
    ]
    w, h = CARD_W, CARD_H
    col_w = w / 4
    parts, right, updated = _card_frame(w, h, "PROFILE OVERVIEW", "GitHub profile overview")

    for i, (value, label) in enumerate(cols):
        cx = col_w * i + col_w / 2
        if i > 0:
            x = col_w * i
            parts.append(
                f'<line x1="{x:.0f}" y1="78" x2="{x:.0f}" y2="132" stroke="{BORDER}"/>'
            )
        parts.append(
            f'<text x="{cx:.0f}" y="111" text-anchor="middle" font-family="{MONO}" '
            f'font-size="38" font-weight="700" fill="{TEXT}">{value}</text>'
        )
        parts.append(
            f'<text x="{cx:.0f}" y="135" text-anchor="middle" font-family="{SANS}" '
            f'font-size="11" font-weight="600" letter-spacing="1.5" '
            f'fill="{TEXT_SUBTLE}">{label}</text>'
        )

    parts.append(
        f'<text x="{right}" y="{h - 24}" text-anchor="end" font-family="{MONO}" '
        f'font-size="10" fill="{TEXT_SUBTLE}">synced {updated} · GitHub API</text>'
    )
    parts.append("</svg>")

    os.makedirs("assets", exist_ok=True)
    with open("assets/stat-overview.svg", "w", encoding="utf-8") as f:
        f.write("".join(parts))
    print("Wrote assets/stat-overview.svg")


def build_language_card(languages):
    n = max(len(languages), 1)
    h = 56 + n * 16 + 28
    w = CARD_W
    parts, right, updated = _card_frame(w, h, "TOP LANGUAGES", "Top repository languages")

    if not languages:
        parts.append(
            f'<text x="{w / 2:.0f}" y="72" text-anchor="middle" font-family="{SANS}" '
            f'font-size="13" fill="{TEXT_SUBTLE}">No language data available</text>'
        )
    else:
        bar_left = INSET
        bar_right = right
        bar_width = bar_right - bar_left - 90
        y_start = 68
        row_h = 16

        for i, lang in enumerate(languages):
            y = y_start + i * row_h
            color = LANG_COLORS.get(lang["name"], ACCENT)
            fill_w = max(bar_width * lang["pct"] / 100, 4)
            parts.append(
                f'<text x="{bar_left}" y="{y}" font-family="{MONO}" font-size="11" '
                f'fill="{TEXT}">{lang["name"]}</text>'
            )
            parts.append(
                f'<rect x="{bar_left + 90}" y="{y - 9}" width="{fill_w:.0f}" '
                f'height="6" rx="3" fill="{color}" opacity="0.85"/>'
            )
            parts.append(
                f'<text x="{bar_right}" y="{y}" text-anchor="end" font-family="{MONO}" '
                f'font-size="10" fill="{TEXT_SUBTLE}">{lang["pct"]}%</text>'
            )

    parts.append(
        f'<text x="{right}" y="{h - 12}" text-anchor="end" font-family="{MONO}" '
        f'font-size="10" fill="{TEXT_SUBTLE}">synced {updated} · GitHub API</text>'
    )
    parts.append("</svg>")

    os.makedirs("assets", exist_ok=True)
    with open("assets/stat-languages.svg", "w", encoding="utf-8") as f:
        f.write("".join(parts))
    print("Wrote assets/stat-languages.svg")


def render_activity(contributions):
    rows = "<ul>\n"
    if contributions:
        for c in contributions:
            rows += (
                f"  <li><b>{c['date']}</b> &nbsp;{c['text']} &nbsp;&middot;&nbsp; "
                f"<a href='{c['repo_url']}'>repo</a></li>\n"
            )
    else:
        rows += "  <li>No recent public activity.</li>\n"
    rows += "</ul>"
    return rows


def update_readme():
    contributions = fetch_contributions()
    stats = fetch_extended_stats()

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    contrib_md = render_activity(contributions)
    content = re.sub(
        r"<!-- CONTRIB_START -->.*?<!-- CONTRIB_END -->",
        f"<!-- CONTRIB_START -->\n{contrib_md}\n<!-- CONTRIB_END -->",
        content,
        flags=re.DOTALL,
    )

    if stats:
        build_stat_card(stats)
        build_language_card(stats.get("languages", []))

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated successfully!")


if __name__ == "__main__":
    update_readme()
