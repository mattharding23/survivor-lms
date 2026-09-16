# survivor-lms

Weekly NFL "Last Man Standing" survivor-pool recommendations for a tracked
group of friends inside a large (~13,860-entry) public pool, plus a shared
static site so everyone can see their own pick.

Straight single-life survivor: one team per week, must win, no reuse.

## Local use

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt      # installs survivor-core (git submodule) editable

python run_week.py --week N --member <name>   # one member's recommendation
python run_week.py --week N --member all      # every member in data/2026/lms/members.csv
python export_site_data.py --week N           # regenerate site/data/ (what the weekly Action runs)
```

The `core/` submodule is [survivor-core](https://github.com/mattharding23/survivor-core)
(shared schedule/odds/EV logic with `survivor-hakim`). Clone with
`git clone --recurse-submodules`, or `git submodule update --init` after a
plain clone.

## Data you maintain

- `data/2026/lms/*.xlsx` — the pool operator's weekly export. Drop in the
  latest file (or let it grow new `WEEK n` sheets); everything is re-parsed
  live, nothing is hand-transcribed.
- `data/2026/lms/members.csv` — `member,entry_name`: maps a friendly name to
  their *exact* entry name in that workbook (case-sensitive). Add a row per
  person you want a personalised recommendation for.
- `data/2026/lms/used_teams.csv` — legacy single-user fallback, only
  consulted without `--member`.
- `.odds_api_key` (git-ignored, one line) or `ODDS_API_KEY` env var — The
  Odds API key. In CI this comes from a Doppler-synced Actions secret named
  `ODDS_API_KEY`.

## Weekly Action

`.github/workflows/weekly.yml` runs every Wednesday, gated on the real
America/New_York wall clock (see the workflow's comments — two cron lines
cover both DST states, a `gate` job checks the actual hour), regenerates
`site/data/*` via `export_site_data.py`, and publishes `site/` to the
`gh-pages` branch. Trigger a manual run any time with
`gh workflow run weekly.yml [-f week=N]` (bypasses the hour gate).

**Not yet enabled:** GitHub Pages itself. Once you're happy with a
`gh-pages` dry run: repo Settings → Pages → Source: **Deploy from a
branch** → Branch **`gh-pages`**, folder **`/(root)`** → Save.
