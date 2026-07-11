# Systemic Tau Platform

*(🇬🇧 English | 🇪🇸 Español | 🇫🇷 Français)*

### 🇬🇧 English
An advanced educational and scientific research web platform ([Streamlit](https://streamlit.io)) dedicated to the exploration, teaching, and interactive experimentation of the **Systemic Tau** paradigm and the **Discrete Extramental Clock (RECD)** model. The platform encompasses theoretical foundations, mathematical formalisms, applied domains, an interactive analytical laboratory, learning pathways, and empirical scientific evidence.

### 🇪🇸 Español
Plataforma web avanzada de investigación y docencia académica ([Streamlit](https://streamlit.io)) orientada a la exploración y experimentación interactiva del paradigma **Tau Sistémica + RECD** (Reloj Extramental Discreto). La plataforma integra fundamentos teóricos, desarrollo matemático, dominios de aplicación, un laboratorio interactivo, itinerarios de aprendizaje y validación mediante evidencia científica.

### 🇫🇷 Français
Plateforme web avancée de recherche scientifique et d'enseignement universitaire ([Streamlit](https://streamlit.io)) dédiée à l'exploration et à l'expérimentation interactive du paradigme **Tau Systémique** et du modèle de **l'Horloge Extramentale Discrète (RECD)**. La plateforme intègre les fondements théoriques, le formalisme mathématique, les domaines d'application, un laboratoire analytique interactif et des preuves scientifiques empiriques.

> Producto diseñado con estándares de calidad universitaria y nivel SaaS — trascendiendo el prototipado convencional.

## Inicio rápido / Quick Start

```bash
cd ~/grok-safe/systemictau

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Ejecutar la plataforma / Launch the platform
PYTHONPATH=src streamlit run app/Home.py
```

Acceda mediante la URL local proporcionada por Streamlit (típicamente `http://localhost:8501`).

## Características de la Versión 1.1.0

| Componente | Estado |
|------------|--------|
| Arquitectura de software modularizada | ✅ |
| Especificación de producto y arquitectura (`docs/SPEC.md`) | ✅ |
| Guías de datos, flujo de laboratorio e ingeniería | ✅ |
| Contenido pedagógico: Fundamentos (6 módulos) | ✅ |
| Contenido sectorial: 5 dominios de aplicación | ✅ |
| Glosario interactivo, FAQ y registro de publicaciones | ✅ |
| Núcleo analítico: ordinal, τ_s, RECD, EWS, surrogates, hash | ✅ |
| Interfaz multipágina Streamlit (Inicio + 8 secciones) | ✅ |
| Laboratorio exhaustivo de extremo a extremo + Exportación Markdown y PDF | ✅ |
| Procesamiento y estimación heurística Auto-Tau | ✅ |
| Explorador visual de Variedades (Manifolds) 3D | ✅ |
| Exportación de muestras clínicas (SDDB y PhysioNet) | ✅ script |

## Documentación Técnica

- [`docs/SPEC.md`](docs/SPEC.md) — Documento maestro de especificación y arquitectura.
- [`docs/DATASETS.md`](docs/DATASETS.md) — Gestión de conjuntos de datos y preprocesamiento.
- [`docs/LAB_FLOW.md`](docs/LAB_FLOW.md) — Flujo operativo del Laboratorio de Análisis.
- [`docs/ENGINEERING.md`](docs/ENGINEERING.md) — Prácticas de ingeniería de software aplicadas.

## Estructura del Proyecto

```text
app/           Interfaz de usuario Streamlit
src/stp/       Lógica principal (núcleo matemático, visualización, reportes)
content/       Documentación y módulos de aprendizaje en formato Markdown
data/          Catálogo central de series temporales y muestras experimentales
docs/          Arquitectura técnica y especificaciones del diseño
tests/         Conjuntos de pruebas y validaciones (Pytest)
scripts/       Herramientas auxiliares y preprocesamiento de datos
```

## Integración con Investigaciones Locales

| Repositorio / Proyecto | Función e Integración |
|------------------------|-----------------------|
| `Investigaciones/nested-recd` | Implementación teórica de Φ₁–Φ₃ y controles surrogados |
| `Investigaciones/Cardiac_CCTP_Pilot` | Caso de referencia en Cardiología (SDDB) |
| `systemictau` | Paridad analítica τ_s y Systemic Tau Studio |
| `Publicaciones/` | Respaldo para la sección de Evidencia Científica |

Para extraer muestras de la cohorte CCTP:

```bash
python scripts/export_sddb_samples.py --records 38,51
```

## Pruebas y Validación (Tests)

```bash
PYTHONPATH=src pytest -q
```

## Citas Académicas

Le rogamos citar la plataforma de software así como los artículos o preprints correspondientes a su dominio de investigación (e.g., CCTP Zenodo `10.5281/zenodo.21270699`, Síntesis Magna, Foundations).

## Licencia

MIT © 2026 Johel Padilla-Villanueva  
ORCID: [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)

**Aviso de exención de responsabilidad:** Esta plataforma constituye una herramienta orientada a la investigación científica y la docencia. No está concebida, diseñada ni validada como un dispositivo médico, y en ningún caso sus resultados constituyen consejo diagnóstico o de inversión.
