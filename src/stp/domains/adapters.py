"""Concrete domain adapters with column heuristics and event detection."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from stp.config.settings import DOMAIN_PRESETS
from stp.domains.base import DomainAdapter, DomainBundle, select_numeric


class CardiologyAdapter(DomainAdapter):
    domain = "cardiology"
    label = "Cardiología"
    suggested_columns = ["z_rr", "z_abs_drr", "rr_ms", "abs_drr"]
    default_params = dict(DOMAIN_PRESETS["cardiology"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        # prefer CCTP proxy columns
        prefer = [c for c in ("z_rr", "z_abs_drr") if c in num.columns]
        if len(prefer) >= 2:
            use = prefer
        elif "rr_ms" in num.columns:
            rr = num["rr_ms"].to_numpy(dtype=float)
            drr = num["abs_drr"].to_numpy(dtype=float) if "abs_drr" in num.columns else np.abs(
                np.diff(rr, prepend=rr[0])
            )
            X = np.column_stack([rr, drr])
            return DomainBundle(
                X=X,
                domain=self.domain,
                variables=["rr_ms", "abs_drr"],
                event_index=kw.get("event_index"),
                event_label=kw.get("event_label", "VFON / evento"),
                meta={"adapter": self.domain},
                source=kw.get("source", "csv"),
            )
        else:
            use = list(num.columns)[: min(3, num.shape[1])]
        X = num[use].to_numpy(dtype=float)
        return DomainBundle(
            X=X,
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "evento"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Cardio: preferir z_rr + z_abs_drr (proxy CCTP) o rr_ms + abs_drr. W≈101, θ₃≈0.08."


class EpidemiologyAdapter(DomainAdapter):
    domain = "epidemiology"
    label = "Epidemiología"
    suggested_columns = ["cases", "cases_z", "rain", "temp", "humidity"]
    default_params = dict(DOMAIN_PRESETS["epidemiology"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [c for c in ("cases_z", "rain", "temp", "cases", "humidity") if c in num.columns]
        use = prefer[:3] if prefer else list(num.columns)[: min(3, num.shape[1])]
        X = num[use].to_numpy(dtype=float)
        return DomainBundle(
            X=X,
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "inicio de brote"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Epi: cases (+ clima). Ventanas cortas (W≈13). Marque el inicio del brote."


class NeuroscienceAdapter(DomainAdapter):
    domain = "neuroscience"
    label = "Neurociencia"
    suggested_columns = ["ch0", "ch1", "ch2", "eeg_a", "eeg_b"]
    default_params = dict(DOMAIN_PRESETS["neuroscience"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        use = list(num.columns)[: min(4, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "onset ictal"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )


class EcologyAdapter(DomainAdapter):
    domain = "ecology"
    label = "Ecología"
    suggested_columns = ["chl_a", "phos", "do", "temp"]
    default_params = dict(DOMAIN_PRESETS["ecology"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [c for c in ("chl_a", "phos", "do", "temp") if c in num.columns]
        use = prefer if prefer else list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "umbral / bloom"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )


class FinanceAdapter(DomainAdapter):
    domain = "finance"
    label = "Finanzas"
    suggested_columns = ["ret", "vol", "spread", "close"]
    default_params = dict(DOMAIN_PRESETS["finance"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        if "close" in num.columns and "ret" not in num.columns:
            close = num["close"].to_numpy(dtype=float)
            ret = np.diff(np.log(np.clip(close, 1e-12, None)), prepend=0.0)
            vol = pd.Series(ret).rolling(5, min_periods=1).std().to_numpy()
            X = np.column_stack([ret, vol])
            return DomainBundle(
                X=X,
                domain=self.domain,
                variables=["ret", "roll_vol"],
                event_index=kw.get("event_index"),
                event_label=kw.get("event_label", "crisis / régimen"),
                meta={"adapter": self.domain},
                source=kw.get("source", "csv"),
            )
        use = list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "crisis / régimen"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )


class ClimateAdapter(DomainAdapter):
    domain = "climate"
    label = "Clima e hidrología"
    suggested_columns = ["temp_anom", "precip", "soil_moisture", "temp", "rain"]
    default_params = dict(DOMAIN_PRESETS["climate"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [
            c
            for c in ("temp_anom", "precip", "soil_moisture", "temp", "rain", "soil")
            if c in num.columns
        ]
        use = prefer[:3] if prefer else list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "inicio de sequía / régimen"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Clima: temp + precip + humedad de suelo. W≈21. Marque el inicio del régimen seco."


class SocialAdapter(DomainAdapter):
    domain = "social"
    label = "Dinámica social"
    suggested_columns = ["opinion_a", "opinion_b", "interaction", "engagement"]
    default_params = dict(DOMAIN_PRESETS["social"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [
            c
            for c in ("opinion_a", "opinion_b", "interaction", "polarization")
            if c in num.columns
        ]
        use = prefer[:3] if prefer else list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "cascada de polarización"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Social: dos opiniones + intensidad de interacción. Demo pedagógica, no predicción social."


class EducationAdapter(DomainAdapter):
    domain = "education"
    label = "Aprendizaje colectivo"
    suggested_columns = ["engagement", "peer_sync", "cognitive_load", "mastery"]
    default_params = dict(DOMAIN_PRESETS["education"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [
            c
            for c in ("engagement", "peer_sync", "cognitive_load", "mastery", "load")
            if c in num.columns
        ]
        use = prefer[:3] if prefer else list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "reorganización del curso"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Aprendizaje: engagement + peer_sync + carga cognitiva. Ideal para docencia del método."


class PhysiologyAdapter(DomainAdapter):
    domain = "physiology"
    label = "Fisiología del sueño"
    suggested_columns = ["hrv", "activity", "core_temp", "temp"]
    default_params = dict(DOMAIN_PRESETS["physiology"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        prefer = [c for c in ("hrv", "activity", "core_temp", "temp") if c in num.columns]
        use = prefer[:3] if prefer else list(num.columns)[: min(3, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "fragmentación del sueño"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )

    def hint(self) -> str:
        return "Sueño: HRV + actividad + temp. W≈51. Puente fisiológico con cardiología."


class SyntheticAdapter(DomainAdapter):
    domain = "synthetic"
    label = "Sintético"
    suggested_columns = ["x0", "x1", "x2"]
    default_params = dict(DOMAIN_PRESETS["synthetic"])

    def prepare(self, df: pd.DataFrame, columns: list[str] | None = None, **kw) -> DomainBundle:
        num = select_numeric(df, columns)
        use = list(num.columns)[: min(4, num.shape[1])]
        return DomainBundle(
            X=num[use].to_numpy(dtype=float),
            domain=self.domain,
            variables=list(use),
            event_index=kw.get("event_index"),
            event_label=kw.get("event_label", "switch"),
            meta={"adapter": self.domain},
            source=kw.get("source", "csv"),
        )


ADAPTERS: dict[str, DomainAdapter] = {
    "cardiology": CardiologyAdapter(),
    "epidemiology": EpidemiologyAdapter(),
    "neuroscience": NeuroscienceAdapter(),
    "ecology": EcologyAdapter(),
    "finance": FinanceAdapter(),
    "climate": ClimateAdapter(),
    "social": SocialAdapter(),
    "education": EducationAdapter(),
    "physiology": PhysiologyAdapter(),
    "synthetic": SyntheticAdapter(),
}


def get_adapter(domain: str) -> DomainAdapter:
    return ADAPTERS.get(domain, SyntheticAdapter())


def domain_hint(domain: str) -> str:
    """Localized short hint for Lab/UI; falls back to adapter Spanish hint."""
    try:
        from stp.i18n.core import t

        key = f"domain_hints.{domain}"
        val = t(key)
        if val != key:
            return val
    except Exception:
        pass
    return get_adapter(domain).hint()


def domain_label(domain: str) -> str:
    """Localized domain display name."""
    try:
        from stp.i18n.core import t

        key = f"domains.{domain}"
        val = t(key)
        if val != key:
            return val
    except Exception:
        pass
    from stp.config.settings import DOMAIN_LABELS

    return DOMAIN_LABELS.get(domain, domain)


def estimate_runtime_seconds(n_samples: int, n_vars: int, params: dict[str, Any]) -> float:
    """Rough Lab ETA (seconds) for UI feedback."""
    w = int(params.get("window", 51))
    stride = int(params.get("stride", 2))
    n_surr = int(params.get("n_surrogates", 8))
    n_win = max(1, (n_samples - w) // max(stride, 1))
    base = 0.0008 * n_win * max(n_vars, 2) ** 1.5
    surr = 0.6 * n_surr * base
    ews = 0.3 * base
    recd = 0.4 * base
    total = base + surr + ews + recd
    if params.get("include_breathing"):
        total *= 1.4
    if params.get("include_memory"):
        total *= 1.15
    if params.get("surrogate_method") == "iaaft":
        total *= 1.8
    return float(max(0.3, total))
