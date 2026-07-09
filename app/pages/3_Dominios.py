from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t
from stp.domains import domain_label

from components.ui import page_link, callout, footer, learning_goals, page_header, section_header
from stp.education.content_loader import read_markdown

st.set_page_config(page_title=t("dominios.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("dominios.title"),
    subtitle=t("dominios.subtitle"),
    eyebrow=t("dominios.eyebrow"),
    icon="🌐",
)

learning_goals(
    [t("dominios.goal_1"), t("dominios.goal_2"), t("dominios.goal_3")]
)

domains = [
    {
        "name": "Cardiología",
        "key": "cardiology",
        "file": "cardiologia.md",
        "icon": "🫀",
        "maturity": "Muy alto",
        "maturity_cls": "high",
        "data": "SDDB / CCTP",
        "lab_dataset": "sddb_rr_38_demo",
        "blurb": "Pre-FV: τ_s y excess3; panel clásico a menudo ambiguo. Ancla empírica v1.0.",
    },
    {
        "name": "Epidemiología",
        "key": "epidemiology",
        "file": "epidemiologia.md",
        "icon": "🦠",
        "maturity": "Alto",
        "maturity_cls": "high",
        "data": "Dengue-like demo",
        "lab_dataset": "dengue_like_demo",
        "blurb": "Brote con acoplamiento cases–clima (reorganización ordinal, no solo rampas).",
    },
    {
        "name": "Neurociencia",
        "key": "neuroscience",
        "file": "neurociencia.md",
        "icon": "🧠",
        "maturity": "Medio-Alto",
        "maturity_cls": "med",
        "data": "EEG-like demo",
        "lab_dataset": "eeg_like_demo",
        "blurb": "Transición de acoplamiento entre canales — gramática ictal de juguete.",
    },
    {
        "name": "Ecología",
        "key": "ecology",
        "file": "ecologia.md",
        "icon": "🌿",
        "maturity": "Medio",
        "maturity_cls": "med",
        "data": "Lago-like demo",
        "lab_dataset": "ecology_like_demo",
        "blurb": "Bloom / eutrofización: puente con la literatura CSD de lagos.",
    },
    {
        "name": "Clima e hidrología",
        "key": "climate",
        "file": "clima.md",
        "icon": "drought",
        "icon_emoji": "🏜️",
        "maturity": "Medio",
        "maturity_cls": "med",
        "data": "Sequía-like demo",
        "lab_dataset": "climate_drought_demo",
        "blurb": "Temp–precip–suelo bajo latente de sequía. CSD climático sin forecast operativo.",
    },
    {
        "name": "Aprendizaje colectivo",
        "key": "education",
        "file": "educacion.md",
        "icon_emoji": "🎓",
        "maturity": "Medio",
        "maturity_cls": "med",
        "data": "Cohorte demo",
        "lab_dataset": "education_cohort_demo",
        "blurb": "Meta-pedagógico: engagement · peers · carga como sistema relacional del aula.",
    },
    {
        "name": "Dinámica social",
        "key": "social",
        "file": "social.md",
        "icon_emoji": "🗣️",
        "maturity": "Bajo-Medio",
        "maturity_cls": "low",
        "data": "Polarización-like",
        "lab_dataset": "social_polarization_demo",
        "blurb": "Modelo de juguete de polarización. Enseña el método; no predice lo social.",
    },
    {
        "name": "Fisiología del sueño",
        "key": "physiology",
        "file": "fisiologia.md",
        "icon_emoji": "😴",
        "maturity": "Medio",
        "maturity_cls": "med",
        "data": "Sueño-like demo",
        "lab_dataset": "sleep_fragmentation_demo",
        "blurb": "HRV · actividad · temp: fragmentación circadiana. Puente con cardio.",
    },
    {
        "name": "Finanzas",
        "key": "finance",
        "file": "finanzas.md",
        "icon_emoji": "📈",
        "maturity": "Medio",
        "maturity_cls": "low",
        "data": "Vol-like demo",
        "lab_dataset": "finance_like_demo",
        "blurb": "Regímenes de volatilidad para transferir el método — no para trading ciego.",
    },
]
# localize display names, blurbs, maturity
_mat_map = {
    "Muy alto": "very_high",
    "Alto": "high",
    "Medio-Alto": "med_high",
    "Medio": "med",
    "Bajo-Medio": "low_med",
    "Bajo": "low",
}
for _d in domains:
    _d["name"] = domain_label(_d["key"])
    _bk = f"domain_blurbs.{_d['key']}"
    _bv = t(_bk)
    if _bv != _bk:
        _d["blurb"] = _bv
    _mk = _mat_map.get(_d.get("maturity", ""), "")
    if _mk:
        _mv = t(f"maturity.{_mk}")
        if _mv != f"maturity.{_mk}":
            _d["maturity"] = _mv

# Normalize icon field
for d in domains:
    d.setdefault("icon", d.get("icon_emoji", "◆"))

section_header(t("dominios.map_header"))
callout(t("dominios.anchor_callout"))

# Two rows of domain cards
row1 = domains[:5]
row2 = domains[5:]
for row in (row1, row2):
    cols = st.columns(len(row))
    for col, d in zip(cols, row):
        with col:
            st.markdown(
                f"""
                <div class="stp-domain-card">
                  <div class="dom-icon">{d['icon']}</div>
                  <h3>{d['name']}</h3>
                  <span class="stp-pill {d['maturity_cls']}">{d['maturity']}</span>
                  <span class="stp-pill purple">{d['data']}</span>
                  <p class="stp-muted" style="margin-top:0.65rem;">{d['blurb']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

section_header(t("dominios.synth_header"))
callout(t("dominios.synth_callout"))

section_header(t("dominios.detail_header"))
choice = st.selectbox(
    t("dominios.select"),
    [d["name"] for d in domains],
    format_func=lambda n: f"{next(d['icon'] for d in domains if d['name']==n)}  {n}",
)
selected = next(d for d in domains if d["name"] == choice)
callout(
    t(
        "dominios.ref_callout",
        data=selected["data"],
        maturity=selected["maturity"],
    )
)

with st.container():
    st.markdown(read_markdown("dominios", selected["file"]))

section_header(t("dominios.open_header"))
st.markdown(t("dominios.open_body", name=selected["name"]))
b1, b2 = st.columns(2)
with b1:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("dominios.lab_preset", name=selected["name"]),
        icon="🔬",
        query_params={"domain": selected["key"], "dataset": selected["lab_dataset"]},
    )
with b2:
    page_link(
        "pages/4_Laboratorio.py",
        label=t("dominios.lab_empty"),
        icon="📂",
    )

page_link(
    "pages/4_Laboratorio.py",
    label=t("dominios.try_lab"),
    icon="🔬",
    query_params={"domain": selected["key"], "dataset": selected["lab_dataset"]},
)
page_link("pages/6_Evidencia.py", label=t("nav.evidence_cctp"), icon="📑")
footer()
