"""Internationalization: Spanish is the source language; EN and FR are full locales."""

from __future__ import annotations

from stp.i18n.core import (
    LANG_LABELS,
    SUPPORTED_LANGS,
    get_lang,
    set_lang,
    t,
    tf,
    clear_catalog_cache,
)
from stp.i18n.content import read_localized_markdown, localized_content_path

__all__ = [
    "SUPPORTED_LANGS",
    "LANG_LABELS",
    "get_lang",
    "set_lang",
    "t",
    "tf",
    "clear_catalog_cache",
    "read_localized_markdown",
    "localized_content_path",
]
