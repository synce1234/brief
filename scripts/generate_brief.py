#!/usr/bin/env python3
"""Generate a daily morning brief and send it to Telegram."""

import os
import re
import requests
from datetime import datetime, timezone, timedelta
import anthropic

SEOUL_TZ = timezone(timedelta(hours=9))


def main():
    today = datetime.now(SEOUL_TZ).strftime("%Y-%m-%d")

    with open("CLAUDE.md") as f:
        focus_areas = f.read()

    print(f"Generating brief for {today}...")
    brief = generate_brief(today, focus_areas)

    save_brief(today, brief)
    send_to_telegram(brief)
    print("Done.")


def generate_brief(today: str, focus_areas: str) -> str:
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 15,
        }],
        messages=[{
            "role": "user",
            "content": (
                f"Today is {today} (Asia/Seoul, UTC+9). "
                "Generate a morning brief covering significant developments from the last 24 hours "
                "based on these focus areas:\n\n"
                f"{focus_areas}\n\n"
                "For each area, search for the latest news, papers, model releases, and announcements. "
                "Organize findings with a markdown header per focus area. "
                f"Start with '# Morning Brief — {today}'. "
                "If there are no notable developments in an area, state that briefly. "
                "Include source links where relevant."
            ),
        }],
    )

    return "".join(
        block.text for block in response.content if hasattr(block, "text")
    )


def save_brief(today: str, brief: str):
    os.makedirs("docs", exist_ok=True)
    path = f"docs/{today}-morning-brief.md"
    with open(path, "w") as f:
        f.write(brief)
    print(f"Saved to {path}")


def markdown_to_telegram_html(text: str) -> str:
    """Convert markdown to Telegram HTML (parse_mode=HTML)."""
    # Escape HTML special chars first (excluding intentional tags added below)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Headers → bold
    text = re.sub(r"^#{1,3} (.+)$", r"<b>\1</b>", text, flags=re.MULTILINE)
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    # Inline code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # Links — must restore & inside URLs
    text = re.sub(
        r"\[(.+?)\]\((.+?)\)",
        lambda m: f'<a href="{m.group(2).replace("&amp;", "&")}">{m.group(1)}</a>',
        text,
    )
    # Horizontal rules
    text = re.sub(r"^---+$", "─" * 20, text, flags=re.MULTILINE)
    return text


def send_to_telegram(text: str):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    html = markdown_to_telegram_html(text)

    # Telegram HTML message limit is 4096 characters
    for i in range(0, len(html), 4096):
        chunk = html[i: i + 4096]
        resp = requests.post(url, json={
            "chat_id": chat_id,
            "text": chunk,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        })
        resp.raise_for_status()


if __name__ == "__main__":
    main()
