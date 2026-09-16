"""EV for each available team this week + optimal multi-week path.

Model
-----
Work in expected-log-survival space.  For a candidate pick T in the current
week w:

    ev_path(T) = log wp[T, w]                     # survive this week
               + best_path(weeks > w, teams - used - {T})   # survive the rest
               - consensus_penalty * crowd(T)     # pool-relative risk
               + contrarian_bonus * under_ownership(T)

`best_path(...)` is an exact linear-assignment solve (one distinct team per
remaining week, maximise summed log win-prob).  The unconditional
`best_path(weeks >= w, teams - used)` is the recommended season plan; the
per-candidate solves show how each Week-w choice reshapes that plan
(the "future value" of saving vs. burning a team falls straight out).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

from .config import Config
from survivor_core.teams import ABBRS, display

NEG = -1.0e6
WP_LO, WP_HI = 0.02, 0.995


def _logwp(p: float) -> float:
    return float(np.log(min(max(p, WP_LO), WP_HI)))


class Optimizer:
    def __init__(self, wp: pd.DataFrame, schedule: pd.DataFrame, cfg: Config,
                 used_teams: list[str]):
        self.cfg = cfg
        self.wp = wp
        self.w0 = cfg.current_week
        self.used = set(used_teams)
        self.weeks = [w for w in range(self.w0, cfg.n_weeks + 1)]
        # availability: team plays that week, week not already resolved
        self.avail = wp.notna() & wp.gt(0.0)
        # a team that has already-resolved games in >= w0 counts as playable for future weeks only
        self.future_weeks = [w for w in range(self.w0 + 1, cfg.n_weeks + 1)]

    # -- core assignment ------------------------------------------------
    def best_path(self, weeks: list[int], allowed: list[str],
                  forced: dict[int, str] | None = None) -> tuple[float, dict[int, str], bool]:
        """Maximise summed log-win-prob assigning one distinct team per week.

        Returns (total_logwp, {week: team}, feasible).
        `forced` pins certain weeks to certain teams.
        """
        forced = forced or {}
        weeks = list(weeks)
        free_weeks = [w for w in weeks if w not in forced]
        used_forced = set(forced.values())
        cols = [t for t in allowed if t not in used_forced]
        if not free_weeks:
            total = sum(_logwp(self.wp.loc[t, w]) for w, t in forced.items())
            return total, dict(forced), True
        if len(cols) < len(free_weeks):
            # pad with impossible dummy teams so the solver still runs
            cols = cols + [f"__dummy{i}" for i in range(len(free_weeks) - len(cols))]
        M = np.full((len(free_weeks), len(cols)), NEG, dtype=float)
        for i, wk in enumerate(free_weeks):
            for j, t in enumerate(cols):
                if t.startswith("__dummy"):
                    continue
                p = self.wp.loc[t, wk] if wk in self.wp.columns else np.nan
                if pd.notna(p) and p > 0.0:
                    M[i, j] = _logwp(p)
        ri, ci = linear_sum_assignment(-M)
        assign = dict(forced)
        feasible = True
        total = sum(_logwp(self.wp.loc[t, w]) for w, t in forced.items())
        for i, j in zip(ri, ci):
            wk, t = free_weeks[i], cols[j]
            if t.startswith("__dummy") or M[i, j] <= NEG / 2:
                feasible = False
                continue
            assign[wk] = t
            total += M[i, j]
        return total, assign, feasible

    # -- future-value display metric ---------------------------------
    def future_value(self, team: str) -> float:
        c = self.cfg.engine
        v = 0.0
        for k in self.future_weeks:
            p = self.wp.loc[team, k] if k in self.wp.columns else np.nan
            if pd.notna(p) and p > c.fv_threshold:
                v += (c.fv_discount ** (k - self.w0)) * (p - c.fv_threshold)
        return float(v)

    # -- main -------------------------------------------------------
    def run(self, crowd: pd.DataFrame) -> dict:
        c = self.cfg.engine
        allowed_all = [t for t in ABBRS if t not in self.used]

        # unconditional optimal plan for the rest of the season
        base_val, base_path, base_feasible = self.best_path(self.weeks, allowed_all)

        # candidates playable THIS week
        candidates = [t for t in allowed_all
                      if self.w0 in self.wp.columns
                      and pd.notna(self.wp.loc[t, self.w0])
                      and self.wp.loc[t, self.w0] > 0.0]

        # crowd normalisation for contrarian bonus: compare ownership to a
        # "fair" ownership proportional to this week's win prob among candidates
        wp_now = self.wp.loc[candidates, self.w0].astype(float)
        fair_owned = wp_now / wp_now.sum()

        rows = []
        for t in candidates:
            cond_val, cond_path, feasible = self.best_path(
                self.weeks, allowed_all, forced={self.w0: t})
            logwp_now = _logwp(self.wp.loc[t, self.w0])
            rest_val = cond_val - logwp_now
            exp_share = float(crowd.loc[t, "exp_share"]) if t in crowd.index else 0.0
            pub = float(crowd.loc[t, "pub_pct"]) if t in crowd.index else 0.0
            under = float(fair_owned.get(t, 0.0) - pub)   # >0 => under-owned vs strength
            fv = self.future_value(t)

            crowd_term = c.consensus_penalty * exp_share          # (b) consensus penalty
            contrarian_term = c.contrarian_bonus * max(under, 0.0)
            fv_term = c.future_value_penalty * fv                 # (c) don't burn a future stud

            # (a) win-prob enters via logwp_now; non-greedy lookahead via cond_val.
            ev_path = cond_val - crowd_term + contrarian_term - fv_term
            ev_myopic = logwp_now - crowd_term + contrarian_term - fv_term
            rows.append(dict(
                team=t, team_name=display(t),
                win_prob=float(self.wp.loc[t, self.w0]),
                pub_pick_pct=pub,
                exp_pool_share=exp_share,
                exp_pool_opponents=float(crowd.loc[t, "exp_opponents"]) if t in crowd.index else 0.0,
                future_value=fv,
                fv_penalty=fv_term,
                consensus_penalty=crowd_term,
                contrarian_bonus=contrarian_term,
                rest_of_season_logwp=rest_val,
                ev_myopic=ev_myopic,
                ev_path=ev_path,
                path_feasible=feasible,
                implied_path={k: cond_path[k] for k in sorted(cond_path)},
            ))

        df = pd.DataFrame(rows).sort_values("ev_path", ascending=False).reset_index(drop=True)
        df["rank"] = df.index + 1
        # readable 0-100 index (relative to the field this week)
        lo, hi = df["ev_path"].min(), df["ev_path"].max()
        df["pick_score"] = ((df["ev_path"] - lo) / (hi - lo) * 100).round(1) if hi > lo else 50.0

        rec = df.iloc[0].to_dict() if len(df) else None
        return dict(
            week=self.w0,
            ranked=df,
            recommendation=rec,
            base_path=dict(sorted(base_path.items())),
            base_path_logwp=base_val,
            base_path_survival=float(np.exp(base_val)),
            base_path_feasible=base_feasible,
            used_teams=sorted(self.used),
        )
