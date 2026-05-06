#!/usr/bin/env python3
"""
Scrape every lecture from learn.makeartnotcontent.com (Teachable course).

Flow:
  1. Launch headful Chromium via Playwright, navigate to the course lecture
     URL. User logs in interactively.
  2. After login, walk the course curriculum sidebar and collect every
     lecture link.
  3. For each lecture, render the page (Teachable injects content via JS),
     extract the lecture body + any video embed URLs, and save HTML +
     markdown into ../bronques/.
  4. Cookies are persisted to cookies.json so reruns can use --skip-login.

Usage:
    python3 scrape.py                  # full run (login + scrape)
    python3 scrape.py --cookies-only   # login + save cookies, then exit
    python3 scrape.py --skip-login     # reuse cookies.json
    python3 scrape.py --skip-login --only 41878133,41878134
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import html2text

SITE = "https://learn.makeartnotcontent.com"
SEED_URL = f"{SITE}/courses/465756/lectures/41878133"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
)

HERE = Path(__file__).resolve().parent
OUT_DIR = HERE.parent / "bronques"
COOKIES_FILE = HERE / "cookies.json"
STATE_FILE = HERE / "storage_state.json"


def login_and_capture(seed_url: str) -> Path:
    """Open a headful browser, let the user log in, save Playwright storage state.

    The script waits for one of two signals before snapshotting cookies:
      - the file `bronques-scraper/.login-done` to be created, or
      - the user to press ENTER in the terminal.
    Whichever comes first wins, so this works whether you're driving the
    terminal directly or having an agent poll the flag file.
    """
    from playwright.sync_api import sync_playwright
    import threading

    flag_file = HERE / ".login-done"
    if flag_file.exists():
        flag_file.unlink()

    print("\n[login] Launching browser. Log in inside the window.")
    print("[login] When the lecture page is loaded and curriculum is visible:")
    print(f"        either press ENTER here, OR `touch {flag_file}`\n")

    enter_pressed = {"v": False}

    def wait_enter():
        try:
            line = input(">>> Press ENTER after logging in (or touch .login-done)... ")
            enter_pressed["v"] = True
        except EOFError:
            # Background / non-TTY: rely on flag file only
            pass

    t = threading.Thread(target=wait_enter, daemon=True)
    t.start()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ctx = browser.new_context(user_agent=UA)
        page = ctx.new_page()
        page.goto(seed_url, wait_until="domcontentloaded")

        # Poll for either the flag file or ENTER
        while not enter_pressed["v"] and not flag_file.exists():
            time.sleep(1.0)

        ctx.storage_state(path=str(STATE_FILE))
        cookies = ctx.cookies()
        COOKIES_FILE.write_text(json.dumps(cookies, indent=2))
        browser.close()

    if flag_file.exists():
        try:
            flag_file.unlink()
        except Exception:
            pass

    print(f"[login] Saved cookies -> {COOKIES_FILE}")
    print(f"[login] Saved storage state -> {STATE_FILE}")
    return STATE_FILE


def sanitize(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9._-]+", "-", name).strip("-")
    return name[:120] or "untitled"


def discover_lectures(page, course_url: str) -> list[dict]:
    """Read the curriculum sidebar on the course page and return [{id,title,url,section}]."""
    page.goto(course_url, wait_until="networkidle")
    # Teachable sidebar lectures are <a href="/courses/<id>/lectures/<lecture_id>">
    items = page.eval_on_selector_all(
        'a[href*="/lectures/"]',
        """els => els.map(a => ({
            href: a.getAttribute('href'),
            text: (a.innerText || a.textContent || '').trim()
        }))""",
    )
    seen = {}
    for it in items:
        href = it["href"] or ""
        m = re.search(r"/lectures/(\d+)", href)
        if not m:
            continue
        lid = m.group(1)
        if lid in seen:
            continue
        full_url = href if href.startswith("http") else f"{SITE}{href}"
        seen[lid] = {
            "id": lid,
            "title": it["text"] or f"lecture-{lid}",
            "url": full_url,
        }
    # Try to also grab section labels by walking the DOM around each link
    try:
        sections = page.eval_on_selector_all(
            'a[href*="/lectures/"]',
            """els => els.map(a => {
                const sec = a.closest('[data-section], .section, li.section, .course-section, .row-fluid');
                let label = '';
                if (sec) {
                    const h = sec.querySelector('h2, h3, .section-title, .row-title');
                    if (h) label = (h.innerText || h.textContent || '').trim();
                }
                const m = (a.getAttribute('href') || '').match(/\\/lectures\\/(\\d+)/);
                return { id: m ? m[1] : null, section: label };
            })""",
        )
        for s in sections:
            if s["id"] in seen and s.get("section"):
                seen[s["id"]]["section"] = s["section"]
    except Exception:
        pass
    return list(seen.values())


def find_course_url(seed_url: str) -> str:
    m = re.match(r"(https?://[^/]+/courses/\d+)", seed_url)
    if not m:
        return seed_url
    return m.group(1)


def extract_lecture(page, url: str) -> dict:
    """Navigate to a lecture URL and pull out title, html body, video sources, and attachments."""
    # `networkidle` hangs on lectures with embedded video players that keep polling.
    # `domcontentloaded` is enough — Teachable renders lecture body server-side.
    page.goto(url, wait_until="domcontentloaded", timeout=45000)
    try:
        page.wait_for_selector(".lecture-content, [class*='lecture'], main", timeout=10000)
    except Exception:
        pass
    time.sleep(1.5)

    data = page.evaluate(
        r"""() => {
            const pickText = sel => {
                const el = document.querySelector(sel);
                return el ? (el.innerText || el.textContent || '').trim() : '';
            };
            const pickHTML = sel => {
                const el = document.querySelector(sel);
                return el ? el.innerHTML : '';
            };
            const title =
                pickText('h1.lecture-name') ||
                pickText('h1.lecture-title') ||
                pickText('.lecture-name') ||
                pickText('h1') ||
                document.title;

            // Teachable wraps lecture body in a few possible containers
            const bodySelectors = [
                '.lecture-attachment-type-text .attachment-wrapper',
                '.lecture-text',
                '.lecture-content',
                '.attachment-text',
                'article',
                'main'
            ];
            let body_html = '';
            for (const sel of bodySelectors) {
                const h = pickHTML(sel);
                if (h && h.length > body_html.length) body_html = h;
            }

            // Collect video sources / embeds
            const videos = [];
            document.querySelectorAll('video, video source, iframe').forEach(el => {
                const src = el.getAttribute('src') || el.src || '';
                if (src) videos.push({ tag: el.tagName.toLowerCase(), src });
            });
            // Wistia / Vimeo data attributes
            document.querySelectorAll('[data-wistia-id], [data-video-id], [data-hashed-id]').forEach(el => {
                videos.push({
                    tag: el.tagName.toLowerCase(),
                    src: el.getAttribute('data-wistia-id') || el.getAttribute('data-video-id') || el.getAttribute('data-hashed-id'),
                    kind: 'data-attr'
                });
            });

            // Attachments / downloads
            const attachments = [];
            document.querySelectorAll('a[href]').forEach(a => {
                const href = a.getAttribute('href') || '';
                if (/\.(pdf|zip|mp3|mp4|mov|jpg|jpeg|png|gif|doc|docx)(\?|$)/i.test(href) ||
                    /\/attachments\//.test(href)) {
                    attachments.push({ text: (a.innerText || '').trim(), href });
                }
            });

            return { title, body_html, videos, attachments, url: location.href };
        }"""
    )
    return data


def save_lecture(meta: dict, lecture: dict, index: int) -> tuple[Path, bool]:
    lid = meta["id"]
    title = lecture.get("title") or meta.get("title") or f"lecture-{lid}"
    slug = sanitize(title)
    stem = f"{int(index):03d}_{lid}_{slug}"

    json_path = OUT_DIR / f"{stem}.json"
    md_path = OUT_DIR / f"{stem}.md"

    payload = {
        "id": lid,
        "title": title,
        "section": meta.get("section", ""),
        "url": lecture.get("url") or meta.get("url"),
        "videos": lecture.get("videos") or [],
        "attachments": lecture.get("attachments") or [],
        "body_html": lecture.get("body_html") or "",
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    body_html = lecture.get("body_html") or ""
    if body_html:
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_links = False
        h.ignore_images = False
        body_md = h.handle(body_html)
    else:
        body_md = "_(no body extracted — page may be video-only or login expired)_"

    md = f"# {title}\n\n"
    if meta.get("section"):
        md += f"*Section: {meta['section']}*\n\n"
    md += f"- id: {lid}\n- url: {payload['url']}\n\n"
    if payload["videos"]:
        md += "## videos\n\n"
        for v in payload["videos"]:
            md += f"- `{v.get('tag')}` {v.get('src')}\n"
        md += "\n"
    if payload["attachments"]:
        md += "## attachments\n\n"
        for a in payload["attachments"]:
            md += f"- [{a.get('text') or a.get('href')}]({a.get('href')})\n"
        md += "\n"
    md += "---\n\n" + body_md
    md_path.write_text(md)

    return md_path, bool(body_html)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", default=SEED_URL, help="any lecture URL inside the target course")
    ap.add_argument("--skip-login", action="store_true", help="reuse storage_state.json")
    ap.add_argument("--cookies-only", action="store_true", help="login + save state, then exit")
    ap.add_argument("--only", help="comma-separated lecture IDs to fetch (skip discovery)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.skip_login:
        if not STATE_FILE.exists():
            print(f"[error] no state at {STATE_FILE}, drop --skip-login", file=sys.stderr)
            sys.exit(1)
    else:
        login_and_capture(args.seed)

    if args.cookies_only:
        return

    from playwright.sync_api import sync_playwright

    course_url = find_course_url(args.seed)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(user_agent=UA, storage_state=str(STATE_FILE))
        page = ctx.new_page()

        if args.only:
            ids = [s.strip() for s in args.only.split(",") if s.strip()]
            lectures = [
                {"id": lid, "title": f"lecture-{lid}", "url": f"{course_url}/lectures/{lid}"}
                for lid in ids
            ]
        else:
            print(f"[discover] {course_url}")
            lectures = discover_lectures(page, course_url)
            print(f"[discover] found {len(lectures)} lectures")
            (OUT_DIR / "_index.json").write_text(
                json.dumps(lectures, indent=2, ensure_ascii=False)
            )

        ok_with_body = 0
        ok_no_body = 0
        failed = []
        for i, meta in enumerate(lectures, 1):
            try:
                lec = extract_lecture(page, meta["url"])
                path, had_body = save_lecture(meta, lec, i)
                status = "✓ body" if had_body else "⚠ no body"
                print(f"[{i}/{len(lectures)}] {status}  {meta['id']} -> {path.name}")
                if had_body:
                    ok_with_body += 1
                else:
                    ok_no_body += 1
            except Exception as e:
                print(f"[{i}/{len(lectures)}] ✗ {meta.get('id')} :: {e}")
                failed.append((meta.get("id"), str(e)))
            time.sleep(0.6)

        browser.close()

    print(
        f"\n[done] with body: {ok_with_body}  no body: {ok_no_body}  failed: {len(failed)}"
    )
    if failed:
        print("failed lectures:")
        for s, err in failed:
            print(f"  - {s}: {err}")


if __name__ == "__main__":
    main()
