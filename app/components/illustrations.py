"""Theoretical illustrations (inline SVG) for Systemic Tau Platform.

Design rules for legibility:
- No HTML inside SVG text (use Unicode subscripts: τₛ, Φ₁…).
- Clear vertical zones: header → body → footer annotation.
- Minimum 16px between text baselines; panels leave 20px padding.
- Unique gradient/filter ids per figure (prefixed).

Contrast (critical — never dark-on-dark / light-on-light):
- Light surfaces (cream, white cards): ink = INK / INK_SOFT / MUTED.
- Dark fills (navy #0D4F6B, deep #1A2332, gradient hero): text = ON_DARK
  (pure white) or ON_DARK_SOFT (high-luminance teal). Never #1A2332 / #5B6775.
- Labels on dark backgrounds sit on solid white chips when secondary text
  would otherwise sit on translucent dark.

Rendering (critical):
- Title and caption live in Streamlit DOM (never inside iframe).
- SVG is embedded as a responsive <img data:image/svg+xml;base64,...>
  so its height is natural (aspect-ratio) and cannot cover the caption.
"""

from __future__ import annotations

import base64
import html as html_lib
from typing import TypedDict

import streamlit as st

from stp.i18n.core import t

# Lazy import to avoid circular deps if ui ever imports illustrations
def _ensure_css() -> None:
    try:
        from components.ui import inject_css

        inject_css()
    except Exception:
        pass


class IllusPayload(TypedDict):
    title: str
    caption: str
    svg: str


def _frame(svg: str, title: str, caption: str) -> IllusPayload:
    """Pack illustration payload (SVG body only — no chrome)."""
    cleaned = "\n".join(line.rstrip() for line in svg.strip().splitlines())
    return {"title": title, "caption": caption, "svg": cleaned}


