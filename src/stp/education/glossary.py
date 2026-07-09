from __future__ import annotations

from functools import lru_cache

import yaml

from stp.config.settings import CONTENT_DIR


@lru_cache(maxsize=1)
def load_glossary() -> list[dict]:
    path = CONTENT_DIR / "learning" / "glossary.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return list(data.get("terms", []))


def search_glossary(query: str) -> list[dict]:
    q = (query or "").strip().lower()
    terms = load_glossary()
    if not q:
        return terms
    out = []
    for t in terms:
        blob = f"{t.get('term','')} {t.get('short','')} {t.get('long','')}".lower()
        if q in blob:
            out.append(t)
    return out
