# Systemic Tau Platform

**Paradigma Tau Sistémico: De la Teoría a la Práctica**

Plataforma web educativa y de investigación ([Streamlit](https://streamlit.io)) para el paradigma **Tau Sistémica + RECD** (Reloj Extramental Discreto): fundamentos, matemática, dominios, laboratorio interactivo, ruta de aprendizaje, evidencia y materiales.

> Producto con calidad SaaS educativa premium — no un prototipo de notebook.

[![CI](https://github.com/johelpadilla/systemic-tau-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/johelpadilla/systemic-tau-platform/actions/workflows/ci.yml)

| | |
|--|--|
| **Versión** | 1.0.0 |
| **Licencia** | MIT |
| **Idiomas** | ES (fuente) · EN · FR |
| **Contacto** | johel.padilla@upr.edu |
| **ORCID** | [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931) |
| **Repo** | https://github.com/johelpadilla/systemic-tau-platform |

## Inicio rápido

```bash
git clone https://github.com/johelpadilla/systemic-tau-platform.git
cd systemic-tau-platform
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Lanzar (navegación multipágina con labels i18n)
stp serve
# o: streamlit run app/streamlit_app.py
```

Abrir la URL local (típicamente `http://localhost:8501`).

### CLI de análisis

```bash
stp analyze data/samples/sddb_rr_38_demo.csv \
  --domain cardiology --columns z_rr,z_abs_drr \
  --event 6800 -o report.md --json result.json
```

## Deploy público

Ver **[`docs/DEPLOY.md`](docs/DEPLOY.md)**:

- **Streamlit Community Cloud** → main file: `app/streamlit_app.py`
- **Docker**: `docker build -t stp . && docker run -p 8501:8501 stp`

## Qué incluye v1.0

| Área | Estado |
|------|--------|
| Core: τ_s, RECD, EWS, surrogates, hash | ✅ |
| Breathing + memoria ordinal + TDA Lab | ✅ |
| Catálogo multi-dominio + adapters | ✅ |
| i18n ES / EN / FR (UI + contenidos) | ✅ |
| Disclaimer + privacidad upload + caps Lab | ✅ |
| About & Legal, citas, contacto | ✅ |
| `st.navigation` labels localizados | ✅ |
| CI (pytest + smoke AppTest) | ✅ |
| Docker + config producción | ✅ |

## Seguridad y límites públicos (Lab web)

- CSV ≤ **15 MB**, ≤ **50 000** filas, ≤ **12** columnas numéricas
- Surrogates ≤ **30**
- Uploads: procesados **en sesión**; no se guardan en catálogo ni se reentrenan modelos
- Detalle: página **Acerca de y legal** en la app + `SECURITY.md`

## Idiomas (i18n)

- **Español** fuente (`content/`, `locales/es/ui.json`)
- **English** / **Français**: `locales/{en,fr}/ui.json` + `locales/{en,fr}/content/`
- Selector en la barra lateral en todas las páginas
- Guía de revisión nativa: `docs/I18N_REVIEW.md`

## Documentación

| Doc | Contenido |
|-----|-----------|
| [`docs/SPEC.md`](docs/SPEC.md) | Especificación maestra |
| [`docs/DEPLOY.md`](docs/DEPLOY.md) | Hosting / Docker / Cloud |
| [`docs/DATASETS.md`](docs/DATASETS.md) | Datasets |
| [`docs/LAB_FLOW.md`](docs/LAB_FLOW.md) | Flujo del Laboratorio |
| [`docs/ENGINEERING.md`](docs/ENGINEERING.md) | Stack |
| [`CHANGELOG.md`](CHANGELOG.md) | Historial de versiones |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Cómo contribuir |
| [`SECURITY.md`](SECURITY.md) | Vulnerabilidades |
| [`FREEZE.md`](FREEZE.md) | Snapshot pre-launch |

## Tests

```bash
pytest -q
python scripts/smoke_apptest.py   # 10 páginas × 3 idiomas + entrypoint
```

## Datos de muestra (PhysioNet)

Los CSV `data/samples/sddb_rr_*_demo.csv` son **exports educativos derivados** (RR procesado), no redistribución de ficheros crudos PhysioNet. Cite PhysioNet/SDDB y el paper de dominio. Ver `content/legal/licenses.md`.

## Citas

1. *Systemic Tau Platform* v1.0 (MIT) — este repositorio  
2. Paper/preprint del dominio (p.ej. CCTP Zenodo `10.5281/zenodo.21270699`)  
3. Dataset original  

## Freeze / rollback

- Tag **`v1.0.0-pre-launch-freeze`**: estado antes del paquete de lanzamiento público  
- Tag **`v1.0.0`**: release actual  
- Tarball hermano (opcional): `../systemic-tau-platform-freeze-prelaunch-*.tar.gz`

## Licencia y disclaimer

MIT © 2026 Johel Padilla-Villanueva  

**Disclaimer:** herramienta de investigación y docencia. **No** es dispositivo médico, **no** es diagnóstico clínico, **no** es consejo de inversión.
