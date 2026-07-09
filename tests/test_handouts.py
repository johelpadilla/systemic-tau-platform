"""Downloadable handouts."""

from __future__ import annotations

from stp.education.handouts import (
    get_handout,
    glossary_to_markdown,
    list_handouts,
    render_handout,
    render_handout_bytes,
)


def test_list_handouts_nonempty():
    hs = list_handouts()
    assert len(hs) >= 10
    ids = {h.id for h in hs}
    assert "guia_rapida" in ids
    assert "faq" in ids
    assert "pack_estudiante" in ids
    assert "pack_docente" in ids


def test_static_handouts_render():
    for hid in ("guia_rapida", "manual_usuario", "teoria", "cheatsheet", "syllabus", "etica"):
        text = render_handout(hid)
        assert len(text) > 200
        assert "STP" in text or "Tau" in text or "τ" in text
        assert render_handout_bytes(hid).startswith(b"#") or b"Systemic" in render_handout_bytes(hid)


def test_faq_and_glossary():
    faq = render_handout("faq")
    assert "Bandt" in faq or "surrogates" in faq.lower() or "Tau" in faq
    gloss = glossary_to_markdown()
    assert "τ" in gloss or "Tau" in gloss
    assert len(gloss) > 300


def test_packs():
    student = render_handout("pack_estudiante")
    teacher = render_handout("pack_docente")
    assert "Parte 1" in student
    assert "Parte 1" in teacher
    assert len(student) > 5000
    assert len(teacher) >= len(student) - 1000  # teacher includes more sections
    fund = render_handout("fundamentos_compilado")
    assert len(fund) > 1000


def test_get_handout_filename():
    h = get_handout("guia_rapida")
    assert h.filename.endswith(".md")
