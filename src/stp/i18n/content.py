"""Localized educational content (Markdown / YAML).

Spanish source lives in ``content/``.
Translations live in ``locales/{lang}/content/`` with the same relative paths.
"""

from __future__ import annotations

from pathlib import Path

from stp.config.settings import CONTENT_DIR
from stp.i18n.core import get_lang, locales_dir, _normalize


def localized_content_path(*parts: str, lang: str | None = None) -> Path:
    """Best path for a content file in the requested language (fallback es)."""
    lang = _normalize(lang or get_lang())
    rel = Path(*parts)
    if lang != "es":
        candidate = locales_dir() / lang / "content" / rel
        if candidate.exists():
            return candidate
    return CONTENT_DIR.joinpath(*parts)


def read_localized_markdown(*parts: str, lang: str | None = None) -> str:
    path = localized_content_path(*parts, lang=lang)
    if not path.exists():
        # final message in current UI language would be nicer; keep simple
        rel = "/".join(parts)
        return f"_Content not found: `{rel}`_"
    return path.read_text(encoding="utf-8")
