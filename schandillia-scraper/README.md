# schandillia scraper

Pulls every article from https://www.schandillia.com (Abhijit Chandillia's Substack)
into `../schandillia/` as JSON + markdown for local analysis.

## Setup

```
pip3 install --break-system-packages --user playwright html2text requests
python3 -m playwright install chromium
```

## Run

```
# first run: logs you in, saves cookies, scrapes everything
python3 scrape.py

# later: reuse existing login
python3 scrape.py --skip-login

# just (re)capture cookies after they expire
python3 scrape.py --cookies-only

# refetch specific slugs
python3 scrape.py --skip-login --only rome-financial-crisis,aksai-chin
```

A headful Chromium window opens on `/account/login`. Sign in (email magic link /
Google / whatever you used on Substack), then come back to the terminal and press
ENTER. Cookies are dumped to `cookies.json` (gitignored) and reused on
`--skip-login` runs.

## Output layout

```
../schandillia/
├── _archive.json                              # full metadata listing
├── 2026-03-11_rome-financial-crisis.json      # raw API payload
├── 2026-03-11_rome-financial-crisis.md        # rendered markdown
└── ...
```

Paid articles that come back without `body_html` (expired cookie / not entitled)
are flagged `⚠ no body` in the run log — re-run `--cookies-only` and then
`--skip-login --only <slug>` to retry just those.
