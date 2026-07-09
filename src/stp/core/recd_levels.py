"""Nested ordinal RECD levels Φ₁, Φ₂, Φ₃ and excess3.

Falls back to a pure implementation; prefers nested_recd when installed.
"""

from __future__ import annotations

from collections import Counter
from typing import Any

import numpy as np

from stp.core.ordinal import multivariate_symbols


def compute_phi1(S: np.ndarray) -> np.ndarray:
    T, N = S.shape
    if N < 2:
        return np.zeros(T)
    pairs = N * (N - 1) / 2.0
    phi1 = np.zeros(T)
    for t in range(T):
        row = S[t]
        matches = sum(1 for i in range(N) for j in range(i + 1, N) if row[i] == row[j])
        phi1[t] = matches / pairs
    return phi1


def _rel_code(a: int, b: int) -> int:
    if a == b:
        return 0
    return 1 if a > b else 2


def compute_phi2(S: np.ndarray, d: int = 4, min_fraction: float = 0.75) -> np.ndarray:
    T, N = S.shape
    if N < 2 or T < d:
        return np.zeros(T)
    num_pairs = N * (N - 1) // 2
    phi2 = np.zeros(T)
    for i in range(N):
        for j in range(i + 1, N):
            rel = np.array([_rel_code(int(S[t, i]), int(S[t, j])) for t in range(T)])
            for t in range(d - 1, T):
                win = rel[t - d + 1 : t + 1]
                if np.mean(win == rel[t]) >= min_fraction:
                    phi2[t] += 1.0
    return np.clip(phi2 / num_pairs, 0.0, 1.0)


def _synergy_and_surprise(win: np.ndarray) -> float:
    T, N = win.shape
    joint = [tuple(int(v) for v in row) for row in win]
    _, counts = np.unique(joint, return_counts=True)
    p = counts / counts.sum()
    H_joint = float(-np.sum(p * np.log2(p + 1e-12)))

    H_margs = []
    for k in range(N):
        _, c = np.unique(win[:, k], return_counts=True)
        pk = c / c.sum()
        H_margs.append(float(-np.sum(pk * np.log2(pk + 1e-12))))
    H_sum = float(np.sum(H_margs))
    tc = max(0.0, H_sum - H_joint)

    pair_mi = []
    for i in range(N):
        for j in range(i + 1, N):
            pairs = list(zip(win[:, i], win[:, j]))
            _, cj = np.unique(pairs, return_counts=True)
            pj = cj / cj.sum()
            H2 = float(-np.sum(pj * np.log2(pj + 1e-12)))
            _, ci = np.unique(win[:, i], return_counts=True)
            pi = ci / ci.sum()
            Hi = float(-np.sum(pi * np.log2(pi + 1e-12)))
            _, cj2 = np.unique(win[:, j], return_counts=True)
            pj2 = cj2 / cj2.sum()
            Hj = float(-np.sum(pj2 * np.log2(pj2 + 1e-12)))
            pair_mi.append(max(0.0, Hi + Hj - H2))
    mi_avg = float(np.mean(pair_mi)) if pair_mi else 0.0
    syn = max(0.0, tc - (N - 1) * mi_avg)

    counter = Counter(joint)
    surprises = []
    for u, cnt in counter.items():
        p_indep = 1.0
        for k, val in enumerate(u):
            p_indep *= max(float(np.mean(win[:, k] == val)), 1e-9)
        p_obs = cnt / T
        ratio = p_obs / max(p_indep, 1e-9)
        excess_log = max(0.0, np.log2(ratio)) if ratio > 1 else 0.0
        surprises.append(excess_log * (cnt / T))
    surprise = float(np.sum(surprises)) if surprises else 0.0
    return 0.6 * syn + 0.4 * surprise


def compute_phi3_excess(
    S: np.ndarray, window: int = 13, theta: float = 0.08, stride: int = 1
) -> tuple[np.ndarray, np.ndarray]:
    T, N = S.shape
    phi3 = np.full(T, np.nan)
    excess = np.full(T, np.nan)
    if T < window or N < 2:
        return phi3, excess
    for t in range(window - 1, T, stride):
        score = _synergy_and_surprise(S[t - window + 1 : t + 1])
        excess[t] = score
        phi3[t] = 1.0 if score > theta else 0.0
    # forward-fill for plotting convenience
    last = np.nan
    for t in range(T):
        if np.isfinite(excess[t]):
            last = excess[t]
        elif np.isfinite(last):
            excess[t] = last
            phi3[t] = 1.0 if last > theta else 0.0
    return phi3, excess


def compute_recd_from_conjunctions(
    X: np.ndarray,
    m: int = 3,
    delay: int = 1,
    d: int = 4,
    theta3: float = 0.08,
    phi_window: int = 13,
    **_: Any,
) -> dict[str, np.ndarray]:
    """Local pure implementation of nested RECD levels."""
    try:
        from nested_recd import compute_recd_from_conjunctions as _ext  # type: ignore

        return _ext(X, m=m, delay=delay, d=d, theta3=theta3)
    except Exception:
        pass

    S = multivariate_symbols(X, m=m, delay=delay)
    if len(S) == 0:
        z = np.array([])
        return {
            "phi1": z,
            "phi2": z,
            "phi3": z,
            "excess3": z,
            "T_recd": z,
            "symbols": S,
        }
    phi1 = compute_phi1(S)
    phi2 = compute_phi2(S, d=d)
    phi3, excess3 = compute_phi3_excess(S, window=min(phi_window, max(5, len(S) // 4)), theta=theta3)
    # simple unweighted clock
    drecd = np.nan_to_num(phi1, nan=0.0) + np.nan_to_num(phi2, nan=0.0) + np.nan_to_num(excess3, nan=0.0)
    T_recd = np.cumsum(drecd)
    return {
        "phi1": phi1,
        "phi2": phi2,
        "phi3": phi3,
        "excess3": excess3,
        "T_recd": T_recd,
        "symbols": S,
        "delta_recd": drecd,
    }
