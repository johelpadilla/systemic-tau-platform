"""Shared Streamlit UI helpers — design system for Systemic Tau Platform."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st

from stp.i18n.core import LANG_LABELS, SUPPORTED_LANGS, get_lang, set_lang, t


def page_link(
    page: str,
    label: str,
    *,
    icon: str | None = None,
    query_params: dict[str, Any] | None = None,
    **kwargs: Any,
) -> None:
    """Multipage link that never crashes outside a full multipage session.

    Streamlit's ``page_link`` raises ``KeyError: url_pathname`` when a page
    is executed in isolation (AppTest, direct script). Fall back to caption.
    """
    try:
        st.page_link(page, label=label, icon=icon, query_params=query_params, **kwargs)
    except (KeyError, Exception):
        prefix = f"{icon} " if icon else ""
        extra = ""
        if query_params:
            qs = "&".join(f"{k}={v}" for k, v in query_params.items())
            extra = f" · `{page}?{qs}`"
        st.caption(f"{prefix}{label}{extra}")


def inject_css() -> None:
    """Inject design-system CSS once per page render."""
    css_path = Path(__file__).resolve().parents[1] / "assets" / "css" / "custom.css"
    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def language_selector() -> str:
    """Sidebar language control. Spanish is the source language."""
    current = get_lang()
    labels = [f"{LANG_LABELS[c]} ({c})" for c in SUPPORTED_LANGS]
    idx = list(SUPPORTED_LANGS).index(current) if current in SUPPORTED_LANGS else 0
    choice = st.sidebar.selectbox(
        t("lang.label"),
        options=list(range(len(SUPPORTED_LANGS))),
        format_func=lambda i: labels[i],
        index=idx,
        key="stp_lang_select",
        help=t("lang.help"),
    )
    lang = SUPPORTED_LANGS[int(choice)]
    if lang != current:
        set_lang(lang)
        st.rerun()
    set_lang(lang)
    return lang


def sidebar_brand() -> None:
    """Compact brand block at top of sidebar + language selector."""
    st.sidebar.markdown(
        """
        <div class="stp-sidebar-brand">
          <div class="logo">
            <div class="mark">τ</div>
            <div>
              <div class="name">Systemic Tau</div>
              <div class="sub">Educational &amp; Research</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    language_selector()


