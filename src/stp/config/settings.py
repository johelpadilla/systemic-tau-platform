from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


ROOT = Path(__file__).resolve().parents[3]
CONTENT_DIR = ROOT / "content"
DATA_DIR = ROOT / "data"
SAMPLES_DIR = DATA_DIR / "samples"
CATALOG_PATH = DATA_DIR / "catalog" / "datasets.yaml"


class ThemeColors(BaseModel):
    navy: str = "#0D4F6B"
    deep: str = "#1A2332"
    teal: str = "#1A8A8A"
    purple: str = "#5B4B8A"
    sand: str = "#F4F1EA"
    alert: str = "#C45C26"
    bg: str = "#FAFBFC"


class AnalysisParams(BaseModel):
    window: int = Field(101, ge=5)
    stride: int = Field(5, ge=1)
    m: int = Field(3, ge=2, le=7)
    delay: int = Field(1, ge=1)
    d_persist: int = Field(4, ge=2)
    theta3: float = Field(0.08, ge=0.0)
    n_surrogates: int = Field(8, ge=0)
    mode: Literal["fast", "full"] = "fast"
    seed: int = 42
    zscore: bool = True
    include_ews: bool = True
    include_tda: bool = False
    include_memory: bool = False

    def for_mode(self) -> "AnalysisParams":
        """Apply Fast/Full defaults without mutating caller unexpectedly."""
        data = self.model_dump()
        if self.mode == "fast":
            data["include_tda"] = False
            data["include_memory"] = False
            data["n_surrogates"] = min(self.n_surrogates, 8) if self.n_surrogates else 8
        else:
            data["include_tda"] = True
            data["include_memory"] = True
            if self.n_surrogates < 50:
                data["n_surrogates"] = 50
        return AnalysisParams(**data)


THEME = ThemeColors()

DOMAIN_PRESETS: dict[str, dict] = {
    "cardiology": {"window": 101, "stride": 5, "theta3": 0.08, "m": 3},
    "epidemiology": {"window": 13, "stride": 1, "theta3": 0.10, "m": 3},
    "neuroscience": {"window": 51, "stride": 2, "theta3": 0.10, "m": 3},
    "ecology": {"window": 25, "stride": 1, "theta3": 0.10, "m": 3},
    "finance": {"window": 21, "stride": 1, "theta3": 0.10, "m": 3},
    "synthetic": {"window": 13, "stride": 1, "theta3": 0.10, "m": 3},
}
