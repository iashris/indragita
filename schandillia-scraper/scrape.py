#!/usr/bin/env python3
"""
Scrape all articles from schandillia.com (Substack publication).

Flow:
  1. Launch headful Chromium via Playwright, navigate to login page.
     User logs in interactively (email magic link / Google / etc.).
  2. Once authenticated, extract cookies and reuse them with `requests`
     to hit the Substack JSON API for every post in the archive.
  3. Save raw JSON + rendered markdown + plain text per post into ../schandillia/

Usage:
    python3 scrape.py               # full run (login + scrape)
    python3 scrape.py --cookies-only   # just save cookies, don't scrape
    python3 scrape.py --skip-login  # reuse saved cookies.json
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

import requests
import html2text

SITE = "https://www.schandillia.com"
ARCHIVE_URL = f"{SITE}/api/v1/archive"
POST_URL = f"{SITE}/api/v1/posts/{{slug}}"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
)

HERE = Path(__file__).resolve().parent
OUT_DIR = HERE.parent / "schandillia"
COOKIES_FILE = HERE / "cookies.json"


def login_and_capture_cookies() -> list[dict]:
    """Open a visible browser, let the user log in, then dump cookies."""
    from playwright.sync_api import sync_playwright

    print("\n[login] Launching browser. Log in to schandillia.com in the window.")
    print("[login] When you see your subscriber dashboard / homepage, come back here and press ENTER.\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context(user_agent=UA)
        page = ctx.new_page()
        page.goto(f"{SITE}/account/login", wait_until="domcontentloaded")

        input(">>> Press ENTER here after you've finished logging in...")

        cookies = ctx.cookies()
        browser.close()

    COOKIES_FILE.write_text(json.dumps(cookies, indent=2))
    print(f"[login] Saved {len(cookies)} cookies -> {COOKIES_FILE}")
    return cookies


def cookies_to_jar(cookies: list[dict]) -> requests.cookies.RequestsCookieJar:
    jar = requests.cookies.RequestsCookieJar()
    for c in cookies:
        jar.set(c["name"], c["value"], domain=c.get("domain"), path=c.get("path", "/"))
    return jar


def list_all_posts(session: requests.Session) -> list[dict]:
    """Page through the archive endpoint (max limit=50) until empty."""
    all_posts = []
    offset = 0
    limit = 50
    while True:
        r = session.get(
            ARCHIVE_URL,
            params={"sort": "new", "search": "", "offset": offset, "limit": limit},
            timeout=30,
        )
        r.raise_for_status()
        batch = r.json()
        if not isinstance(batch, list) or not batch:
            break
        all_posts.extend(batch)
        print(f"[archive] offset={offset} got {len(batch)} (total so far {len(all_posts)})")
        if len(batch) < limit:
            break
        offset += limit
        time.sleep(0.5)
    return all_posts


def fetch_post(session: requests.Session, slug: str) -> dict:
    r = session.get(
        POST_URL.format(slug=slug),
        headers={"referer": f"{SITE}/p/{slug}"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()


def sanitize(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-") or "untitled"


def save_post(post: dict) -> tuple[Path, bool]:
    """Write JSON + markdown. Returns (path, had_body)."""
    slug = post.get("slug") or f"id-{post.get('id')}"
    date = (post.get("post_date") or "")[:10]
    filename_stem = f"{date}_{sanitize(slug)}" if date else sanitize(slug)

    json_path = OUT_DIR / f"{filename_stem}.json"
    md_path = OUT_DIR / f"{filename_stem}.md"

    json_path.write_text(json.dumps(post, indent=2, ensure_ascii=False))

    body_html = post.get("body_html") or ""
    title = post.get("title") or slug
    subtitle = post.get("subtitle") or ""
    audience = post.get("audience") or ""
    canonical = post.get("canonical_url") or ""

    if body_html:
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_links = False
        h.ignore_images = False
        body_md = h.handle(body_html)
    else:
        # fall back to whatever teaser text the API exposed
        body_md = post.get("truncated_body_text") or "_(no body returned — paywalled or login expired)_"

    md = f"# {title}\n\n"
    if subtitle:
        md += f"*{subtitle}*\n\n"
    md += f"- date: {date}\n- audience: {audience}\n- url: {canonical}\n- slug: {slug}\n\n---\n\n"
    md += body_md
    md_path.write_text(md)

    return md_path, bool(body_html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-login", action="store_true", help="reuse cookies.json")
    ap.add_argument("--cookies-only", action="store_true", help="login + save cookies, then exit")
    ap.add_argument("--only", help="comma-separated slugs to fetch (skip archive listing)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.skip_login:
        if not COOKIES_FILE.exists():
            print(f"[error] no cookies file at {COOKIES_FILE}, drop --skip-login", file=sys.stderr)
            sys.exit(1)
        cookies = json.loads(COOKIES_FILE.read_text())
    else:
        cookies = login_and_capture_cookies()

    if args.cookies_only:
        return

    session = requests.Session()
    session.headers.update({"user-agent": UA, "accept": "*/*"})
    session.cookies = cookies_to_jar(cookies)

    if args.only:
        slugs = [s.strip() for s in args.only.split(",") if s.strip()]
        posts_meta = [{"slug": s} for s in slugs]
    else:
        posts_meta = list_all_posts(session)
        print(f"[archive] total posts: {len(posts_meta)}")
        (OUT_DIR / "_archive.json").write_text(
            json.dumps(posts_meta, indent=2, ensure_ascii=False)
        )

    ok_with_body = 0
    ok_no_body = 0
    failed = []
    for i, meta in enumerate(posts_meta, 1):
        slug = meta["slug"]
        try:
            full = fetch_post(session, slug)
            path, had_body = save_post(full)
            status = "✓ body" if had_body else "⚠ no body"
            print(f"[{i}/{len(posts_meta)}] {status}  {slug} -> {path.name}")
            if had_body:
                ok_with_body += 1
            else:
                ok_no_body += 1
        except Exception as e:
            print(f"[{i}/{len(posts_meta)}] ✗ {slug} :: {e}")
            failed.append((slug, str(e)))
        time.sleep(0.8)

    print(
        f"\n[done] with body: {ok_with_body}  no body: {ok_no_body}  failed: {len(failed)}"
    )
    if failed:
        print("failed slugs:")
        for s, err in failed:
            print(f"  - {s}: {err}")


if __name__ == "__main__":
    main()
