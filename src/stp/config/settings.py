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
    include_breathing: bool = False
    surrogate_method: Literal["phase_shuffle", "iaaft"] = "phase_shuffle"

    def for_mode(self) -> "AnalysisParams":
        """Apply mode defaults without stripping user-enabled extensions.

        Fast mode is lighter only when the caller leaves extension flags at
        their defaults. Explicit ``include_tda`` / breathing / memory from the
        Lab or CLI are always respected.
        """
        data = self.model_dump()
        if self.mode == "full":
            # Suggest richer defaults only if still at factory False
            # (Lab sets flags explicitly; CLI may rely on mode.)
            if not self.include_tda and data.get("include_tda") is False:
                # keep False unless caller opted in — Lab checkbox drives this
                pass
        return AnalysisParams(**data)

    def eta_hint(self, n_samples: int = 800, n_vars: int = 2) -> str:
        n_s = self.n_surrogates if self.mode == "fast" else max(self.n_surrogates, 20)
        # crude
        base = 0.5 + 0.15 * (n_samples / 500) * max(n_vars, 2)
        surr = 0.4 * n_s * (1.8 if self.surrogate_method == "iaaft" else 1.0)
        sec = base + surr
        if self.include_breathing:
            sec *= 1.3
        if sec < 3:
            return f"~{sec:.0f}–{sec+2:.0f} s"
        if sec < 30:
            return f"~{sec:.0f} s"
        return f"~{sec/60:.1f} min"


THEME = ThemeColors()

DOMAIN_PRESETS: dict[str, dict] = {
    "cardiology": {
        "window": 101,
        "stride": 5,
        "theta3": 0.08,
        "m": 3,
        "delay": 1,
        "d_persist": 4,
    },
    "epidemiology": {
        "window": 13,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "neuroscience": {
        "window": 51,
        "stride": 2,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 4,
    },
    "ecology": {
        "window": 25,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "finance": {
        "window": 21,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "climate": {
        "window": 21,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "social": {
        "window": 21,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "education": {
        "window": 17,
        "stride": 1,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 3,
    },
    "physiology": {
        "window": 51,
        "stride": 2,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 4,
    },
    "synthetic": {
        "window": 31,
        "stride": 2,
        "theta3": 0.10,
        "m": 3,
        "delay": 1,
        "d_persist": 4,
    },
}

DOMAIN_LABELS = {
    "cardiology": "Cardiología",
    "epidemiology": "Epidemiología",
    "neuroscience": "Neurociencia",
    "ecology": "Ecología",
    "finance": "Finanzas",
    "climate": "Clima e hidrología",
    "social": "Dinámica social",
    "education": "Aprendizaje colectivo",
    "physiology": "Fisiología del sueño",
    "synthetic": "Sintético",
}
