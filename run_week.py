#!/usr/bin/env python
"""Run the LMS survivor optimiser for one week.

    python run_week.py --week 1                     # analyse Week 1 (legacy single-user)
    python run_week.py --week 1 --member Mattymo     # personalised for one group member
    python run_week.py --week 5 --refresh            # force re-download schedule/odds
    python run_week.py --week 1 --member all         # every configured member (used by the weekly Action)

Members are looked up in data/2026/lms/members.csv (member -> exact entry_name in
the pool operator's workbook, data/2026/lms/*.xlsx) and their already-used teams
are derived automatically from that workbook. Without --member, used teams come
from the legacy data/2026/lms/used_teams.csv instead.

Set your paid Odds API key first (optional but recommended):
    export ODDS_API_KEY=xxxxxxxxxxxxxxxxxxxx
"""
from __future__ import annotations

import argparse
import sys

from survivor_lms.config import Config
from survivor_lms.pipeline import run


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--week", type=int, default=1, help="NFL week to analyse (1-18)")
    ap.add_argument("--refresh", action="store_true", help="force refresh cached data")
    ap.add_argument("--member", default=None,
                    help="run for one group member (see data/2026/lms/members.csv); "
                         "'all' runs every configured member")
    args = ap.parse_args()

    cfg = Config()
    if not (1 <= args.week <= cfg.n_weeks):
        ap.error("--week must be 1..18")

    members = [args.member]
    if args.member and args.member.lower() == "all":
        from survivor_lms import lms as lms_mod
        members = list(lms_mod.load_members(cfg)) or [None]

    for m in members:
        res = run(args.week, force_refresh=args.refresh, cfg=cfg, member=m)
        print("\n" + res["report"]["markdown"])
        print(f"\nWritten to: {res['report']['dir']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