def show_illustration(name: str, *, caption: str | None = None) -> None:
    """Render a named illustration. Unknown names are silent no-ops.

    Title + caption are Streamlit DOM siblings *below* the graphic (never in an
    iframe). The SVG is a responsive base64 <img>, so its height is natural
    and cannot cover the caption.
    """
    fn = ILLUSTRATIONS.get(name)
    if fn is None:
        return
    _ensure_css()
    payload = fn(caption)
    title = payload["title"]
    cap = caption if caption is not None else payload["caption"]
    svg = payload["svg"]

    # Standalone image needs xmlns
    if "xmlns=" not in svg[:160]:
        svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)

    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    title_esc = html_lib.escape(title)
    cap_esc = html_lib.escape(cap)
    alt_esc = html_lib.escape(title)

    st.markdown(
        f"""
        <div class="stp-illus">
          <div class="stp-illus-title">{title_esc}</div>
          <div class="stp-illus-canvas">
            <img src="data:image/svg+xml;base64,{b64}"
                 alt="{alt_esc}"
                 loading="lazy"
                 decoding="async" />
          </div>
          <div class="stp-illus-cap">{cap_esc}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_illustration_pair(left: str, right: str) -> None:
    c1, c2 = st.columns(2)
    with c1:
        show_illustration(left)
    with c2:
        show_illustration(right)


# Shared palette + typeface (explicit hex — never inherit CSS color)
_FONT = "Inter, 'Segoe UI', system-ui, sans-serif"
_INK = "#1A2332"          # primary text on light
_INK_SOFT = "#5B6775"     # secondary on light
_MUTED = "#8B95A1"        # labels / eyebrows on light
_ON_DARK = "#FFFFFF"      # primary text on navy / deep
_ON_DARK_SOFT = "#D4EEF0" # secondary text on navy (high luminance)
_NAVY = "#0D4F6B"
_TEAL = "#1A8A8A"
_PURPLE = "#5B4B8A"
_CHIP = "#FFFFFF"         # solid light chip on dark grounds


# ===========================================================================
# 1. Tau relational
# ===========================================================================


def _svg_tau_relational(caption: str | None = None) -> str:
    cap = caption or t("illus.tau_cap")
    svg = f"""
<svg viewBox="0 0 920 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tau relacional">
  <defs>
    <linearGradient id="tr-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F4ED"/><stop offset="100%" stop-color="#EEF4F7"/>
    </linearGradient>
    <linearGradient id="tr-wa" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0D4F6B" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#0D4F6B" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="tr-wb" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#5B4B8A" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="#5B4B8A" stop-opacity="0.02"/>
    </linearGradient>
  </defs>
  <rect width="920" height="360" rx="16" fill="url(#tr-bg)"/>

  <!-- LEFT PANEL -->
  <rect x="24" y="24" width="428" height="312" rx="14" fill="#fff" stroke="#E4E9EF"/>
  <text x="44" y="52" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">{t("illus.svg_classic_panel")}</text>
  <text x="44" y="76" font-family="{_FONT}" font-size="15" font-weight="700" fill="#1A2332">
    {t("illus.svg_more_amp")}
  </text>

  <!-- graph zone (top-right of panel, clear of title) -->
  <g transform="translate(300,100)">
    <circle cx="0" cy="0" r="10" fill="#0D4F6B"/>
    <circle cx="48" cy="-18" r="10" fill="#1A8A8A"/>
    <circle cx="36" cy="28" r="10" fill="#5B4B8A"/>
    <line x1="0" y1="0" x2="48" y2="-18" stroke="#0D4F6B" stroke-width="1.8" opacity="0.55"/>
    <line x1="48" y1="-18" x2="36" y2="28" stroke="#1A8A8A" stroke-width="1.8" opacity="0.55"/>
    <line x1="36" y1="28" x2="0" y2="0" stroke="#5B4B8A" stroke-width="1.8" opacity="0.55"/>
  </g>
  <text x="280" y="158" font-family="{_FONT}" font-size="11" fill="#8B95A1">grafo estable</text>

  <!-- wave in lower half only -->
  <path d="M48 220 C 90 200, 120 175, 160 185 S 230 250, 270 230 S 340 165, 380 180 S 420 230, 430 210"
        fill="none" stroke="#0D4F6B" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M48 220 C 90 200, 120 175, 160 185 S 230 250, 270 230 S 340 165, 380 180 S 420 230, 430 210
           L 430 280 L 48 280 Z" fill="url(#tr-wa)"/>
  <text x="44" y="312" font-family="{_FONT}" font-size="12" fill="#5B6775">
    var ↑ · AR1 ? · relaciones ≈
  </text>

  <!-- RIGHT PANEL -->
  <rect x="468" y="24" width="428" height="312" rx="14" fill="#fff" stroke="#E4E9EF"/>
  <text x="488" y="52" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">PANEL RELACIONAL</text>
  <text x="488" y="76" font-family="{_FONT}" font-size="15" font-weight="700" fill="#1A2332">
    {t("illus.svg_same_amp")}
  </text>

  <g transform="translate(740,100)">
    <circle cx="0" cy="0" r="10" fill="#0D4F6B"/>
    <circle cx="52" cy="-14" r="10" fill="#1A8A8A"/>
    <circle cx="28" cy="32" r="10" fill="#5B4B8A"/>
    <circle cx="68" cy="22" r="8" fill="#C45C26"/>
    <line x1="0" y1="0" x2="28" y2="32" stroke="#0D4F6B" stroke-width="2.2" opacity="0.8"/>
    <line x1="28" y1="32" x2="68" y2="22" stroke="#C45C26" stroke-width="2.4" opacity="0.9"/>
    <line x1="52" y1="-14" x2="68" y2="22" stroke="#1A8A8A" stroke-width="1.4" opacity="0.4" stroke-dasharray="3 3"/>
    <line x1="0" y1="0" x2="52" y2="-14" stroke="#5B4B8A" stroke-width="1.2" opacity="0.3" stroke-dasharray="2 3"/>
  </g>
  <text x="720" y="158" font-family="{_FONT}" font-size="11" fill="#8B95A1">{t("illus.svg_reordered")}</text>

  <path d="M492 220 C 540 210, 580 195, 620 205 S 690 245, 730 225 S 800 175, 850 195 S 880 220, 880 215"
        fill="none" stroke="#5B4B8A" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M492 220 C 540 210, 580 195, 620 205 S 690 245, 730 225 S 800 175, 850 195 S 880 220, 880 215
           L 880 280 L 492 280 Z" fill="url(#tr-wb)"/>
  <text x="488" y="312" font-family="{_FONT}" font-size="12" fill="#5B6775">
    {t("illus.svg_tau_reads")}
  </text>
</svg>"""
    return _frame(svg, t("illus.tau_title"), cap)


# ===========================================================================
# 2. Dual reading
# ===========================================================================


def _svg_dual_reading(caption: str | None = None) -> str:
    cap = caption or t("illus.dual_cap")
    svg = f"""
<svg viewBox="0 0 920 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Lectura dual">
  <defs>
    <linearGradient id="dr-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F4F1EA"/><stop offset="100%" stop-color="#EAF3F5"/>
    </linearGradient>
    <linearGradient id="dr-n" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0D4F6B"/><stop offset="100%" stop-color="#1A8A8A"/>
    </linearGradient>
  </defs>
  <rect width="920" height="320" rx="16" fill="url(#dr-bg)"/>

  <!-- LEFT -->
  <rect x="28" y="28" width="380" height="264" rx="14" fill="#fff" stroke="#E4E9EF"/>
  <text x="48" y="56" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1">INSTRUMENTO A</text>
  <text x="48" y="82" font-family="{_FONT}" font-size="15" font-weight="700" fill="#1A2332">
    {t("illus.svg_ews_univ")}
  </text>

  <text x="48" y="120" font-family="ui-monospace,monospace" font-size="13" font-weight="700" fill="#0D4F6B">var</text>
  <rect x="48" y="130" width="160" height="12" rx="6" fill="#EEF2F5"/>
  <rect x="48" y="130" width="120" height="12" rx="6" fill="#0D4F6B"/>
  <text x="220" y="141" font-family="{_FONT}" font-size="12" fill="#5B6775">↑ a menudo</text>

  <text x="48" y="180" font-family="ui-monospace,monospace" font-size="13" font-weight="700" fill="#0D4F6B">AR1</text>
  <rect x="48" y="190" width="160" height="12" rx="6" fill="#EEF2F5"/>
  <rect x="48" y="190" width="64" height="12" rx="6" fill="#C45C26"/>
  <text x="220" y="201" font-family="{_FONT}" font-size="12" fill="#5B6775">↓ a menudo (pre-FV)</text>

  <text x="48" y="250" font-family="{_FONT}" font-size="12" fill="#5B6775">
    {t("illus.svg_ambiguous")}
  </text>

  <!-- CENTER badge (between panels, not overlapping) -->
  <circle cx="460" cy="160" r="32" fill="url(#dr-n)"/>
  <text x="460" y="155" text-anchor="middle" font-family="{_FONT}" font-size="10"
        font-weight="700" fill="{_ON_DARK}">LECTURA</text>
  <text x="460" y="172" text-anchor="middle" font-family="{_FONT}" font-size="10"
        font-weight="700" fill="{_ON_DARK_SOFT}">DUAL</text>

  <!-- RIGHT -->
  <rect x="512" y="28" width="380" height="264" rx="14" fill="#fff" stroke="#E4E9EF"/>
  <text x="532" y="56" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1">INSTRUMENTO B</text>
  <text x="532" y="82" font-family="{_FONT}" font-size="15" font-weight="700" fill="#1A2332">
    τₛ + RECD (relacional)
  </text>

  <!-- rings left, labels right — no collision -->
  <g transform="translate(580,175)">
    <circle r="48" fill="none" stroke="#E6F5F5" stroke-width="9"/>
    <circle r="48" fill="none" stroke="#1A8A8A" stroke-width="9"
            stroke-dasharray="180 300" stroke-linecap="round" transform="rotate(-90)"/>
    <circle r="30" fill="none" stroke="#EEF0F8" stroke-width="7"/>
    <circle r="30" fill="none" stroke="#5B4B8A" stroke-width="7"
            stroke-dasharray="110 190" stroke-linecap="round" transform="rotate(-35)"/>
    <circle r="14" fill="#0D4F6B"/>
    <text text-anchor="middle" y="5" font-family="{_FONT}" font-size="12" font-weight="700" fill="{_ON_DARK}">τ</text>
  </g>
  <text x="660" y="150" font-family="ui-monospace,monospace" font-size="13" font-weight="700" fill="#0D4F6B">Δτₛ</text>
  <text x="660" y="170" font-family="{_FONT}" font-size="12" fill="#5B6775">reorganización</text>
  <text x="660" y="200" font-family="ui-monospace,monospace" font-size="13" font-weight="700" fill="#5B4B8A">excess3</text>
  <text x="660" y="220" font-family="{_FONT}" font-size="12" fill="#5B6775">{t("illus.svg_clock")}</text>

  <text x="532" y="268" font-family="{_FONT}" font-size="12" fill="#5B6775">
    {t("illus.svg_diff_q")}
  </text>
</svg>"""
    return _frame(svg, t("illus.dual_title"), cap)


# ===========================================================================
# 3. RECD nested
# ===========================================================================


def _svg_recd_nested(caption: str | None = None) -> str:
    cap = caption or t("illus.recd_cap")
    svg = f"""
<svg viewBox="0 0 920 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="RECD anidado">
  <defs>
    <radialGradient id="rn-bg" cx="40%" cy="55%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF"/><stop offset="100%" stop-color="#F0F4F7"/>
    </radialGradient>
    <linearGradient id="rn1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0D4F6B"/><stop offset="100%" stop-color="#1A6F8A"/>
    </linearGradient>
    <linearGradient id="rn2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1A8A8A"/><stop offset="100%" stop-color="#3AA8A0"/>
    </linearGradient>
    <linearGradient id="rn3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5B4B8A"/><stop offset="100%" stop-color="#7B6BB0"/>
    </linearGradient>
  </defs>
  <rect width="920" height="380" rx="16" fill="url(#rn-bg)"/>

  <text x="36" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">RELOJ INTERNO DEL SISTEMA</text>
  <text x="36" y="66" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    RECD ordinal anidado · Φ₁ ⊂ Φ₂ ⊂ Φ₃
  </text>

  <!-- rings: center left, below header, clear of cards -->
  <g transform="translate(230,230)">
    <circle r="118" fill="#F4F0FA" stroke="#5B4B8A" stroke-width="1.4"/>
    <circle r="118" fill="none" stroke="url(#rn3)" stroke-width="12"
            stroke-dasharray="250 740" stroke-linecap="round" transform="rotate(-100)"/>
    <circle r="82" fill="#E8F6F5" stroke="#1A8A8A" stroke-width="1.1"/>
    <circle r="82" fill="none" stroke="url(#rn2)" stroke-width="10"
            stroke-dasharray="180 520" stroke-linecap="round" transform="rotate(-30)"/>
    <circle r="48" fill="#E6F0F5" stroke="#0D4F6B" stroke-width="1"/>
    <circle r="48" fill="none" stroke="url(#rn1)" stroke-width="9"
            stroke-dasharray="110 300" stroke-linecap="round" transform="rotate(20)"/>
    <circle r="20" fill="url(#rn1)"/>
    <text text-anchor="middle" y="5" font-family="{_FONT}" font-size="12" font-weight="700" fill="{_ON_DARK}">core</text>
  </g>
  <!-- ring legend under rings -->
  <text x="230" y="365" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#8B95A1">
    exterior Φ₃ · medio Φ₂ · interior Φ₁
  </text>

  <!-- cards fully to the right of rings (rings extend ~ x 112–348) -->
  <g>
    <rect x="420" y="100" width="460" height="70" rx="12" fill="#fff" stroke="#E4E9EF"/>
    <circle cx="448" cy="135" r="11" fill="url(#rn1)"/>
    <text x="474" y="128" font-family="{_FONT}" font-size="14" font-weight="700" fill="#1A2332">
      {t("illus.svg_phi1")}
    </text>
    <text x="474" y="150" font-family="{_FONT}" font-size="12" fill="#5B6775">
      {t("illus.svg_phi1_q")}
    </text>
  </g>
  <g>
    <rect x="420" y="186" width="460" height="70" rx="12" fill="#fff" stroke="#E4E9EF"/>
    <circle cx="448" cy="221" r="11" fill="url(#rn2)"/>
    <text x="474" y="214" font-family="{_FONT}" font-size="14" font-weight="700" fill="#1A2332">
      {t("illus.svg_phi2")}
    </text>
    <text x="474" y="236" font-family="{_FONT}" font-size="12" fill="#5B6775">
      {t("illus.svg_phi2_b")}
    </text>
  </g>
  <g>
    <rect x="420" y="272" width="460" height="70" rx="12" fill="#fff" stroke="#E4E9EF"/>
    <circle cx="448" cy="307" r="11" fill="url(#rn3)"/>
    <text x="474" y="300" font-family="{_FONT}" font-size="14" font-weight="700" fill="#1A2332">
      {t("illus.svg_phi3")}
    </text>
    <text x="474" y="322" font-family="{_FONT}" font-size="12" fill="#5B6775">
      excess3 continuo: preferido bajo ruido real
    </text>
  </g>
</svg>"""
    return _frame(svg, t("illus.recd_title"), cap)


# ===========================================================================
# 4. Bandt–Pompe
# ===========================================================================


def _svg_bandt_pompe(caption: str | None = None) -> str:
    cap = caption or t("illus.bp_cap")
    patterns = [
        (0, 1, 2, "012"),
        (0, 2, 1, "021"),
        (1, 0, 2, "102"),
        (1, 2, 0, "120"),
        (2, 0, 1, "201"),
        (2, 1, 0, "210"),
    ]
    # 6 cards, equal gap: margin 32, gap 12, card_w = (920-64-5*12)/6 = 132.67 → 132
    card_w = 132
    gap = 12
    margin = 32
    cards = []
    colors = ["#0D4F6B", "#1A8A8A", "#5B4B8A"]
    for i, (a, b, c, lab) in enumerate(patterns):
        x = margin + i * (card_w + gap)
        bars = ""
        for j, rank in enumerate((a, b, c)):
            h = 36 + rank * 18
            bx = x + 28 + j * 28
            by = 210 - h
            bars += f'<rect x="{bx}" y="{by}" width="20" height="{h}" rx="4" fill="{colors[j]}"/>'
        cx = x + card_w / 2
        cards.append(
            f"""
            <rect x="{x}" y="96" width="{card_w}" height="176" rx="12" fill="#fff" stroke="#E4E9EF"/>
            <text x="{cx}" y="122" text-anchor="middle" font-family="{_FONT}"
                  font-size="12" font-weight="700" fill="#8B95A1">π{i}</text>
            {bars}
            <text x="{cx}" y="248" text-anchor="middle" font-family="ui-monospace,monospace"
                  font-size="14" font-weight="600" fill="#1A2332">{lab}</text>
            """
        )
    svg = f"""
<svg viewBox="0 0 920 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bandt-Pompe">
  <defs>
    <linearGradient id="bp-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F8FA"/><stop offset="100%" stop-color="#EEF6F6"/>
    </linearGradient>
  </defs>
  <rect width="920" height="320" rx="16" fill="url(#bp-bg)"/>
  <text x="32" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">ALFABETO ORDINAL</text>
  <text x="32" y="68" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    {t("illus.svg_bp_m3")}
  </text>
  {''.join(cards)}
  <text x="32" y="300" font-family="{_FONT}" font-size="12" fill="#5B6775">
    {t("illus.svg_bp_cards")}
  </text>
</svg>"""
    return _frame(svg, t("illus.bp_title"), cap)


# ===========================================================================
# 5. Surrogates
# ===========================================================================


def _svg_surrogates(caption: str | None = None) -> str:
    cap = caption or t("illus.surr_cap")
    svg = f"""
<svg viewBox="0 0 920 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Surrogates">
  <defs>
    <linearGradient id="su-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F4F1EA"/><stop offset="100%" stop-color="#F0F3F8"/>
    </linearGradient>
    <marker id="su-ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#5B6775"/>
    </marker>
  </defs>
  <rect width="920" height="320" rx="16" fill="url(#su-bg)"/>
  <text x="32" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">FALSABILIDAD</text>
  <text x="32" y="66" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    Phase-shuffle · nulo para dependencia cruzada
  </text>

  <!-- card 1 -->
  <rect x="32" y="96" width="260" height="180" rx="12" fill="#fff" stroke="#E4E9EF"/>
  <text x="48" y="124" font-family="{_FONT}" font-size="13" font-weight="700" fill="#0D4F6B">
    Datos observados
  </text>
  <path d="M52 160 C 90 140, 120 185, 150 160 S 210 135, 240 165 S 270 190, 275 170"
        fill="none" stroke="#0D4F6B" stroke-width="2"/>
  <path d="M52 200 C 90 215, 120 175, 150 205 S 210 220, 240 185 S 270 165, 275 195"
        fill="none" stroke="#1A8A8A" stroke-width="2"/>
  <path d="M100 155 Q 145 140 190 170" fill="none" stroke="#5B4B8A" stroke-width="1.4" stroke-dasharray="3 2"/>
  <text x="48" y="250" font-family="{_FONT}" font-size="12" fill="#5B6775">canales acoplados</text>

  <!-- arrow zone -->
  <line x1="310" y1="186" x2="380" y2="186" stroke="#5B6775" stroke-width="1.8" marker-end="url(#su-ar)"/>
  <text x="345" y="172" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#5B6775">shuffle</text>
  <text x="345" y="208" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#5B6775">fases</text>

  <!-- card 2 -->
  <rect x="400" y="96" width="260" height="180" rx="12" fill="#fff" stroke="#E4E9EF"/>
  <text x="416" y="124" font-family="{_FONT}" font-size="13" font-weight="700" fill="#5B4B8A">
    Surrogates
  </text>
  <path d="M420 160 C 455 185, 485 140, 520 165 S 575 195, 610 150 S 640 140, 645 175"
        fill="none" stroke="#0D4F6B" stroke-width="2" opacity="0.75"/>
  <path d="M420 205 C 455 180, 485 215, 520 185 S 575 165, 610 210 S 640 225, 645 190"
        fill="none" stroke="#1A8A8A" stroke-width="2" opacity="0.75"/>
  <text x="416" y="250" font-family="{_FONT}" font-size="12" fill="#5B6775">
    espectro ≈ · cruce roto
  </text>

  <!-- p box — own column, no overlap -->
  <rect x="700" y="120" width="180" height="130" rx="14" fill="{_NAVY}"/>
  <text x="790" y="158" text-anchor="middle" font-family="{_FONT}" font-size="12"
        font-weight="600" fill="{_ON_DARK_SOFT}">p_surr</text>
  <text x="790" y="198" text-anchor="middle" font-family="{_FONT}" font-size="26"
        font-weight="700" fill="{_ON_DARK}">&lt; α ?</text>
  <text x="790" y="228" text-anchor="middle" font-family="{_FONT}" font-size="12"
        fill="{_ON_DARK_SOFT}">efecto + nulo</text>
</svg>"""
    return _frame(svg, t("illus.surr_title"), cap)


# ===========================================================================
# 6. Pipeline — 2 rows of 4 to avoid cramming
# ===========================================================================


def _svg_pipeline(caption: str | None = None) -> str:
    cap = caption or t("illus.pipe_cap")
    row1 = [
        ("Datos", "serie / CSV"),
        ("z-score", "escala"),
        ("Bandt–Pompe", "símbolos"),
        ("τₛ", "relacional"),
    ]
    row2 = [
        ("RECD", "Φ₁–Φ₃"),
        ("EWS", "var · AR1"),
        ("Surrogates", "nulo"),
        ("Hash", "SHA-256"),
    ]
    highlight = {"τₛ", "RECD", "Hash"}

    def row_nodes(items: list[tuple[str, str]], y: int) -> str:
        # 4 nodes, wide cards
        w, gap, m = 190, 18, 40
        parts = []
        for i, (t, s) in enumerate(items):
            x = m + i * (w + gap)
            hi = t in highlight
            fill = _NAVY if hi else _CHIP
            tc = _ON_DARK if hi else _INK
            sc = _ON_DARK_SOFT if hi else _INK_SOFT
            stroke = "none" if hi else "#E4E9EF"
            parts.append(
                f"""
                <rect x="{x}" y="{y}" width="{w}" height="64" rx="12"
                      fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
                <text x="{x + w/2}" y="{y + 28}" text-anchor="middle" font-family="{_FONT}"
                      font-size="14" font-weight="700" fill="{tc}">{t}</text>
                <text x="{x + w/2}" y="{y + 48}" text-anchor="middle" font-family="{_FONT}"
                      font-size="12" fill="{sc}">{s}</text>
                """
            )
            if i < len(items) - 1:
                parts.append(
                    f'<line x1="{x + w}" y1="{y + 32}" x2="{x + w + gap}" y2="{y + 32}" '
                    f'stroke="#C5CED6" stroke-width="2"/>'
                )
        return "".join(parts)

    svg = f"""
<svg viewBox="0 0 920 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pipeline">
  <defs>
    <linearGradient id="pl-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F8FA"/><stop offset="100%" stop-color="#EEF4F7"/>
    </linearGradient>
  </defs>
  <rect width="920" height="280" rx="16" fill="url(#pl-bg)"/>
  <text x="40" y="38" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">PIPELINE DEL LABORATORIO</text>
  <text x="40" y="64" font-family="{_FONT}" font-size="15" font-weight="700" fill="#1A2332">
    Definir → calcular → comparar → nular → documentar
  </text>
  {row_nodes(row1, 88)}
  <!-- vertical connector hint -->
  <text x="460" y="172" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#8B95A1">↓</text>
  {row_nodes(row2, 184)}
  <text x="40" y="268" font-family="{_FONT}" font-size="12" fill="#5B6775">
    {t("illus.svg_nodes")}
  </text>
</svg>"""
    return _frame(svg, t("illus.pipe_title"), cap)


# ===========================================================================
# 7. Chronos / Kairos — labels inside safe zone
# ===========================================================================


def _svg_chronos_kairos(caption: str | None = None) -> str:
    cap = caption or t("illus.ck_cap")
    svg = f"""
<svg viewBox="0 0 920 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chronos Kairos">
  <defs>
    <linearGradient id="ck-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F4ED"/><stop offset="100%" stop-color="#ECEFF5"/>
    </linearGradient>
    <linearGradient id="ck-a" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0D4F6B"/><stop offset="100%" stop-color="#1A6F8A"/>
    </linearGradient>
    <linearGradient id="ck-b" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#5B4B8A"/><stop offset="100%" stop-color="#1A8A8A"/>
    </linearGradient>
  </defs>
  <rect width="920" height="320" rx="16" fill="url(#ck-bg)"/>
  <text x="36" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">DOS TIEMPOS</text>
  <text x="36" y="66" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    Chronos del protocolo · Kairos del sistema
  </text>

  <!-- Chronos -->
  <g transform="translate(240,185)">
    <circle r="78" fill="#fff" stroke="#E4E9EF" stroke-width="2"/>
    <circle r="68" fill="none" stroke="#EEF2F5" stroke-width="1"/>
    <g stroke="#0D4F6B" stroke-width="2" stroke-linecap="round">
      <line y1="-62" y2="-52"/><line y1="52" y2="62"/>
      <line x1="-62" x2="-52"/><line x1="52" x2="62"/>
    </g>
    <line x1="0" y1="0" x2="0" y2="-42" stroke="url(#ck-a)" stroke-width="3.5" stroke-linecap="round"/>
    <line x1="0" y1="0" x2="28" y2="16" stroke="#1A8A8A" stroke-width="2.5" stroke-linecap="round"/>
    <circle r="5" fill="#0D4F6B"/>
  </g>
  <text x="240" y="290" text-anchor="middle" font-family="{_FONT}" font-size="15"
        font-weight="700" fill="#0D4F6B">Chronos</text>
  <text x="240" y="310" text-anchor="middle" font-family="{_FONT}" font-size="12" fill="#5B6775">
    tiempo del protocolo
  </text>

  <path d="M460 100 C 480 140, 440 180, 460 220 S 480 280, 460 300"
        fill="none" stroke="#D0D7DE" stroke-width="2" stroke-dasharray="5 6"/>

  <!-- Kairos -->
  <g transform="translate(680,185)">
    <circle r="78" fill="#fff" stroke="#E4E9EF" stroke-width="2"/>
    <ellipse rx="54" ry="40" fill="none" stroke="#5B4B8A" stroke-width="2.2"
             transform="rotate(-25)" opacity="0.85"/>
    <ellipse rx="40" ry="54" fill="none" stroke="#1A8A8A" stroke-width="1.8"
             transform="rotate(15)" opacity="0.7"/>
    <circle cx="24" cy="-26" r="7" fill="url(#ck-b)"/>
    <circle cx="-20" cy="20" r="5" fill="#0D4F6B"/>
    <circle cx="8" cy="30" r="4" fill="#C45C26"/>
    <circle r="6" fill="#5B4B8A"/>
  </g>
  <text x="680" y="290" text-anchor="middle" font-family="{_FONT}" font-size="15"
        font-weight="700" fill="#5B4B8A">Kairos</text>
  <text x="680" y="310" text-anchor="middle" font-family="{_FONT}" font-size="12" fill="#5B6775">
    tiempo del sistema
  </text>
</svg>"""
    return _frame(svg, t("illus.ck_title"), cap)


# ===========================================================================
# 8. CCTP
# ===========================================================================


def _svg_cctp_finding(caption: str | None = None) -> str:
    cap = caption or t("illus.cctp_cap")
    svg = f"""
<svg viewBox="0 0 920 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CCTP">
  <defs>
    <linearGradient id="ct-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F8FA"/><stop offset="100%" stop-color="#F4F1EA"/>
    </linearGradient>
  </defs>
  <rect width="920" height="320" rx="16" fill="url(#ct-bg)"/>
  <text x="36" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">{t("illus.svg_anchor")}</text>
  <text x="36" y="66" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    {t("illus.svg_pre_vf")}
  </text>

  <!-- callouts above timeline, well spaced -->
  <rect x="80" y="96" width="200" height="52" rx="10" fill="#fff" stroke="#E4E9EF"/>
  <text x="180" y="118" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#8B95A1">
    {t("illus.svg_ews_short")}
  </text>
  <text x="180" y="138" text-anchor="middle" font-family="{_FONT}" font-size="13"
        font-weight="700" fill="#0D4F6B">a menudo ambiguas</text>

  <rect x="360" y="96" width="200" height="52" rx="10" fill="#fff" stroke="#E4E9EF"/>
  <text x="460" y="118" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#8B95A1">
    τₛ · excess3
  </text>
  <text x="460" y="138" text-anchor="middle" font-family="{_FONT}" font-size="13"
        font-weight="700" fill="#5B4B8A">reorganización</text>

  <!-- timeline -->
  <line x1="80" y1="200" x2="840" y2="200" stroke="#D0D7DE" stroke-width="3" stroke-linecap="round"/>
  <circle cx="180" cy="200" r="9" fill="#1A8A8A"/>
  <circle cx="460" cy="200" r="9" fill="#0D4F6B"/>
  <circle cx="760" cy="200" r="11" fill="#C45C26"/>

  <text x="180" y="232" text-anchor="middle" font-family="{_FONT}" font-size="12" fill="#5B6775">
    baseline
  </text>
  <text x="460" y="232" text-anchor="middle" font-family="{_FONT}" font-size="12" fill="#5B6775">
    ventana pre-FV
  </text>
  <text x="760" y="232" text-anchor="middle" font-family="{_FONT}" font-size="12"
        font-weight="600" fill="#C45C26">evento FV</text>

  <rect x="620" y="252" width="240" height="48" rx="10" fill="{_NAVY}"/>
  <text x="740" y="272" text-anchor="middle" font-family="{_FONT}" font-size="11"
        fill="{_ON_DARK_SOFT}">concordancia de signo</text>
  <text x="740" y="290" text-anchor="middle" font-family="{_FONT}" font-size="15"
        font-weight="700" fill="{_ON_DARK}">8 / 10</text>
</svg>"""
    return _frame(svg, t("illus.cctp_title"), cap)


# ===========================================================================
# 9. excess3
# ===========================================================================


def _svg_excess3(caption: str | None = None) -> str:
    cap = caption or t("illus.ex_cap")
    svg = f"""
<svg viewBox="0 0 920 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="excess3">
  <defs>
    <linearGradient id="ex-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F7F8FA"/><stop offset="100%" stop-color="#F0ECF7"/>
    </linearGradient>
    <linearGradient id="ex-c" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1A8A8A"/><stop offset="100%" stop-color="#5B4B8A"/>
    </linearGradient>
  </defs>
  <rect width="920" height="300" rx="16" fill="url(#ex-bg)"/>
  <text x="36" y="40" font-family="{_FONT}" font-size="11" font-weight="600" fill="#8B95A1"
        letter-spacing="1.2">NIVEL 3 EN RUIDO REAL</text>
  <text x="36" y="66" font-family="{_FONT}" font-size="16" font-weight="700" fill="#1A2332">
    excess3 continuo frente a Φ₃ binario
  </text>

  <!-- left panel: binary — all labels INSIDE -->
  <rect x="36" y="92" width="410" height="180" rx="12" fill="#fff" stroke="#E4E9EF"/>
  <text x="56" y="120" font-family="{_FONT}" font-size="14" font-weight="700" fill="#0D4F6B">
    Φ₃ (umbral θ₃)
  </text>
  <text x="56" y="142" font-family="{_FONT}" font-size="12" fill="#5B6775">salida 0 / 1</text>
  <polyline points="60,230 170,230 170,175 420,175" fill="none" stroke="#C45C26"
            stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="170" y1="160" x2="170" y2="248" stroke="#D0D7DE" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="170" y="262" text-anchor="middle" font-family="{_FONT}" font-size="11" fill="#8B95A1">θ₃</text>
  <text x="300" y="160" font-family="{_FONT}" font-size="11" fill="#C45C26">puede quedar en 0</text>

  <!-- right panel: continuous -->
  <rect x="474" y="92" width="410" height="180" rx="12" fill="#fff" stroke="#E4E9EF"/>
  <text x="494" y="120" font-family="{_FONT}" font-size="14" font-weight="700" fill="#5B4B8A">
    excess3
  </text>
  <text x="494" y="142" font-family="{_FONT}" font-size="12" fill="#5B6775">gradiente continuo</text>
  <path d="M500 235 C 560 228, 610 205, 670 185 S 780 150, 860 145"
        fill="none" stroke="url(#ex-c)" stroke-width="3" stroke-linecap="round"/>
  <circle cx="760" cy="155" r="5" fill="#5B4B8A"/>
  <text x="772" y="152" font-family="{_FONT}" font-size="11" fill="#5B4B8A">Δ detectable</text>
</svg>"""
    return _frame(svg, t("illus.ex_title"), cap)


# ===========================================================================
# 10. Hero
# ===========================================================================


def _svg_hero_constellation(caption: str | None = None) -> str:
    cap = caption or t("illus.hero_cap")
    # Solid white chips + dark ink on navy ground (never translucent + light text
    # that can collapse to black/invisible under browser / export quirks).
    sats = [
        (200, 95, "BP", "ordinal"),
        (160, 210, "RECD", "Φ₁–Φ₃"),
        (300, 265, "EWS", t("illus.svg_sat_classical")),
        (720, 95, "Surr.", t("illus.svg_sat_nulls")),
        (760, 210, "Hash", "repro"),
        (620, 265, "Lab", t("illus.svg_sat_run")),
    ]
    edges = "".join(
        f'<line x1="460" y1="155" x2="{x}" y2="{y}" '
        f'stroke="{_ON_DARK}" stroke-opacity="0.28" stroke-width="1.6"/>'
        for x, y, *_ in sats
    )
    nodes = ""
    for x, y, a, b in sats:
        nodes += f"""
        <circle cx="{x}" cy="{y}" r="40" fill="{_CHIP}"
                stroke="{_ON_DARK_SOFT}" stroke-width="1.5"/>
        <text x="{x}" y="{y - 5}" text-anchor="middle" font-family="{_FONT}"
              font-size="13" font-weight="700" fill="{_NAVY}">{a}</text>
        <text x="{x}" y="{y + 13}" text-anchor="middle" font-family="{_FONT}"
              font-size="11" font-weight="500" fill="{_INK_SOFT}">{b}</text>
        """
    svg = f"""
<svg viewBox="0 0 920 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mapa conceptual">
  <defs>
    <linearGradient id="he-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{_NAVY}"/>
      <stop offset="55%" stop-color="#1A5F78"/>
      <stop offset="100%" stop-color="#1A2332"/>
    </linearGradient>
    <linearGradient id="he-g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{_TEAL}"/><stop offset="100%" stop-color="{_PURPLE}"/>
    </linearGradient>
    <filter id="he-soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0A2A38" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect width="920" height="340" rx="18" fill="url(#he-bg)"/>
  {edges}
  <circle cx="460" cy="155" r="54" fill="url(#he-g)" filter="url(#he-soft)"/>
  <circle cx="460" cy="155" r="54" fill="none" stroke="{_ON_DARK}" stroke-opacity="0.45" stroke-width="1.5"/>
  <text x="460" y="168" text-anchor="middle"
        font-family="Times New Roman, Georgia, serif"
        font-size="34" font-weight="700" fill="{_ON_DARK}">τₛ</text>
  {nodes}
  <!-- Footer on solid dark bar so soft teal never sinks into the gradient -->
  <rect x="200" y="298" width="520" height="28" rx="14" fill="#0A2A38" fill-opacity="0.55"/>
  <text x="460" y="317" text-anchor="middle" font-family="{_FONT}"
        font-size="12" font-weight="600" fill="{_ON_DARK}">
    {t("illus.svg_hero_foot")}
  </text>
</svg>"""
    return _frame(svg, t("illus.hero_title"), cap)


# ===========================================================================
# Registry
# ===========================================================================

ILLUSTRATIONS = {
    "hero": _svg_hero_constellation,
    "tau_relational": _svg_tau_relational,
    "dual_reading": _svg_dual_reading,
    "recd_nested": _svg_recd_nested,
    "bandt_pompe": _svg_bandt_pompe,
    "surrogates": _svg_surrogates,
    "pipeline": _svg_pipeline,
    "chronos_kairos": _svg_chronos_kairos,
    "cctp": _svg_cctp_finding,
    "excess3": _svg_excess3,
}
