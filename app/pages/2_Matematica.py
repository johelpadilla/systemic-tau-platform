from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import math

import numpy as np
import streamlit as st
from stp.i18n.core import t

from components.illustrations import show_illustration
from components.ui import page_link, callout, footer, learning_goals, page_header, section_header
from stp.core.ordinal import bandt_pompe_symbols
from stp.core.pipeline import run_analysis
from stp.config.settings import AnalysisParams
from stp.data.generators import coupled_logistic
from stp.education.content_loader import read_markdown
from stp.visualization.series_plots import plot_recd_panel, plot_tau

st.set_page_config(page_title=t("matematica.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("matematica.title"),
    subtitle=t("matematica.subtitle"),
    eyebrow=t("matematica.eyebrow"),
    icon="📐",
)

learning_goals(
    [t("matematica.goal_1"), t("matematica.goal_2"), t("matematica.goal_3")]
)

with st.container():
    st.markdown(read_markdown("matematica", "overview.md"))

show_illustration("bandt_pompe")

section_header(t("matematica.sandbox"), number="1")
callout(t("matematica.sandbox_callout"))

ctrl1, ctrl2, _ = st.columns([1, 1, 2])
with ctrl1:
    m = st.slider(t("matematica.dim_m"), 2, 5, 3, help=t("matematica.dim_m_help"))
with ctrl2:
    delay = st.slider(t("matematica.delay"), 1, 5, 1)

x = np.sin(np.linspace(0, 12, 200)) + 0.1 * np.random.default_rng(0).normal(size=200)
sym = bandt_pompe_symbols(x, m=m, delay=delay)

c1, c2 = st.columns(2)
with c1:
    st.markdown(f"##### {t('matematica.series_demo')}")
    st.line_chart(x, height=260)
    st.caption(t("matematica.series_cap"))
with c2:
    st.markdown(f"##### {t('matematica.hist_title', n=math.factorial(m))}")
    st.bar_chart(np.bincount(sym, minlength=math.factorial(m)), height=260)
    st.caption(t("matematica.hist_cap"))

section_header(t("matematica.demo_header"), number="2")
show_illustration("tau_relational")
st.markdown(t("matematica.demo_body"))

mode_col, btn_col = st.columns([1, 2])
with mode_col:
    mode = st.radio(
        t("matematica.mode"),
        ["fast", "full"],
        horizontal=True,
        index=0,
        help=t("matematica.mode_help"),
    )
with btn_col:
    st.write("")
    run = st.button(t("matematica.run_btn"), type="primary", width="stretch")

if run:
    X = coupled_logistic(T=600, coupling=0.2, switch_at=300, seed=7)
    params = AnalysisParams(window=51, stride=2, mode=mode, n_surrogates=4 if mode == "fast" else 20)
    with st.spinner(t("matematica.computing")):
        result = run_analysis(X, params)
    st.success(
        t(
            "matematica.ready",
            hash=result.repro_hash[:16],
            dtau=result.metrics.get("delta_tau_s", float("nan")),
            ex=result.metrics.get("mean_excess3", float("nan")),
        )
    )
    st.caption(t("matematica.switch_cap"))
    g1, g2 = st.columns(2)
    with g1:
        st.plotly_chart(plot_tau(result), width="stretch")
    with g2:
        st.plotly_chart(plot_recd_panel(result), width="stretch")
    with st.expander(t("matematica.metrics_exp")):
        st.json(result.metrics)
        st.code(result.repro_hash, language="text")

with st.expander(t("matematica.extensions"), expanded=True):
    st.markdown(t("matematica.ext_body", table=t("matematica.ext_table")))

try:
    from stp.education.handouts import render_handout_bytes

    st.download_button(
        t("matematica.dl_math"),
        data=render_handout_bytes("matematica"),
        file_name="stp_04_matematica_practica.md",
        mime="text/markdown",
        width="stretch",
    )
except Exception:
    pass

page_link("pages/4_Laboratorio.py", label=t("matematica.go_lab"), icon="🔬")
page_link("pages/1_Fundamentos.py", label=t("matematica.review_fund"), icon="📘")
page_link("pages/8_Materiales.py", label=t("nav.materials"), icon="📦")
footer()
