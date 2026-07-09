"""Systemic Tau Platform — Home."""

from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parent
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.illustrations import show_illustration
from components.ui import (
    page_link,
    achieve_card,
    callout,
    feature_card,
    footer,
    learning_goals,
    metrics_strip,
    nav_card,
    render_hero,
    section_header,
)
from stp.education.content_loader import read_markdown
from stp.i18n.core import t

st.set_page_config(
    page_title=t("meta.app_title"),
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_hero(
    tagline=t("home.tagline"),
    description=t("home.description"),
)

learning_goals(
    [t("home.goal_1"), t("home.goal_2"), t("home.goal_3")],
    title=t("home.goals_title"),
)

callout(t("home.audience"))

show_illustration("hero")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        feature_card(t("home.card_ordinal_title"), t("home.card_ordinal_body"), icon="⬡", accent="navy"),
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        feature_card(t("home.card_recd_title"), t("home.card_recd_body"), icon="◈", accent="teal"),
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        feature_card(t("home.card_falsable_title"), t("home.card_falsable_body"), icon="◎", accent="purple"),
        unsafe_allow_html=True,
    )

section_header(t("home.core_header"))
show_illustration("pipeline")

a1, a2, a3, a4 = st.columns(4)
with a1:
    st.markdown(
        achieve_card(t("home.achieve_pipe_title"), t("home.achieve_pipe_body"), t("common.operational")),
        unsafe_allow_html=True,
    )
with a2:
    st.markdown(
        achieve_card(t("home.achieve_ev_title"), t("home.achieve_ev_body"), t("common.documented")),
        unsafe_allow_html=True,
    )
with a3:
    st.markdown(
        achieve_card(t("home.achieve_curr_title"), t("home.achieve_curr_body"), t("common.available")),
        unsafe_allow_html=True,
    )
with a4:
    st.markdown(
        achieve_card(t("home.achieve_tda_title"), t("home.achieve_tda_body"), t("common.operational")),
        unsafe_allow_html=True,
    )

with st.expander(t("home.core_detail"), expanded=False):
    st.markdown(read_markdown("learning", "v1_logros.md"))

section_header(t("home.scale_header"))
metrics_strip(
    [
        ("9+", t("home.metric_domains")),
        ("3", t("home.metric_recd")),
        ("TDA+BW", t("home.metric_ext")),
        ("SHA-256", t("home.metric_repro")),
    ]
)

section_header(t("home.pick_domain"))
st.caption(t("home.pick_domain_cap"))

domains = [
    (t("home.dom_cardio"), "🫀", t("home.dom_cardio_hint"), "cardio"),
    (t("home.dom_epi"), "🦠", t("home.dom_epi_hint"), "epi"),
    (t("home.dom_neuro"), "🧠", t("home.dom_neuro_hint"), "neuro"),
    (t("home.dom_eco"), "🌿", t("home.dom_eco_hint"), "eco"),
    (t("home.dom_fin"), "📈", t("home.dom_fin_hint"), "fin"),
]

cols = st.columns(5)
for col, (name, icon, hint, key) in zip(cols, domains):
    with col:
        selected = st.session_state.get("domain_interest_key") == key
        if st.button(
            f"{icon}\n{name.split('(')[0].strip()}",
            key=f"dom_{key}",
            width="stretch",
            type="primary" if selected else "secondary",
        ):
            st.session_state["domain_interest"] = name
            st.session_state["domain_interest_key"] = key
            st.rerun()
        st.caption(hint)

domain = st.session_state.get("domain_interest", domains[0][0])
st.session_state["domain_interest"] = domain
dom_key = st.session_state.get("domain_interest_key", "cardio")

if dom_key == "cardio":
    callout(t("home.active_cardio", domain=domain))
else:
    callout(t("home.active_other", domain=domain))

section_header(t("home.route_header"))
r1, r2, r3 = st.columns(3)
with r1:
    st.markdown(
        feature_card(t("home.route_1_title"), t("home.route_1_body"), icon="📘", accent="navy"),
        unsafe_allow_html=True,
    )
with r2:
    st.markdown(
        feature_card(t("home.route_2_title"), t("home.route_2_body"), icon="🔬", accent="teal"),
        unsafe_allow_html=True,
    )
with r3:
    st.markdown(
        feature_card(t("home.route_3_title"), t("home.route_3_body"), icon="📑", accent="purple"),
        unsafe_allow_html=True,
    )

section_header(t("home.explore"))

n1, n2, n3, n4 = st.columns(4)
with n1:
    st.markdown(nav_card(t("home.nav_fund_title"), t("home.nav_fund_body"), "📘"), unsafe_allow_html=True)
    page_link("pages/1_Fundamentos.py", label=t("nav.open_fundamentos"), icon="📘")
with n2:
    st.markdown(nav_card(t("home.nav_math_title"), t("home.nav_math_body"), "📐"), unsafe_allow_html=True)
    page_link("pages/2_Matematica.py", label=t("nav.open_matematica"), icon="📐")
with n3:
    st.markdown(nav_card(t("home.nav_lab_title"), t("home.nav_lab_body"), "🔬"), unsafe_allow_html=True)
    page_link("pages/4_Laboratorio.py", label=t("nav.open_lab"), icon="🔬")
with n4:
    st.markdown(nav_card(t("home.nav_ev_title"), t("home.nav_ev_body"), "📑"), unsafe_allow_html=True)
    page_link("pages/6_Evidencia.py", label=t("nav.open_evidencia"), icon="📑")

section_header(t("home.more_routes"))
r1, r2, r3, r4 = st.columns(4)
with r1:
    page_link("pages/3_Dominios.py", label=t("nav.domains_app"), icon="🌐")
with r2:
    page_link("pages/5_Ruta_Aprendizaje.py", label=t("nav.learning_path"), icon="🗺️")
with r3:
    page_link("pages/7_Docencia.py", label=t("nav.teaching_6w"), icon="🎓")
with r4:
    page_link("pages/8_Materiales.py", label=t("nav.downloadable"), icon="📦")

last = st.session_state.get("lab_result")
if last is not None:
    section_header(t("home.last_analysis"))
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Δτ_s", f"{last.metrics.get('delta_tau_s', 0):.4f}")
    m2.metric("Δexcess3", f"{last.metrics.get('delta_excess3', 0):.4f}")
    pval = last.surrogate_stats.get("tau_s", {}).get("p_value")
    m3.metric("p_surr", f"{pval:.3f}" if pval is not None else "—")
    m4.metric(t("common.domain"), getattr(last, "domain", "—"))
    st.caption(f"`repro_hash` = {last.repro_hash}")
    page_link("pages/4_Laboratorio.py", label=t("nav.back_lab"), icon="🔬")

section_header(t("home.lab_shortcuts"))
a1, a2, a3 = st.columns(3)
with a1:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("home.shortcut_logistic"),
        icon="🔬",
        query_params={"dataset": "synthetic_coupled_logistic", "domain": "synthetic"},
    )
with a2:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("home.shortcut_sddb"),
        icon="🫀",
        query_params={"dataset": "sddb_rr_38_demo", "domain": "cardiology"},
    )
with a3:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("home.shortcut_dengue"),
        icon="🦠",
        query_params={"dataset": "dengue_like_demo", "domain": "epidemiology"},
    )

with st.expander(t("home.about"), expanded=False):
    st.markdown(t("home.about_body"))

footer()
