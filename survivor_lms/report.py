"""Human-facing output: ranked table, recommendation, season-path summary, chart."""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .config import Config
from survivor_core.teams import display


def _fmt_path(path: dict[int, str]) -> str:
    return "  ".join(f"W{w}:{path[w]}" for w in sorted(path))


def build_tables(result: dict, cfg: Config) -> pd.DataFrame:
    df = result["ranked"].copy()
    show = pd.DataFrame({
        "rank": df["rank"],
        "team": df["team"],
        "pick_score": df["pick_score"],
        "win_%": (df["win_prob"] * 100).round(1),
        "public_%": (df["pub_pick_pct"] * 100).round(1),
        "pool_dupes": df["exp_pool_opponents"].round(2),
        "pool_%": (df["exp_pool_share"] * 100).round(1),
        "future_val": df["future_value"].round(3),
        "EV_path": df["ev_path"].round(4),
        "rest_logwp": df["rest_of_season_logwp"].round(3),
        "implied_next_picks": [
            _fmt_path({k: v for k, v in p.items() if k <= cfg.current_week + 4})
            for p in df["implied_path"]
        ],
    })
    return show


def to_markdown(show: pd.DataFrame) -> str:
    try:
        return show.to_markdown(index=False)
    except Exception:
        return show.to_string(index=False)


def write_outputs(result: dict, meta: dict, cfg: Config, out_dir: Path | None = None) -> dict:
    out_dir = out_dir or cfg.week_out_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    show = build_tables(result, cfg)
    show.to_csv(out_dir / "ranked_teams.csv", index=False)
    result["ranked"].to_csv(out_dir / "ranked_teams_full.csv", index=False)

    rec = result["recommendation"]
    lines = []
    who = meta.get("member")
    title = f"Survivor — Week {cfg.current_week} ({cfg.season})"
    if who:
        title += f" — {who}" + (f" ({meta['entry_name']})" if meta.get("entry_name") != who else "")
    lines.append(f"# {title}\n")
    lines.append(f"- Win-prob sources: **{meta.get('winprob_sources')}**")
    lines.append(f"- Public pick %: **{meta.get('consensus', {}).get('source')}** "
                 f"{meta.get('consensus', {}).get('url', '')}")
    lines.append(f"- Opponents tracked: **{meta.get('n_participants', 0)}** "
                 f"({meta.get('n_alive', 0)} alive)")
    lines.append(f"- Teams already used by you: "
                 f"**{', '.join(result['used_teams']) or 'none'}**\n")

    if rec is not None:
        lines.append(f"## ✅ Recommended Week {cfg.current_week} pick: **{rec['team']} "
                     f"({display(rec['team'])})**")
        lines.append(f"- Market win probability: **{rec['win_prob']*100:.1f}%**")
        lines.append(f"- Public pick %: {rec['pub_pick_pct']*100:.1f}%  |  "
                     f"expected dupes in your pool: {rec['exp_pool_opponents']:.2f} "
                     f"({rec['exp_pool_share']*100:.1f}% of those alive)")
        lines.append(f"- EV(path) = {rec['ev_path']:.4f}   EV(myopic) = {rec['ev_myopic']:.4f}")
        lines.append(f"- Implied season plan if you take {rec['team']} now:")
        lines.append(f"  `{_fmt_path(rec['implied_path'])}`\n")

    base_w1 = result["base_path"].get(cfg.current_week)
    if rec is not None and base_w1 and base_w1 != rec["team"]:
        lines.append(f"> ℹ️ The pure win-probability path optimiser would open with **{base_w1}** "
                     f"this week; **{rec['team']}** ranks #1 once the future-value guard and "
                     f"consensus penalty are applied. Both are shown below — adjust "
                     f"`future_value_penalty` / `consensus_penalty` in config.py to taste.\n")

    lines.append(f"## Unconditional optimal season plan (pure Π win-prob)")
    lines.append(f"`{_fmt_path(result['base_path'])}`")
    lines.append(f"- Expected weeks survived (Π win-prob): "
                 f"**{result['base_path_survival']:.3f}**  "
                 f"(sum log wp = {result['base_path_logwp']:.3f})")
    if not result["base_path_feasible"]:
        lines.append("- ⚠️ plan is infeasible somewhere (a week could not be filled — "
                     "check byes / used teams).")
    lines.append("")
    lines.append("## Ranked available teams")
    lines.append(to_markdown(show))
    lines.append("")

    charts = _branded_charts(result, cfg, out_dir)
    if charts:
        lines.append("\n## Charts")
        for c in charts:
            lines.append(f"- `{c.split('/')[-1]}`")

    md = "\n".join(lines)
    (out_dir / "recommendation.md").write_text(md)
    _path_chart(result, cfg, out_dir / f"week_{cfg.current_week:02d}_optimal_path.png")
    return {"markdown": md, "dir": str(out_dir), "table": show, "charts": charts}


