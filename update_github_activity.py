import urllib.request
import json
from datetime import datetime
import os
import re

USERNAME = "knownassurajit"
TOKEN = os.environ.get("GITHUB_TOKEN")

def fetch_contributions():
    url = f"https://api.github.com/users/{USERNAME}/events/public"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

            contributions = []
            count = 0
            for event in data:
                if count >= 5:
                    break

                repo_name = event['repo']['name']
                event_type = event['type']
                date_str = event['created_at']

                dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
                formatted_date = dt.strftime("%B %d, %Y")

                desc = ""
                if event_type == "PushEvent":
                    commits = len(event['payload'].get('commits', []))
                    desc = f"Pushed {commits} commit(s) to"
                elif event_type == "CreateEvent":
                    ref_type = event['payload'].get('ref_type', 'repository')
                    desc = f"Created {ref_type} at"
                elif event_type == "PullRequestEvent":
                    action = event['payload'].get('action', 'opened')
                    desc = f"{action.capitalize()} pull request in"
                elif event_type == "IssuesEvent":
                    action = event['payload'].get('action', 'opened')
                    desc = f"{action.capitalize()} issue in"
                elif event_type == "WatchEvent":
                    desc = "Starred"
                elif event_type == "ForkEvent":
                    desc = "Forked"
                else:
                    continue

                contributions.append({
                    "description": desc,
                    "repo": repo_name,
                    "date": formatted_date,
                    "url": f"https://github.com/{repo_name}"
                })
                count += 1

            return contributions

    except Exception as e:
        print(f"Error fetching contributions: {e}")
        return []

def fetch_user_stats():
    url = f"https://api.github.com/users/{USERNAME}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.v3+json")
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return {
                "repos": data.get("public_repos", 0),
                "followers": data.get("followers", 0),
                "following": data.get("following", 0)
            }
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return {}

def update_readme():
    contributions = fetch_contributions()
    stats = fetch_user_stats()

    with open("README.md", "r") as f:
        content = f.read()

    contrib_md = "<ul>\n"
    if contributions:
        for c in contributions:
            contrib_md += f"  <li>📅 <b>{c['date']}</b>: {c['description']} <a href='{c['url']}'>{c['repo']}</a></li>\n"
    else:
        contrib_md += "  <li>No recent activity found.</li>\n"
    contrib_md += "</ul>"

    stats_md = ""
    if stats:
        stats_md = f"**{stats['repos']}** Public Repositories • **{stats['followers']}** Followers • **{stats['following']}** Following"

    if "<!-- CONTRIB_START -->" in content and "<!-- CONTRIB_END -->" in content:
        content = re.sub(r"<!-- CONTRIB_START -->.*?<!-- CONTRIB_END -->",
                         f"<!-- CONTRIB_START -->\n{contrib_md}\n<!-- CONTRIB_END -->",
                         content, flags=re.DOTALL)

    if "<!-- STATS_START -->" in content and "<!-- STATS_END -->" in content:
        content = re.sub(r"<!-- STATS_START -->.*?<!-- STATS_END -->",
                         f"<!-- STATS_START -->\n{stats_md}\n<!-- STATS_END -->",
                         content, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(content)

    print("README updated successfully!")

if __name__ == "__main__":
    update_readme()