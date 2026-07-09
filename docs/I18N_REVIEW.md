# i18n review checklist (item 15)

Spanish (`es`) is the **source of truth**. EN/FR must keep **leaf-key parity** in `locales/*/ui.json` and mirrored content under `locales/{en,fr}/content/`.

## Automated (CI)

- `tests/test_i18n.py` — catalog parse, key parity, content loaders, interpretation locales
- `scripts/smoke_apptest.py` — every page × ES/EN/FR without exceptions

## Human / native pass (recommended before major public announcements)

Review these pages in **EN** and **FR** (sidebar language selector):

| Priority | Page | Focus |
|----------|------|--------|
| P0 | Home | Tagline, goals, disclaimer banner |
| P0 | Laboratorio | Privacy banner, caps messages, run labels |
| P0 | About & Legal | Disclaimer, privacy, citation, contact |
| P1 | Fundamentos | Scientific tone, no leftover Spanish headings |
| P1 | Materiales | Pack titles, download CTAs |
| P2 | Dominios / Evidencia / Docencia / Ruta | Domain blurbs, maturity notes |

### Sign-off log

| Date | Lang | Reviewer | Notes |
|------|------|----------|-------|
| 2026-07-09 | EN | Agent (structural + terminology pass) | Key parity; legal/disclaimer strings authored in EN |
| 2026-07-09 | FR | Agent (structural + terminology pass) | Key parity; legal/disclaimer strings authored in FR |
| _pending_ | EN | Native/scientific reviewer | Spot-check Fundamentos + Lab |
| _pending_ | FR | Native/scientific reviewer | Spot-check Fundamentos + Lab |

## How to fix a string

1. Edit `locales/es/ui.json` if the source concept changes.
2. Update `locales/en/ui.json` and `locales/fr/ui.json` the same key path.
3. Run `pytest tests/test_i18n.py -q` and smoke AppTest.
