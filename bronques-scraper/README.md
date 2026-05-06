# bronques scraper

Pulls every lecture from the Make Art Not Content course on
`learn.makeartnotcontent.com` (Teachable) into `../bronques/` as JSON +
markdown for local analysis.

## Setup

```
pip3 install --break-system-packages --user playwright html2text requests
python3 -m playwright install chromium
```

## Run

```
# first run: opens browser, you log in, scraper saves cookies + scrapes
python3 scrape.py

# later: reuse existing login
python3 scrape.py --skip-login

# just (re)capture cookies after they expire
python3 scrape.py --cookies-only

# refetch specific lectures by id
python3 scrape.py --skip-login --only 41878133,41878134
```

Headful Chromium opens on the seeded lecture URL. Sign in (Teachable login
or Google OAuth — whatever the course uses), wait until the curriculum
sidebar is visible, then come back to the terminal and press ENTER.
Playwright `storage_state.json` is gitignored and reused on `--skip-login`.

## Output layout

```
../bronques/
├── _index.json                      # discovered lectures
├── 001_41878133_intro.json          # raw extraction (html, video, attachments)
├── 001_41878133_intro.md            # rendered markdown
└── ...
```

Lectures that come back without body HTML (video-only, or expired session)
are flagged `⚠ no body` — re-run `--cookies-only` and then
`--skip-login --only <id>` to retry.
