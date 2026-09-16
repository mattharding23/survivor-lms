"""End-to-end: schedule -> win prob -> consensus -> optimise -> report."""
from __future__ import annotations

import pandas as pd

from .config import Config
from survivor_core.constraints import Roster, load_used_teams
from survivor_core.consensus import expected_duplication, fetch_public_pick_pct
from survivor_core.elo import EloModel
from .engine import Optimizer
from . import lms as lms_mod
from .report import write_outputs
from survivor_core.schedule import load_history, load_season_schedule
from survivor_core import survivorgrid as sg_mod
from survivor_core.teams import ABBRS
from survivor_core.winprob import build_winprob_matrix


def _load_adjustments(cfg: Config) -> pd.DataFrame:
    p = cfg.adjustments_csv
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(columns=["team", "adjustment", "expires_week"]).to_csv(p, index=False)
        return pd.DataFrame(columns=["team", "adjustment", "expires_week"])
    try:
        return pd.read_csv(p)
    except Exception:
        return pd.DataFrame(columns=["team", "adjustment", "expires_week"])


def run(current_week: int, force_refresh: bool = False, cfg: Config | None = None,
        member: str | None = None) -> dict:
    """Run one week for the LMS pool.

    `member` (optional) looks up an entry_name in data/<season>/lms/members.csv and
    derives that person's already-used teams straight from the pool operator's
    workbook (data/<season>/lms/*.xlsx) instead of the legacy used_teams.csv. Pass
    nothing to keep the old single-user, hand-maintained-CSV behaviour.
    """
    cfg = cfg or Config()
    cfg.current_week = current_week

    schedule = load_season_schedule(cfg.season, force=force_refresh)
    history = load_history(cfg.season, cfg.elo.lookback_seasons, force=force_refresh)

    elo = EloModel(cfg.elo).fit(history)
    if history["season"].max() < cfg.season or (
        history[history["season"] == cfg.season].empty):
        elo.preseason_regress()
    elo.apply_adjustments(_load_adjustments(cfg), current_week)

    sg = sg_mod.load(force=force_refresh)
    if not sg.ok:
        print(f"[survivorgrid] unavailable: {sg.note}")
    elif sg.week and sg.week != current_week:
        print(f"[survivorgrid] NOTE: live grid looks like Week {sg.week} but you asked for "
              f"Week {current_week}; public %/W% may be for the wrong week.")

    wp, src = build_winprob_matrix(schedule, elo, cfg, sg=sg)

    entries = lms_mod.load_all_entries(cfg)
    entry_name = None
    if member:
        members = lms_mod.load_members(cfg)
        entry_name = members.get(member)
        if entry_name is None:
            known = ", ".join(members) or "(none configured)"
            raise SystemExit(f"Unknown LMS member {member!r}. Known members: {known} "
                             f"— add them to {cfg.lms_dir / 'members.csv'}")

    used = set(load_used_teams(cfg.used_teams_csv))
    if entry_name:
        used |= lms_mod.member_used_teams(entries, entry_name, current_week)
    used = sorted(used)

    roster = Roster.load(cfg.participants_csv)

    # availability this week for the crowd model
    avail_week = pd.Series(
        {t: (current_week in wp.columns and pd.notna(wp.loc[t, current_week])
             and wp.loc[t, current_week] > 0.0 and t not in used) for t in ABBRS})

    real_pct, real_meta = lms_mod.load_pick_pct(cfg, current_week)
    if real_pct is not None:
        public_pct, cmeta = real_pct, real_meta
    else:
        public_pct, cmeta = fetch_public_pick_pct(
            current_week, wp_week=wp[current_week] if current_week in wp.columns else None, sg=sg)
    crowd = expected_duplication(current_week, wp, public_pct, roster, avail_week)

    opt = Optimizer(wp, schedule, cfg, used)
    result = opt.run(crowd)

    src_counts = src[current_week].value_counts().to_dict() if current_week in src.columns else {}
    meta = dict(
        winprob_sources=", ".join(f"{k}:{v}" for k, v in src_counts.items()),
        consensus=cmeta,
        n_participants=len(roster.participants),
        n_alive=roster.n_opponents_alive(),
        member=member,
        entry_name=entry_name,
    )
    result["elo_top"] = elo.ratings_frame().head(10).to_dict("records")
    result["winprob_matrix"] = wp
    result["winprob_source_matrix"] = src
    result["crowd"] = crowd
    result["public_pct"] = public_pct
    result["roster"] = roster
    out_dir = cfg.week_out_dir() / "lms" / member if member else None
    out = write_outputs(result, meta, cfg, out_dir=out_dir)
    result["report"] = out
    result["meta"] = meta
    return result
