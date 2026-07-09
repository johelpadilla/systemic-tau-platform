# Systemic Tau Platform

**Paradigma Tau Sistémico: De la Teoría a la Práctica**

Plataforma web educativa y de investigación (Streamlit) para el paradigma **Tau Sistémica + RECD** (Reloj Extramental Discreto): fundamentos, matemática, dominios, laboratorio interactivo, ruta de aprendizaje y evidencia científica.

> Producto con calidad SaaS educativa premium — no un prototipo de notebook.

## Inicio rápido

```bash
cd ~/grok-safe/systemic-tau-platform

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Lanzar la app
pip install -e .
stp serve
# o: PYTHONPATH=src streamlit run app/Home.py
```

Abrir la URL local que indique Streamlit (típicamente `http://localhost:8501`).

### CLI de análisis

```bash
stp analyze data/samples/sddb_rr_38_demo.csv \
  --domain cardiology --columns z_rr,z_abs_drr \
  --event 6800 -o report.md --json result.json
```

## Qué incluye v1.0+

| Área | Estado |
|------|--------|
| Arquitectura completa de carpetas | ✅ |
| Core: τ_s, RECD, EWS, phase-shuffle + IAAFT, hash | ✅ |
| Breathing window + memoria ordinal (extensión Lab) | ✅ |
| TDA / Betti en ventanas (ripser opcional o VR skeleton) | ✅ |
| Catálogo multi-dominio + adapters + presets | ✅ |
| Lab: evento, lectura dual, extensiones, MD/JSON/Methods | ✅ |
| Deep-links Dominios / Ruta → Lab | ✅ |
| Evidencia: figura regenerable SDDB-38 | ✅ |
| Materiales descargables (handouts / packs) | ✅ |
| **i18n ES (fuente) · EN · FR** — selector en sidebar, UI + contenidos | ✅ |
| CLI `stp analyze --breathing --tda` / `stp serve` | ✅ |
| Tests de propiedades, catálogo, extensiones e i18n | ✅ |
| TDA multi-escala producción / pagos SaaS | 🔲 roadmap |

## Idiomas (i18n)

- **Español** es la lengua fuente (`content/`, `locales/es/ui.json`).
- **English** y **Français** son locales completas: UI (`locales/{en,fr}/ui.json`) + contenidos educativos (`locales/{en,fr}/content/…`).
- En la app: selector **Idioma / Language / Langue** en la barra lateral (todas las páginas).
- Fallback: si falta una clave o un MD traducido, se usa el español.
- Programático: `STP_LANG=en` o `from stp.i18n import set_lang, t`.

## Documentación

- [`docs/SPEC.md`](docs/SPEC.md) — especificación maestra (navegación, UI, roadmap)
- [`docs/DATASETS.md`](docs/DATASETS.md) — datasets y preprocess
- [`docs/LAB_FLOW.md`](docs/LAB_FLOW.md) — flujo del Laboratorio
- [`docs/ENGINEERING.md`](docs/ENGINEERING.md) — stack y prácticas

## Estructura

```text
app/           Streamlit UI
src/stp/       Lógica (core, viz, education, reports)
content/       Markdown pedagógico
data/          Catálogo + samples
docs/          Especificación
tests/         Pytest
scripts/       Export / preprocess
```

## Integración con investigación local

| Proyecto | Uso |
|----------|-----|
| `Investigaciones/nested-recd` | Φ₁–Φ₃ / surrogates |
| `Investigaciones/Cardiac_CCTP_Pilot` | Cardiología SDDB |
| `systemictau` | Paridad τ_s / Studio |
| `Publicaciones/` | Sección Evidencia |

Exportar samples CCTP:

```bash
python scripts/export_sddb_samples.py --records 38,51
```

## Tests

```bash
PYTHONPATH=src pytest -q
```

## Citas

Cite el software y los papers/preprints del dominio correspondiente (CCTP Zenodo `10.5281/zenodo.21270699`, Síntesis Magna, Foundations, etc.).

## Licencia

MIT © 2026 Johel Padilla-Villanueva  
ORCID: [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)

**Disclaimer:** herramienta de investigación y docencia. No es dispositivo médico ni consejo de inversión.
