from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st
import yaml

from components.hero import inject_css
from stp.config.settings import CONTENT_DIR

st.set_page_config(page_title="Evidencia | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Evidencia científica y publicaciones")

path = CONTENT_DIR / "evidencia" / "publications.yaml"
data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}

st.subheader("Publicaciones y preprints del paradigma")
for pub in data.get("publications", []):
    with st.container():
        st.markdown(f"### {pub.get('title')}")
        st.caption(
            f"{pub.get('authors')} · {pub.get('year')} · {pub.get('type')} · dominio: {pub.get('domain')}"
        )
        if pub.get("doi"):
            st.markdown(f"DOI: `{pub['doi']}`")
        for h in pub.get("highlights", []):
            st.markdown(f"- {h}")
        st.markdown("---")

st.subheader("Comparación con otros enfoques")
rows = data.get("comparison_matrix", [])
if rows:
    st.dataframe(rows, use_container_width=True)

st.info(
    "Caso validado de referencia: **CCTP/SDDB** (N=10) — reorganización relacional pre-FV "
    "con τ_s y excess3; ver `Investigaciones/Cardiac_CCTP_Pilot/`."
)
