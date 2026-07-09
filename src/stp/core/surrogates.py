"""Null models: phase-shuffle and IAAFT (per column, independent)."""

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


def iaaft_column(x: np.ndarray, n_iter: int = 20, seed: int = 0) -> np.ndarray:
    """
    Iterative Amplitude Adjusted Fourier Transform surrogate (single series).

    Preserves amplitude distribution and approximately the power spectrum.
    """
    rng = np.random.default_rng(seed)
    x = np.asarray(x, dtype=float).ravel()
    n = len(x)
    # sorted amplitudes (target distribution)
    x_sorted = np.sort(x)
    # start from random shuffle of values
    y = rng.permutation(x)
    mag = np.abs(np.fft.rfft(x))
    for _ in range(n_iter):
        # match spectrum
        y_fft = np.fft.rfft(y)
        phase = np.angle(y_fft)
        y = np.fft.irfft(mag * np.exp(1j * phase), n=n).real
        # match amplitude distribution via rank replace
        ranks = np.argsort(np.argsort(y))
        y = x_sorted[ranks]
    return y


def iaaft_independent(X: np.ndarray, n_iter: int = 20, seed: int = 0) -> np.ndarray:
    """IAAFT independently per column (breaks cross-dependence, keeps marginal spectrum+PDF)."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]
    out = np.empty_like(X)
    for j in range(X.shape[1]):
        out[:, j] = iaaft_column(X[:, j], n_iter=n_iter, seed=seed + 17 * j)
    return out


def make_surrogate(
    X: np.ndarray,
    method: str = "phase_shuffle",
    seed: int = 0,
    n_iter: int = 20,
) -> np.ndarray:
    method = (method or "phase_shuffle").lower()
    if method in ("iaaft", "iAAFT"):
        return iaaft_independent(X, n_iter=n_iter, seed=seed)
    return phase_shuffle_independent(X, seed=seed)


def surrogate_delta_metric(
    X: np.ndarray,
    metric_fn,
    n: int = 8,
    seed: int = 42,
    split: int | None = None,
    method: str = "phase_shuffle",
) -> dict:
    """
    Compare observed Δmetric (second half - first half, or custom split)
    against surrogate nulls.
    """
    X = np.asarray(X, dtype=float)
    obs = metric_fn(X)
    if split is None:
        split = len(obs) // 2
    split = int(np.clip(split, 1, max(1, len(obs) - 1)))
    if len(obs) < 4:
        return {
            "observed_delta": 0.0,
            "null_deltas": np.array([]),
            "p_value": 1.0,
            "method": method,
            "n": n,
            "split": split,
        }

    obs_delta = float(np.nanmean(obs[split:]) - np.nanmean(obs[:split]))
    nulls = []
    for i in range(n):
        Xs = make_surrogate(X, method=method, seed=seed + i)
        m = metric_fn(Xs)
        if len(m) < 4:
            continue
        sp = int(np.clip(split if split < len(m) else len(m) // 2, 1, len(m) - 1))
        nulls.append(float(np.nanmean(m[sp:]) - np.nanmean(m[:sp])))
    nulls_arr = np.asarray(nulls, dtype=float) if nulls else np.array([0.0])
    # two-sided Monte Carlo
    p = float(np.mean(np.abs(nulls_arr) >= abs(obs_delta))) if len(nulls_arr) else 1.0
    return {
        "observed_delta": obs_delta,
        "null_deltas": nulls_arr,
        "p_value": max(p, 1.0 / (n + 1)),
        "n": n,
        "method": method,
        "split": split,
    }
