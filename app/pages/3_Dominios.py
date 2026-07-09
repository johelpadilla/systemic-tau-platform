from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css
from stp.education.content_loader import read_markdown

st.set_page_config(page_title="Dominios | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Aplicaciones por dominio")
st.markdown(
    """
    La misma firma — **reorganización relacional ordinal** — se investiga en dominios
    aparentemente distantes. Elija un dominio en el menú lateral (3a–3e) o explore el resumen abajo.
    """
)

domains = [
    ("Cardiología", "cardiologia.md", "Muy alto", "SDDB / CCTP"),
    ("Epidemiología", "epidemiologia.md", "Alto", "Dengue PR / DengAI"),
    ("Neurociencia", "neurociencia.md", "Medio-Alto", "CHB-MIT"),
    ("Ecología", "ecologia.md", "Medio", "Lake Mendota / LTER"),
    ("Finanzas", "finanzas.md", "Medio", "S&P 500"),
]

cols = st.columns(5)
for col, (name, _, maturity, data) in zip(cols, domains):
    with col:
        st.markdown(
            f"""
            <div class="stp-card">
              <h3>{name}</h3>
              <p class="stp-muted"><b>Madurez:</b> {maturity}<br/><b>Datos:</b> {data}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")
choice = st.selectbox("Vista previa del contenido", [d[0] for d in domains])
fname = dict((d[0], d[1]) for d in domains)[choice]
st.markdown(read_markdown("dominios", fname))
