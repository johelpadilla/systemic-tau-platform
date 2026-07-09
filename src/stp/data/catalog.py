"""Dataset catalog loader + sample resolution."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from stp.config.settings import DATA_DIR, DOMAIN_PRESETS, SAMPLES_DIR


def _generators():
    """Lazy import so a stale generators module cannot break catalog load."""
    from stp.data import generators as g

    return g


@lru_cache(maxsize=1)
def load_catalog() -> dict[str, Any]:
    path = DATA_DIR / "catalog" / "datasets.yaml"
    if not path.exists():
        return {"datasets": {}}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data


def list_datasets(domain: str | None = None, available_only: bool = True) -> list[dict[str, Any]]:
    cat = load_catalog().get("datasets") or {}
    out = []
    for key, meta in cat.items():
        item = {"id": key, **meta}
        if domain and item.get("domain") != domain:
            continue
        if available_only and item.get("status") == "pending_export":
            # still allow if path exists or generator
            path = item.get("path")
            if path and not (DATA_DIR / path).exists() and not item.get("generator"):
                continue
        out.append(item)
    return out


def resolve_sample_path(rel: str | None) -> Path | None:
    if not rel:
        return None
    p = DATA_DIR / rel
    if p.exists():
        return p
    # try samples/ basename
    alt = SAMPLES_DIR / Path(rel).name
    return alt if alt.exists() else None


def load_dataset(dataset_id: str, **gen_kw) -> tuple[np.ndarray, dict[str, Any]]:
    """
    Load matrix X and metadata (domain, event_index, variables, title, ...).
    """
    cat = load_catalog().get("datasets") or {}
    if dataset_id not in cat:
        raise KeyError(f"Unknown dataset: {dataset_id}")
    meta = dict(cat[dataset_id])
    meta["id"] = dataset_id
    domain = meta.get("domain", "synthetic")
    event = meta.get("event_index")
    if event is None and meta.get("event_fraction") is not None:
        # filled after load for generators
        pass

    path = resolve_sample_path(meta.get("path"))
    if path is not None:
        df = pd.read_csv(path)
        vars_ = meta.get("variables") or list(df.select_dtypes(include=[np.number]).columns)
        vars_ = [v for v in vars_ if v in df.columns]
        if not vars_:
            vars_ = list(df.select_dtypes(include=[np.number]).columns)[:3]
        X = df[vars_].to_numpy(dtype=float)
        meta["variables"] = vars_
        if event is None and meta.get("event_fraction") is not None:
            event = int(float(meta["event_fraction"]) * len(X))
        meta["event_index"] = event
        meta["source"] = str(path.name)
        return X, meta

    gen = meta.get("generator")
    T = int(gen_kw.get("T", meta.get("T", 800)))
    seed = int(gen_kw.get("seed", meta.get("seed", 0)))
    g = _generators()

    def _event_at(default_frac: float) -> int:
        """Prefer explicit event_at kw, then YAML event_index / event_fraction."""
        if "event_at" in gen_kw:
            return int(gen_kw["event_at"])
        if "switch_at" in gen_kw:
            return int(gen_kw["switch_at"])
        if meta.get("event_index") is not None:
            return int(meta["event_index"])
        frac = meta.get("event_fraction", default_frac)
        if frac is None:
            return T // 2
        return int(float(frac) * T)

    # name -> (callable kwargs builder, default event frac or None, variables)
    if gen == "coupled_logistic":
        switch = _event_at(0.5)
        X = g.coupled_logistic(T=T, coupling=0.18, switch_at=switch, seed=seed)
        meta["event_index"] = switch
        meta["variables"] = list(meta.get("variables") or ["x0", "x1"])
    elif gen == "ar_noise":
        X = g.ar_noise(T=T, N=3, seed=seed)
        meta["event_index"] = None
        meta["variables"] = list(meta.get("variables") or ["x0", "x1", "x2"])
    elif gen in getattr(g, "GENERATOR_REGISTRY", {}):
        fn = g.GENERATOR_REGISTRY[gen]
        # Generators with event_at keyword
        import inspect

        sig = inspect.signature(fn)
        kwargs: dict[str, Any] = {"T": T, "seed": seed}
        if "event_at" in sig.parameters:
            kwargs["event_at"] = _event_at(0.6)
        if "switch_at" in sig.parameters:
            kwargs["switch_at"] = _event_at(0.5)
        if "N" in sig.parameters and gen == "ar_noise":
            kwargs["N"] = 3
        X = fn(**{k: v for k, v in kwargs.items() if k in sig.parameters})
        if "event_at" in kwargs:
            meta["event_index"] = kwargs["event_at"]
        elif "switch_at" in kwargs:
            meta["event_index"] = kwargs["switch_at"]
        # Prefer YAML variables; fall back to sensible defaults
        defaults = {
            "cardiac_like_rr": ["rr", "abs_drr"],
            "dengue_like": ["cases", "rain", "temp"],
            "eeg_like": ["ch0", "ch1", "ch2"],
            "ecology_like": ["chl_a", "phos", "do"],
            "finance_like": ["ret", "vol", "spread"],
            "climate_like": ["temp_anom", "precip", "soil_moisture"],
            "social_like": ["opinion_a", "opinion_b", "interaction"],
            "education_like": ["engagement", "peer_sync", "cognitive_load"],
            "sleep_like": ["hrv", "activity", "core_temp"],
            "coupled_logistic": ["x0", "x1"],
            "ar_noise": ["x0", "x1", "x2"],
        }
        meta["variables"] = list(meta.get("variables") or defaults.get(gen, [f"x{i}" for i in range(X.shape[1])]))
    else:
        raise ValueError(f"No path or known generator for {dataset_id}")

    meta["source"] = f"generator:{gen}"
    meta.setdefault("default_params", DOMAIN_PRESETS.get(domain, DOMAIN_PRESETS["synthetic"]))
    return X, meta


def dataset_title(dataset: dict | str) -> str:
    """Localized catalog title; falls back to YAML title."""
    if isinstance(dataset, str):
        ds_id = dataset
        title = dataset
        cat = load_catalog().get("datasets") or {}
        if ds_id in cat:
            title = cat[ds_id].get("title", ds_id)
    else:
        ds_id = dataset.get("id", "")
        title = dataset.get("title", ds_id)
    try:
        from stp.i18n.core import t

        key = f"catalog.{ds_id}"
        val = t(key)
        if val != key:
            return val
    except Exception:
        pass
    return str(title)
