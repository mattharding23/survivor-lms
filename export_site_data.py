#!/usr/bin/env python
"""Generate site/data/*.json + per-member markdown for the static site.

Reuses survivor_lms.pipeline.run() exactly as run_week.py does -- no new
computation, just serializes what it already returns. Runs the shared
(member=None) pipeline once for the league-wide view, then once per member
in data/2026/lms/members.csv for their personal recommendation.

    python export_site_data.py --week 2
    python export_site_data.py                 # auto-detects the current week
                                                 # (the first week with an
                                                 # unplayed game) -- what the
                                                 # weekly Action uses
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from survivor_core.schedule import load_season_schedule
from survivor_lms import lms as lms_mod
from survivor_lms.config import Config
from survivor_lms.pipeline import run

SITE_DATA = Path(__file__).resolve().parent / "site" / "data"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return s or "member"


def _auto_week(cfg: Config) -> int:
    """First week with at least one game not yet played. Matches the same
    week a human would currently be picking for -- a week isn't "done" until
    every one of its games has finished, even if most have."""
    schedule = load_season_schedule(cfg.season)
    for wk in range(1, cfg.n_weeks + 1):
        wk_games = schedule[schedule["week"] == wk]
        if not wk_games.empty and not bool(wk_games["played"].all()):
            return wk
    return cfg.n_weeks


def _clean(obj):
    """Recursively swap NaN/NaT for None so json.dumps doesn't choke, and
    stringify dict keys (JSON object keys must be strings; ours are often
    int week numbers)."""
    if isinstance(obj, float) and np.isnan(obj):
        return None
    if isinstance(obj, dict):
        return {str(k): _clean(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_clean(v) for v in obj]
    if isinstance(obj, pd.Series):
        return _clean(obj.to_dict())
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return None if np.isnan(obj) else float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    return obj


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_clean(data), indent=2, default=str))


def _matrix_to_dict(df: pd.DataFrame) -> dict:
    return {team: {str(wk): _clean(v) for wk, v in df.loc[team].items()} for team in df.index}


def _ranked_records(df: pd.DataFrame) -> list[dict]:
    if df is None or df.empty:
        return []
    return _clean(df.to_dict("records"))


def export_shared(cfg: Config, week: int, result: dict) -> None:
    schedule = load_season_schedule(cfg.season).copy()
    schedule["gameday"] = schedule["gameday"].astype(str)
    _write_json(SITE_DATA / "schedule.json", dict(
        season=cfg.season, week=week, generated_at=_now(),
        games=schedule.to_dict("records"),
    ))

    _write_json(SITE_DATA / "winprob.json", dict(
        week=week, generated_at=_now(),
        teams=_matrix_to_dict(result["winprob_matrix"]),
        sources=_matrix_to_dict(result["winprob_source_matrix"].astype(object)),
    ))

    pct = result["public_pct"]
    _write_json(SITE_DATA / "public_pct.json", dict(
        week=week, generated_at=_now(),
        source=result["meta"]["consensus"].get("source"),
        pct={t: _clean(v) for t, v in pct.items()},
    ))

    _write_json(SITE_DATA / "league_ev.json", dict(
        week=week, generated_at=_now(),
        teams=_ranked_records(result["ranked"]),
        base_path=result["base_path"],
        base_path_survival=result["base_path_survival"],
    ))


def export_member(week: int, member: str, result: dict) -> str:
    slug = _slugify(member)
    _write_json(SITE_DATA / "members" / f"{slug}.json", dict(
        member=member, week=week, generated_at=_now(),
        teams=_ranked_records(result["ranked"]),
        recommendation=_clean(result["recommendation"]),
        base_path=result["base_path"],
        base_path_survival=result["base_path_survival"],
        used_teams=result["used_teams"],
    ))
    (SITE_DATA / "members" / f"{slug}.md").write_text(result["report"]["markdown"])
    return slug


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--week", type=int, default=None,
                    help="NFL week (default: auto-detect the current week)")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    cfg = Config()
    week = args.week or _auto_week(cfg)
    if not (1 <= week <= cfg.n_weeks):
        ap.error("--week must be 1..18")

    print(f"[export] Week {week} ({'explicit' if args.week else 'auto-detected'})")

    shared = run(week, force_refresh=args.refresh, cfg=cfg, member=None)
    export_shared(cfg, week, shared)

    members = lms_mod.load_members(cfg)
    index = []
    for name in members:
        res = run(week, force_refresh=False, cfg=cfg, member=name)
        slug = export_member(week, name, res)
        index.append(dict(name=name, slug=slug))
        print(f"[export] {name} -> {slug}")

    _write_json(SITE_DATA / "members" / "index.json", dict(
        week=week, generated_at=_now(), members=index,
    ))
    print(f"[export] wrote site data for {len(index)} member(s) -> {SITE_DATA}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
