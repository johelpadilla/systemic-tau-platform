from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from stp.core.pipeline import AnalysisResult
from stp.visualization.style import apply_theme, line_fig


def plot_series(X: np.ndarray, title: str = "Series multivariada") -> go.Figure:
    apply_theme()
    X = np.asarray(X)
    fig = go.Figure()
    if X.ndim == 1:
        fig.add_trace(go.Scatter(y=X, mode="lines", name="x"))
    else:
        for j in range(X.shape[1]):
            fig.add_trace(go.Scatter(y=X[:, j], mode="lines", name=f"var_{j}"))
    fig.update_layout(title=title, height=360, xaxis_title="t")
    return fig


def plot_tau(result: AnalysisResult) -> go.Figure:
    fig = line_fig(
        result.tau_centers,
        result.tau_s,
        "τ_s",
        "Systemic Tau (ventana deslizante)",
        "τ_s",
    )
    # Feigenbaum Topological Zones
    fig.add_hrect(y0=0.5, y1=1.0, fillcolor="#2E7D32", opacity=0.15, line_width=0, layer="below", annotation_text="Sincronización (Φ₁)")
    fig.add_hrect(y0=-0.41, y1=0.41, fillcolor="#C62828", opacity=0.15, line_width=0, layer="below", annotation_text="Caos / Disonancia")
    fig.add_hrect(y0=-1.0, y1=-0.41, fillcolor="#6A1B9A", opacity=0.15, line_width=0, layer="below", annotation_text="Antisincronización")
    fig.update_yaxes(range=[-1.05, 1.05])
    return fig


def plot_recd_panel(result: AnalysisResult) -> go.Figure:
    apply_theme()
    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("excess3 (Nivel 3 continuo)", "Φ₁ / Φ₂", "T_recd (reloj acumulado)"),
        vertical_spacing=0.08,
    )
    t = np.arange(len(result.excess3))
    fig.add_trace(go.Scatter(x=t, y=result.excess3, name="excess3", line=dict(color="#5B4B8A")), row=1, col=1)
    fig.add_trace(go.Scatter(x=t, y=result.phi1, name="Φ₁", line=dict(color="#0D4F6B")), row=2, col=1)
    fig.add_trace(go.Scatter(x=t, y=result.phi2, name="Φ₂", line=dict(color="#1A8A8A")), row=2, col=1)
    fig.add_trace(go.Scatter(x=t, y=result.T_recd, name="T_recd", line=dict(color="#C45C26")), row=3, col=1)
    fig.update_layout(height=720, title="RECD — niveles ordinales anidados", showlegend=True)
    return fig


def plot_ews_comparison(result: AnalysisResult) -> go.Figure:
    apply_theme()
    fig = go.Figure()
    if not result.ews:
        fig.update_layout(title="EWS clásicos no calculados")
        return fig

    def _norm(a: np.ndarray) -> np.ndarray:
        a = np.asarray(a, dtype=float)
        s = np.nanstd(a)
        return (a - np.nanmean(a)) / s if s > 1e-12 else a * 0

    c = result.ews.get("centers", result.tau_centers)
    fig.add_trace(go.Scatter(x=result.tau_centers, y=_norm(result.tau_s), name="τ_s (z)", line=dict(width=2.5)))
    if "variance" in result.ews:
        fig.add_trace(go.Scatter(x=c, y=_norm(result.ews["variance"]), name="var (z)", line=dict(dash="dot")))
    if "ar1" in result.ews:
        fig.add_trace(go.Scatter(x=c, y=_norm(result.ews["ar1"]), name="AR1 (z)", line=dict(dash="dash")))
    fig.update_layout(
        title="Comparación normalizada: τ_s vs EWS clásicos",
        height=400,
        yaxis_title="z-score en el tramo",
    )
    return fig
