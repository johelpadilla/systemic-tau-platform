"""Ordinal memory — symbolic mutual information across lag (educational)."""

from __future__ import annotations

import numpy as np

from stp.core.ordinal import bandt_pompe_symbols


def _symbol_mi(a: np.ndarray, b: np.ndarray, n_sym: int) -> float:
    """Mutual information (nats) between two integer symbol series of equal length."""
    a = np.asarray(a, dtype=int)
    b = np.asarray(b, dtype=int)
    n = min(len(a), len(b))
    if n < 8:
        return 0.0
    a, b = a[:n], b[:n]
    joint = np.zeros((n_sym, n_sym), dtype=float)
    for i, j in zip(a, b):
        if 0 <= i < n_sym and 0 <= j < n_sym:
            joint[i, j] += 1.0
    joint /= joint.sum() + 1e-15
    pa = joint.sum(axis=1)
    pb = joint.sum(axis=0)
    mi = 0.0
    for i in range(n_sym):
        for j in range(n_sym):
            if joint[i, j] <= 0:
                continue
            mi += joint[i, j] * np.log((joint[i, j] + 1e-15) / (pa[i] * pb[j] + 1e-15))
    return float(mi)


def ordinal_memory_profile(
    x: np.ndarray,
    m: int = 3,
    delay: int = 1,
    max_lag: int = 10,
) -> dict:
    """
    Self ordinal MI at lags 1..max_lag (memory of pattern sequence).

    Returns dict with lags, mi, half_life_est.
    """
    x = np.asarray(x, dtype=float).ravel()
    n_sym = 1
    for k in range(2, m + 1):
        n_sym *= k

    sym = bandt_pompe_symbols(x, m=m, delay=delay)
    lags = list(range(1, max_lag + 1))
    mis = []
    for lag in lags:
        if lag >= len(sym):
            mis.append(0.0)
            continue
        mis.append(_symbol_mi(sym[:-lag], sym[lag:], n_sym))
    mis_arr = np.asarray(mis, dtype=float)
    # crude half-life: first lag where MI < half of lag-1
    half = None
    if len(mis_arr) and mis_arr[0] > 1e-9:
        thr = 0.5 * mis_arr[0]
        for lag, v in zip(lags, mis_arr):
            if v <= thr:
                half = lag
                break
    return {
        "lags": np.asarray(lags, dtype=int),
        "mi": mis_arr,
        "half_life_est": half,
        "mi_lag1": float(mis_arr[0]) if len(mis_arr) else 0.0,
    }


def cross_ordinal_mi(
    X: np.ndarray,
    m: int = 3,
    delay: int = 1,
    lag: int = 0,
) -> float:
    """Mean pairwise cross-variable ordinal MI (lag applied to second series)."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        return ordinal_memory_profile(X, m=m, delay=delay, max_lag=max(1, lag or 1))["mi_lag1"]
    n_sym = 1
    for k in range(2, m + 1):
        n_sym *= k
    N = X.shape[1]
    vals = []
    for i in range(N):
        for j in range(i + 1, N):
            si = bandt_pompe_symbols(X[:, i], m=m, delay=delay)
            sj = bandt_pompe_symbols(X[:, j], m=m, delay=delay)
            if lag > 0:
                if lag >= len(si) or lag >= len(sj):
                    continue
                vals.append(_symbol_mi(si[:-lag], sj[lag:], n_sym))
            else:
                n = min(len(si), len(sj))
                vals.append(_symbol_mi(si[:n], sj[:n], n_sym))
    return float(np.mean(vals)) if vals else 0.0
