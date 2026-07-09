"""End-to-end analysis pipeline for the Interactive Lab."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from stp.config.settings import AnalysisParams
from stp.core.breathing_window import compute_tau_s_breathing
from stp.core.ews_classical import classical_ews_bundle
from stp.core.interpretation import interpret_dual_reading, methods_paragraph
from stp.core.ordinal_memory import cross_ordinal_mi, ordinal_memory_profile
from stp.core.recd_levels import compute_recd_from_conjunctions
from stp.core.reproducibility import repro_hash
from stp.core.surrogates import surrogate_delta_metric
from stp.core.tau_s import compute_tau_s, ensure_multivariate
from stp.core.tda_betti import has_ripser, sliding_betti, tda_summary
from stp import __version__


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
    event_index: int | None = None
    domain: str = "generic"
    interpretation: dict[str, Any] = field(default_factory=dict)
    methods_text: str = ""
    breathing_windows: np.ndarray | None = None
    memory: dict[str, Any] = field(default_factory=dict)
    tda: dict[str, Any] = field(default_factory=dict)
    variables: list[str] = field(default_factory=list)


def _prepare_X(X: np.ndarray, zscore: bool) -> np.ndarray:
    """Z-score columns after ensuring N≥2 (univariate → [x, |Δx|] proxy)."""
    X = ensure_multivariate(X)
    if zscore:
        out = np.zeros_like(X)
        for j in range(X.shape[1]):
            col = X[:, j]
            s = np.nanstd(col)
            out[:, j] = (col - np.nanmean(col)) / s if s > 1e-12 else 0.0
        return out
    return X


def _split_for_centers(centers: np.ndarray, event_index: int | None) -> int | None:
    """Index into metric series corresponding to event in original time."""
    if event_index is None or len(centers) < 4:
        return None
    # first center >= event
    idx = int(np.searchsorted(centers, event_index, side="left"))
    return int(np.clip(idx, 1, len(centers) - 1))


def _delta(arr: np.ndarray, split: int | None = None) -> float:
    arr = np.asarray(arr, dtype=float)
    if len(arr) < 4:
        return 0.0
    sp = split if split is not None else len(arr) // 2
    sp = int(np.clip(sp, 1, len(arr) - 1))
    return float(np.nanmean(arr[sp:]) - np.nanmean(arr[:sp]))


def run_analysis(
    X: np.ndarray,
    params: AnalysisParams | None = None,
    *,
    event_index: int | None = None,
    domain: str = "generic",
    variables: list[str] | None = None,
) -> AnalysisResult:
    params = (params or AnalysisParams()).for_mode()
    Xp = _prepare_X(X, zscore=params.zscore)

    breathing_w = None
    if params.include_breathing:
        tau_s, tau_centers, breathing_w = compute_tau_s_breathing(
            Xp,
            stride=params.stride,
            w_min=max(5, params.window // 4 * 2 + 1),
            w_max=params.window,
            zscore=False,
        )
    else:
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

    tau_split = _split_for_centers(tau_centers, event_index)
    recd_t = np.arange(len(recd["excess3"]))
    recd_split = _split_for_centers(recd_t, event_index)

    surr: dict[str, Any] = {}
    if params.n_surrogates > 0:

        def _tau_metric(arr: np.ndarray) -> np.ndarray:
            t, _ = compute_tau_s(arr, window=params.window, stride=params.stride, zscore=True)
            return t

        # map event to surrogate metric index: use fraction of time
        surr_split = None
        if event_index is not None and Xp.shape[0] > 0:
            # approximate: half of metric length * event fraction
            pass  # filled inside via centers length after first call
        surr["tau_s"] = surrogate_delta_metric(
            Xp,
            _tau_metric,
            n=params.n_surrogates,
            seed=params.seed,
            split=tau_split,
            method=params.surrogate_method,
        )

    memory: dict[str, Any] = {}
    if params.include_memory:
        memory["self_ch0"] = ordinal_memory_profile(Xp[:, 0], m=params.m, delay=params.delay)
        memory["cross_mi"] = float(cross_ordinal_mi(Xp, m=params.m, delay=params.delay))

    tda: dict[str, Any] = {}
    if params.include_tda:
        # Slightly coarser stride for TDA cost; still pedagogically informative
        tda_stride = max(params.stride, max(2, params.window // 10))
        tda = sliding_betti(
            Xp,
            window=params.window,
            stride=tda_stride,
            embed_m=min(params.m, 3),
            embed_delay=params.delay,
            max_points=50 if params.mode == "fast" else 70,
            prefer_ripser=True,
        )
        # keep only array-like keys serializable + backend name
        tda = {
            "centers": tda["centers"],
            "beta0": tda["beta0"],
            "beta1": tda["beta1"],
            "radius": tda["radius"],
            "backend_name": tda.get("backend_name", "vr_skeleton"),
        }

    metrics = {
        "mean_tau_s": float(np.nanmean(tau_s)) if len(tau_s) else 0.0,
        "delta_tau_s": _delta(tau_s, tau_split),
        "mean_excess3": float(np.nanmean(recd["excess3"])) if len(recd["excess3"]) else 0.0,
        "delta_excess3": _delta(recd["excess3"], recd_split),
        "final_T_recd": float(recd["T_recd"][-1]) if len(recd["T_recd"]) else 0.0,
        "event_index": event_index,
        "split_tau": tau_split,
        "n_samples": int(Xp.shape[0]),
        "n_vars": int(Xp.shape[1]),
        "breathing": bool(params.include_breathing),
        "tda": bool(params.include_tda),
    }
    if memory:
        metrics["ordinal_cross_mi"] = memory.get("cross_mi", 0.0)
        metrics["ordinal_mi_lag1"] = float(memory.get("self_ch0", {}).get("mi_lag1", 0.0))
    if tda:
        metrics.update(tda_summary(tda, event_index=event_index))
        metrics["tda_backend"] = str(tda.get("backend_name", "vr_skeleton"))

    h = repro_hash(
        params.model_dump(),
        Xp,
        extra={"event_index": event_index, "domain": domain},
    )
    interpretation = interpret_dual_reading(
        metrics, surr, event_index=event_index, domain=domain
    )
    methods = methods_paragraph(
        params,
        domain=domain,
        event_index=event_index,
        surrogate_method=params.surrogate_method,
        n=params.n_surrogates,
        repro_hash=h,
    )

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
        lib_versions={
            "stp": __version__,
            "numpy": np.__version__,
            "tda_backend": (
                "ripser" if (params.include_tda and has_ripser()) else
                ("vr_skeleton" if params.include_tda else "off")
            ),
        },
        event_index=event_index,
        domain=domain,
        interpretation=interpretation,
        methods_text=methods,
        breathing_windows=breathing_w,
        memory=memory,
        tda=tda,
        variables=list(variables or []),
    )


def result_to_jsonable(result: AnalysisResult) -> dict[str, Any]:
    """Serialize AnalysisResult for JSON export (arrays as lists)."""

    def arr(a):
        if a is None:
            return None
        return np.asarray(a).tolist()

    surr = {}
    for k, v in (result.surrogate_stats or {}).items():
        if isinstance(v, dict):
            surr[k] = {
                sk: (arr(sv) if isinstance(sv, np.ndarray) else sv) for sk, sv in v.items()
            }
        else:
            surr[k] = v

    mem = {}
    for k, v in (result.memory or {}).items():
        if isinstance(v, dict):
            mem[k] = {
                sk: (arr(sv) if isinstance(sv, np.ndarray) else sv) for sk, sv in v.items()
            }
        else:
            mem[k] = v

    return {
        "repro_hash": result.repro_hash,
        "domain": result.domain,
        "event_index": result.event_index,
        "variables": result.variables,
        "params": result.params.model_dump(),
        "metrics": result.metrics,
        "interpretation": result.interpretation,
        "methods_text": result.methods_text,
        "lib_versions": result.lib_versions,
        "tau_s": arr(result.tau_s),
        "tau_centers": arr(result.tau_centers),
        "excess3": arr(result.excess3),
        "phi1": arr(result.phi1),
        "phi2": arr(result.phi2),
        "phi3": arr(result.phi3),
        "T_recd": arr(result.T_recd),
        "ews": {k: arr(v) for k, v in (result.ews or {}).items()},
        "surrogate_stats": surr,
        "memory": mem,
        "breathing_windows": arr(result.breathing_windows),
        "tda": {
            k: (arr(v) if isinstance(v, np.ndarray) else v)
            for k, v in (result.tda or {}).items()
        },
    }
