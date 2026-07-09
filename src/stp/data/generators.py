"""Synthetic demos for the Lab and tutorials (all domains).

Design principle (pedagogy first)
---------------------------------
Each *event* demo is built so that the transition reorganizes **joint ordinal
structure** between variables — not only mean/variance levels. That is the
scientific question τ_s + RECD address. Control series (AR noise) keep weak
cross-coupling on purpose so students can contrast “signal” vs “almost-null”.

All series are finite, multivariate (T×N), and deterministic given `seed`.
"""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------------
# Shared building blocks
# ---------------------------------------------------------------------------


def _shared_coupling_ar(
    T: int,
    N: int,
    event_at: int | None,
    *,
    c_before: float = 0.08,
    c_after: float = 0.50,
    phi: float = 0.55,
    scales: np.ndarray | None = None,
    force: np.ndarray | None = None,
    seed: int = 0,
) -> np.ndarray:
    """
    Multivariate AR(1) with a latent shared innovation whose weight jumps at event_at.

    force: optional (T, N) additive drift (e.g. outbreak ramp, drought).
    """
    rng = np.random.default_rng(seed)
    X = np.zeros((T, N))
    sc = np.ones(N) if scales is None else np.asarray(scales, dtype=float)
    f = np.zeros((T, N)) if force is None else np.asarray(force, dtype=float)
    for t in range(1, T):
        c = c_after if (event_at is not None and t >= event_at) else c_before
        noise = rng.normal(0.0, 1.0, size=N) * sc
        shared = rng.normal(0.0, 1.0)
        innov = (1.0 - c) * noise + c * shared * sc
        X[t] = phi * X[t - 1] + innov + f[t]
    return X


def _apply_mix_reorg(
    base: np.ndarray,
    event_at: int,
    *,
    weights: tuple[float, ...] = (0.55, 0.45),
    amp: float = 1.5,
    seed: int = 0,
) -> np.ndarray:
    """Post-event: channels lock onto a shared mixture (eeg-style reorg)."""
    rng = np.random.default_rng(seed)
    out = base.copy()
    T, N = out.shape
    w = np.array(weights[:N], dtype=float)
    if w.sum() == 0:
        w = np.ones(N) / N
    else:
        w = w / w.sum()
    for i in range(event_at, T):
        mix = float(np.dot(w, out[i]))
        for j in range(N):
            out[i, j] = amp * mix * (0.85 + 0.15 * j) + 0.2 * rng.normal()
    return out


# ---------------------------------------------------------------------------
# Synthetic / control
# ---------------------------------------------------------------------------


def coupled_logistic(
    T: int = 800,
    r: float = 3.8,
    coupling: float = 0.15,
    seed: int = 0,
    switch_at: int | None = None,
) -> np.ndarray:
    """Two coupled logistic maps; optional coupling jump at switch_at."""
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.1, 0.9, size=2)
    out = np.zeros((T, 2))
    c = 0.0
    for t in range(T):
        if switch_at is not None and t >= switch_at:
            c = coupling
        x0 = (1 - c) * r * x[0] * (1 - x[0]) + c * r * x[1] * (1 - x[1])
        x1 = (1 - c) * r * x[1] * (1 - x[1]) + c * r * x[0] * (1 - x[0])
        x = np.array([x0, x1])
        out[t] = x
    return out


def ar_noise(T: int = 800, N: int = 3, phi: float = 0.6, seed: int = 1) -> np.ndarray:
    """Independent AR(1) channels — pedagogical near-null control (no designed event)."""
    rng = np.random.default_rng(seed)
    X = np.zeros((T, N))
    for t in range(1, T):
        X[t] = phi * X[t - 1] + rng.normal(0, 1, size=N)
    return X


# ---------------------------------------------------------------------------
# Domain demos (improved for ordinal reorganization)
# ---------------------------------------------------------------------------


