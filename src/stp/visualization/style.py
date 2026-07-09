"""Plotly institutional theme."""

from __future__ import annotations

import plotly.graph_objects as go
import plotly.io as pio

from stp.config.settings import THEME


def apply_theme() -> None:
    pio.templates["stp_institutional"] = go.layout.Template(
        layout=go.Layout(
            font=dict(family="Inter, Helvetica, Arial, sans-serif", color=THEME.deep),
            paper_bgcolor="white",
            plot_bgcolor="white",
            colorway=[THEME.navy, THEME.teal, THEME.purple, THEME.alert, "#6B7280"],
            title=dict(font=dict(size=16, color=THEME.navy)),
            margin=dict(l=50, r=30, t=50, b=40),
            xaxis=dict(gridcolor="#EEF2F6", zerolinecolor="#D0D7DE"),
            yaxis=dict(gridcolor="#EEF2F6", zerolinecolor="#D0D7DE"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
        )
    )
    pio.templates.default = "stp_institutional"


def line_fig(x, y, name: str, title: str, y_title: str = "") -> go.Figure:
    apply_theme()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=name, line=dict(width=2)))
    fig.update_layout(title=title, xaxis_title="t", yaxis_title=y_title or name, height=360)
    return fig
