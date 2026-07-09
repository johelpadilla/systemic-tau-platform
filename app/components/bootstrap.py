"""Ensure Streamlit pages import *this* repo's ``stp`` package.

Two failure modes we defend against:

1. Editable install pointing at an old scratch tree (wrong path).
2. Streamlit hot-reload reusing a stale ``stp.*`` module in ``sys.modules``
   that was imported before symbols like ``DOMAIN_LABELS`` existed
   (ImportError: cannot import name … from the correct file path).
"""

from __future__ import annotations

import sys
from pathlib import Path


def ensure_stp_path(page_file: str | Path) -> Path:
    """
    Insert ``<repo>/src`` at the front of ``sys.path`` and drop every
    already-imported ``stp*`` module so the next import reads current source.
    """
    page = Path(page_file).resolve()
    # pages live in app/pages/*.py → parents[2] = repo root
    # Home.py lives in app/ → parents[1] = repo root
    if page.parent.name == "pages":
        root = page.parents[2]
    else:
        root = page.parents[1]
    src = (root / "src").resolve()
    src_s = str(src)
    app_s = str((root / "app").resolve())

    # Prefer this tree
    for p in (src_s, app_s):
        while p in sys.path:
            sys.path.remove(p)
    sys.path.insert(0, src_s)
    sys.path.insert(0, app_s)

    # Critical for Streamlit: always re-import stp from disk
    for name in list(sys.modules):
        if name == "stp" or name.startswith("stp."):
            del sys.modules[name]

    return root
