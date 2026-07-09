"""Public Lab caps and launch helpers."""

from __future__ import annotations

from stp.config.settings import (
    CONTACT_EMAIL,
    GITHUB_URL,
    MAX_CSV_COLS,
    MAX_CSV_MB,
    MAX_CSV_ROWS,
    MAX_SURROGATES_PUBLIC,
)
from stp.i18n.core import clear_catalog_cache, set_lang, t


def test_public_caps_sane():
    assert MAX_CSV_ROWS >= 1000
    assert MAX_CSV_COLS >= 2
    assert 1.0 <= MAX_CSV_MB <= 50.0
    assert 1 <= MAX_SURROGATES_PUBLIC <= 100


def test_contact_and_github_present():
    assert "@" in CONTACT_EMAIL
    assert GITHUB_URL.startswith("https://")


def test_disclaimer_keys_all_langs():
    clear_catalog_cache()
    for lang in ("es", "en", "fr"):
        set_lang(lang)
        body = t("common.disclaimer_body")
        assert len(body) > 40
        assert "medical" in body.lower() or "médic" in body.lower() or "dispositif" in body.lower()
        assert t("nav.about")
        assert t("lab.privacy_banner")
        assert t("about.title")
    set_lang("es")
    clear_catalog_cache()
