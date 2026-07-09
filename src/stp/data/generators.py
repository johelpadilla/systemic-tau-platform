"""Synthetic demos for the Lab and tutorials."""

from __future__ import annotations

import numpy as np


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
    rng = np.random.default_rng(seed)
    X = np.zeros((T, N))
    for t in range(1, T):
        X[t] = phi * X[t - 1] + rng.normal(0, 1, size=N)
    return X


def cardiac_like_rr(T: int = 5000, seed: int = 2, event_at: int = 4000) -> np.ndarray:
    """Rough RR-like series with increased irregularity near event_at."""
    rng = np.random.default_rng(seed)
    rr = np.zeros(T)
    rr[0] = 800.0
    for t in range(1, T):
        base = 800 + 40 * np.sin(2 * np.pi * t / 300)
        noise_scale = 15.0 if t < event_at else 45.0
        rr[t] = base + rng.normal(0, noise_scale)
        if t > event_at:
            rr[t] += 20 * np.sin(2 * np.pi * t / 17)
    drr = np.abs(np.diff(rr, prepend=rr[0]))
    return np.column_stack([rr, drr])


def simulate_reloj_extramental(T: int = 1000, r_control: float = 3.8, coupling: float = 0.2, seed: int = 10) -> np.ndarray:
    """Generador basado en el Apéndice A (Feigenbaum δ)."""
    rng = np.random.default_rng(seed)
    # Basic coupled maps to simulate complex biology
    x = rng.uniform(0.1, 0.9, size=3)
    out = np.zeros((T, 3))
    for t in range(T):
        x0 = (1 - coupling) * r_control * x[0] * (1 - x[0]) + coupling * r_control * x[1] * (1 - x[1])
        x1 = (1 - coupling) * r_control * x[1] * (1 - x[1]) + coupling * r_control * x[2] * (1 - x[2])
        x2 = (1 - coupling) * r_control * x[2] * (1 - x[2]) + coupling * r_control * x[0] * (1 - x[0])
        x = np.array([x0, x1, x2])
        # Add tiny stochastic biological noise
        x += rng.normal(0, 0.005, size=3)
        x = np.clip(x, 0, 1)
        out[t] = x
    return out


def aedes_antisync_control(T: int = 1500, fumigation_at: int = 1000, seed: int = 42) -> np.ndarray:
    """Simulador de la divergencia antisincrónica (Caso Caño Martín Peña)."""
    rng = np.random.default_rng(seed)
    
    # 3 variables: Poblacion hembras, Huevos, Clima local (proxy)
    x = rng.uniform(0.1, 0.9, size=3)
    out = np.zeros((T, 3))
    
    r_normal = 3.6 # Chaotic but bounded
    r_fumigation = 3.99 # Forces extreme stress and divergance
    
    for t in range(T):
        is_intervention = t >= fumigation_at and t < fumigation_at + 200
        
        r_current = r_fumigation if is_intervention else r_normal
        coupling = -0.3 if is_intervention else 0.15 # Negative coupling forces anti-phase
        
        x0 = (1 - abs(coupling)) * r_current * x[0] * (1 - x[0]) + coupling * r_current * x[1] * (1 - x[1])
        x1 = (1 - abs(coupling)) * r_current * x[1] * (1 - x[1]) + coupling * r_current * x[2] * (1 - x[2])
        x2 = (1 - abs(coupling)) * r_current * x[2] * (1 - x[2]) + coupling * r_current * x[0] * (1 - x[0])
        
        x = np.array([x0, x1, x2])
        x += rng.normal(0, 0.01, size=3)
        x = np.clip(x, 0.001, 0.999)
        out[t] = x
        
    return out
