from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from stp.i18n.content import localized_content_path
from stp.i18n.core import get_lang


@lru_cache(maxsize=8)
def _load_glossary_lang(lang: str) -> tuple[dict[str, Any], ...]:
    path = localized_content_path("learning", "glossary.yaml", lang=lang)
    if not path.exists():
        return tuple()
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    terms = list(data.get("terms", []))
    return tuple(terms)


def clear_glossary_cache() -> None:
    _load_glossary_lang.cache_clear()


def load_glossary(lang: str | None = None) -> list[dict]:
    """Load glossary terms for the active (or given) language; falls back via localized_content_path."""
    lang = lang or get_lang()
    return [dict(t) for t in _load_glossary_lang(lang)]


def search_glossary(query: str, lang: str | None = None) -> list[dict]:
    q = (query or "").strip().lower()
    terms = load_glossary(lang=lang)
    if not q:
        return terms
    out = []
    for item in terms:
        blob = f"{item.get('term', '')} {item.get('short', '')} {item.get('long', '')} {item.get('id', '')}".lower()
        if q in blob:
            out.append(item)
    return out
