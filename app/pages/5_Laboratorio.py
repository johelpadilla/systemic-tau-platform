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
from stp.reports.pdf_report import generate_pdf_report
from stp.visualization.series_plots import (
    plot_ews_comparison,
    plot_recd_panel,
    plot_series,
    plot_tau,
    plot_manifold_3d,
)
from locales import t

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

st.set_page_config(page_title=f"{t('lab_page_title')} | STP", page_icon="🌀", layout="wide")
inject_css()

st.title(t("lab_page_title"))
st.caption(t("lab_caption"))

# ---- Step 1: data ----
st.header(t("lab_s1"))
source = st.radio(
    t("lab_origin"),
    [t("lab_o1"), t("lab_o2"), t("lab_o3"), "Datos Reales (PhysioNet)"],
    horizontal=True,
)

X = None
domain = "synthetic"
extra_params = {}

if source == t("lab_o1"):
    kind = st.selectbox(t("lab_type"), [
        "Logísticos acoplados (switch)", 
        "AR ruido",
        "Simulador Reloj Extramental (Feigenbaum)",
        "Controlador Antisincrónico (Mosquito)"
    ])
    T = st.slider(t("lab_len"), 300, 3000, 800, 100)
    
    if kind == "Simulador Reloj Extramental (Feigenbaum)":
        extra_params["r"] = st.slider(t("lab_r"), 3.0, 4.0, 3.8, 0.05)
    elif kind == "Controlador Antisincrónico (Mosquito)":
        extra_params["fum_at"] = st.slider(t("lab_fum"), int(T*0.2), int(T*0.8), int(T*0.6), 50)
        
    X = generate_data("Sintético pedagógico", kind, T, 42, extra_params)
    domain = "synthetic"
elif source == t("lab_o3"):
    T = st.slider(t("lab_beats"), 1000, 8000, 4000, 500)
    X = generate_data("Cardio-like demo", "", T, 5, {})
    domain = "cardiology"
elif source == "Datos Reales (PhysioNet)":
    dataset = st.selectbox("Seleccione el dataset:", ["Normal Sinus Rhythm (NSR)", "Congestive Heart Failure (CHF)"])
    if dataset == "Normal Sinus Rhythm (NSR)":
        df = pd.read_csv('data/physionet_samples/nsr_16265.csv')
    else:
        df = pd.read_csv('data/physionet_samples/chf_chf01.csv')
    T_real = st.slider(t("lab_beats"), 500, len(df), 2000, 500)
    X = df.head(T_real).to_numpy(dtype=float)
    domain = "cardiology"
else:
    up = st.file_uploader(t("lab_up"), type=["csv"])
    if up is not None:
        df = pd.read_csv(up)
        num = df.select_dtypes(include=[np.number])
        st.dataframe(num.head())
        cols = st.multiselect(t("lab_vars"), list(num.columns), default=list(num.columns)[: min(3, num.shape[1])])
        if len(cols) >= 1:
            X = num[cols].to_numpy(dtype=float)
        domain = st.selectbox(t("lab_dom"), list(DOMAIN_PRESETS.keys()), index=0)

if X is not None:
    st.plotly_chart(plot_series(X, t("lab_prev")), use_container_width=True)

# ---- Step 2-3: params ----
st.header(t("lab_s2"))
preset = DOMAIN_PRESETS.get(domain, DOMAIN_PRESETS["synthetic"])
mode = st.radio(t("math_mode"), ["fast", "full"], horizontal=True)

auto_tune = st.toggle("Auto-sintonizar parámetros (Auto-Tau)", value=False)

c1, c2, c3 = st.columns(3)
if auto_tune:
    c1.info("El tamaño de ventana se calculará automáticamente.")
    c2.info("El stride (retraso) se calculará mediante Información Mutua/Autocorrelación.")
    window = int(preset["window"])
    stride = int(preset["stride"])
    m = 3
else:
    window = c1.number_input(t("lab_w"), 5, 301, int(preset["window"]), 2)
    stride = c2.number_input(t("lab_stride"), 1, 50, int(preset["stride"]))
    m = st.select_slider(t("lab_m"), options=[2, 3, 4, 5], value=int(preset.get("m", 3)))

theta3 = c3.number_input(t("lab_t3"), 0.01, 0.5, float(preset["theta3"]), 0.01)
n_surr = st.slider(t("lab_nsurr"), 0, 50, 8 if mode == "fast" else 20)
seed = st.number_input(t("lab_seed"), 0, 10_000, 42)

# ---- Step 4: run ----
st.header(t("lab_s3"))
if X is None:
    st.warning(t("lab_warn"))
elif st.button(t("lab_run"), type="primary"):
    params = AnalysisParams(
        window=int(window),
        stride=int(stride),
        m=int(m),
        theta3=float(theta3),
        n_surrogates=int(n_surr),
        mode=mode,
        seed=int(seed),
        include_ews=True,
        auto_tune=auto_tune,
    )
    with st.status(t("lab_status"), expanded=True) as status:
        st.write(t("lab_st1"))
        st.write(t("lab_st2"))
        st.write(t("lab_st3"))
        st.write(t("lab_st4"))
        if n_surr:
            st.write(t("lab_st5"))
        
        # Call cached function
        result = cached_run_analysis(X, params.model_dump_json())
        
        st.write(t("lab_st6"))
        status.update(label=t("lab_st7"), state="complete")

    st.session_state["lab_result"] = result
    st.session_state["lab_domain"] = domain
    st.success(t("lab_succ", hash=result.repro_hash[:16]))

# ---- Step 5: results ----
result = st.session_state.get("lab_result")
if result is not None:
    st.header(t("lab_s4"))
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Δτ_s", f"{result.metrics['delta_tau_s']:.4f}")
    k2.metric("mean excess3", f"{result.metrics['mean_excess3']:.4f}")
    k3.metric("Δexcess3", f"{result.metrics['delta_excess3']:.4f}")
    pval = result.surrogate_stats.get("tau_s", {}).get("p_value", None)
    k4.metric(t("lab_psurr"), f"{pval:.3f}" if pval is not None else "—")

    t1, t2, t3, t4, t5 = st.tabs([t("lab_t1"), t("lab_t2"), t("lab_t3"), t("lab_t4"), "Manifold 3D"])
    with t1:
        st.plotly_chart(plot_tau(result), use_container_width=True)
    with t2:
        st.plotly_chart(plot_recd_panel(result), use_container_width=True)
    with t3:
        st.plotly_chart(plot_ews_comparison(result), use_container_width=True)
    with t4:
        md = render_markdown_report(result, domain=st.session_state.get("lab_domain", domain))
        st.download_button(
            t("lab_down"),
            data=md,
            file_name="stp_report.md",
            mime="text/markdown",
        )
        
        pdf_bytes = generate_pdf_report(result, domain=st.session_state.get("lab_domain", domain))
        st.download_button(
            "Exportar Reporte Científico (PDF)",
            data=pdf_bytes,
            file_name="stp_scientific_report.pdf",
            mime="application/pdf",
        )
        
        st.code(result.repro_hash, language="text")
        st.json(result.metrics)
    with t5:
        st.plotly_chart(plot_manifold_3d(result), use_container_width=True)
