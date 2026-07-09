from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from stp.config.settings import THEME
from stp.core.pipeline import AnalysisResult
from stp.i18n.core import t
from stp.visualization.style import apply_theme, line_fig


def _event_vline(fig: go.Figure, event_index: int | None, label: str | None = None) -> None:
    if event_index is None:
        return
    if label is None:
        label = t("plots.event")
    fig.add_vline(
        x=event_index,
        line_width=2,
        line_dash="dash",
        line_color=THEME.alert,
        annotation_text=label,
        annotation_position="top",
        annotation_font_color=THEME.alert,
    )


def plot_series(
    X: np.ndarray,
    title: str | None = None,
    event_index: int | None = None,
    event_label: str | None = None,
    names: list[str] | None = None,
) -> go.Figure:
    apply_theme()
    if title is None:
        title = t("plots.series_title")
    if event_label is None:
        event_label = t("plots.event")
    X = np.asarray(X)
    fig = go.Figure()
    if X.ndim == 1:
        fig.add_trace(go.Scatter(y=X, mode="lines", name=names[0] if names else "x"))
    else:
        for j in range(X.shape[1]):
            nm = names[j] if names and j < len(names) else f"var_{j}"
            fig.add_trace(go.Scatter(y=X[:, j], mode="lines", name=nm))
    fig.update_layout(title=title, height=360, xaxis_title="t")
    _event_vline(fig, event_index, event_label)
    return fig


def plot_tau(
    result: AnalysisResult,
    event_index: int | None = None,
    event_label: str | None = None,
) -> go.Figure:
    if event_label is None:
        event_label = t("plots.event")
    fig = line_fig(
        result.tau_centers,
        result.tau_s,
        "τ_s",
        t("plots.tau_title"),
        "τ_s",
    )
    ev = event_index if event_index is not None else result.event_index
    _event_vline(fig, ev, event_label)
    if result.breathing_windows is not None and len(result.breathing_windows) == len(result.tau_s):
        fig.add_trace(
            go.Scatter(
                x=result.tau_centers,
                y=result.breathing_windows,
                name="W(t)",
                yaxis="y2",
                line=dict(color=THEME.purple, width=1, dash="dot"),
                opacity=0.7,
            )
        )
        fig.update_layout(
            yaxis2=dict(title="W", overlaying="y", side="right", showgrid=False),
            title=t("plots.tau_breathing_title"),
        )
    return fig


def plot_recd_panel(
    result: AnalysisResult,
    event_index: int | None = None,
    event_label: str | None = None,
) -> go.Figure:
    apply_theme()
    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(
            t("plots.recd_excess"),
            t("plots.recd_phi"),
            t("plots.recd_clock"),
        ),
        vertical_spacing=0.08,
    )
    tt = np.arange(len(result.excess3))
    fig.add_trace(
        go.Scatter(x=tt, y=result.excess3, name="excess3", line=dict(color="#5B4B8A")),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=tt, y=result.phi1, name="Φ₁", line=dict(color="#0D4F6B")), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=tt, y=result.phi2, name="Φ₂", line=dict(color="#1A8A8A")), row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=tt, y=result.T_recd, name="T_recd", line=dict(color="#C45C26")),
        row=3,
        col=1,
    )
    fig.update_layout(height=720, title=t("plots.recd_title"), showlegend=True)
    ev = event_index if event_index is not None else result.event_index
    if ev is not None:
        for r in (1, 2, 3):
            fig.add_vline(
                x=ev,
                line_width=1.5,
                line_dash="dash",
                line_color=THEME.alert,
                row=r,
                col=1,
            )
    return fig


def plot_ews_comparison(
    result: AnalysisResult,
    event_index: int | None = None,
    event_label: str | None = None,
) -> go.Figure:
    apply_theme()
    if event_label is None:
        event_label = t("plots.event")
    fig = go.Figure()
    if not result.ews:
        fig.update_layout(title=t("plots.ews_off"))
        return fig

    def _norm(a: np.ndarray) -> np.ndarray:
        a = np.asarray(a, dtype=float)
        s = np.nanstd(a)
        return (a - np.nanmean(a)) / s if s > 1e-12 else a * 0

    c = result.ews.get("centers", result.tau_centers)
    fig.add_trace(
        go.Scatter(x=result.tau_centers, y=_norm(result.tau_s), name="τ_s (z)", line=dict(width=2.5))
    )
    if "variance" in result.ews:
        fig.add_trace(
            go.Scatter(x=c, y=_norm(result.ews["variance"]), name="var (z)", line=dict(dash="dot"))
        )
    if "ar1" in result.ews:
        fig.add_trace(
            go.Scatter(x=c, y=_norm(result.ews["ar1"]), name="AR1 (z)", line=dict(dash="dash"))
        )
    fig.update_layout(
        title=t("plots.ews_title"),
        height=400,
        yaxis_title=t("plots.ews_yaxis"),
    )
    ev = event_index if event_index is not None else result.event_index
    _event_vline(fig, ev, event_label)
    return fig


