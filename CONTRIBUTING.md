# Contributing

Thanks for helping improve Systemic Tau Platform (research + education).

## Development setup

```bash
git clone https://github.com/johelpadilla/systemic-tau-platform.git
cd systemic-tau-platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e ".[dev]"
```

Run the app:

```bash
stp serve
# or: streamlit run app/streamlit_app.py
```

Tests:

```bash
pytest -q
python scripts/smoke_apptest.py
```

## Guidelines

1. **Spanish is the source language** for UI strings (`locales/es/ui.json`) and educational content under `content/`. Keep EN/FR in parity when you add keys or pages.
2. **Core science stays Streamlit-free** (`src/stp/core`). Put UI only under `app/`.
3. Prefer small, focused PRs with tests for pipeline or i18n changes.
4. Do not commit `.venv/`, secrets, raw PhysioNet `.dat` files, or large private datasets.
5. Lab public caps (`MAX_CSV_*`, `MAX_SURROGATES_PUBLIC`) protect shared hosting — raise them only with a documented reason.

## Translations (item 15)

- UI: edit `locales/{es,en,fr}/ui.json` together (same leaf keys).
- Content: mirror files under `locales/{en,fr}/content/…`.
- Critical pages for native review: Fundamentos, Lab, About & Legal (disclaimer/privacy).

## Code style

- Python 3.10+
- `ruff` (optional locally): `ruff check src app tests`
- Type hints encouraged in `src/stp`

## Pull requests

- Describe *why* and how you tested.
- Link related issues.
- Ensure CI is green (pytest + smoke AppTest).
