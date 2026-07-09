from __future__ import annotations

from pathlib import Path

import streamlit as st
import components.theme as theme
from locales import t


def inject_css() -> None:
    """Inject design-system CSS once per page render."""
    theme.inject_theme_css()
    css_path = Path(__file__).resolve().parents[1] / "assets" / "css" / "custom.css"
    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )


def sidebar_brand() -> None:
    """Compact brand block at top of sidebar."""
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
    
    # Language Selector
    lang_options = {"es": "🇪🇸 Español", "en": "🇬🇧 English", "fr": "🇫🇷 Français"}
    current_lang = st.session_state.get("lang", "es")
    
    selected_lang_name = st.sidebar.selectbox(
        t("sidebar_lang"),
        options=list(lang_options.values()),
        index=list(lang_options.keys()).index(current_lang),
        key="lang_selector"
    )
    
    # Map back to code
    for code, name in lang_options.items():
        if name == selected_lang_name:
            if code != current_lang:
                st.session_state["lang"] = code
                st.rerun()
            break
            
    is_dark = theme.get_current_theme_base() == "dark"
    new_theme = st.sidebar.toggle(t("sidebar_dark_mode"), value=is_dark)
    if new_theme != is_dark:
        theme.toggle_theme(new_theme)


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
    st.markdown(
        f"""
        <div class="stp-footer">
          <div>{t("footer_text")}</div>
          <div class="stp-footer-disclaimer">{t("footer_disclaimer")}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def lab_stepper(active: int = 1, has_data: bool = False, has_result: bool = False) -> None:
    """Visual progress for Lab: 1 Datos · 2 Parámetros · 3 Ejecutar · 4 Resultados."""
    labels = ["Datos", "Parámetros", "Ejecutar", "Resultados"]
    chips = []
    for i, label in enumerate(labels, start=1):
        if i < active or (i == 1 and has_data) or (i == 4 and has_result):
            if i < active or (i == 1 and has_data and active > 1) or (i == 4 and has_result and active > 4):
                cls = "done"
            elif i == active:
                cls = "active"
            else:
                cls = "done" if (i == 1 and has_data) or (i == 4 and has_result) else ""
        else:
            cls = "active" if i == active else ""
        if i == 1 and has_data and active != 1:
            cls = "done"
        if i == 4 and has_result:
            cls = "done" if active != 4 else "active"
        if i == active:
            cls = "active"
        chips.append(
            f'<span class="stp-step-chip {cls}"><span class="n">{i}</span>{label}</span>'
        )
    st.markdown(f'<div class="stp-steps">{"".join(chips)}</div>', unsafe_allow_html=True)
