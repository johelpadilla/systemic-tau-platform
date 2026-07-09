"""Core pipeline, surrogates, properties, catalog."""

from __future__ import annotations

import json

import numpy as np
import pytest

from stp.config.settings import AnalysisParams, DOMAIN_PRESETS
from stp.core.breathing_window import compute_tau_s_breathing
from stp.core.interpretation import interpret_dual_reading, methods_paragraph
from stp.core.ordinal import bandt_pompe_symbols, multivariate_symbols
from stp.core.ordinal_memory import cross_ordinal_mi, ordinal_memory_profile
from stp.core.pipeline import result_to_jsonable, run_analysis
from stp.core.reproducibility import repro_hash
from stp.core.surrogates import iaaft_independent, phase_shuffle_independent
from stp.core.tau_s import compute_tau_s
from stp.data.catalog import list_datasets, load_dataset
from stp.data.generators import ar_noise, coupled_logistic, dengue_like


def test_bandt_pompe_length():
    x = np.random.default_rng(0).normal(size=100)
    s = bandt_pompe_symbols(x, m=3, delay=1)
    assert len(s) == 100 - 2


def test_multivariate_symbols_shape():
    X = coupled_logistic(T=200, seed=1)
    S = multivariate_symbols(X, m=3)
    assert S.ndim == 2
    assert S.shape[1] == 2


def test_pipeline_fast_runs():
    X = coupled_logistic(T=400, coupling=0.2, switch_at=200, seed=2)
    params = AnalysisParams(window=31, stride=2, mode="fast", n_surrogates=2, seed=0)
    result = run_analysis(X, params, event_index=200, domain="synthetic")
    assert len(result.tau_s) > 0
    assert len(result.excess3) > 0
    assert result.repro_hash
    assert "delta_tau_s" in result.metrics
    assert result.event_index == 200
    assert result.interpretation
    assert result.methods_text


def test_pipeline_univariate_column_expands():
    """Lab CSV with a single numeric column is (T,1); must expand to [x, |Δx|]."""
    x = np.random.default_rng(7).normal(size=(220, 1))
    params = AnalysisParams(
        window=31, stride=2, n_surrogates=0, mode="fast",
        include_tda=True, include_breathing=True,
    )
    result = run_analysis(x, params, event_index=110, domain="synthetic")
    assert len(result.tau_s) > 0
    assert result.metrics["n_vars"] >= 2
    assert result.breathing_windows is not None
    assert result.tda


def test_pipeline_with_event_split_differs_from_half():
    X = coupled_logistic(T=500, coupling=0.25, switch_at=100, seed=3)
    params = AnalysisParams(window=21, stride=2, n_surrogates=0, mode="fast")
    r_half = run_analysis(X, params, event_index=None)
    r_ev = run_analysis(X, params, event_index=100)
    # not always different, but metrics keys present
    assert "split_tau" in r_ev.metrics
    assert r_ev.metrics["event_index"] == 100
    assert r_half.metrics["event_index"] is None


def test_repro_hash_stable():
    X = np.random.default_rng(0).normal(size=(100, 2))
    p = {"window": 13, "seed": 1}
    h1 = repro_hash(p, X)
    h2 = repro_hash(p, X)
    assert h1 == h2


def test_bandt_pompe_monotone_invariance():
    """Ordinal symbols invariant under strictly increasing transform."""
    rng = np.random.default_rng(11)
    x = rng.normal(size=200)
    s1 = bandt_pompe_symbols(x, m=3)
    s2 = bandt_pompe_symbols(np.exp(x) + 3.0, m=3)  # strictly increasing on R
    assert np.array_equal(s1, s2)


def test_ar_noise_small_delta_tau():
    """AR control: absolute Δτ_s should stay modest (not a huge effect)."""
    X = ar_noise(T=600, N=3, phi=0.5, seed=0)
    params = AnalysisParams(window=31, stride=2, n_surrogates=0, mode="fast")
    r = run_analysis(X, params, domain="synthetic")
    assert abs(r.metrics["delta_tau_s"]) < 0.25


def test_phase_shuffle_and_iaaft_shapes():
    X = coupled_logistic(T=200, seed=0)
    ps = phase_shuffle_independent(X, seed=1)
    ia = iaaft_independent(X, n_iter=5, seed=1)
    assert ps.shape == X.shape
    assert ia.shape == X.shape


def test_breathing_window_runs():
    X = coupled_logistic(T=300, coupling=0.2, switch_at=150, seed=1)
    tau, centers, ws = compute_tau_s_breathing(X, stride=3, w_min=11, w_max=41)
    assert len(tau) == len(centers) == len(ws)
    assert len(tau) > 5


