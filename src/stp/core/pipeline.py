"""End-to-end analysis pipeline for the Interactive Lab."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from stp.config.settings import AnalysisParams
from stp.core.ews_classical import classical_ews_bundle
from stp.core.recd_levels import compute_recd_from_conjunctions
from stp.core.reproducibility import repro_hash
from stp.core.surrogates import surrogate_delta_metric
from stp.core.tau_s import compute_tau_s


@dataclass
class AnalysisResult:
    tau_s: np.ndarray
    tau_centers: np.ndarray
    phi1: np.ndarray
    phi2: np.ndarray
    phi3: np.ndarray
    excess3: np.ndarray
    T_recd: np.ndarray
    ews: dict[str, np.ndarray]
    surrogate_stats: dict[str, Any]
    metrics: dict[str, Any]
    params: AnalysisParams
    repro_hash: str
    lib_versions: dict[str, str] = field(default_factory=dict)


def _prepare_X(X: np.ndarray, zscore: bool) -> np.ndarray:
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        logging.info("El array de entrada es 1D. Expandiendo a 2D (proxy bivariado con primera derivada absoluta).")
        dx = np.abs(np.diff(X, prepend=X[0]))
        X = np.column_stack([X, dx])
    if zscore:
        out = np.zeros_like(X)
        for j in range(X.shape[1]):
            col = X[:, j]
            s = np.nanstd(col)
            out[:, j] = (col - np.nanmean(col)) / s if s > 1e-12 else 0.0
        return out
    return X


def run_analysis(X: np.ndarray, params: AnalysisParams | None = None) -> AnalysisResult:
    params = (params or AnalysisParams()).for_mode()
    Xp = _prepare_X(X, zscore=params.zscore)

    tau_s, tau_centers = compute_tau_s(
        Xp, window=params.window, stride=params.stride, zscore=False
    )
    recd = compute_recd_from_conjunctions(
        Xp,
        m=params.m,
        delay=params.delay,
        d=params.d_persist,
        theta3=params.theta3,
        phi_window=min(params.window, 51),
    )

    ews: dict[str, np.ndarray] = {}
    if params.include_ews:
        ews = classical_ews_bundle(Xp, window=params.window, stride=params.stride)

    surr: dict[str, Any] = {}
    if params.n_surrogates > 0:

        def _tau_metric(arr: np.ndarray) -> np.ndarray:
            t, _ = compute_tau_s(arr, window=params.window, stride=params.stride, zscore=True)
            return t

        surr["tau_s"] = surrogate_delta_metric(
            Xp, _tau_metric, n=params.n_surrogates, seed=params.seed
        )

    half = len(tau_s) // 2
    metrics = {
        "mean_tau_s": float(np.nanmean(tau_s)) if len(tau_s) else 0.0,
        "delta_tau_s": float(np.nanmean(tau_s[half:]) - np.nanmean(tau_s[:half]))
        if len(tau_s) >= 4
        else 0.0,
        "mean_excess3": float(np.nanmean(recd["excess3"])) if len(recd["excess3"]) else 0.0,
        "delta_excess3": float(
            np.nanmean(recd["excess3"][len(recd["excess3"]) // 2 :])
            - np.nanmean(recd["excess3"][: len(recd["excess3"]) // 2])
        )
        if len(recd["excess3"]) >= 4
        else 0.0,
        "final_T_recd": float(recd["T_recd"][-1]) if len(recd["T_recd"]) else 0.0,
    }

    h = repro_hash(params.model_dump(), Xp)
    return AnalysisResult(
        tau_s=tau_s,
        tau_centers=tau_centers,
        phi1=recd["phi1"],
        phi2=recd["phi2"],
        phi3=recd["phi3"],
        excess3=recd["excess3"],
        T_recd=recd["T_recd"],
        ews=ews,
        surrogate_stats=surr,
        metrics=metrics,
        params=params,
        repro_hash=h,
        lib_versions={"stp": "1.0.0", "numpy": np.__version__},
    )
