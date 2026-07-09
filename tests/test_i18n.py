"""Internationalization: catalogs, content fallback, interpretation locales."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from stp.config.settings import AnalysisParams
from stp.core.interpretation import interpret_dual_reading, methods_paragraph
from stp.core.pipeline import run_analysis
from stp.data.generators import coupled_logistic
from stp.education.content_loader import read_markdown
from stp.education.handouts import list_handouts, render_handout
from stp.i18n.core import (
    LANG_LABELS,
    SUPPORTED_LANGS,
    clear_catalog_cache,
    get_lang,
    locales_dir,
    set_lang,
    t,
)


@pytest.fixture(autouse=True)
def _reset_lang():
    clear_catalog_cache()
    set_lang("es")
    yield
    set_lang("es")
    clear_catalog_cache()


def test_supported_langs():
    assert SUPPORTED_LANGS == ("es", "en", "fr")
    assert set(LANG_LABELS) == set(SUPPORTED_LANGS)


def test_ui_catalogs_exist_and_parse():
    for lang in SUPPORTED_LANGS:
        path = locales_dir() / lang / "ui.json"
        assert path.exists(), path
        data = json.loads(path.read_text(encoding="utf-8"))
        assert "home" in data and "lab" in data and "interp" in data
        # key structural parity with Spanish source
        es = json.loads((locales_dir() / "es" / "ui.json").read_text(encoding="utf-8"))
        assert set(data.keys()) == set(es.keys())


def test_t_switches_language():
    set_lang("es")
    es_title = t("lab.title")
    set_lang("en")
    en_title = t("lab.title")
    set_lang("fr")
    fr_title = t("lab.title")
    assert es_title != en_title
    assert en_title != fr_title
    assert "Laboratorio" in es_title or "laboratorio" in es_title.lower()
    assert "Laboratory" in en_title or "laboratory" in en_title.lower()
    assert "Laboratoire" in fr_title or "laboratoire" in fr_title.lower()


def test_t_fallback_unknown_key():
    assert t("this.key.does.not.exist.at.all") == "this.key.does.not.exist.at.all"


def test_content_localized_fundamentos():
    set_lang("es")
    es = read_markdown("fundamentos", "01_tau.md")
    set_lang("en")
    en = read_markdown("fundamentos", "01_tau.md")
    set_lang("fr")
    fr = read_markdown("fundamentos", "01_tau.md")
    assert "τ_s" in es or "Tau" in es
    assert "Systemic Tau" in en or "τ_s" in en
    assert "Tau systémique" in fr or "τ_s" in fr
    assert es != en
    assert en != fr


def test_content_fallback_to_spanish_when_missing(tmp_path, monkeypatch):
    # existing file always present for fundamentos; use a nonsense path
    set_lang("en")
    text = read_markdown("no_such_section", "missing.md")
    assert "Content not found" in text or "no_such_section" in text


def test_interpretation_language():
    X = coupled_logistic(T=200, seed=0)
    params = AnalysisParams(window=31, stride=2, n_surrogates=0, mode="fast")
    result = run_analysis(X, params, event_index=100, domain="synthetic")
    set_lang("en")
    en = interpret_dual_reading(result.metrics, result.surrogate_stats, 100, "synthetic", lang="en")
    fr = interpret_dual_reading(result.metrics, result.surrogate_stats, 100, "synthetic", lang="fr")
    es = interpret_dual_reading(result.metrics, result.surrogate_stats, 100, "synthetic", lang="es")
    assert "Dual reading" in en["title"] or "dual" in en["title"].lower()
    assert "Lecture duale" in fr["title"] or "duale" in fr["title"].lower()
    assert "Lectura dual" in es["title"] or "dual" in es["title"].lower()
    assert en["summary"] != es["summary"] or en["bullets"][0] != es["bullets"][0]


def test_methods_paragraph_languages():
    p = AnalysisParams(window=31, stride=2, n_surrogates=4, include_tda=True, include_breathing=True)
    es = methods_paragraph(p, domain="synthetic", event_index=10, n=4, repro_hash="abc", lang="es")
    en = methods_paragraph(p, domain="synthetic", event_index=10, n=4, repro_hash="abc", lang="en")
    fr = methods_paragraph(p, domain="synthetic", event_index=10, n=4, repro_hash="abc", lang="fr")
    assert "estandarizaron" in es or "z-score" in es
    assert "z-scored" in en
    assert "standardisées" in fr or "z-score" in fr


def test_handouts_titles_localize():
    set_lang("es")
    es_titles = {h.id: h.title for h in list_handouts()}
    set_lang("en")
    en_titles = {h.id: h.title for h in list_handouts()}
    assert es_titles["guia_rapida"] != en_titles["guia_rapida"]
    set_lang("en")
    body = render_handout("guia_rapida")
    assert "Quick guide" in body or "minutes" in body.lower()


def test_set_lang_normalizes():
    assert set_lang("EN") == "en"
    assert set_lang("fr-FR") == "fr"
    assert set_lang("de") == "es"  # unsupported → Spanish source
    assert get_lang() == "es"


def _flatten(d: dict, prefix: str = "") -> dict[str, str]:
    out: dict[str, str] = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(_flatten(v, key))
        else:
            out[key] = str(v)
    return out


def test_ui_leaf_key_parity():
    es = _flatten(json.loads((locales_dir() / "es" / "ui.json").read_text(encoding="utf-8")))
    for lang in ("en", "fr"):
        other = _flatten(json.loads((locales_dir() / lang / "ui.json").read_text(encoding="utf-8")))
        assert set(es) == set(other), f"{lang} key mismatch: missing={set(es)-set(other)} extra={set(other)-set(es)}"


def test_content_file_parity():
    from stp.config.settings import CONTENT_DIR

    src = {p.relative_to(CONTENT_DIR).as_posix() for p in CONTENT_DIR.rglob("*") if p.is_file() and not p.name.startswith(".")}
    for lang in ("en", "fr"):
        loc = locales_dir() / lang / "content"
        have = {p.relative_to(loc).as_posix() for p in loc.rglob("*") if p.is_file()}
        assert src == have, f"{lang} content missing {src - have} extra {have - src}"


def test_glossary_localized_not_spanish():
    from stp.education.glossary import clear_glossary_cache, load_glossary

    clear_glossary_cache()
    set_lang("es")
    es = load_glossary()
    set_lang("en")
    clear_glossary_cache()
    en = load_glossary()
    set_lang("fr")
    clear_glossary_cache()
    fr = load_glossary()
    assert es and en and fr
    assert es[0]["term"] != en[0]["term"] or es[0]["short"] != en[0]["short"]
    assert "Systemic Tau" in en[0]["term"] or "ordinal" in en[0]["short"].lower()
    assert "systémique" in fr[0]["term"].lower() or "ordinale" in fr[0]["short"].lower()
    # EN glossary must not be a copy of Spanish short defs
    assert "reorganización de acoplamiento" not in en[0].get("short", "")
    assert "reorganización de acoplamiento" not in fr[0].get("short", "")


def test_page_ui_keys_resolve_all_langs():
    """Critical surface strings used outside Lab must resolve (not return raw keys)."""
    keys = [
        "matematica.sandbox_callout",
        "dominios.synth_header",
        "ruta.tab_path",
        "ruta.b1",
        "evidencia.regen_btn",
        "docencia.syl_header",
        "materiales.packs_header",
        "illus.tau_title",
        "handouts.pack_student_title",
    ]
    for lang in SUPPORTED_LANGS:
        set_lang(lang)
        for key in keys:
            val = t(key)
            assert val != key, f"{lang}: unresolved {key}"
            assert not val.startswith(key + "."), f"{lang}: bad {key}={val}"
