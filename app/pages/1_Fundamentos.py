from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.illustrations import show_illustration
from components.ui import page_link, footer, learning_goals, page_header
from stp.education.content_loader import read_markdown
from stp.i18n.core import t

st.set_page_config(page_title=t("fundamentos.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("fundamentos.title"),
    subtitle=t("fundamentos.subtitle"),
    eyebrow=t("fundamentos.eyebrow"),
    icon="📘",
)

learning_goals(
    [t("fundamentos.goal_1"), t("fundamentos.goal_2"), t("fundamentos.goal_3")]
)

tabs = st.tabs(
    [
        t("fundamentos.tab_1"),
        t("fundamentos.tab_2"),
        t("fundamentos.tab_3"),
        t("fundamentos.tab_4"),
        t("fundamentos.tab_5"),
        t("fundamentos.tab_6"),
    ]
)

files = [
    ("fundamentos", "01_tau.md"),
    ("fundamentos", "02_ews_limits.md"),
    ("fundamentos", "03_recd_levels.md"),
    ("fundamentos", "04_excess3.md"),
    ("fundamentos", "05_csd.md"),
    ("fundamentos", "06_filosofia.md"),
]

tab_illustrations = [
    "tau_relational",
    "dual_reading",
    "recd_nested",
    "excess3",
    "dual_reading",
    "chronos_kairos",
]

for tab, parts, illus in zip(tabs, files, tab_illustrations):
    with tab:
        show_illustration(illus)
        st.markdown(read_markdown(*parts))

st.sidebar.markdown(
    f'<div class="stp-sidebar-section">{t("common.suggested_path")}</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(t("fundamentos.sidebar_path"))
try:
    from stp.education.handouts import render_handout_bytes

    st.download_button(
        t("fundamentos.dl_fund"),
        data=render_handout_bytes("fundamentos_compilado"),
        file_name="stp_fundamentos_compilado.md",
        mime="text/markdown",
        width="stretch",
    )
    st.download_button(
        t("fundamentos.dl_theory"),
        data=render_handout_bytes("teoria"),
        file_name="stp_03_teoria_tau_recd.md",
        mime="text/markdown",
        width="stretch",
    )
except Exception:
    pass

page_link("pages/2_Matematica.py", label=t("nav.next_math"), icon="📐")
page_link("pages/4_Laboratorio.py", label=t("nav.practice_lab"), icon="🔬")
page_link("pages/8_Materiales.py", label=t("nav.materials"), icon="📦")

footer()
