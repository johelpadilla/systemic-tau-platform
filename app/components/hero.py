"""Backward-compatible re-exports. Prefer: from components.ui import ..."""

from __future__ import annotations

from .ui import (  # noqa: F401
    callout,
    empty_state,
    feature_card,
    footer,
    inject_css,
    lab_stepper,
    metrics_strip,
    nav_card,
    page_header,
    render_hero,
    section_header,
    sidebar_brand,
)

__all__ = [
    "callout",
    "empty_state",
    "feature_card",
    "footer",
    "inject_css",
    "lab_stepper",
    "metrics_strip",
    "nav_card",
    "page_header",
    "render_hero",
    "section_header",
    "sidebar_brand",
]
