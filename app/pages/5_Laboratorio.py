from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "app"))

import numpy as np
import pandas as pd
import streamlit as st

from components.hero import inject_css
from stp.config.settings import AnalysisParams, DOMAIN_PRESETS
from stp.core.pipeline import run_analysis
from stp.data.synthetic_generators import (
    ar_noise,
    cardiac_like_rr,
    coupled_logistic,
    simulate_reloj_extramental,
    aedes_antisync_control,
)
from stp.reports.markdown_report import render_markdown_report
from stp.visualization.series_plots import (
    plot_ews_comparison,
    plot_recd_panel,
    plot_series,
    plot_tau,
)

@st.cache_data(show_spinner=False)
def generate_data(source: str, kind: str, T: int, seed: int, extra: dict) -> np.ndarray:
    if source == "Cardio-like demo":
        return cardiac_like_rr(T=T, event_at=int(T * 0.8), seed=seed)
    elif kind == "Logísticos acoplados (switch)":
        return coupled_logistic(T=T, coupling=0.18, switch_at=T // 2, seed=seed)
    elif kind == "AR ruido":
        return ar_noise(T=T, N=3, seed=seed)
    elif kind == "Simulador Reloj Extramental (Feigenbaum)":
        return simulate_reloj_extramental(T=T, r_control=extra.get("r", 3.8), seed=seed)
    elif kind == "Controlador Antisincrónico (Mosquito)":
        return aedes_antisync_control(T=T, fumigation_at=extra.get("fum_at", int(T*0.6)), seed=seed)
    return np.zeros((T, 2))

@st.cache_data(show_spinner=False)
def cached_run_analysis(X_array: np.ndarray, params_json: str):
    import json
    p = AnalysisParams(**json.loads(params_json))
    return run_analysis(X_array, p)

st.set_page_config(page_title="Laboratorio | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Laboratorio interactivo")
st.caption("Carga → parámetros → análisis (τ_s + RECD + EWS + surrogates) → export con hash.")

# ---- Step 1: data ----
st.header("1. Datos")
source = st.radio(
    "Origen",
    ["Sintético pedagógico", "Subir CSV", "Cardio-like demo"],
    horizontal=True,
)

X = None
domain = "synthetic"
extra_params = {}

if source == "Sintético pedagógico":
    kind = st.selectbox("Tipo", [
        "Logísticos acoplados (switch)", 
        "AR ruido",
        "Simulador Reloj Extramental (Feigenbaum)",
        "Controlador Antisincrónico (Mosquito)"
    ])
    T = st.slider("Longitud T", 300, 3000, 800, 100)
    
    if kind == "Simulador Reloj Extramental (Feigenbaum)":
        extra_params["r"] = st.slider("Constante r (Feigenbaum proxy)", 3.0, 4.0, 3.8, 0.05)
    elif kind == "Controlador Antisincrónico (Mosquito)":
        extra_params["fum_at"] = st.slider("Fumigación en t=", int(T*0.2), int(T*0.8), int(T*0.6), 50)
        
    X = generate_data(source, kind, T, 42, extra_params)
    domain = "synthetic"
elif source == "Cardio-like demo":
    T = st.slider("Latidos (aprox.)", 1000, 8000, 4000, 500)
    X = generate_data(source, "", T, 5, {})
    domain = "cardiology"
else:
    up = st.file_uploader("CSV numérico (columnas = variables)", type=["csv"])
    if up is not None:
        df = pd.read_csv(up)
        num = df.select_dtypes(include=[np.number])
        st.dataframe(num.head())
        cols = st.multiselect("Variables", list(num.columns), default=list(num.columns)[: min(3, num.shape[1])])
        if len(cols) >= 1:
            X = num[cols].to_numpy(dtype=float)
        domain = st.selectbox("Dominio (preset)", list(DOMAIN_PRESETS.keys()), index=0)

if X is not None:
    st.plotly_chart(plot_series(X, "Vista previa"), use_container_width=True)

# ---- Step 2-3: params ----
st.header("2. Parámetros")
preset = DOMAIN_PRESETS.get(domain, DOMAIN_PRESETS["synthetic"])
mode = st.radio("Modo", ["fast", "full"], horizontal=True)
c1, c2, c3 = st.columns(3)
window = c1.number_input("Ventana W", 5, 301, int(preset["window"]), 2)
stride = c2.number_input("Stride", 1, 50, int(preset["stride"]))
theta3 = c3.number_input("θ₃", 0.01, 0.5, float(preset["theta3"]), 0.01)
m = st.select_slider("m (Bandt–Pompe)", options=[2, 3, 4, 5], value=int(preset.get("m", 3)))
n_surr = st.slider("n surrogates", 0, 50, 8 if mode == "fast" else 20)
seed = st.number_input("Seed", 0, 10_000, 42)

# ---- Step 4: run ----
st.header("3. Ejecutar")
if X is None:
    st.warning("Seleccione o cargue datos para continuar.")
elif st.button("▶ Ejecutar análisis completo", type="primary"):
    params = AnalysisParams(
        window=int(window),
        stride=int(stride),
        m=int(m),
        theta3=float(theta3),
        n_surrogates=int(n_surr),
        mode=mode,
        seed=int(seed),
        include_ews=True,
    )
    with st.status("Pipeline en ejecución…", expanded=True) as status:
        st.write("Preprocess + z-score…")
        st.write("Systemic Tau…")
        st.write("RECD Φ₁–Φ₃ + excess3…")
        st.write("EWS clásicos…")
        if n_surr:
            st.write("Surrogates phase-shuffle…")
        
        # Call cached function
        result = cached_run_analysis(X, params.model_dump_json())
        
        st.write("Hash de reproducibilidad…")
        status.update(label="Análisis completo (desde caché si aplica)", state="complete")

    st.session_state["lab_result"] = result
    st.session_state["lab_domain"] = domain
    st.success(f"Listo. `repro_hash = {result.repro_hash}`")

# ---- Step 5: results ----
result = st.session_state.get("lab_result")
if result is not None:
    st.header("4. Resultados")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Δτ_s", f"{result.metrics['delta_tau_s']:.4f}")
    k2.metric("mean excess3", f"{result.metrics['mean_excess3']:.4f}")
    k3.metric("Δexcess3", f"{result.metrics['delta_excess3']:.4f}")
    pval = result.surrogate_stats.get("tau_s", {}).get("p_value", None)
    k4.metric("p_surr (τ_s)", f"{pval:.3f}" if pval is not None else "—")

    t1, t2, t3, t4 = st.tabs(["τ_s", "RECD", "EWS clásicos", "Export"])
    with t1:
        st.plotly_chart(plot_tau(result), use_container_width=True)
    with t2:
        st.plotly_chart(plot_recd_panel(result), use_container_width=True)
    with t3:
        st.plotly_chart(plot_ews_comparison(result), use_container_width=True)
    with t4:
        md = render_markdown_report(result, domain=st.session_state.get("lab_domain", domain))
        st.download_button(
            "Descargar reporte Markdown",
            data=md,
            file_name="stp_report.md",
            mime="text/markdown",
        )
        st.code(result.repro_hash, language="text")
        st.json(result.metrics)
