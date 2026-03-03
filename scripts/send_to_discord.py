import os
import requests
from typing import List
import sys

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

author = os.environ.get("AUTHOR")
commit_message = os.environ.get("COMMIT_MESSAGE")
commit_sha = os.environ.get("COMMIT_SHA")
changed_files = os.environ.get("FILES")
repo = os.environ.get("REPO_NAME")

commit_link = (
    f"https://github.com/{author}/{repo}/commit/{commit_sha}" if commit_sha else "N/A"
)


embeds = []


def send_to_discord():
    if not WEBHOOK_URL or not changed_files:
        sys.exit(0)
    list_files = changed_files.split()

    for file in list_files:
        parts = file.split("/")

        if len(parts) < 2:
            continue

        title = parts[-1].split(".")[0]

        embed = {
            "title": f"📝 Solved `{title}`",
            "url": f"{commit_link}",
            "description": f"**Author:** {author}\n**Commit:** `{commit_message}`",
            "color": 0x347C1B,
            "fields": [
                {"name": "Scheme", "value": parts[0], "inline": True},
                {"name": "Topic", "value": parts[1], "inline": True},
                {"name": "File", "value": parts[-1], "inline": True},
            ],
            "footer": {"text": "NeetCode Daily Challenge 💡"},
        }

        embeds.append(embed)

    payload = {"content": "", "embeds": embeds}
    res = requests.post(
        WEBHOOK_URL,
        json=payload,
    )
    print(res.status_code, res.text)


send_to_discord()
