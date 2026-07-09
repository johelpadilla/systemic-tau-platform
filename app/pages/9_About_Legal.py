"""About, legal, privacy, citations, contact."""

from __future__ import annotations

import sys
from pathlib import Path

_APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_APP))
from components.bootstrap import ensure_stp_path  # noqa: E402

ROOT = ensure_stp_path(__file__)

import streamlit as st

from components.ui import (
    callout,
    footer,
    learning_goals,
    page_header,
    safe_set_page_config,
    section_header,
)
from stp.config.settings import (
    CONTACT_EMAIL,
    GITHUB_URL,
    MAX_CSV_COLS,
    MAX_CSV_MB,
    MAX_CSV_ROWS,
    MAX_SURROGATES_PUBLIC,
    ORCID,
)
from stp.education.content_loader import read_markdown
from stp.i18n.core import t

safe_set_page_config(page_title=t("about.page_title"), page_icon="🌀", layout="wide")

page_header(
    t("about.title"),
    subtitle=t("about.subtitle"),
    eyebrow=t("about.eyebrow"),
    icon="⚖️",
    show_disclaimer=True,
)

learning_goals([t("about.goal_1"), t("about.goal_2"), t("about.goal_3")])

section_header(t("about.disclaimer_h"))
callout(t("about.disclaimer_body"))

section_header(t("about.privacy_h"))
st.markdown(t("about.privacy_body"))
st.caption(
    t(
        "common.limits_note",
        rows=MAX_CSV_ROWS,
        cols=MAX_CSV_COLS,
        surr=MAX_SURROGATES_PUBLIC,
        mb=int(MAX_CSV_MB),
    )
)

section_header(t("about.software"))
st.markdown(t("about.software_body"))
st.markdown(f"- GitHub: {GITHUB_URL}")
st.markdown(f"- Email: `{CONTACT_EMAIL}`")
st.markdown(f"- ORCID: [{ORCID}](https://orcid.org/{ORCID})")

section_header(t("about.data_h"))
st.markdown(t("about.data_body"))
legal_md = read_markdown("legal", "licenses.md")
if legal_md:
    with st.expander(t("common.about_legal"), expanded=False):
        st.markdown(legal_md)

section_header(t("about.cite_h"))
st.markdown(t("about.cite_body"))

section_header(t("about.contact_h"))
st.markdown(t("about.contact_body"))

section_header(t("about.limits_h"))
st.markdown(t("about.limits_body"))

section_header(t("about.review_h"))
st.markdown(t("about.review_body"))

footer()