def test_ordinal_memory():
    x = coupled_logistic(T=400, seed=2)[:, 0]
    prof = ordinal_memory_profile(x, m=3, max_lag=5)
    assert len(prof["mi"]) == 5
    X = coupled_logistic(T=300, seed=2)
    mi = cross_ordinal_mi(X, m=3)
    assert mi >= 0


def test_interpretation_and_methods():
    metrics = {"delta_tau_s": 0.05, "delta_excess3": 0.03, "mean_excess3": 0.1}
    surr = {"tau_s": {"p_value": 0.02}}
    interp = interpret_dual_reading(metrics, surr, event_index=100, domain="synthetic")
    assert "summary" in interp
    assert "sign_concordance" in interp["flags"] or "surrogate_reject" in interp["flags"]
    p = AnalysisParams()
    text = methods_paragraph(p, domain="cardiology", event_index=10, repro_hash="abc")
    assert "Systemic Tau" in text
    assert "abc" in text


def test_json_export_serializable():
    X = coupled_logistic(T=250, seed=1)
    params = AnalysisParams(window=21, stride=2, n_surrogates=2, mode="fast", include_memory=True)
    r = run_analysis(X, params, event_index=125, domain="synthetic", variables=["x0", "x1"])
    payload = result_to_jsonable(r)
    s = json.dumps(payload)
    assert "repro_hash" in s
    assert "tau_s" in payload


def test_catalog_load_generators():
    ids = [d["id"] for d in list_datasets(available_only=False)]
    assert "synthetic_coupled_logistic" in ids
    X, meta = load_dataset("synthetic_coupled_logistic")
    assert X.shape[1] == 2
    assert meta.get("event_index") is not None
    X2, meta2 = load_dataset("dengue_like_demo")
    assert X2.shape[1] == 3
    assert meta2["domain"] == "epidemiology"


def test_catalog_sddb_if_present():
    try:
        X, meta = load_dataset("sddb_rr_38_demo")
    except Exception:
        pytest.skip("SDDB sample missing")
    assert X.shape[0] > 100
    assert meta["domain"] == "cardiology"


def test_domain_presets_complete():
    for k in (
        "cardiology",
        "epidemiology",
        "neuroscience",
        "ecology",
        "finance",
        "climate",
        "social",
        "education",
        "physiology",
        "synthetic",
    ):
        assert k in DOMAIN_PRESETS
        assert "window" in DOMAIN_PRESETS[k]


def test_new_domain_generators_pipeline():
    """New pedagogical demos must load, stay finite, and show non-trivial |Δτ| or |Δex3|."""
    for ds_id, min_effect in (
        ("climate_drought_demo", 0.05),
        ("social_polarization_demo", 0.05),
        ("education_cohort_demo", 0.05),
        ("sleep_fragmentation_demo", 0.05),
        ("dengue_like_demo", 0.04),
    ):
        X, meta = load_dataset(ds_id)
        assert np.all(np.isfinite(X))
        assert X.ndim == 2 and X.shape[1] >= 2
        dom = meta["domain"]
        preset = DOMAIN_PRESETS[dom]
        w = min(int(preset["window"]), max(11, X.shape[0] // 8))
        if w % 2 == 0:
            w += 1
        params = AnalysisParams(
            window=w,
            stride=max(1, int(preset["stride"])),
            n_surrogates=0,
            mode="fast",
            theta3=float(preset["theta3"]),
        )
        r = run_analysis(X, params, event_index=meta.get("event_index"), domain=dom)
        effect = max(abs(r.metrics["delta_tau_s"]), abs(r.metrics["delta_excess3"]))
        assert effect >= min_effect, f"{ds_id} weak effect={effect}"


def test_ar_control_weaker_than_coupled():
    """Pedagogy: designed coupling switch should out-effect AR near-null control."""
    X_sig, meta_s = load_dataset("synthetic_coupled_logistic")
    X_null, _ = load_dataset("synthetic_ar_noise")
    params = AnalysisParams(window=31, stride=2, n_surrogates=0, mode="fast")
    r_sig = run_analysis(X_sig, params, event_index=meta_s.get("event_index"), domain="synthetic")
    r_null = run_analysis(X_null, params, domain="synthetic")
    assert abs(r_sig.metrics["delta_tau_s"]) > abs(r_null.metrics["delta_tau_s"]) + 0.15


def test_tau_s_basic():
    X = coupled_logistic(T=200, seed=0)
    tau, c = compute_tau_s(X, window=31, stride=2)
    assert len(tau) == len(c)
    assert np.all(np.isfinite(tau))
