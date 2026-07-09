"""Load Markdown educational content."""

from __future__ import annotations

from pathlib import Path

from stp.config.settings import CONTENT_DIR


def read_markdown(*parts: str) -> str:
    path = CONTENT_DIR.joinpath(*parts)
    if not path.exists():
        return f"_Contenido no encontrado: `{path.relative_to(CONTENT_DIR)}`_"
    return path.read_text(encoding="utf-8")


def list_section(section: str) -> list[Path]:
    d = CONTENT_DIR / section
    if not d.exists():
        return []
    return sorted(d.glob("*.md"))
