"""Null models: independent phase-shuffle per column."""

from __future__ import annotations

import numpy as np


def phase_shuffle_independent(X: np.ndarray, seed: int = 0) -> np.ndarray:
    """Preserve approximate power spectrum of each column; destroy cross-dependence."""
    rng = np.random.default_rng(seed)
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]
    out = np.empty_like(X)
    for j in range(X.shape[1]):
        col = X[:, j]
        fft = np.fft.rfft(col)
        mag = np.abs(fft)
        phase = rng.uniform(0, 2 * np.pi, size=len(fft))
        phase[0] = 0.0
        if len(phase) > 1:
            phase[-1] = 0.0 if len(col) % 2 == 0 else phase[-1]
        shuffled = np.fft.irfft(mag * np.exp(1j * phase), n=len(col))
        out[:, j] = shuffled.real
    return out


def surrogate_delta_metric(
    X: np.ndarray,
    metric_fn,
    n: int = 8,
    seed: int = 42,
    split: int | None = None,
) -> dict:
    """
    Compare observed Δmetric (second half - first half, or custom split)
    against phase-shuffle nulls.
    """
    X = np.asarray(X, dtype=float)
    obs = metric_fn(X)
    if split is None:
        split = len(obs) // 2
    if len(obs) < 4:
        return {"observed_delta": 0.0, "null_deltas": [], "p_value": 1.0}

    obs_delta = float(np.nanmean(obs[split:]) - np.nanmean(obs[:split]))
    nulls = []
    for i in range(n):
        Xs = phase_shuffle_independent(X, seed=seed + i)
        m = metric_fn(Xs)
        if len(m) < 4:
            continue
        sp = len(m) // 2
        nulls.append(float(np.nanmean(m[sp:]) - np.nanmean(m[:sp])))
    nulls = np.asarray(nulls) if nulls else np.array([0.0])
    # two-sided
    p = float(np.mean(np.abs(nulls) >= abs(obs_delta))) if len(nulls) else 1.0
    return {
        "observed_delta": obs_delta,
        "null_deltas": nulls,
        "p_value": max(p, 1.0 / (n + 1)),
        "n": n,
    }
