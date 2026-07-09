"""TDA Betti + breathing extensions in pipeline."""

from __future__ import annotations

import numpy as np

from stp.config.settings import AnalysisParams
from stp.core.pipeline import run_analysis, result_to_jsonable
from stp.core.tda_betti import (
    betti_vr_skeleton,
    delay_embed_multivariate,
    has_ripser,
    sliding_betti,
    tda_summary,
)
from stp.data.generators import coupled_logistic


def test_delay_embed_and_betti_skeleton():
    X = coupled_logistic(T=200, seed=0)
    pts = delay_embed_multivariate(X[:80], m=3, delay=1, max_points=40)
    assert pts.ndim == 2 and pts.shape[0] >= 5
    b = betti_vr_skeleton(pts, radius_quantile=0.4)
    assert b["beta0"] >= 1
    assert b["beta1"] >= 0


def test_sliding_betti_shapes():
    X = coupled_logistic(T=300, coupling=0.2, switch_at=150, seed=1)
    tda = sliding_betti(X, window=41, stride=5, max_points=40, prefer_ripser=False)
    assert len(tda["centers"]) == len(tda["beta0"]) == len(tda["beta1"])
    assert len(tda["centers"]) > 5
    s = tda_summary(tda, event_index=150)
    assert "delta_beta0" in s and "mean_beta1" in s


def test_pipeline_with_breathing_and_tda():
    X = coupled_logistic(T=350, coupling=0.22, switch_at=175, seed=2)
    params = AnalysisParams(
        window=31,
        stride=3,
        n_surrogates=0,
        mode="fast",
        include_breathing=True,
        include_tda=True,
        include_memory=False,
        include_ews=True,
    )
    r = run_analysis(X, params, event_index=175, domain="synthetic")
    assert r.breathing_windows is not None
    assert len(r.breathing_windows) == len(r.tau_s)
    assert r.tda and "beta0" in r.tda
    assert r.metrics.get("tda") is True
    assert r.metrics.get("breathing") is True
    assert "delta_beta0" in r.metrics
    assert "breathing" in (r.methods_text or "").lower() or "Breathing" in (r.methods_text or "")
    payload = result_to_jsonable(r)
    assert "tda" in payload and payload["tda"].get("beta0") is not None
    # interpretation mentions extension when TDA on
    flags = (r.interpretation or {}).get("flags") or []
    assert "breathing" in flags or any("TDA" in b for b in (r.interpretation or {}).get("bullets") or [])


def test_has_ripser_bool():
    assert isinstance(has_ripser(), bool)
