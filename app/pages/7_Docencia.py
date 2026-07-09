from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "app"))

import streamlit as st

from components.hero import inject_css

st.set_page_config(page_title="Docencia | STP", page_icon="🌀", layout="wide")
inject_css()

st.title("Recursos para docencia e investigación")

st.markdown(
    """
    ## Syllabus sugerido (6 semanas)

    | Semana | Tema | Actividad Lab |
    |--------|------|----------------|
    | 1 | EWS clásicas y sus límites | Comparar var/AR1 en sintético |
    | 2 | Bandt–Pompe y τ_s | Sandbox matemática |
    | 3 | RECD Φ₁–Φ₃ y excess3 | Demo logísticos acoplados |
    | 4 | Cardiología CCTP | Cardio-like + lectura preprint |
    | 5 | Dengue / ecología | Transferencia entre dominios |
    | 6 | Surrogates y reportes | Export MD + hash |

    ## Materiales (v1.0)

    - Contenido Markdown en `content/` (Fundamentos, Dominios, FAQ).
    - Notebooks de ejemplo en `notebooks/` (añadir en P2).
    - Código alineado con `systemictau` y `nested-recd`.

    ## Licencias

    | Uso | Condición |
    |-----|-----------|
    | **Académico** | Libre con citación del software y papers |
    | **Comercial / consultoría** | Licencia Professional o Institutional |
    | **Datos de terceros** | Sujetos a ToS de PhysioNet, LTER, etc. |

    ## Notebooks previstos

    1. `01_bandt_pompe_intro.ipynb`
    2. `02_tau_s_sliding.ipynb`
    3. `03_recd_levels_excess3.ipynb`
    4. `04_cctp_record38.ipynb`
    5. `05_surrogates_nulls.ipynb`
    """
)
