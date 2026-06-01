#!/usr/bin/env python3
"""Morning brief generator — 2-tier architecture.
Tier 1: Collect raw data from arXiv, HuggingFace, GitHub, Reddit, RSS feeds.
Tier 2: Claude synthesizes collected data into a brief (no web search needed).
"""

import os
import re
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

import anthropic
import requests
from bs4 import BeautifulSoup

SEOUL_TZ = timezone(timedelta(hours=9))
NOW = datetime.now(SEOUL_TZ)
NOW_UTC = NOW.astimezone(timezone.utc)
TODAY = NOW.strftime("%Y-%m-%d")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

RSS_FEEDS = {
    "Android Developers Blog":  "https://android-developers.googleblog.com/feeds/posts/default",
    "Google AI Blog":            "https://blog.google/technology/ai/rss/",
    "TechCrunch AI":             "https://techcrunch.com/category/artificial-intelligence/feed/",
    "AppsFlyer Blog":            "https://www.appsflyer.com/blog/feed/",
    "Sensor Tower Blog":         "https://sensortower.com/blog/rss.xml",
}

# Reddit subreddits polled via JSON API (no auth needed)
REDDIT_SUBS = [
    "MachineLearning",
    "LocalLLaMA",
    "androiddev",
    "gamedev",       # ads/IAP signal
]


# ── helpers ───────────────────────────────────────────────────────────────────

def _get(url: str, **kwargs):
    try:
        r = requests.get(url, timeout=15, headers=HEADERS, **kwargs)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"  [warn] {url}: {e}")
        return None


# ── Tier 1: data collection ───────────────────────────────────────────────────

def collect_arxiv(categories: list[str], keywords: list[str] | None = None,
                  max_results: int = 12) -> list[dict]:
    cat_q = "+OR+".join(f"cat:{c}" for c in categories)
    if keywords:
        kw_q = "+OR+".join(f"ti:{k}" for k in keywords)
        query = f"({cat_q})+AND+({kw_q})"
    else:
        query = cat_q

    url = (
        "https://export.arxiv.org/api/query"
        f"?search_query={query}"
        "&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={max_results}"
    )
    r = _get(url)
    if not r:
        return []

    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(r.text)
    except ET.ParseError as e:
        print(f"  [warn] arXiv XML parse: {e}")
        return []

    papers = []
    for entry in root.findall("a:entry", ns):
        pub_text = entry.find("a:published", ns).text
        pub_dt = datetime.fromisoformat(pub_text.replace("Z", "+00:00"))
        if (NOW_UTC - pub_dt.astimezone(timezone.utc)) > timedelta(hours=48):
            continue
        papers.append({
            "title": entry.find("a:title", ns).text.strip(),
            "summary": entry.find("a:summary", ns).text.strip()[:300],
            "url": entry.find("a:id", ns).text.strip(),
            "published": pub_text,
        })
    return papers


def collect_huggingface_papers() -> list[dict]:
    r = _get(f"https://huggingface.co/api/daily_papers?date={TODAY}")
    if not r:
        return []
    try:
        data = r.json()
        items = data if isinstance(data, list) else data.get("papers", [])
        return [
            {
                "title": p.get("paper", {}).get("title", ""),
                "summary": p.get("paper", {}).get("summary", "")[:300],
                "url": "https://huggingface.co/papers/" + p.get("paper", {}).get("id", ""),
            }
            for p in items[:15]
        ]
    except Exception as e:
        print(f"  [warn] HF papers: {e}")
        return []


def collect_huggingface_trending_models() -> list[dict]:
    r = _get("https://huggingface.co/api/models?sort=trending&limit=15&direction=-1")
    if not r:
        return []
    try:
        return [
            {
                "id": m.get("id", ""),
                "downloads": m.get("downloads", 0),
                "likes": m.get("likes", 0),
                "tags": m.get("tags", [])[:5],
            }
            for m in r.json()
        ]
    except Exception as e:
        print(f"  [warn] HF models: {e}")
        return []


def collect_github_trending() -> list[dict]:
    r = _get("https://github.com/trending?since=daily")
    if not r:
        return []
    try:
        soup = BeautifulSoup(r.text, "html.parser")
        repos = []
        for article in soup.select("article.Box-row")[:15]:
            name_tag = article.select_one("h2 a")
            desc_tag = article.select_one("p")
            stars_tag = article.select_one("span.d-inline-block.float-sm-right")
            if not name_tag:
                continue
            repos.append({
                "name": name_tag.get_text(" ", strip=True).replace(" / ", "/"),
                "description": desc_tag.get_text(strip=True) if desc_tag else "",
                "stars_today": stars_tag.get_text(strip=True) if stars_tag else "",
                "url": "https://github.com" + name_tag["href"],
            })
        return repos
    except Exception as e:
        print(f"  [warn] GitHub trending: {e}")
        return []


def collect_reddit(subreddits: list[str], max_per_sub: int = 5) -> dict[str, list[dict]]:
    """Fetch hot posts via Reddit JSON API — no auth required."""
    cutoff = NOW_UTC - timedelta(hours=48)
    results: dict[str, list[dict]] = {}
    for sub in subreddits:
        r = _get(f"https://www.reddit.com/r/{sub}/new.json?limit=25")
        if not r:
            results[sub] = []
            continue
        try:
            posts = r.json()["data"]["children"]
            items = []
            for post in posts:
                d = post["data"]
                created = datetime.fromtimestamp(d["created_utc"], tz=timezone.utc)
                if created < cutoff:
                    continue
                items.append({
                    "title": d.get("title", ""),
                    "url": "https://reddit.com" + d.get("permalink", ""),
                    "score": d.get("score", 0),
                    "flair": d.get("link_flair_text", ""),
                })
                if len(items) >= max_per_sub:
                    break
            results[sub] = items
        except Exception as e:
            print(f"  [warn] Reddit r/{sub}: {e}")
            results[sub] = []
    return results


