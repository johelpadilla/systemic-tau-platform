#!/usr/bin/env python3
"""Smoke: AppTest all main pages × ES/EN/FR. Exit non-zero on any exception."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(APP))

from components.bootstrap import ensure_stp_path  # noqa: E402

ensure_stp_path(APP / "Home.py")

from streamlit.testing.v1 import AppTest  # noqa: E402

from stp.i18n.core import set_lang  # noqa: E402

PAGES = [
    APP / "Home.py",
    APP / "pages" / "1_Fundamentos.py",
    APP / "pages" / "2_Matematica.py",
    APP / "pages" / "3_Dominios.py",
    APP / "pages" / "4_Laboratorio.py",
    APP / "pages" / "5_Ruta_Aprendizaje.py",
    APP / "pages" / "6_Evidencia.py",
    APP / "pages" / "7_Docencia.py",
    APP / "pages" / "8_Materiales.py",
    APP / "pages" / "9_About_Legal.py",
]

LANGS = ("es", "en", "fr")


def main() -> int:
    failures: list[str] = []
    for lang in LANGS:
        set_lang(lang)
        for page in PAGES:
            rel = page.relative_to(ROOT)
            try:
                at = AppTest.from_file(str(page), default_timeout=60)
                at.run()
                if at.exception:
                    for exc in at.exception:
                        failures.append(f"{lang} {rel}: {exc}")
                else:
                    print(f"OK  {lang} {rel}")
            except Exception as e:  # noqa: BLE001
                failures.append(f"{lang} {rel}: {type(e).__name__}: {e}")
                print(f"ERR {lang} {rel}: {e}")

    # Entrypoint navigation (single lang smoke)
    try:
        set_lang("es")
        at = AppTest.from_file(str(APP / "streamlit_app.py"), default_timeout=60)
        at.run()
        if at.exception:
            for exc in at.exception:
                failures.append(f"es streamlit_app.py: {exc}")
        else:
            print("OK  es streamlit_app.py")
    except Exception as e:  # noqa: BLE001
        failures.append(f"es streamlit_app.py: {type(e).__name__}: {e}")
        print(f"ERR streamlit_app: {e}")

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(" -", f)
        return 1
    print(f"\nAll smoke checks passed ({len(PAGES)} pages × {len(LANGS)} langs + entry).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
