from __future__ import annotations

import json
import sys
from pathlib import Path

# Prefer this repo's src/ over a stale editable install elsewhere
_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import numpy as np
import pandas as pd
import streamlit as st

from components.illustrations import show_illustration
from components.ui import (
    callout,
    empty_state,
    footer,
    interpret_box,
    lab_stepper,
    learning_goals,
    page_header,
    section_header,
)
from stp.config import settings as _settings
from stp.config.settings import AnalysisParams, DOMAIN_PRESETS

# Defensive: hot-reload / stale modules must not crash the Lab
DOMAIN_LABELS = getattr(
    _settings,
    "DOMAIN_LABELS",
    {
        "cardiology": "Cardiología",
        "epidemiology": "Epidemiología",
        "neuroscience": "Neurociencia",
        "ecology": "Ecología",
        "finance": "Finanzas",
        "climate": "Clima e hidrología",
        "social": "Dinámica social",
        "education": "Aprendizaje colectivo",
        "physiology": "Fisiología del sueño",
        "synthetic": "Sintético",
    },
)
from stp.core.pipeline import result_to_jsonable, run_analysis
from stp.i18n.core import t
from stp.data.catalog import dataset_title, list_datasets, load_dataset
from stp.domains import domain_hint, domain_label, estimate_runtime_seconds, get_adapter
from stp.reports.markdown_report import render_markdown_report, render_methods_only
from stp.core.tda_betti import has_ripser
from stp.visualization.series_plots import (
    plot_breathing,
    plot_dual_summary,
    plot_ews_comparison,
    plot_recd_panel,
    plot_series,
    plot_tau,
    plot_tda_betti,
)

