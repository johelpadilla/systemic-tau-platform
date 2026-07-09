"""Entrypoint with localized multipage navigation (st.navigation).

Prefer:
  streamlit run app/streamlit_app.py
  stp serve

Individual pages remain runnable for AppTest isolation.
"""

from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parent
if str(_APP) not in sys.path:
    sys.path.insert(0, str(_APP))

from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.ui import safe_set_page_config
from stp.i18n.core import get_lang, t

# Restore language from session/env so nav labels match the UI language.
_ = get_lang()

safe_set_page_config(
    page_title=t("meta.app_title"),
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Paths relative to this file (app/).
pages = [
    st.Page("Home.py", title=t("nav.home"), icon="🏠", default=True),
    st.Page("pages/1_Fundamentos.py", title=t("nav.fundamentos"), icon="📘"),
    st.Page("pages/2_Matematica.py", title=t("nav.matematica"), icon="📐"),
    st.Page("pages/3_Dominios.py", title=t("nav.dominios"), icon="🌐"),
    st.Page("pages/4_Laboratorio.py", title=t("nav.laboratorio"), icon="🔬"),
    st.Page("pages/5_Ruta_Aprendizaje.py", title=t("nav.ruta"), icon="🗺️"),
    st.Page("pages/6_Evidencia.py", title=t("nav.evidencia"), icon="📑"),
    st.Page("pages/7_Docencia.py", title=t("nav.docencia"), icon="🎓"),
    st.Page("pages/8_Materiales.py", title=t("nav.materiales"), icon="📦"),
    st.Page("pages/9_About_Legal.py", title=t("nav.about"), icon="⚖️"),
]

st.navigation(pages).run()
