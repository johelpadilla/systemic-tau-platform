"""Smoke tests for core pipeline."""

from __future__ import annotations

import numpy as np

from stp.config.settings import AnalysisParams
from stp.core.ordinal import bandt_pompe_symbols, multivariate_symbols
from stp.core.pipeline import run_analysis
from stp.core.reproducibility import repro_hash
from stp.data.generators import coupled_logistic


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
    result = run_analysis(X, params)
    assert len(result.tau_s) > 0
    assert len(result.excess3) > 0
    assert result.repro_hash
    assert "delta_tau_s" in result.metrics


def test_repro_hash_stable():
    X = np.random.default_rng(0).normal(size=(100, 2))
    p = {"window": 13, "seed": 1}
    h1 = repro_hash(p, X)
    h2 = repro_hash(p, X)
    assert h1 == h2
