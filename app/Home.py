"""Systemic Tau Platform — Home."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


import streamlit as st

from components.hero import render_hero

st.set_page_config(
    page_title="Systemic Tau Platform",
    page_icon="🌀",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_hero()
load_css()

st.markdown(
    """
    **Público:** investigadores, posgrado y profesionales que ya conocen el paradigma
    y necesitan rigor, conexiones ontológicas y experimentación reproducible.
    """
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class="stp-card">
          <h3>Ordinal & relacional</h3>
          <p class="stp-muted">Observables basados en orden y conjunciones, no solo en varianza.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="stp-card">
          <h3>RECD anidado</h3>
          <p class="stp-muted">Φ₁ · Φ₂ · Φ₃ y excess3 como proxy de sinergia irreducible.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="stp-card">
          <h3>Falsable</h3>
          <p class="stp-muted">Surrogates, comparación con EWS clásicos y hash de reproducibilidad.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("Dominio de interés")
domain = st.selectbox(
    "Seleccione un dominio para personalizar la navegación",
    options=[
        "Cardiología (SDDB / pre-FV)",
        "Epidemiología (Dengue)",
        "Neurociencia (Epilepsia / EEG)",
        "Ecología (Eutrofización de lagos)",
        "Finanzas (regímenes de volatilidad)",
    ],
    index=0,
)
st.session_state["domain_interest"] = domain
st.info(
    f"Dominio activo: **{domain}**. Use el menú lateral para Fundamentos, Matemática, Dominios y Laboratorio."
)

st.subheader("Accesos rápidos")
a, b, c, d = st.columns(4)
a.page_link("pages/1_Fundamentos.py", label="Fundamentos teóricos", icon="📘")
b.page_link("pages/3_Matematica.py", label="Matemática", icon="📐")
c.page_link("pages/5_Laboratorio.py", label="Laboratorio", icon="🔬")
d.page_link("pages/6_Evidencia.py", label="Evidencia", icon="📑")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Dominios", "5")
m2.metric("Niveles RECD", "3")
m3.metric("Cohorte CCTP", "N=10")
m4.metric("Versión", "1.0.0")

with st.expander("Sobre el producto"):
    st.markdown(
        """
        *Systemic Tau Platform* unifica el conocimiento de Tau Sistémica y RECD en un producto
        educativo/científico de calidad universitaria: teoría, matemática, aplicaciones por dominio,
        laboratorio interactivo, ruta de aprendizaje y evidencia publicada.

        Código alineado con `systemictau`, `nested-recd` y el piloto **CCTP/SDDB**.
        """
    )
