from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import math

import numpy as np
import streamlit as st

from components.hero import inject_css
from stp.core.ordinal import bandt_pompe_symbols
from stp.core.pipeline import run_analysis
from stp.config.settings import AnalysisParams
from stp.data.generators import coupled_logistic
from stp.education.content_loader import read_markdown
from stp.visualization.series_plots import plot_recd_panel, plot_tau

st.set_page_config(page_title="Matemática | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Matemática del paradigma")
st.markdown(read_markdown("matematica", "overview.md"))

st.subheader("Sandbox: Bandt–Pompe")
m = st.slider("Dimensión m", 2, 5, 3)
delay = st.slider("Delay", 1, 5, 1)
x = np.sin(np.linspace(0, 12, 200)) + 0.1 * np.random.default_rng(0).normal(size=200)
sym = bandt_pompe_symbols(x, m=m, delay=delay)
c1, c2 = st.columns(2)
with c1:
    st.line_chart(x)
    st.caption("Serie demo (seno + ruido)")
with c2:
    st.bar_chart(np.bincount(sym, minlength=math.factorial(m)))
    st.caption(f"Histograma de símbolos (m! = {math.factorial(m)})")

st.subheader("Demo rápida: τ_s + RECD en mapas logísticos acoplados")
mode = st.radio("Modo", ["fast", "full"], horizontal=True, index=0)
if st.button("Ejecutar demo matemática", type="primary"):
    X = coupled_logistic(T=600, coupling=0.2, switch_at=300, seed=7)
    params = AnalysisParams(window=51, stride=2, mode=mode, n_surrogates=4 if mode == "fast" else 20)
    with st.spinner("Calculando..."):
        result = run_analysis(X, params)
    st.success(f"Hash: `{result.repro_hash[:16]}…`")
    st.plotly_chart(plot_tau(result), use_container_width=True)
    st.plotly_chart(plot_recd_panel(result), use_container_width=True)
    st.json(result.metrics)

with st.expander("Ventana adaptativa, TDA, memoria ordinal, surrogates"):
    st.markdown(
        """
        - **Breathing Window:** W se adapta al régimen (implementación completa en roadmap P4).
        - **TDA / Betti:** disponible en modo Full cuando el extra `tda` está instalado.
        - **Memoria ordinal:** TE simbólica / MI de rangos (Full).
        - **Surrogates:** phase-shuffle e IAAFT — ver Laboratorio para controles nulos completos.

        Documentación de ingeniería: `docs/ENGINEERING.md` y `docs/LAB_FLOW.md`.
        """
    )