def render_hero(
    title: str = "Systemic Tau Platform",
    tagline: str = "Paradigma Tau Sistémico: de la teoría a la práctica",
    badge: str = "v1.0 · Educational & Research",
    description: str | None = None,
) -> None:
    inject_css()
    sidebar_brand()
    desc = description or (
        "Plataforma premium para fundamentos, matemática, dominios y laboratorio "
        "interactivo de Tau Sistémica + RECD (Φ₁–Φ₃, excess3)."
    )
    st.markdown(
        f"""
        <div class="stp-hero">
          <div class="stp-badge">{badge}</div>
          <h1>{title}</h1>
          <p class="tagline">{tagline}</p>
          <p class="desc">{desc}</p>
          <div class="stp-hero-meta">
            <span class="stp-badge stp-badge-solid">τ<sub>s</sub> + RECD</span>
            <span class="stp-badge">CCTP / SDDB</span>
            <span class="stp-badge">Surrogates · hash SHA-256</span>
            <span class="stp-badge">5 dominios</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(
    title: str,
    subtitle: str = "",
    eyebrow: str = "",
    icon: str = "",
) -> None:
    """Consistent page title block used across multipage app."""
    inject_css()
    sidebar_brand()
    eye = f"{icon} {eyebrow}".strip() if icon or eyebrow else ""
    eye_html = f'<div class="eyebrow">{eye}</div>' if eye else ""
    sub_html = f'<p class="subtitle">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div class="stp-page-header">
          {eye_html}
          <h1>{title}</h1>
          {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, number: str | int | None = None) -> None:
    num_html = f'<span class="stp-section-num">{number}</span>' if number is not None else ""
    st.markdown(
        f"""
        <div class="stp-section">
          {num_html}
          <h2>{title}</h2>
          <div class="line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def feature_card(title: str, body: str, icon: str = "", accent: str = "teal") -> str:
    icon_html = f'<span class="icon">{icon}</span>' if icon else ""
    return f"""
    <div class="stp-card stp-card-accent {accent}">
      {icon_html}
      <h3>{title}</h3>
      <p class="stp-muted">{body}</p>
    </div>
    """


def nav_card(title: str, body: str, icon: str = "◉") -> str:
    return f"""
    <div class="stp-nav-card">
      <div class="icon">{icon}</div>
      <h3>{title}</h3>
      <p class="stp-muted">{body}</p>
    </div>
    """


def metrics_strip(items: list[tuple[str, str]]) -> None:
    """items: list of (value, label)."""
    cells = "".join(
        f'<div class="stp-metric"><div class="val">{v}</div><div class="lbl">{l}</div></div>'
        for v, l in items
    )
    st.markdown(f'<div class="stp-metrics">{cells}</div>', unsafe_allow_html=True)


def callout(text: str) -> None:
    st.markdown(f'<div class="stp-callout">{text}</div>', unsafe_allow_html=True)


def learning_goals(items: list[str], title: str | None = None) -> None:
    """Pedagogical goals box at the top of a page/section."""
    title = title if title is not None else t("common.learning_goals")
    lis = "".join(f"<li>{item}</li>" for item in items)
    st.markdown(
        f"""
        <div class="stp-learn">
          <div class="title">{title}</div>
          <ul>{lis}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def tip(text: str, label: str | None = None) -> None:
    """Inline note. Prefer scientific labels (Nota, Alcance, Interpretación).

    Avoid teacher-facing metalanguage (\"Para el aula\", \"Honestidad pedagógica\",
    \"Enseñe…\") — write the claim itself, not instructions about how to teach it.
    """
    label = label if label is not None else t("common.note")
    st.markdown(
        f'<div class="stp-tip"><strong>{label}:</strong> {text}</div>',
        unsafe_allow_html=True,
    )


def achieve_card(title: str, body: str, status: str | None = None) -> str:
    status = status if status is not None else t("common.operational")
    low = status.lower()
    cls = "partial" if any(
        k in low
        for k in ("parcial", "partial", "partiel", "roadmap", "desarrollo", "extensión", "extension")
    ) else ""
    return f"""
    <div class="stp-achieve">
      <div class="status {cls}">{status}</div>
      <h4>{title}</h4>
      <p>{body}</p>
    </div>
    """


def interpret_box(title: str, steps: list[str]) -> None:
    lis = "".join(f"<li>{s}</li>" for s in steps)
    st.markdown(
        f"""
        <div class="stp-interpret">
          <h4>{title}</h4>
          <ol>{lis}</ol>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_state(message: str, icon: str = "📂") -> None:
    st.markdown(
        f"""
        <div class="stp-empty">
          <div class="icon">{icon}</div>
          <div>{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer() -> None:
    """Institutional footer strip (shared by all pages)."""
    st.markdown(
        f'<div class="stp-footer">{t("common.footer")}</div>',
        unsafe_allow_html=True,
    )


def lab_stepper(active: int = 1, has_data: bool = False, has_result: bool = False) -> None:
    """Visual progress for Lab: 1 Data · 2 Parameters · 3 Run · 4 Results."""
    labels = [
        t("lab.step_data"),
        t("lab.step_params"),
        t("lab.step_run"),
        t("lab.step_results"),
    ]
    chips = []
    for i, label in enumerate(labels, start=1):
        if i == active:
            cls = "active"
        elif i < active or (i == 1 and has_data) or (i == 4 and has_result):
            cls = "done"
        else:
            cls = ""
        chips.append(
            f'<span class="stp-step-chip {cls}"><span class="n">{i}</span>{label}</span>'
        )
    st.markdown(f'<div class="stp-steps">{"".join(chips)}</div>', unsafe_allow_html=True)