def cardiac_like_rr(T: int = 3500, seed: int = 2, event_at: int = 2800) -> np.ndarray:
    """
    RR (ms) + abs successive difference (CCTP-style pair) with reorg near event_at.

    Pre: two weakly related physiological drivers (resp on RR, slow baro on dRR).
    Post: channels lock onto a shared pathological mixture (same design pattern as
    eeg_like) so ordinal co-structure — not only variance — changes for the Lab demo.
    """
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    resp = np.sin(2 * np.pi * t / 12.0)
    baro = np.sin(2 * np.pi * t / 48.0)
    path = np.sin(2 * np.pi * t / 17.0)
    # Independent-ish bases pre-event
    rr = 800 + 35 * baro + 18 * resp + 12 * rng.normal(size=T)
    drr = 14 + 6 * np.sin(2 * np.pi * t / 55.0) + 4 * rng.normal(size=T)
    out = np.column_stack([rr, drr])
    for i in range(event_at, T):
        # normalize-ish local values then mix (eeg-style lock-in)
        z0 = (out[i, 0] - 800) / 30.0
        z1 = (out[i, 1] - 14) / 6.0
        mix = 0.55 * z0 + 0.45 * z1 + 0.35 * path[i]
        out[i, 0] = 800 + 48 * mix + 22 * path[i] + 6 * rng.normal()
        out[i, 1] = 14 + 16 * abs(mix) + 5 * abs(path[i]) + 2.5 * abs(rng.normal())
    return out


def dengue_like(T: int = 400, seed: int = 7, event_at: int = 260) -> np.ndarray:
    """
    Weekly-ish cases + rain + temp.

    Pre-outbreak: weak climate–cases coupling + seasonality.
    Post: shared latent (transmission pressure) couples the three channels while
    cases ramp — ordinal reorganization, not only a level shift.
    """
    rng = np.random.default_rng(seed)
    season = 0.5 + 0.5 * np.sin(2 * np.pi * np.arange(T) / 52.0)
    cases = np.zeros(T)
    rain = np.zeros(T)
    temp = np.zeros(T)
    cases[0], rain[0], temp[0] = 8.0, 22.0, 26.0
    for i in range(1, T):
        c = 0.10 if i < event_at else 0.48
        shared = rng.normal(0, 1)
        e_c, e_r, e_t = rng.normal(0, 1, 3)
        ramp = 0.0 if i < event_at else (i - event_at) / max(1, T - event_at)
        rain[i] = (
            0.45 * rain[i - 1]
            + 14
            + 20 * season[i]
            + 8 * ramp
            + (1 - c) * 4 * e_r
            + c * 7 * shared
        )
        temp[i] = (
            0.55 * temp[i - 1]
            + 0.45 * (26 + 2.8 * np.sin(2 * np.pi * i / 52.0 + 0.4) + 0.8 * ramp)
            + (1 - c) * 0.45 * e_t
            + c * 0.9 * shared
        )
        base_cases = 6 + 5 * season[i] + 0.12 * max(0.0, rain[i] - 12) + 35 * ramp
        cases[i] = (
            0.40 * cases[i - 1]
            + 0.60 * base_cases
            + (1 - c) * 2.2 * e_c
            + c * 5.0 * shared
        )
    cases = np.clip(cases, 0, None)
    rain = np.clip(rain, 0, None)
    return np.column_stack([cases, rain, temp])


def eeg_like(T: int = 2000, seed: int = 8, event_at: int = 1400) -> np.ndarray:
    """3-channel oscillatory mixture; higher coupling + amplitude post-event."""
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    f1, f2 = 0.04, 0.07
    base = np.column_stack(
        [
            np.sin(2 * np.pi * f1 * t) + 0.3 * rng.normal(size=T),
            np.sin(2 * np.pi * f2 * t + 0.5) + 0.3 * rng.normal(size=T),
            np.sin(2 * np.pi * 0.055 * t + 1.0) + 0.3 * rng.normal(size=T),
        ]
    )
    out = base.copy()
    for i in range(event_at, T):
        mix = 0.55 * base[i, 0] + 0.45 * base[i, 1]
        out[i, 0] = 1.6 * mix + 0.2 * rng.normal()
        out[i, 1] = 1.5 * mix + 0.25 * rng.normal()
        out[i, 2] = 1.4 * (0.5 * mix + 0.5 * base[i, 2]) + 0.2 * rng.normal()
    return out


