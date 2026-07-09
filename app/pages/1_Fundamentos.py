from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css
from stp.education.content_loader import read_markdown

st.set_page_config(page_title="Fundamentos | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Fundamentos teóricos")
st.caption("Definiciones precisas, límites de las EWS clásicas y ontología del RECD.")

tabs = st.tabs(
    [
        "Tau Sistémica",
        "Límites EWS",
        "RECD Φ₁–Φ₃",
        "excess3",
        "CSD",
        "Filosofía",
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

for tab, parts in zip(tabs, files):
    with tab:
        st.markdown(read_markdown(*parts))

st.sidebar.markdown("### En esta sección")
st.sidebar.markdown(
    """
    1. ¿Qué es Tau Sistémica?
    2. Problema de las EWS clásicas
    3. RECD y niveles anidados
    4. excess3
    5. Transiciones críticas / CSD
    6. Polo y tiempo extramental
    """
)