st.set_page_config(page_title=t("lab.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("lab.title"),
    subtitle=t("lab.subtitle"),
    eyebrow=t("lab.eyebrow"),
    icon="🔬",
)

learning_goals(
    [t("lab.goal_1"), t("lab.goal_2"), t("lab.goal_3")]
)

# ---- Deep-link / session bootstrap ----
qp = st.query_params
if "dataset" in qp and "lab_bootstrapped" not in st.session_state:
    try:
        X0, meta0 = load_dataset(qp["dataset"])
        st.session_state["lab_X"] = X0
        st.session_state["lab_meta"] = meta0
        st.session_state["lab_domain"] = meta0.get("domain", "synthetic")
        st.session_state["lab_event"] = meta0.get("event_index")
        st.session_state["lab_has_data"] = True
        st.session_state["lab_bootstrapped"] = True
        st.session_state["lab_source_label"] = meta0.get("title", qp["dataset"])
    except Exception as e:
        st.warning(t("lab.query_fail", err=e))

if "domain" in qp and "lab_domain_qp" not in st.session_state:
    d = qp["domain"]
    if d in DOMAIN_PRESETS:
        st.session_state["lab_domain"] = d
        st.session_state["lab_domain_qp"] = d

show_illustration("pipeline")
show_illustration("dual_reading")

# ---- State ----
X = st.session_state.get("lab_X")
domain = st.session_state.get("lab_domain", "synthetic")
event_index = st.session_state.get("lab_event")
event_label = st.session_state.get("lab_event_label", t("common.event"))
result = st.session_state.get("lab_result")
has_result = result is not None
has_data = X is not None
if has_result:
    step = 4
elif has_data:
    step = 3
else:
    step = 1
lab_stepper(active=step, has_data=has_data, has_result=has_result)

# ============================================================
# Step 1 — Datos
# ============================================================
section_header(t("lab.step_data"), number="1")
st.markdown(t("lab.data_blurb"))

source_opts = [t("lab.source_catalog"), t("lab.source_csv")]
source = st.radio("src", source_opts, horizontal=True, label_visibility="collapsed")

if source == t("lab.source_catalog"):
    all_ds = list_datasets(available_only=False)
    # filter generators + available paths
    usable = []
    for d in all_ds:
        if d.get("generator") or d.get("path"):
            usable.append(d)
    by_dom: dict[str, list] = {}
    for d in usable:
        by_dom.setdefault(d.get("domain", "synthetic"), []).append(d)

    cdom, cds = st.columns([1, 2])
    with cdom:
        dom_keys = sorted(by_dom.keys())
        # honor session domain
        idx0 = dom_keys.index(domain) if domain in dom_keys else 0
        domain = st.selectbox(
            t("lab.domain"),
            dom_keys,
            index=idx0,
            format_func=lambda k: domain_label(k),
        )
    with cds:
        options = by_dom.get(domain, [])
        labels = [f"{d['id']} — {dataset_title(d)}" for d in options]
        pick = st.selectbox(t("lab.dataset"), range(len(options)), format_func=lambda i: labels[i]) if options else None

    if options and pick is not None:
        ds = options[pick]
        st.caption(
            f"{ds.get('ground_truth') or ds.get('maturity', '')} · "
            f"license: {ds.get('license', '—')}"
        )
        if st.button(t("lab.load_dataset"), type="primary"):
            X, meta = load_dataset(ds["id"])
            st.session_state["lab_X"] = X
            st.session_state["lab_meta"] = meta
            st.session_state["lab_domain"] = meta.get("domain", domain)
            st.session_state["lab_event"] = meta.get("event_index")
            st.session_state["lab_event_label"] = meta.get("event_label") or (
                "switch / event" if meta.get("event_index") is not None else t("common.event")
            )
            st.session_state["lab_has_data"] = True
            st.session_state["lab_source_label"] = meta.get("title", ds["id"])
            st.session_state.pop("lab_result", None)
            st.rerun()

else:
    up = st.file_uploader(t("lab.csv_upload"), type=["csv"])
    domain = st.selectbox(
        t("lab.domain_preset"),
        list(DOMAIN_PRESETS.keys()),
        index=list(DOMAIN_PRESETS.keys()).index(domain) if domain in DOMAIN_PRESETS else 0,
        format_func=lambda k: domain_label(k),
    )
    st.caption(domain_hint(domain))
    if up is not None:
        df = pd.read_csv(up)
        num = df.select_dtypes(include=[np.number])
        st.dataframe(num.head(8), width="stretch")
        adapter = get_adapter(domain)
        suggested = [c for c in adapter.suggested_columns if c in num.columns]
        default_cols = suggested[:3] if suggested else list(num.columns)[: min(3, num.shape[1])]
        cols = st.multiselect(
            t("lab.vars"),
            list(num.columns),
            default=default_cols,
            help=t("lab.vars_help"),
        )
        use_event = st.checkbox(t("lab.mark_event"), value=False)
        ev = None
        if use_event:
            ev = st.number_input(
                t("lab.event_index"),
                min_value=0,
                max_value=max(0, len(num) - 1),
                value=len(num) // 2,
                step=1,
            )
            event_label = st.text_input(t("lab.event_label"), value=t("common.event"))
        if len(cols) >= 1 and st.button(t("lab.use_csv"), type="primary"):
            bundle = adapter.prepare(df, columns=cols, event_index=int(ev) if use_event else None)
            st.session_state["lab_X"] = bundle.X
            st.session_state["lab_domain"] = domain
            st.session_state["lab_event"] = bundle.event_index
            st.session_state["lab_event_label"] = event_label if use_event else t("common.event")
            st.session_state["lab_meta"] = {
                "variables": bundle.variables,
                "source": up.name,
                "title": up.name,
            }
            st.session_state["lab_has_data"] = True
            st.session_state["lab_source_label"] = up.name
            st.session_state.pop("lab_result", None)
            st.rerun()
    else:
        empty_state(t("lab.empty_csv"), "📄")

# refresh from state
X = st.session_state.get("lab_X")
domain = st.session_state.get("lab_domain", domain)
event_index = st.session_state.get("lab_event")
event_label = st.session_state.get("lab_event_label", t("common.event"))
meta = st.session_state.get("lab_meta") or {}
vars_ = meta.get("variables") or []

if X is not None:
    with st.expander(t("lab.preview"), expanded=True):
        st.plotly_chart(
            plot_series(
                X,
                title=st.session_state.get("lab_source_label", "Serie"),
                event_index=event_index,
                event_label=event_label,
                names=vars_ if vars_ else None,
            ),
            width="stretch",
        )
        n_vars = X.shape[1] if X.ndim > 1 else 1
        ev_txt = t("lab.with_event", t=event_index) if event_index is not None else t("lab.no_event")
        st.caption(t("lab.shape_cap", n=X.shape[0], v=n_vars, domain=domain, ev=ev_txt))
        # allow override event after load
        with st.container():
            oe1, oe2 = st.columns(2)
            with oe1:
                new_ev_on = st.checkbox(
                    t("lab.adjust_event"),
                    value=event_index is not None,
                    key="adj_ev",
                )
            with oe2:
                if new_ev_on:
                    event_index = st.number_input(
                        t("lab.t_event"),
                        0,
                        max(0, X.shape[0] - 1),
                        value=int(event_index) if event_index is not None else X.shape[0] // 2,
                        key="ev_num",
                    )
                    st.session_state["lab_event"] = int(event_index)
                else:
                    st.session_state["lab_event"] = None
                    event_index = None

# ============================================================
# Step 2 — Parámetros
# ============================================================
section_header(t("lab.step_params"), number="2")
preset = DOMAIN_PRESETS.get(domain, DOMAIN_PRESETS["synthetic"])
st.markdown(
    t(
        "lab.preset_line",
        label=domain_label(domain),
        window=preset["window"],
        stride=preset["stride"],
        theta3=preset["theta3"],
        m=preset.get("m", 3),
        hint=domain_hint(domain),
    )
)

p1, p2, p3 = st.columns([1, 1, 2])
with p1:
    mode = st.radio(
        t("lab.mode"),
        ["fast", "full"],
        horizontal=True,
        help=t("lab.mode_help"),
    )
with p2:
    surr_method = st.selectbox(
        t("lab.null"),
        ["phase_shuffle", "iaaft"],
        format_func=lambda x: t("lab.phase_shuffle") if x == "phase_shuffle" else t("lab.iaaft"),
        help=t("lab.null_help"),
    )
with p3:
    n_surr_default = 8 if mode == "fast" else 24
    eta_params = {
        "window": preset["window"],
        "stride": preset["stride"],
        "n_surrogates": n_surr_default,
        "surrogate_method": surr_method,
    }
    n_s = int(X.shape[0]) if X is not None else 800
    n_v = int(X.shape[1]) if X is not None and X.ndim > 1 else 2
    eta = estimate_runtime_seconds(n_s, n_v, {**eta_params, "n_surrogates": n_surr_default})
    st.info(t("lab.eta", eta=eta, mode=mode, surr=surr_method))

c1, c2, c3, c4 = st.columns(4)
window = c1.number_input(t("lab.window"), 5, 301, int(preset["window"]), 2)
stride = c2.number_input(t("lab.stride"), 1, 50, int(preset["stride"]))
theta3 = c3.number_input(t("lab.theta3"), 0.01, 0.5, float(preset["theta3"]), 0.01)
seed = c4.number_input(t("lab.seed"), 0, 10_000, 42)

m1, m2, m3, m4 = st.columns(4)
m = m1.select_slider(t("lab.m_bp"), options=[2, 3, 4, 5], value=int(preset.get("m", 3)))
n_surr = m2.slider(t("lab.n_surr"), 0, 50, n_surr_default)
with m3:
    include_breathing = st.checkbox(
        t("lab.breathing"),
        value=(mode == "full"),
        help=t("lab.breathing_help"),
    )
    include_tda = st.checkbox(
        t("lab.tda"),
        value=(mode == "full"),
        help=t("lab.tda_help"),
    )
with m4:
    include_memory = st.checkbox(
        t("lab.memory"),
        value=(mode == "full"),
        help=t("lab.memory_help"),
    )
    tda_note = t("lab.tda_ripser") if has_ripser() else t("lab.tda_vr")
    st.caption(t("lab.tda_backend", note=tda_note))

# ============================================================
# Step 3 — Run
# ============================================================
section_header(t("lab.step_run"), number="3")
if X is None:
    st.warning(t("lab.need_data"))
elif st.button(t("lab.run_btn"), type="primary", width="stretch"):
    params = AnalysisParams(
        window=int(window),
        stride=int(stride),
        m=int(m),
        delay=int(preset.get("delay", 1)),
        d_persist=int(preset.get("d_persist", 4)),
        theta3=float(theta3),
        n_surrogates=int(n_surr),
        mode=mode,
        seed=int(seed),
        include_ews=True,
        include_breathing=bool(include_breathing),
        include_tda=bool(include_tda),
        include_memory=bool(include_memory),
        surrogate_method=surr_method,  # type: ignore[arg-type]
    )
    with st.status(t("lab.status_run"), expanded=True) as status:
        st.write(t("lab.step1"))
        st.write(t("lab.step2b") if include_breathing else t("lab.step2"))
        st.write(t("lab.step3"))
        st.write(t("lab.step4"))
        st.write(t("lab.step5", method=surr_method, n=n_surr))
        st.write(t("lab.step6") if include_tda else t("lab.step6_skip"))
        st.write(t("lab.step7") if include_memory else t("lab.step7_skip"))
        result = run_analysis(
            X,
            params,
            event_index=int(event_index) if event_index is not None else None,
            domain=domain,
            variables=vars_ if vars_ else None,
        )
        st.write(t("lab.step8"))
        status.update(label=t("lab.status_done"), state="complete")

    st.session_state["lab_result"] = result
    st.session_state["lab_domain"] = domain
    st.session_state["lab_flash"] = t("lab.flash_ok", hash=result.repro_hash)
    st.rerun()

# ============================================================
# Step 4 — Results
# ============================================================
result = st.session_state.get("lab_result")
if result is not None:
    flash = st.session_state.pop("lab_flash", None)
    if flash:
        st.success(flash)
    section_header(t("lab.results_header"), number="4")
    interp = result.interpretation or {}
    interpret_box(
        interp.get("title", t("lab.tab_dual")),
        [interp.get("summary", "")] + list(interp.get("bullets") or []) + [interp.get("caution", "")],
    )

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Δτ_s", f"{result.metrics['delta_tau_s']:.4f}")
    k2.metric("mean excess3", f"{result.metrics['mean_excess3']:.4f}")
    k3.metric("Δexcess3", f"{result.metrics['delta_excess3']:.4f}")
    pval = result.surrogate_stats.get("tau_s", {}).get("p_value", None)
    k4.metric("p_surr (τ_s)", f"{pval:.3f}" if pval is not None else "—")

    ext_bits = []
    if result.memory:
        ext_bits.append(
            t(
                "lab.mem_cap",
                mi=result.metrics.get("ordinal_mi_lag1", 0),
                cmi=result.metrics.get("ordinal_cross_mi", 0),
            )
        )
    if result.tda:
        ext_bits.append(
            t(
                "lab.tda_cap",
                backend=result.metrics.get("tda_backend", "—"),
                db0=result.metrics.get("delta_beta0", 0),
                db1=result.metrics.get("delta_beta1", 0),
            )
        )
    if result.breathing_windows is not None:
        w = result.breathing_windows
        ext_bits.append(t("lab.bw_cap", wmin=int(np.min(w)), wmax=int(np.max(w))))
    if ext_bits:
        st.caption(" · ".join(ext_bits))

    t1, t2, t3, t4, t5, t6 = st.tabs(
        [t("lab.tab_dual"), t("lab.tab_tau"), t("lab.tab_recd"), t("lab.tab_ews"), t("lab.tab_ext"), t("lab.tab_export")]
    )
    with t1:
        st.plotly_chart(plot_dual_summary(result), width="stretch")
    with t2:
        st.plotly_chart(
            plot_tau(result, event_index=result.event_index, event_label=event_label),
            width="stretch",
        )
    with t3:
        st.plotly_chart(
            plot_recd_panel(result, event_index=result.event_index, event_label=event_label),
            width="stretch",
        )
    with t4:
        st.plotly_chart(
            plot_ews_comparison(result, event_index=result.event_index, event_label=event_label),
            width="stretch",
        )
    with t5:
        st.markdown(t("lab.ext_blurb"))
        e1, e2 = st.columns(2)
        with e1:
            st.plotly_chart(
                plot_breathing(result, event_index=result.event_index),
                width="stretch",
            )
        with e2:
            st.plotly_chart(
                plot_tda_betti(result, event_index=result.event_index),
                width="stretch",
            )
        if not result.tda and result.breathing_windows is None:
            st.info(t("lab.ext_off"))
    with t6:
        md = render_markdown_report(result, domain=result.domain)
        methods = render_methods_only(result)
        payload = result_to_jsonable(result)

        d1, d2, d3 = st.columns(3)
        d1.download_button(
            t("lab.dl_md"),
            data=md,
            file_name="stp_report.md",
            mime="text/markdown",
            type="primary",
            width="stretch",
        )
        d2.download_button(
            t("lab.dl_methods"),
            data=methods,
            file_name="stp_methods.txt",
            mime="text/plain",
            width="stretch",
        )
        d3.download_button(
            t("lab.dl_json"),
            data=json.dumps(payload, indent=2),
            file_name="stp_result.json",
            mime="application/json",
            width="stretch",
        )
        st.markdown(f"##### {t('lab.repro_header')}")
        st.code(result.repro_hash, language="text")
        st.markdown(f"##### {t('lab.methods_copy')}")
        st.code(methods, language="markdown")
        with st.expander(t("lab.metrics_json")):
            st.json(result.metrics)
else:
    if X is not None:
        empty_state(t("lab.empty_run"), "▶")

footer()
