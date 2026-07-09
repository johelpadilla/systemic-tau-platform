from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css

st.set_page_config(page_title="Planes | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Planes")
st.caption("Posicionamiento SaaS educativo premium. v1.0 es funcionalmente abierta; los gates de pago son UI.")

plans = [
    {
        "name": "Free",
        "price": "$0",
        "items": [
            "Fundamentos y Matemática",
            "Samples sintéticos",
            "Lab modo Fast",
            "Reporte Markdown sin branding",
        ],
    },
    {
        "name": "Academic",
        "price": "$0 (verificación)",
        "items": [
            "Todo Free",
            "Lab Full (surrogates altos)",
            "Notebooks de docencia",
            "Sin watermark institucional",
        ],
    },
    {
        "name": "Professional",
        "price": "SaaS",
        "items": [
            "Reportes PDF con branding",
            "Datasets propios ilimitados (sesión)",
            "API futura",
            "Soporte prioritario",
        ],
    },
    {
        "name": "Institutional",
        "price": "Cotización",
        "items": [
            "White-label",
            "Multi-usuario / SSO",
            "Curricula personalizada",
            "Integración con LMS",
        ],
    },
]

cols = st.columns(4)
for col, plan in zip(cols, plans):
    with col:
        st.markdown(f"### {plan['name']}")
        st.markdown(f"**{plan['price']}**")
        for item in plan["items"]:
            st.markdown(f"- {item}")
        st.button(f"Elegir {plan['name']}", key=plan["name"], disabled=plan["name"] != "Free")

st.info("En v1.0 todos los análisis del Lab están disponibles en local sin backend de pagos.")
