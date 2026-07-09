"""Bandt–Pompe ordinal patterns (pure NumPy)."""

from __future__ import annotations

import numpy as np


def bandt_pompe_symbols(x: np.ndarray, m: int = 3, delay: int = 1) -> np.ndarray:
    """
    Generate Bandt–Pompe ordinal symbols for a 1D series.

    Parameters
    ----------
    x : array_like
        Univariate series.
    m : int
        Embedding dimension (alphabet size m!).
    delay : int
        Embedding delay.

    Returns
    -------
    symbols : ndarray of int, shape (T - (m-1)*delay,)
    """
    x = np.asarray(x, dtype=float).ravel()
    n = len(x) - (m - 1) * delay
    if n <= 0:
        return np.array([], dtype=int)

    # Factorials for Lehmer-code style encoding
    fact = np.ones(m, dtype=int)
    for i in range(1, m):
        fact[i] = fact[i - 1] * i

    symbols = np.zeros(n, dtype=int)
    for i in range(n):
        word = np.array([x[i + j * delay] for j in range(m)])
        # argsort with stable tie-break by index
        perm = np.argsort(word, kind="mergesort")
        symbol = 0
        for j in range(m - 1):
            cnt = int(np.sum(perm[j + 1 :] < perm[j]))
            symbol += cnt * fact[m - 1 - j]
        symbols[i] = symbol
    return symbols


def multivariate_symbols(X: np.ndarray, m: int = 3, delay: int = 1) -> np.ndarray:
    """
    Build symbol matrix S of shape (T_eff, N).
    """
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X must have shape (T, N)")
    cols = [bandt_pompe_symbols(X[:, i], m=m, delay=delay) for i in range(X.shape[1])]
    min_len = min(len(c) for c in cols)
    if min_len == 0:
        return np.zeros((0, X.shape[1]), dtype=int)
    return np.column_stack([c[:min_len] for c in cols])
