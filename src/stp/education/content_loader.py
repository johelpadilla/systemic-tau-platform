"""Load Markdown educational content (language-aware)."""

from __future__ import annotations

from pathlib import Path

from stp.config.settings import CONTENT_DIR
from stp.i18n.content import localized_content_path, read_localized_markdown
from stp.i18n.core import t


def read_markdown(*parts: str, lang: str | None = None) -> str:
    """Read educational markdown in the active (or given) language; fall back to Spanish."""
    path = localized_content_path(*parts, lang=lang)
    if not path.exists():
        rel = "/".join(parts)
        return f"_{t('common.content_missing', path=rel)}_"
    return path.read_text(encoding="utf-8")


def list_section(section: str, lang: str | None = None) -> list[Path]:
    """List markdown files for a section (Spanish inventory; localized paths when present)."""
    d = CONTENT_DIR / section
    if not d.exists():
        return []
    out: list[Path] = []
    for p in sorted(d.glob("*.md")):
        out.append(localized_content_path(section, p.name, lang=lang))
    return out


# re-export for callers that want the low-level helper
__all__ = ["read_markdown", "list_section", "read_localized_markdown", "localized_content_path"]