def _branded_charts(result: dict, cfg: Config, out_dir) -> list[str]:
    """Recreate the old R/ggplot visuals: win prob, pick distribution, best picks,
    and (when roster data exists) teams-remaining-across-the-pool."""
    from survivor_core import viz
    w = cfg.current_week
    made = []
    try:
        wp = result["winprob_matrix"]
        made.append(str(viz.win_probability(
            wp[w], cfg, out_dir / f"week_{w:02d}_win_probability.png")))
    except Exception as e:  # noqa: BLE001
        print(f"[viz] win_probability failed: {e}")
    try:
        made.append(str(viz.pick_distribution(
            result["public_pct"], cfg, out_dir / f"week_{w:02d}_pick_distribution.png")))
    except Exception as e:  # noqa: BLE001
        print(f"[viz] pick_distribution failed: {e}")
    try:
        made.append(str(viz.best_picks(
            result["ranked"], cfg, out_dir / f"week_{w:02d}_best_picks.png")))
    except Exception as e:  # noqa: BLE001
        print(f"[viz] best_picks failed: {e}")
    try:
        rec = result.get("recommendation") or {}
        made.append(str(viz.ranked_table(
            result["ranked"], cfg, out_dir / f"week_{w:02d}_ranked_table.png",
            recommend_team=rec.get("team"))))
    except Exception as e:  # noqa: BLE001
        print(f"[viz] ranked_table failed: {e}")
    # teams-remaining chart only meaningful once you've logged opponents
    roster = result.get("roster")
    if roster is not None and len(roster.participants) > 0:
        try:
            n_alive = roster.n_opponents_alive()
            used_counts = {}
            for opp in roster.alive():
                for t in roster.used_by(opp, cfg.current_week + 1):
                    used_counts[t] = used_counts.get(t, 0) + 1
            from .teams import ABBRS
            rows = [dict(team=t, players_left=n_alive - used_counts.get(t, 0),
                        total_players_left=n_alive) for t in ABBRS]
            made.append(str(viz.people_remaining(
                pd.DataFrame(rows), cfg, out_dir / f"week_{w:02d}_teams_remaining.png")))
        except Exception as e:  # noqa: BLE001
            print(f"[viz] people_remaining failed: {e}")
    return made


def _path_chart(result: dict, cfg: Config, path: Path) -> None:
    bp = result["base_path"]
    weeks = sorted(bp)
    fig, ax = plt.subplots(figsize=(12, 3.2))
    ax.axis("off")
    ax.set_title(f"Optimal season plan from Week {cfg.current_week} "
                 f"(E[weeks survived] = {result['base_path_survival']:.2f})", fontsize=11)
    n = len(weeks)
    for i, w in enumerate(weeks):
        ax.text(i / max(n - 1, 1), 0.6, f"W{w}", ha="center", fontsize=9, color="#555")
        ax.text(i / max(n - 1, 1), 0.3, bp[w], ha="center", fontsize=12, weight="bold")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)