def ecology_like(T: int = 300, seed: int = 9, event_at: int = 180) -> np.ndarray:
    """
    chl_a, phosphorus, dissolved oxygen — bloom / eutrophication reorg.

    Nutrient pulse forces a shared latent that re-couples the triad (classic
    Scheffer-style teaching case for ordinal early warning).
    """
    rng = np.random.default_rng(seed)
    chl = np.zeros(T)
    phos = np.zeros(T)
    do = np.zeros(T)
    phos[0], chl[0], do[0] = 0.04, 6.0, 9.0
    for i in range(1, T):
        c = 0.10 if i < event_at else 0.52
        season = np.sin(2 * np.pi * i / 52.0)
        shared = rng.normal(0, 1)
        e = rng.normal(0, 1, 3)
        ramp = 0.0 if i < event_at else (i - event_at) / max(1.0, T - event_at)
        phos[i] = (
            0.65 * phos[i - 1]
            + 0.35 * (0.04 + 0.012 * season + 0.05 * ramp)
            + (1 - c) * 0.004 * e[0]
            + c * 0.01 * shared
        )
        chl[i] = (
            0.50 * chl[i - 1]
            + 0.50 * (5 + 2 * season + 45 * phos[i] + 20 * ramp)
            + (1 - c) * 0.9 * e[1]
            + c * 3.0 * shared
        )
        do[i] = (
            0.55 * do[i - 1]
            + 0.45 * (9 - 0.14 * chl[i] - 1.5 * ramp)
            + (1 - c) * 0.25 * e[2]
            - c * 1.4 * shared
        )
    return np.column_stack([chl, phos, do])


def finance_like(T: int = 600, seed: int = 10, event_at: int = 330) -> np.ndarray:
    """
    Returns, realized-vol proxy, spread — volatility regime with co-movement jump.

    Pedagogical note: useful to transfer the *method*, not for trading claims.
    """
    rng = np.random.default_rng(seed)
    ret = np.zeros(T)
    vol = np.zeros(T)
    spread = np.zeros(T)
    for t in range(T):
        c = 0.10 if t < event_at else 0.55
        sigma = 0.008 if t < event_at else 0.028
        shared = rng.normal(0, 1)
        e = rng.normal(0, 1, 3)
        ret[t] = (1 - c) * sigma * e[0] + c * sigma * shared
        vol[t] = (
            sigma
            + 0.18 * abs(ret[t])
            + (1 - c) * 0.002 * abs(e[1])
            + c * 0.012 * abs(shared)
        )
        spread[t] = (
            0.001
            + 2.2 * vol[t]
            + (1 - c) * 0.0003 * e[2]
            + c * 0.0025 * abs(shared)
        )
    return np.column_stack([ret, vol, spread])


# ---------------------------------------------------------------------------
# New pedagogical domains
# ---------------------------------------------------------------------------


def climate_like(T: int = 480, seed: int = 11, event_at: int = 300) -> np.ndarray:
    """
    Temperature anomaly, precipitation, soil moisture — drought / hydro-climate regime.

    Bridges classical CSD lake/climate literature with ordinal multivariate reading:
    after event_at a shared drought latent reorganizes the triad (hot–dry–stressed soil).
    """
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    season = np.sin(2 * np.pi * t / 12.0)
    # weakly coupled pre-drought seasonal climate
    temp = 0.45 * season + 0.35 * rng.normal(size=T)
    precip = 2.0 + 0.9 * season + 0.45 * rng.normal(size=T)
    soil = 0.55 + 0.12 * season + 0.07 * rng.normal(size=T)
    out = np.column_stack([temp, precip, soil])
    for i in range(event_at, T):
        ramp = (i - event_at) / max(1, T - event_at)
        latent = 1.15 * ramp + 0.45 * rng.normal()  # drought severity
        out[i, 0] = 0.25 * season[i] + 1.05 * latent + 0.12 * rng.normal()
        out[i, 1] = max(0.0, 2.0 + 0.5 * season[i] - 1.35 * latent + 0.18 * rng.normal())
        out[i, 2] = float(
            np.clip(0.55 + 0.08 * season[i] - 0.38 * latent + 0.04 * rng.normal(), 0.0, 1.0)
        )
    return out


def social_like(T: int = 500, seed: int = 12, event_at: int = 280) -> np.ndarray:
    """
    Opinion A, opinion B, interaction intensity — polarization cascade (toy model).

    Pre: mild independent fluctuations (pluralistic noise).
    Post: a latent polarization driver anti-correlates A/B and inflates interaction —
    collective ordinal reorganization without claiming real social prediction.
    """
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    a = 0.2 * np.sin(2 * np.pi * t / 80.0) + 0.28 * rng.normal(size=T)
    b = 0.2 * np.sin(2 * np.pi * t / 90.0 + 1.0) + 0.28 * rng.normal(size=T)
    inter = 0.4 + 0.1 * np.sin(2 * np.pi * t / 40.0) + 0.1 * rng.normal(size=T)
    out = np.column_stack([a, b, inter])
    for i in range(event_at, T):
        ramp = (i - event_at) / max(1, T - event_at)
        latent = ramp + 0.28 * rng.normal()
        out[i, 0] = 0.95 * latent + 0.12 * rng.normal()
        out[i, 1] = -0.95 * latent + 0.12 * rng.normal()
        out[i, 2] = 0.4 + 1.15 * abs(latent) + 0.08 * rng.normal()
    return out


