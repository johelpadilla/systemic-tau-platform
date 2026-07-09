from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st
from stp.i18n.core import t

from components.ui import page_link, callout, footer, learning_goals, page_header, section_header
from stp.education.content_loader import read_markdown
from stp.education.glossary import search_glossary

st.set_page_config(page_title=t("ruta.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("ruta.title"),
    subtitle=t("ruta.subtitle_full"),
    eyebrow=t("ruta.eyebrow_full"),
    icon="🗺️",
)

learning_goals(
    [t("ruta.goal_1_full"), t("ruta.goal_2_full"), t("ruta.goal_3_full")]
)

tabs = st.tabs(
    [t("ruta.tab_path"), t("ruta.tab_scope"), t("ruta.tab_glossary"), t("ruta.tab_faq")]
)

with tabs[0]:
    section_header(t("ruta.path_header"))
    callout(t("ruta.path_callout"))

    st.markdown(
        f"""
        <div class="stp-path">
          <div class="stp-path-step">
            <div class="stp-path-rail"><div class="stp-path-num">1</div></div>
            <div class="stp-path-body">
              <div class="level-tag">{t("ruta.lvl1_tag")}</div>
              <h3>{t("ruta.lvl1_title")}</h3>
              <p class="stp-muted">{t("ruta.lvl1_body")}</p>
            </div>
          </div>
          <div class="stp-path-step">
            <div class="stp-path-rail"><div class="stp-path-num">2</div></div>
            <div class="stp-path-body">
              <div class="level-tag">{t("ruta.lvl2_tag")}</div>
              <h3>{t("ruta.lvl2_title")}</h3>
              <p class="stp-muted">{t("ruta.lvl2_body")}</p>
            </div>
          </div>
          <div class="stp-path-step">
            <div class="stp-path-rail"><div class="stp-path-num">3</div></div>
            <div class="stp-path-body">
              <div class="level-tag">{t("ruta.lvl3_tag")}</div>
              <h3>{t("ruta.lvl3_title")}</h3>
              <p class="stp-muted">{t("ruta.lvl3_body")}</p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    levels = [
        {
            "key": t("ruta.level_basic"),
            "sk": "basic",
            "items": [t(f"ruta.b{i}") for i in range(1, 6)],
        },
        {
            "key": t("ruta.level_inter"),
            "sk": "inter",
            "items": [t(f"ruta.i{i}") for i in range(1, 7)],
        },
        {
            "key": t("ruta.level_adv"),
            "sk": "adv",
            "items": [t(f"ruta.a{i}") for i in range(1, 6)],
        },
    ]

    for lvl in levels:
        done = sum(
            1
            for i, _ in enumerate(lvl["items"])
            if st.session_state.get(f"lp_{lvl['sk']}_{i}", False)
        )
        total = len(lvl["items"])
        with st.expander(
            t("ruta.checklist", level=lvl["key"], done=done, total=total),
            expanded=(lvl["sk"] == "basic"),
        ):
            for i, item in enumerate(lvl["items"]):
                st.checkbox(item, key=f"lp_{lvl['sk']}_{i}")

    section_header(t("ruta.exp_header"))
    st.markdown(t("ruta.exp_blurb"))
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown(t("ruta.exp_basic"))
        page_link(
            "pages/4_Laboratorio.py",
            label=t("ruta.lab_logistic"),
            icon="🔬",
            query_params={"dataset": "synthetic_coupled_logistic", "domain": "synthetic"},
        )
    with e2:
        st.markdown(t("ruta.exp_inter"))
        page_link(
            "pages/4_Laboratorio.py",
            label=t("ruta.lab_sddb"),
            icon="🫀",
            query_params={"dataset": "sddb_rr_38_demo", "domain": "cardiology"},
        )
    with e3:
        st.markdown(t("ruta.exp_xfer"))
        page_link(
            "pages/4_Laboratorio.py",
            label=t("ruta.lab_dengue"),
            icon="🦠",
            query_params={"dataset": "dengue_like_demo", "domain": "epidemiology"},
        )

with tabs[1]:
    section_header(t("ruta.scope_header"))
    st.markdown(read_markdown("learning", "v1_logros.md"))

with tabs[2]:
    section_header(t("ruta.gloss_header"))
    st.markdown(t("ruta.gloss_blurb"))
    q = st.text_input(t("ruta.search"), "", placeholder=t("ruta.search_ph"))
    terms = search_glossary(q)
    if not terms:
        st.info(t("ruta.no_term"))
    else:
        for term in terms:
            level = term.get("level", "—")
            with st.expander(f"{term.get('term', '?')}"):
                st.markdown(
                    f'<span class="stp-term-level">{level}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(f"**{term.get('short', '')}**")
                st.markdown(term.get("long", ""))

with tabs[3]:
    section_header(t("ruta.faq_header"))
    st.markdown(read_markdown("learning", "faq.md"))
    try:
        from stp.education.handouts import render_handout_bytes

        st.download_button(
            t("ruta.dl_faq"),
            data=render_handout_bytes("faq"),
            file_name="stp_faq.md",
            mime="text/markdown",
        )
        st.download_button(
            t("ruta.dl_gloss"),
            data=render_handout_bytes("glosario"),
            file_name="stp_glosario.md",
            mime="text/markdown",
        )
    except Exception:
        pass
    page_link("pages/8_Materiales.py", label=t("nav.more_materials"), icon="📦")

page_link("pages/1_Fundamentos.py", label=t("nav.start_fundamentos"), icon="📘")
page_link("pages/4_Laboratorio.py", label=t("nav.practice_lab"), icon="🔬")
page_link("pages/8_Materiales.py", label=t("nav.materials"), icon="📦")
footer()
