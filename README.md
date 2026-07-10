# Systemic Tau Platform

*(🇬🇧 English | 🇪🇸 Español | 🇫🇷 Français)*

### 🇬🇧 English
Educational and research web platform ([Streamlit](https://streamlit.io)) for teaching, exploring, and interactive experimentation with the **Systemic Tau** paradigm and the **Discrete Extramental Clock (RECD)** model. Includes fundamentals, mathematics, domains, interactive laboratory, learning path, and scientific evidence.

### 🇪🇸 Español
Plataforma web educativa y de investigación ([Streamlit](https://streamlit.io)) para el paradigma **Tau Sistémica + RECD** (Reloj Extramental Discreto): fundamentos, matemática, dominios, laboratorio interactivo, ruta de aprendizaje y evidencia científica.

### 🇫🇷 Français
Plateforme web éducative et de recherche ([Streamlit](https://streamlit.io)) pour l'enseignement, l'exploration et l'expérimentation interactive avec le paradigme **Tau Systémique** et le modèle de **l'Horloge Extramentale Discrète (RECD)**. Comprend les fondamentaux, les mathématiques, les domaines, le laboratoire interactif et les preuves scientifiques.

> Producto con calidad SaaS educativa premium — no un prototipo de notebook.

## Inicio rápido

```bash
cd ~/grok-safe/systemic-tau-platform

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Lanzar la app
PYTHONPATH=src streamlit run app/Home.py
```

Abrir la URL local que indique Streamlit (típicamente `http://localhost:8501`).

## Qué incluye v1.0

| Área | Estado |
|------|--------|
| Arquitectura completa de carpetas | ✅ |
| Especificación de producto (`docs/SPEC.md`) | ✅ |
| Guías datasets, Lab flow, ingeniería | ✅ |
| Contenido Fundamentos (6 secciones) | ✅ |
| Contenido 5 dominios | ✅ |
| Glosario + FAQ + publicaciones YAML | ✅ |
| Core: ordinal, τ_s, RECD, EWS, surrogates, hash | ✅ |
| App multipágina Streamlit (Home + 8 secciones) | ✅ |
| Lab Fast end-to-end + export Markdown | ✅ |
| Samples SDDB export script | ✅ script |
| PDF branding / TDA Full / pagos | 🔲 roadmap |

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
