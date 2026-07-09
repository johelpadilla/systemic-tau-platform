"""Materiales descargables — handouts, FAQ, packs."""

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
from stp.education.handouts import get_handout, list_handouts, render_handout, render_handout_bytes

st.set_page_config(page_title=t("materiales.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("materiales.title"),
    subtitle=t("materiales.subtitle"),
    eyebrow=t("materiales.eyebrow"),
    icon="📦",
)

learning_goals(
    [t("materiales.goal_1"), t("materiales.goal_2"), t("materiales.goal_3")]
)

callout(t("materiales.format_callout"))

# ---- Featured packs ----
section_header(t("materiales.packs_header"))
# also show fundamentos as pack-like
featured_ids = ["pack_estudiante", "pack_docente", "fundamentos_compilado", "guia_rapida", "syllabus"]
cols = st.columns(len(featured_ids))
for col, hid in zip(cols, featured_ids):
    h = get_handout(hid)
    with col:
        st.markdown(f"**{h.title}**")
        st.caption(h.description)
        data = render_handout_bytes(hid)
        st.download_button(
            label=t("materiales.download_md"),
            data=data,
            file_name=h.filename,
            mime="text/markdown",
            key=f"feat_{hid}",
            width="stretch",
            type="primary" if hid.startswith("pack") else "secondary",
        )

# ---- Filter ----
section_header(t("materiales.catalog"))
audiences = sorted({tag for h in list_handouts() for tag in h.tags})
sel = st.multiselect(
    t("materiales.filter_tags"),
    options=audiences,
    default=[],
    help=t("materiales.filter_help"),
)
q = st.text_input(t("materiales.search"), "")

handouts = list_handouts()
if sel:
    handouts = [h for h in handouts if any(tag in h.tags for tag in sel)]
if q.strip():
    ql = q.strip().lower()
    handouts = [
        h
        for h in handouts
        if ql in h.title.lower() or ql in h.description.lower() or ql in h.id
    ]

if not handouts:
    st.info(t("materiales.no_match"))
else:
    for h in handouts:
        with st.container():
            c1, c2 = st.columns([3, 1])
            with c1:
                tags = " · ".join(h.tags) if h.tags else h.audience
                st.markdown(f"#### {h.title}")
                st.caption(f"`{h.filename}` · {tags}")
                st.markdown(h.description)
            with c2:
                try:
                    data = render_handout_bytes(h.id)
                    st.download_button(
                        t("materiales.dl_short"),
                        data=data,
                        file_name=h.filename,
                        mime="text/markdown",
                        key=f"dl_{h.id}",
                        width="stretch",
                    )
                    with st.expander(t("materiales.preview")):
                        preview = render_handout(h.id)
                        st.markdown(preview[:2500] + ("…" if len(preview) > 2500 else ""))
                except Exception as e:
                    st.error(t("materiales.gen_error", err=e))
            st.divider()

# ---- How to convert ----
section_header(t("materiales.howto_header"))
st.markdown(t("materiales.howto_body"))

page_link("pages/7_Docencia.py", label=t("nav.syllabus_docencia"), icon="🎓")
page_link("pages/5_Ruta_Aprendizaje.py", label=t("nav.faq_screen"), icon="🗺️")
page_link("pages/4_Laboratorio.py", label=t("nav.lab"), icon="🔬")
footer()
