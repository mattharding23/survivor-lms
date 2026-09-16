"""LMS-specific configuration: directory layout on top of survivor_core's
pool-agnostic BaseConfig."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from survivor_core import cache as _cache
from survivor_core.config import (BaseConfig, EloConfig, EngineConfig,
                                  resolve_odds_key, set_odds_api_key)

ROOT = Path(__file__).resolve().parent.parent           # repo root (survivor-lms/)
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "outputs"

SEASON = 2026
N_WEEKS = 18

# Resolve + register the shared secret and cache dir once, at import time,
# before any survivor_core call that needs them.
ODDS_API_KEY = resolve_odds_key(ROOT)
set_odds_api_key(ODDS_API_KEY)
_cache.set_cache_dir(DATA_DIR / "cache")


@dataclass
class Config(BaseConfig):
    season: int = SEASON
    n_weeks: int = N_WEEKS
    current_week: int = 1
    elo: EloConfig = field(default_factory=EloConfig)
    engine: EngineConfig = field(default_factory=EngineConfig)

    @property
    def year_dir(self) -> Path:
        return DATA_DIR / str(self.season)

    @property
    def lms_dir(self) -> Path:
        d = self.year_dir / "lms"
        d.mkdir(parents=True, exist_ok=True)
        return d

    @property
    def used_teams_csv(self) -> Path:
        return self.lms_dir / "used_teams.csv"

    @property
    def participants_csv(self) -> Path:
        return self.lms_dir / "participants.csv"

    @property
    def adjustments_csv(self) -> Path:
        return self.year_dir / "adjustments" / f"week_{self.current_week:02d}.csv"

    def week_out_dir(self) -> Path:
        d = OUT_DIR / f"week_{self.current_week:02d}"
        d.mkdir(parents=True, exist_ok=True)
        return d