def _parse_rss_date(date_str: str) -> datetime | None:
    for fmt in (
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
    ):
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def collect_rss(feeds: dict[str, str], max_per_feed: int = 5) -> dict[str, list[dict]]:
    cutoff = NOW_UTC - timedelta(hours=48)
    results: dict[str, list[dict]] = {}
    for name, url in feeds.items():
        r = _get(url)
        if not r:
            results[name] = []
            continue
        try:
            soup = BeautifulSoup(r.content, "lxml-xml")
            entries = soup.find_all("item") or soup.find_all("entry")
            items = []
            for entry in entries:
                title = (entry.find("title") or {}).get_text(strip=True)
                link_tag = entry.find("link")
                link = (
                    link_tag.get("href") or link_tag.get_text(strip=True)
                    if link_tag else ""
                )
                desc = (
                    entry.find("description")
                    or entry.find("summary")
                    or entry.find("content")
                )
                summary = desc.get_text(strip=True)[:200] if desc else ""

                pub_tag = (
                    entry.find("pubDate")
                    or entry.find("published")
                    or entry.find("updated")
                )
                if pub_tag:
                    pub_dt = _parse_rss_date(pub_tag.get_text(strip=True))
                    if pub_dt and pub_dt.astimezone(timezone.utc) < cutoff:
                        continue

                items.append({"title": title, "summary": summary, "url": link})
                if len(items) >= max_per_feed:
                    break
            results[name] = items
        except Exception as e:
            print(f"  [warn] RSS {name}: {e}")
            results[name] = []
    return results


# ── Tier 2: Claude synthesis ──────────────────────────────────────────────────

def generate_brief(focus_areas: str, collected: dict) -> str:
    client = anthropic.Anthropic()
    data_dump = json.dumps(collected, ensure_ascii=False, indent=2)

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": (
                f"Today is {TODAY} (Asia/Seoul, UTC+9).\n\n"
                "You are generating a daily morning brief for a software engineer "
                "focused on speech recognition, AI models, Android development, and ads/IAP.\n\n"
                f"FOCUS AREAS (from CLAUDE.md):\n{focus_areas}\n\n"
                "RAW DATA collected in the last 24–48 h from arXiv, HuggingFace, "
                "GitHub, Reddit, and RSS feeds:\n"
                f"{data_dump}\n\n"
                "Instructions:\n"
                f"- Start with '# Morning Brief — {TODAY}'\n"
                "- One markdown header per focus area\n"
                "- Highlight only what is NEW or CHANGED — no generic background info\n"
                "- Include source links from the data where available\n"
                "- 3–6 bullet points per section, concise\n"
                "- If no data was collected for an area, note it in one line\n"
            ),
        }],
    )

    return "".join(block.text for block in response.content if hasattr(block, "text"))


# ── output ────────────────────────────────────────────────────────────────────

def save_brief(brief: str):
    os.makedirs("docs", exist_ok=True)
    path = f"docs/{TODAY}-morning-brief.md"
    with open(path, "w") as f:
        f.write(brief)
    print(f"  Saved → {path}")


def _md_to_html(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"^#{1,3} (.+)$", r"<b>\1</b>", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(
        r"\[(.+?)\]\((.+?)\)",
        lambda m: f'<a href="{m.group(2).replace("&amp;","&")}">{m.group(1)}</a>',
        text,
    )
    text = re.sub(r"^---+$", "─" * 20, text, flags=re.MULTILINE)
    return text


def send_to_telegram(text: str):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    html = _md_to_html(text)
    for i in range(0, len(html), 4096):
        resp = requests.post(url, json={
            "chat_id": chat_id,
            "text": html[i: i + 4096],
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        })
        resp.raise_for_status()


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    with open("CLAUDE.md") as f:
        focus_areas = f.read()

    print(f"📡 Collecting data for {TODAY}...")

    print("  → arXiv: speech / ASR")
    asr_papers = collect_arxiv(categories=["cs.SD", "eess.AS"], max_results=12)

    print("  → arXiv: AI / LLM")
    ai_papers = collect_arxiv(
        categories=["cs.LG", "cs.AI", "cs.CL"],
        keywords=["LLM", "language+model", "multimodal", "agent", "speech"],
        max_results=12,
    )

    print("  → HuggingFace: daily papers")
    hf_papers = collect_huggingface_papers()

    print("  → HuggingFace: trending models")
    hf_models = collect_huggingface_trending_models()

    print("  → GitHub: trending repos")
    github_trending = collect_github_trending()

    print("  → Reddit")
    reddit = collect_reddit(REDDIT_SUBS)

    print("  → RSS feeds")
    rss = collect_rss(RSS_FEEDS)

    collected = {
        "arxiv_speech_asr":          asr_papers,
        "arxiv_ai_llm":              ai_papers,
        "huggingface_daily_papers":  hf_papers,
        "huggingface_trending_models": hf_models,
        "github_trending_today":     github_trending,
        "reddit":                    reddit,
        "rss":                       rss,
    }

    total = (
        len(asr_papers) + len(ai_papers) + len(hf_papers) + len(hf_models)
        + len(github_trending)
        + sum(len(v) for v in reddit.values())
        + sum(len(v) for v in rss.values())
    )
    print(f"  Collected {total} items total\n")

    print("✍️  Generating brief with Claude...")
    brief = generate_brief(focus_areas, collected)

    print("💾 Saving brief...")
    save_brief(brief)

    print("📨 Sending to Telegram...")
    send_to_telegram(brief)

    print("✅ Done!")


if __name__ == "__main__":
    main()
