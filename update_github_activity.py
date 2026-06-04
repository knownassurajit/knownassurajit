"""
Refreshes the profile README with live GitHub data and regenerates the
Atlassian-dark "Profile Overview" stat card.

Fixes over the previous version:
  * PushEvent payloads from /events/public carry no `commits`/`size` array,
    so the old "Pushed N commit(s)" always printed 0. We now derive the
    branch from `ref` and use payload `size` only when present.
  * Handles Delete/Create/Release/Fork/Issue-comment events instead of
    silently dropping them.
  * De-noises the feed: collapses consecutive identical actions on the same
    repo (automation tends to fire many near-identical events).
  * Emits assets/stat-overview.svg with the live repo/follower/following
    counts so the README shows a dynamic, on-brand card.
"""

import urllib.request
import json
from datetime import datetime, timezone
import os
import re

USERNAME = "knownassurajit"
TOKEN = os.environ.get("GITHUB_TOKEN")
API = "https://api.github.com"

# ---- Atlassian Design System (dark theme) tokens -------------------------
SURFACE = "#22272B"   # elevation.surface.raised
SURFACE_SUNK = "#1D2125"
BORDER = "#2C333A"     # color.border
TEXT = "#C7D1DB"       # color.text
TEXT_SUBTLE = "#9FADBC"  # color.text.subtle
TEXT_FAINT = "#8C9BAB"
ACCENT = "#0C66E4"     # color.background.brand.bold
ACCENT_TEXT = "#579DFF"  # color.text.brand


def _request(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", f"{USERNAME}-profile-bot")
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode())


def short_repo(full_name):
    """`owner/name` -> `name` for readability."""
    return full_name.split("/", 1)[-1]


def describe(event):
    """Return (icon, text) for a public event, or None to skip it."""
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
        return ("\U0001F4E6", f"{label} <code>{branch}</code> on <b>{repo}</b>")

    if etype == "PullRequestEvent":
        action = payload.get("action", "opened")
        num = payload.get("number")
        ref = f" #{num}" if num else ""
        return ("\U0001F500", f"{action.capitalize()} pull request{ref} in <b>{repo}</b>")

    if etype == "IssuesEvent":
        action = payload.get("action", "opened")
        return ("\U0001F4CC", f"{action.capitalize()} issue in <b>{repo}</b>")

    if etype == "IssueCommentEvent":
        return ("\U0001F4AC", f"Commented on an issue in <b>{repo}</b>")

    if etype == "CreateEvent":
        ref_type = payload.get("ref_type", "repository")
        return ("✨", f"Created {ref_type} in <b>{repo}</b>")

    if etype == "DeleteEvent":
        ref_type = payload.get("ref_type", "branch")
        return ("\U0001F5D1️", f"Deleted {ref_type} in <b>{repo}</b>")

    if etype == "ReleaseEvent":
        tag = payload.get("release", {}).get("tag_name", "")
        return ("\U0001F680", f"Released {tag} on <b>{repo}</b>".strip())

    if etype == "ForkEvent":
        return ("\U0001F374", f"Forked <b>{repo}</b>")

    if etype == "WatchEvent":
        return ("⭐", f"Starred <b>{repo}</b>")

    return None


def fetch_contributions(limit=5):
    try:
        data = _request(f"{API}/users/{USERNAME}/events/public")
    except Exception as e:
        print(f"Error fetching contributions: {e}")
        return []

    out, seen = [], None
    for event in data:
        described = describe(event)
        if not described:
            continue
        icon, text = described
        # collapse consecutive identical actions (automation noise)
        key = (event.get("type"), event.get("repo", {}).get("name"), text)
        if key == seen:
            continue
        seen = key

        dt = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        out.append({
            "icon": icon,
            "text": text,
            "date": dt.strftime("%b %d, %Y"),
            "repo_url": f"https://github.com/{event['repo']['name']}",
        })
        if len(out) >= limit:
            break
    return out


def fetch_user_stats():
    try:
        data = _request(f"{API}/users/{USERNAME}")
        return {
            "repos": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0),
        }
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return {}


