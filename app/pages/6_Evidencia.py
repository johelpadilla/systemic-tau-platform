from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t
import yaml

from components.illustrations import show_illustration
from components.ui import page_link, callout, footer, learning_goals, page_header, section_header
from stp.config.settings import AnalysisParams
from stp.core.pipeline import run_analysis
from stp.data.catalog import load_dataset
from stp.i18n.content import localized_content_path
from stp.visualization.series_plots import plot_dual_summary, plot_ews_comparison

st.set_page_config(page_title=t("evidencia.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("evidencia.title_full"),
    subtitle=t("evidencia.subtitle_full"),
    eyebrow=t("evidencia.eyebrow_full"),
    icon="📑",
)

learning_goals(
    [t("evidencia.goal_1_full"), t("evidencia.goal_2_full"), t("evidencia.goal_3_full")]
)

path = localized_content_path("evidencia", "publications.yaml")
data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}

section_header(t("evidencia.anchor_header"))
show_illustration("cctp")
callout(t("evidencia.anchor_callout"))
show_illustration("surrogates")

c1, c2, c3 = st.columns(3)
c1.metric(t("common.cohort"), "N=10")
c2.metric(t("common.sign_concordance"), "8/10")
c3.metric(t("common.main_null"), "phase-shuffle")

section_header(t("evidencia.fig_header"))
callout(t("evidencia.fig_callout"))
if st.button(t("evidencia.regen_btn"), type="primary"):
    with st.spinner(t("evidencia.running")):
        X, meta = load_dataset("sddb_rr_38_demo")
        # subsample for UI speed if very long
        if X.shape[0] > 4000:
            X = X[-4000:]
            if meta.get("event_index") is not None:
                meta["event_index"] = max(0, int(meta["event_index"]) - (meta.get("n", 0) or 0))
                # event near end for demo exports
                meta["event_index"] = int(0.85 * len(X))
        params = AnalysisParams(
            window=101,
            stride=5,
            m=3,
            theta3=0.08,
            n_surrogates=4,
            mode="fast",
            seed=42,
            include_ews=True,
        )
        res = run_analysis(
            X,
            params,
            event_index=meta.get("event_index") or int(0.85 * len(X)),
            domain="cardiology",
            variables=meta.get("variables"),
        )
        st.session_state["evid_result"] = res

res = st.session_state.get("evid_result")
if res is not None:
    m1, m2, m3 = st.columns(3)
    m1.metric("Δτ_s", f"{res.metrics['delta_tau_s']:.4f}")
    m2.metric("Δexcess3", f"{res.metrics['delta_excess3']:.4f}")
    pval = res.surrogate_stats.get("tau_s", {}).get("p_value")
    m3.metric("p_surr", f"{pval:.3f}" if pval is not None else "—")
    st.plotly_chart(plot_dual_summary(res), width="stretch")
    st.plotly_chart(plot_ews_comparison(res), width="stretch")
    st.caption(t("evidencia.hash_cap", hash=res.repro_hash))
    page_link(
        "pages/4_Laboratorio.py",
        label=t("evidencia.open_same"),
        icon="🔬",
        query_params={"dataset": "sddb_rr_38_demo", "domain": "cardiology"},
    )
else:
    st.caption(t("evidencia.press_regen"))

section_header(t("evidencia.pubs_header"))
pubs = data.get("publications", [])
if not pubs:
    st.info(t("evidencia.no_pubs"))
else:
    for pub in pubs:
        highlights = pub.get("highlights") or []
        hl_html = ""
        if highlights:
            items = "".join(f"<li>{h}</li>" for h in highlights)
            hl_html = f"<ul>{items}</ul>"
        doi = pub.get("doi")
        doi_html = f'<span class="stp-pill purple">DOI {doi}</span>' if doi else ""
        st.markdown(
            f"""
            <div class="stp-pub">
              <h3>{pub.get('title', t('common.untitled'))}</h3>
              <div class="meta">
                {pub.get('authors', '')} · {pub.get('year', '')} ·
                <span class="stp-pill">{pub.get('type', '')}</span>
                <span class="stp-pill high">{pub.get('domain', '')}</span>
                {doi_html}
              </div>
              {hl_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

section_header(t("evidencia.cmp_header"))
st.markdown(t("evidencia.cmp_body"))
rows = data.get("comparison_matrix", [])
if rows:
    # bool/str mix breaks Arrow serialization; normalize for display
    safe_rows = [
        {
            k: ("✓" if v is True else "—" if v is False else str(v))
            for k, v in r.items()
        }
        for r in rows
    ]
    st.dataframe(safe_rows, width="stretch", hide_index=True)
else:
    st.caption(t("evidencia.no_matrix"))

section_header(t("evidencia.scope_header"))
st.markdown(t("evidencia.scope_table"))

footer()