def education_like(T: int = 360, seed: int = 13, event_at: int = 200) -> np.ndarray:
    """
    Engagement, peer synchrony, cognitive load — classroom / cohort dynamics.

    Meta-pedagogical demo: mid-course reorganization when load, engagement and
    peer sync start sharing a latent (breakthrough or crisis of the learning system).
    Teaches the same ordinal grammar on a domain close to teaching practice.
    """
    rng = np.random.default_rng(seed)
    eng = np.zeros(T)
    peer = np.zeros(T)
    load = np.zeros(T)
    eng[0], peer[0], load[0] = 0.55, 0.35, 0.4
    for i in range(1, T):
        c = 0.10 if i < event_at else 0.52
        shared = rng.normal(0, 1)
        e = rng.normal(0, 1, 3)
        week = i % 12
        semester = 0.12 * np.sin(2 * np.pi * i / 90.0)
        ramp = 0.0 if i < event_at else (i - event_at) / max(1, T - event_at)
        load[i] = (
            0.55 * load[i - 1]
            + 0.22
            + 0.08 * (1 if week > 8 else 0)
            + 0.18 * ramp
            + (1 - c) * 0.12 * e[2]
            + c * 0.22 * shared
        )
        eng[i] = (
            0.50 * eng[i - 1]
            + 0.22
            + semester
            - 0.18 * load[i]
            + 0.2 * ramp
            + (1 - c) * 0.14 * e[0]
            + c * 0.38 * shared
        )
        peer[i] = (
            0.48 * peer[i - 1]
            + 0.12
            + 0.28 * eng[i]
            + 0.22 * ramp
            + (1 - c) * 0.12 * e[1]
            + c * 0.42 * shared
        )
        eng[i] = float(np.clip(eng[i], 0.0, 1.25))
        peer[i] = float(np.clip(peer[i], 0.0, 1.25))
        load[i] = float(np.clip(load[i], 0.0, 1.25))
    return np.column_stack([eng, peer, load])


def sleep_like(T: int = 2000, seed: int = 14, event_at: int = 1400) -> np.ndarray:
    """
    HRV proxy, activity, core temperature — sleep-architecture fragmentation.

    Physiology companion to cardiology: circadian drivers reorganize when
    fragmentation (high-freq latent) replaces clean circadian coupling.
    """
    rng = np.random.default_rng(seed)
    t = np.arange(T)
    circ = np.sin(2 * np.pi * t / 100.0)
    frag = np.sin(2 * np.pi * t / 17.0)
    hrv = np.zeros(T)
    act = np.zeros(T)
    temp = np.zeros(T)
    for i in range(T):
        if i < event_at:
            c = 0.12
            shared = circ[i] + 0.25 * rng.normal()
        else:
            c = 0.55
            shared = 0.25 * circ[i] + 0.75 * frag[i] + 0.35 * rng.normal()
        e = rng.normal(0, 1, 3)
        hrv[i] = 40 + 14 * circ[i] + (1 - c) * 5 * e[0] + c * 20 * shared
        act[i] = 0.3 - 0.18 * circ[i] + (1 - c) * 0.1 * e[1] - c * 0.28 * shared
        temp[i] = 36.5 + 0.28 * circ[i] + (1 - c) * 0.05 * e[2] + c * 0.16 * shared
    return np.column_stack([hrv, act, temp])


# Registry for catalog / CLI introspection
GENERATOR_REGISTRY: dict[str, callable] = {
    "coupled_logistic": coupled_logistic,
    "ar_noise": ar_noise,
    "cardiac_like_rr": cardiac_like_rr,
    "dengue_like": dengue_like,
    "eeg_like": eeg_like,
    "ecology_like": ecology_like,
    "finance_like": finance_like,
    "climate_like": climate_like,
    "social_like": social_like,
    "education_like": education_like,
    "sleep_like": sleep_like,
}
