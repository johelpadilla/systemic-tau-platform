"""Classical early-warning signals for comparison panels."""

from __future__ import annotations

import numpy as np


def rolling_variance(x: np.ndarray, window: int, stride: int = 1) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(x, dtype=float).ravel()
    vals, centers = [], []
    for start in range(0, len(x) - window + 1, stride):
        w = x[start : start + window]
        vals.append(float(np.nanvar(w)))
        centers.append(start + window // 2)
    return np.asarray(vals), np.asarray(centers)


def rolling_ar1(x: np.ndarray, window: int, stride: int = 1) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(x, dtype=float).ravel()
    vals, centers = [], []
    for start in range(0, len(x) - window + 1, stride):
        w = x[start : start + window]
        if len(w) < 3:
            vals.append(np.nan)
        else:
            a, b = w[:-1], w[1:]
            if np.nanstd(a) < 1e-12:
                vals.append(0.0)
            else:
                vals.append(float(np.corrcoef(a, b)[0, 1]))
        centers.append(start + window // 2)
    return np.asarray(vals), np.asarray(centers)


def classical_ews_bundle(
    X: np.ndarray, window: int = 101, stride: int = 5
) -> dict[str, np.ndarray]:
    """Compute var and AR1 on the first column (primary observable)."""
    X = np.asarray(X, dtype=float)
    primary = X[:, 0] if X.ndim == 2 else X
    var, c = rolling_variance(primary, window, stride)
    ar1, _ = rolling_ar1(primary, window, stride)
    return {"variance": var, "ar1": ar1, "centers": c}