def plot_breathing(result: AnalysisResult, event_index: int | None = None) -> go.Figure:
    """W(t) from breathing window alongside τ_s."""
    apply_theme()
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(t("plots.breathing_tau"), t("plots.breathing_w")),
        vertical_spacing=0.12,
    )
    fig.add_trace(
        go.Scatter(
            x=result.tau_centers,
            y=result.tau_s,
            name="τ_s",
            line=dict(color=THEME.navy, width=2),
        ),
        row=1,
        col=1,
    )
    if result.breathing_windows is not None and len(result.breathing_windows):
        fig.add_trace(
            go.Scatter(
                x=result.tau_centers,
                y=result.breathing_windows,
                name="W(t)",
                line=dict(color=THEME.purple, width=2),
                fill="tozeroy",
                fillcolor="rgba(91,75,138,0.12)",
            ),
            row=2,
            col=1,
        )
    else:
        fig.add_annotation(
            text=t("plots.breathing_off"),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.25,
            showarrow=False,
        )
    ev = event_index if event_index is not None else result.event_index
    if ev is not None:
        for r in (1, 2):
            fig.add_vline(x=ev, line_dash="dash", line_color=THEME.alert, row=r, col=1)
    fig.update_layout(
        height=480,
        title=t("plots.breathing_title"),
        showlegend=True,
    )
    fig.update_yaxes(title_text="τ_s", row=1, col=1)
    fig.update_yaxes(title_text="W", row=2, col=1)
    return fig


def plot_tda_betti(result: AnalysisResult, event_index: int | None = None) -> go.Figure:
    """Sliding Betti-0/1 curves (TDA extension)."""
    apply_theme()
    tda = result.tda or {}
    centers = tda.get("centers")
    b0 = tda.get("beta0")
    b1 = tda.get("beta1")
    backend = tda.get("backend_name", "—")
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(t("plots.beta0", backend=backend), t("plots.beta1")),
        vertical_spacing=0.12,
    )
    if centers is None or b0 is None or len(centers) == 0:
        fig.add_annotation(
            text=t("plots.tda_off"),
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
        fig.update_layout(height=420, title=t("plots.tda_short"))
        return fig

    fig.add_trace(
        go.Scatter(
            x=centers,
            y=b0,
            name="β₀",
            line=dict(color=THEME.teal, width=2),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=centers,
            y=b1,
            name="β₁",
            line=dict(color=THEME.alert, width=2),
        ),
        row=2,
        col=1,
    )
    ev = event_index if event_index is not None else result.event_index
    if ev is not None:
        for r in (1, 2):
            fig.add_vline(x=ev, line_dash="dash", line_color=THEME.alert, row=r, col=1)
    fig.update_layout(
        height=480,
        title=t("plots.tda_title"),
        showlegend=True,
    )
    fig.update_yaxes(title_text="β₀", row=1, col=1)
    fig.update_yaxes(title_text="β₁", row=2, col=1)
    return fig


def plot_dual_summary(result: AnalysisResult) -> go.Figure:
    """Compact dual panel: τ_s + excess3 with shared event marker."""
    apply_theme()
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=False,
        subplot_titles=("τ_s", "excess3"),
        vertical_spacing=0.12,
    )
    fig.add_trace(
        go.Scatter(
            x=result.tau_centers, y=result.tau_s, name="τ_s", line=dict(color=THEME.navy, width=2)
        ),
        row=1,
        col=1,
    )
    tt = np.arange(len(result.excess3))
    fig.add_trace(
        go.Scatter(x=tt, y=result.excess3, name="excess3", line=dict(color=THEME.purple, width=2)),
        row=2,
        col=1,
    )
    if result.event_index is not None:
        fig.add_vline(x=result.event_index, line_dash="dash", line_color=THEME.alert, row=1, col=1)
        fig.add_vline(x=result.event_index, line_dash="dash", line_color=THEME.alert, row=2, col=1)
    fig.update_layout(height=480, title=t("plots.dual_title"), showlegend=False)
    return fig
