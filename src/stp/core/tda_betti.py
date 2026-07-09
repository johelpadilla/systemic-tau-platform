"""Sliding-window TDA proxies (Betti-0 / Betti-1) for the Lab.

Design
------
Educational extension of the STP core — **not** a replacement for τ_s / RECD.

- Prefer **ripser** when installed (`pip install systemic-tau-platform[tda]`).
- Otherwise use a pure NumPy/SciPy **Vietoris–Rips 1-skeleton**:
  β₀ = connected components, β₁ = cyclomatic number (|E|−|V|+β₀).

Point clouds are built from short delay embeddings of the multivariate series
inside each analysis window (subsampled for speed).
"""

from __future__ import annotations

from typing import Any

import numpy as np
from scipy.spatial.distance import pdist, squareform

# Optional heavy backend
try:
    import ripser as _ripser  # type: ignore

    _HAS_RIPSER = True
except Exception:  # pragma: no cover
    _ripser = None
    _HAS_RIPSER = False


def has_ripser() -> bool:
    return bool(_HAS_RIPSER)


def delay_embed_multivariate(
    X: np.ndarray,
    m: int = 3,
    delay: int = 1,
    max_points: int = 80,
) -> np.ndarray:
    """
    Build a point cloud from multivariate delay coordinates.

    Each point is the concatenation of m lagged samples across all channels.
    Subsamples evenly to at most ``max_points`` rows.
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]
    T, N = X.shape
    need = (m - 1) * delay + 1
    if T < need + 2:
        # fallback: raw rows
        pts = X.copy()
    else:
        rows = []
        for t in range(need - 1, T):
            block = [X[t - k * delay] for k in range(m)]
            rows.append(np.concatenate(block))
        pts = np.asarray(rows, dtype=float)
    if len(pts) > max_points:
        idx = np.linspace(0, len(pts) - 1, max_points).astype(int)
        pts = pts[idx]
    # z-score features for scale-free distance
    s = np.nanstd(pts, axis=0)
    s = np.where(s < 1e-12, 1.0, s)
    pts = (pts - np.nanmean(pts, axis=0)) / s
    return pts


def _union_find_components(n: int, edges: list[tuple[int, int]]) -> int:
    parent = list(range(n))
    rank = [0] * n

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1

    for i, j in edges:
        union(i, j)
    return len({find(i) for i in range(n)})


def betti_vr_skeleton(
    points: np.ndarray,
    radius: float | None = None,
    radius_quantile: float = 0.35,
) -> dict[str, float]:
    """
    Betti numbers of the Vietoris–Rips **1-skeleton** at a single radius.

    β₀ = # connected components  
    β₁ = |E| − |V| + β₀  (cyclomatic number; pedagogical proxy)
    """
    pts = np.asarray(points, dtype=float)
    n = len(pts)
    if n < 3:
        return {"beta0": float(max(n, 0)), "beta1": 0.0, "radius": 0.0, "n_points": float(n)}

    dmat = squareform(pdist(pts, metric="euclidean"))
    # ignore diagonal
    tri = dmat[np.triu_indices(n, k=1)]
    if radius is None:
        radius = float(np.quantile(tri, radius_quantile)) if len(tri) else 0.0
    radius = float(max(radius, 1e-12))

    edges: list[tuple[int, int]] = []
    ii, jj = np.triu_indices(n, k=1)
    for a, b, dist in zip(ii, jj, dmat[ii, jj]):
        if dist <= radius:
            edges.append((int(a), int(b)))

    beta0 = float(_union_find_components(n, edges))
    e = len(edges)
    # cyclomatic number of the undirected graph
    beta1 = float(max(0, e - n + int(beta0)))
    return {
        "beta0": beta0,
        "beta1": beta1,
        "radius": radius,
        "n_points": float(n),
        "n_edges": float(e),
    }


def betti_ripser(points: np.ndarray, maxdim: int = 1) -> dict[str, float]:
    """Betti counts from ripser persistence (finite bars at mid-scale heuristic)."""
    if not _HAS_RIPSER:
        raise RuntimeError("ripser not installed")
    pts = np.asarray(points, dtype=float)
    if len(pts) < 3:
        return {"beta0": float(len(pts)), "beta1": 0.0, "radius": 0.0, "n_points": float(len(pts))}
    # subsample hard cap for speed
    if len(pts) > 100:
        idx = np.linspace(0, len(pts) - 1, 100).astype(int)
        pts = pts[idx]
    dgms = _ripser.ripser(pts, maxdim=maxdim)["dgms"]
    # Count bars with persistence above a relative threshold
    out: dict[str, float] = {"n_points": float(len(pts)), "radius": float("nan")}
    for dim, dgm in enumerate(dgms):
        if dgm is None or len(dgm) == 0:
            out[f"beta{dim}"] = 0.0
            continue
        births = dgm[:, 0]
        deaths = dgm[:, 1]
        finite = np.isfinite(deaths)
        pers = np.where(finite, deaths - births, 0.0)
        thr = float(np.quantile(pers[pers > 0], 0.5)) if np.any(pers > 0) else 0.0
        # essential H0 often has inf death — count finite long bars + 1 component family
        count = int(np.sum(pers >= thr)) if thr > 0 else int(np.sum(finite))
        if dim == 0:
            # at least the connected-components story: long bars
            count = max(count, 1)
        out[f"beta{dim}"] = float(count)
    out.setdefault("beta0", 1.0)
    out.setdefault("beta1", 0.0)
    return out


def betti_point_cloud(
    points: np.ndarray,
    *,
    prefer_ripser: bool = True,
    radius_quantile: float = 0.35,
) -> dict[str, float]:
    """Dispatch: ripser if available and preferred, else VR skeleton."""
    if prefer_ripser and _HAS_RIPSER and len(points) >= 4:
        try:
            r = betti_ripser(points, maxdim=1)
            r["backend"] = 1.0  # marker: 1=ripser (stored as float for arrays)
            r["backend_name"] = "ripser"  # type: ignore[assignment]
            return r
        except Exception:
            pass
    r = betti_vr_skeleton(points, radius_quantile=radius_quantile)
    r["backend"] = 0.0
    return r


def sliding_betti(
    X: np.ndarray,
    window: int = 51,
    stride: int = 5,
    embed_m: int = 3,
    embed_delay: int = 1,
    max_points: int = 60,
    radius_quantile: float = 0.35,
    prefer_ripser: bool = True,
) -> dict[str, np.ndarray]:
    """
    Sliding-window Betti-0/1 curves along a multivariate series.

    Returns centers, beta0, beta1, radius (nan if ripser).
    """
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X[:, None]
    T = X.shape[0]
    w = int(max(5, window))
    if w % 2 == 0:
        w += 1
    half = w // 2
    centers: list[int] = []
    b0: list[float] = []
    b1: list[float] = []
    rad: list[float] = []
    backend_flags: list[float] = []

    for c in range(half, T - half, max(1, stride)):
        seg = X[c - half : c + half + 1]
        pts = delay_embed_multivariate(seg, m=embed_m, delay=embed_delay, max_points=max_points)
        stats = betti_point_cloud(
            pts, prefer_ripser=prefer_ripser, radius_quantile=radius_quantile
        )
        centers.append(c)
        b0.append(float(stats.get("beta0", 0.0)))
        b1.append(float(stats.get("beta1", 0.0)))
        rad.append(float(stats.get("radius", np.nan)))
        backend_flags.append(float(stats.get("backend", 0.0)))

    backend_name = "ripser" if (prefer_ripser and _HAS_RIPSER and any(backend_flags)) else "vr_skeleton"
    return {
        "centers": np.asarray(centers, dtype=int),
        "beta0": np.asarray(b0, dtype=float),
        "beta1": np.asarray(b1, dtype=float),
        "radius": np.asarray(rad, dtype=float),
        "backend": np.asarray(backend_flags, dtype=float),
        "backend_name": backend_name,  # type: ignore[dict-item]
    }


def tda_summary(tda: dict[str, Any], event_index: int | None = None) -> dict[str, float]:
    """Scalar summaries for metrics / interpretation."""
    b0 = np.asarray(tda.get("beta0", []), dtype=float)
    b1 = np.asarray(tda.get("beta1", []), dtype=float)
    centers = np.asarray(tda.get("centers", []), dtype=float)
    if len(b0) < 4:
        return {
            "mean_beta0": float(np.nanmean(b0)) if len(b0) else 0.0,
            "mean_beta1": float(np.nanmean(b1)) if len(b1) else 0.0,
            "delta_beta0": 0.0,
            "delta_beta1": 0.0,
        }

    def _delta(arr: np.ndarray) -> float:
        if event_index is not None and len(centers):
            sp = int(np.searchsorted(centers, event_index, side="left"))
            sp = int(np.clip(sp, 1, len(arr) - 1))
        else:
            sp = len(arr) // 2
        return float(np.nanmean(arr[sp:]) - np.nanmean(arr[:sp]))

    return {
        "mean_beta0": float(np.nanmean(b0)),
        "mean_beta1": float(np.nanmean(b1)),
        "delta_beta0": _delta(b0),
        "delta_beta1": _delta(b1),
    }
