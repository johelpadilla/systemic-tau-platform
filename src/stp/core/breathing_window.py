"""Breathing window — adaptive window size for τ_s.

When local volatility rises, the window contracts (faster response);
when the series is stable, it expands (smoother coupling estimate).
"""

from __future__ import annotations

import numpy as np

from stp.core.tau_s import ensure_multivariate, pairwise_mean_kendall


def local_volatility(X: np.ndarray, lookback: int = 21) -> np.ndarray:
    """Mean column-wise rolling std; length T."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]
    T = X.shape[0]
    vol = np.zeros(T)
    for t in range(T):
        a = max(0, t - lookback + 1)
        seg = X[a : t + 1]
        vol[t] = float(np.nanmean(np.nanstd(seg, axis=0)))
    return vol


def breathing_windows(
    vol: np.ndarray,
    w_min: int = 11,
    w_max: int = 101,
    vol_lo: float | None = None,
    vol_hi: float | None = None,
) -> np.ndarray:
    """Map local volatility to odd window sizes in [w_min, w_max]."""
    vol = np.asarray(vol, dtype=float)
    if vol_lo is None:
        vol_lo = float(np.nanpercentile(vol, 15))
    if vol_hi is None:
        vol_hi = float(np.nanpercentile(vol, 85))
    span = max(vol_hi - vol_lo, 1e-12)
    # high vol → small window
    u = np.clip((vol - vol_lo) / span, 0.0, 1.0)
    w = w_max - u * (w_max - w_min)
    w = np.round(w).astype(int)
    w = np.where(w % 2 == 0, w + 1, w)
    return np.clip(w, w_min + (1 - w_min % 2), w_max)


def compute_tau_s_breathing(
    X: np.ndarray,
    stride: int = 5,
    w_min: int = 11,
    w_max: int = 101,
    lookback: int = 21,
    zscore: bool = True,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Sliding τ_s with per-center breathing window.

    Returns
    -------
    tau_s, centers, windows_used
    """
    X = ensure_multivariate(X)
    if zscore:
        out = np.zeros_like(X)
        for j in range(X.shape[1]):
            s = np.nanstd(X[:, j])
            out[:, j] = (X[:, j] - np.nanmean(X[:, j])) / s if s > 1e-12 else 0.0
        X = out

    T = X.shape[0]
    vol = local_volatility(X, lookback=lookback)
    w_series = breathing_windows(vol, w_min=w_min, w_max=min(w_max, max(w_min, T // 2 * 2 + 1)))

    taus, centers, used = [], [], []
    # centers spaced by stride; window drawn from local w_series
    for c in range(w_max // 2, T - w_max // 2, stride):
        w = int(w_series[c])
        half = w // 2
        start = c - half
        end = start + w
        if start < 0 or end > T:
            continue
        taus.append(pairwise_mean_kendall(X[start:end]))
        centers.append(c)
        used.append(w)

    return (
        np.asarray(taus, dtype=float),
        np.asarray(centers, dtype=int),
        np.asarray(used, dtype=int),
    )
