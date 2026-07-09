from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t

from components.ui import page_link, callout, feature_card, footer, learning_goals, page_header, section_header
from stp.education.handouts import render_handout_bytes

st.set_page_config(page_title=t("docencia.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("docencia.title_full"),
    subtitle=t("docencia.subtitle_full"),
    eyebrow=t("docencia.eyebrow_full"),
    icon="🎓",
)

learning_goals(
    [t("docencia.goal_1_full"), t("docencia.goal_2_full"), t("docencia.goal_3_full")]
)

section_header(t("docencia.comp_header"))
callout(t("docencia.comp_callout"))

section_header(t("docencia.syl_header"))
st.markdown(t("docencia.syl_table"), unsafe_allow_html=True)

section_header(t("docencia.rubric_header"))
st.markdown(t("docencia.rubric_body"))

section_header(t("docencia.export_header"))
d1, d2, d3 = st.columns(3)
with d1:
    st.download_button(
        t("docencia.dl_syllabus"),
        data=render_handout_bytes("syllabus"),
        file_name="stp_08_syllabus_6_semanas.md",
        mime="text/markdown",
        type="primary",
        width="stretch",
    )
with d2:
    st.download_button(
        t("docencia.dl_teacher"),
        data=render_handout_bytes("pack_docente"),
        file_name="stp_pack_docente.md",
        mime="text/markdown",
        width="stretch",
    )
with d3:
    st.download_button(
        t("docencia.dl_student"),
        data=render_handout_bytes("pack_estudiante"),
        file_name="stp_pack_estudiante.md",
        mime="text/markdown",
        width="stretch",
    )
page_link("pages/8_Materiales.py", label=t("nav.full_materials"), icon="📦")
page_link(
    "pages/4_Laboratorio.py",
    label=t("docencia.open_week2"),
    icon="🔬",
    query_params={"dataset": "synthetic_coupled_logistic", "domain": "synthetic"},
)

section_header(t("docencia.mat_header"))
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(
        feature_card(
            t("docencia.card_md_t"),
            t("docencia.card_md_b"),
            icon="📝",
            accent="navy",
        ),
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        feature_card(
            t("docencia.card_lab_t"),
            t("docencia.card_lab_b"),
            icon="🔬",
            accent="teal",
        ),
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        feature_card(
            t("docencia.card_code_t"),
            t("docencia.card_code_b"),
            icon="⚙️",
            accent="purple",
        ),
        unsafe_allow_html=True,
    )

section_header(t("docencia.lic_header"))
st.markdown(t("docencia.lic_table"), unsafe_allow_html=True)

section_header(t("docencia.nb_header"))
notebooks = [
    ("01", "bandt_pompe_intro", t("docencia.nb_01")),
    ("02", "tau_s_sliding", t("docencia.nb_02")),
    ("03", "recd_levels_excess3", t("docencia.nb_03")),
    ("04", "cctp_record38", t("docencia.nb_04")),
    ("05", "surrogates_nulls", t("docencia.nb_05")),
]
for num, slug, desc in notebooks:
    st.markdown(
        f"""
        <div class="stp-card" style="margin-bottom:0.5rem;padding:0.85rem 1.1rem;">
          <span class="stp-pill">NB {num}</span>
          <strong style="color:#1A2332;margin-left:0.35rem;">{slug}.ipynb</strong>
          <span class="stp-muted"> — {desc}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

callout(t("docencia.nb_note"))
footer()