def build_stat_card(stats):
    """Atlassian-dark 'Profile Overview' card with the live counts."""
    cols = [
        (stats.get("repos", 0), "REPOSITORIES"),
        (stats.get("followers", 0), "FOLLOWERS"),
        (stats.get("following", 0), "FOLLOWING"),
    ]
    w, h = 520, 150
    third = w / 3
    mono = "ui-monospace,'JetBrains Mono',SFMono-Regular,Menlo,monospace"
    sans = "'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
    updated = datetime.now(timezone.utc).strftime("%d %b %Y")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="GitHub profile overview">',
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="14" '
        f'fill="{SURFACE}" stroke="{BORDER}"/>',
        # accent rail
        f'<rect x="0.5" y="0.5" width="4" height="{h-1}" rx="2" fill="{ACCENT}"/>',
        # header
        f'<circle cx="30" cy="30" r="4" fill="{ACCENT_TEXT}"/>',
        f'<text x="44" y="34" font-family="{sans}" font-size="13" font-weight="600" '
        f'letter-spacing="2" fill="{TEXT_SUBTLE}">PROFILE OVERVIEW</text>',
        f'<text x="{w-22}" y="34" text-anchor="end" font-family="{mono}" font-size="11" '
        f'fill="{TEXT_FAINT}">@{USERNAME}</text>',
        f'<line x1="22" y1="50" x2="{w-22}" y2="50" stroke="{BORDER}"/>',
    ]
    for i, (value, label) in enumerate(cols):
        cx = third * i + third / 2
        if i > 0:
            x = third * i
            parts.append(
                f'<line x1="{x:.0f}" y1="70" x2="{x:.0f}" y2="124" stroke="{BORDER}"/>')
        parts.append(
            f'<text x="{cx:.0f}" y="104" text-anchor="middle" font-family="{mono}" '
            f'font-size="38" font-weight="700" fill="{TEXT}">{value}</text>')
        parts.append(
            f'<text x="{cx:.0f}" y="128" text-anchor="middle" font-family="{sans}" '
            f'font-size="11" font-weight="600" letter-spacing="1.5" '
            f'fill="{TEXT_FAINT}">{label}</text>')
    parts.append(
        f'<text x="{w-22}" y="{h-12}" text-anchor="end" font-family="{mono}" '
        f'font-size="10" fill="{TEXT_FAINT}">synced {updated} · GitHub API</text>')
    parts.append('</svg>')

    svg = "".join(parts)
    os.makedirs("assets", exist_ok=True)
    with open("assets/stat-overview.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Wrote assets/stat-overview.svg")


def render_activity(contributions):
    rows = "<table>\n  <tr>\n    <td>\n      <ul>\n"
    if contributions:
        for c in contributions:
            rows += (
                f"        <li>{c['icon']} <b>{c['date']}</b> &nbsp;"
                f"{c['text']} &nbsp;&middot;&nbsp; "
                f"<a href='{c['repo_url']}'>repo &#8599;</a></li>\n"
            )
    else:
        rows += "        <li>No recent public activity.</li>\n"
    rows += "      </ul>\n    </td>\n  </tr>\n</table>"
    return rows


def update_readme():
    contributions = fetch_contributions()
    stats = fetch_user_stats()

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    contrib_md = render_activity(contributions)
    content = re.sub(
        r"<!-- CONTRIB_START -->.*?<!-- CONTRIB_END -->",
        f"<!-- CONTRIB_START -->\n{contrib_md}\n<!-- CONTRIB_END -->",
        content, flags=re.DOTALL)

    if stats:
        build_stat_card(stats)
        stats_md = (
            f"`{stats['repos']}` repositories &nbsp;&middot;&nbsp; "
            f"`{stats['followers']}` followers &nbsp;&middot;&nbsp; "
            f"`{stats['following']}` following"
        )
        content = re.sub(
            r"<!-- STATS_START -->.*?<!-- STATS_END -->",
            f"<!-- STATS_START -->\n{stats_md}\n<!-- STATS_END -->",
            content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated successfully!")


if __name__ == "__main__":
    update_readme()
