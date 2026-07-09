# User manual

## Install
```bash
cd systemic-tau-platform
python -m venv .venv && source .venv/bin/activate
pip install -e .
streamlit run app/Home.py
```

## Map
Home · Foundations · Mathematics · Domains · Lab · Path · Evidence · Teaching · Materials.

## Language
Sidebar **Language**: Español (source) · English · Français. All UI and educational content follow the selection.

## Lab steps
1. Data (catalog / CSV) 2. Parameters 3. Run 4. Results + export.

## CLI
```bash
stp analyze data.csv --domain cardiology --breathing --tda -o report.md
stp serve
```

## Troubleshooting
Import errors: reinstall editable package; hard-refresh Streamlit. Univariate CSV: automatic [x, |Δx|] proxy.
