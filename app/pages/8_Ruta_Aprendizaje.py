from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css
from stp.education.content_loader import read_markdown
from stp.education.glossary import search_glossary

st.set_page_config(page_title="Aprendizaje | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Ruta de aprendizaje")

levels = {
    "Básico": [
        "Leer Fundamentos → Tau Sistémica y límites de EWS",
        "Glosario: τ_s, RECD, Bandt–Pompe, Kairos",
        "Demo Lab sintético (Fast)",
    ],
    "Intermedio": [
        "RECD Φ₁–Φ₃ y excess3",
        "Dominio Cardiología (CCTP) + comparación EWS",
        "Surrogates phase-shuffle: interpretar p-valores",
        "Dominio Dengue",
    ],
    "Avanzado": [
        "Breathing Window y pesos α(λ)",
        "TDA Tier 4 + memoria ordinal",
        "Diseñar un estudio con hash de reproducibilidad",
        "Leer Síntesis Magna y preprint CCTP",
    ],
}

for level, items in levels.items():
    with st.expander(f"Nivel {level}", expanded=(level == "Básico")):
        for i, item in enumerate(items):
            key = f"lp_{level}_{i}"
            st.checkbox(item, key=key)

st.subheader("Glosario interactivo")
q = st.text_input("Buscar término", "")
for term in search_glossary(q):
    with st.expander(term.get("term", "?")):
        st.markdown(f"**{term.get('short','')}**")
        st.markdown(term.get("long", ""))
        st.caption(f"Nivel: {term.get('level', '—')}")

st.subheader("FAQ")
st.markdown(read_markdown("learning", "faq.md"))
