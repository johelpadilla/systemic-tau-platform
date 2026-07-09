# Systemic Tau Platform — Especificación de Producto v1.0

**Nombre de producto:** *Systemic Tau Platform*  
**Tagline:** *Paradigma Tau Sistémico: De la Teoría a la Práctica*  
**Framework:** Streamlit multipágina  
**Audiencia:** intermedio–avanzado · académicos · investigadores · posgrado  
**Estado:** diseño + scaffold v1.0 (Julio 2026)

---

## 1. Visión y posicionamiento

La plataforma es un **producto SaaS educativo/científico premium** que unifica:

| Capa | Contenido |
|------|-----------|
| **Teoría** | Tau Sistémica, RECD (Φ₁–Φ₃), exceso de Nivel 3, ontología Polo / tiempo extramental |
| **Matemática** | Bandt–Pompe, τ_s, Breathing Window, TDA/Betti, memoria ordinal, surrogates |
| **Evidencia** | CCTP/SDDB (VF), dengue PR, EEG, lagos, finanzas |
| **Laboratorio** | Análisis interactivo + reportes reproducibles + comparación EWS clásicos |

**Principio de marca:** no es un prototipo de notebook; es una **plataforma de investigación y docencia** con calidad de curso universitario y de consultoría metodológica.

### 1.1 Públicos

1. **Intermedio–avanzado** — ya conoce Tau/RECD a nivel conceptual; necesita rigor, conexiones ontológicas y experimentación.
2. **Académicos / posgrado** — integran el paradigma en papers, tesis o currículos de sistemas complejos, epidemiología, cardiología computacional o ciencia de datos de sistemas vivos.

### 1.2 Tono

Riguroso, elegante, académico-moderno. Precisión terminológica + pedagogía. Nunca condescendiente ni “pop-science”.

### 1.3 Diferenciador comercial

| Competidor típico | Systemic Tau Platform |
|-------------------|------------------------|
| Dashboards de EWS clásicos (var, AR1) | τ_s + RECD ordinal anidado |
| Cajas negras ML | Métricas interpretables + surrogates |
| Papers PDF estáticos | Lab interactivo + reportes con hash de reproducibilidad |
| Studio de análisis crudo | Narrativa pedagógica + learning path + planes SaaS |

---

## 2. Arquitectura de carpetas y archivos

```text
systemic-tau-platform/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .streamlit/config.toml
├── .gitignore
│
├── app/                              # Capa Streamlit (UI)
│   ├── Home.py                       # Entry point (streamlit multipage root)
│   ├── pages/
│   │   ├── 1_Fundamentos.py
│   │   ├── 2_Matematica.py
│   │   ├── 3_Dominios.py             # Hub de dominios
│   │   ├── 3a_Cardiologia.py
│   │   ├── 3b_Epidemiologia.py
│   │   ├── 3c_Neurociencia.py
│   │   ├── 3d_Ecologia.py
│   │   ├── 3e_Finanzas.py
│   │   ├── 4_Laboratorio.py
│   │   ├── 5_Ruta_Aprendizaje.py
│   │   ├── 6_Evidencia.py
│   │   ├── 7_Docencia.py
│   │   └── 8_Planes.py
│   ├── components/                   # Widgets reutilizables
│   │   ├── hero.py
│   │   ├── domain_cards.py
│   │   ├── metric_cards.py
│   │   ├── glossary_widget.py
│   │   ├── plot_panel.py
│   │   ├── parameter_sidebar.py
│   │   └── report_download.py
│   └── assets/
│       ├── css/custom.css
│       ├── images/
│       └── icons/
│
├── src/stp/                          # Paquete Python (lógica, sin UI)
│   ├── __init__.py
│   ├── cli.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py               # Pydantic settings
│   │   ├── theme.py
│   │   └── domains.yaml
│   ├── core/                         # Matemática central
│   │   ├── __init__.py
│   │   ├── ordinal.py                # Bandt–Pompe
│   │   ├── tau_s.py                  # Systemic Tau
│   │   ├── recd_levels.py            # Φ₁, Φ₂, Φ₃, excess3
│   │   ├── breathing_window.py
│   │   ├── tda_betti.py              # Tier 4 (opcional)
│   │   ├── ordinal_memory.py         # TE simbólica / MI rangos
│   │   ├── surrogates.py             # IAAFT / phase-shuffle
│   │   ├── ews_classical.py          # var, AR1, DFA (comparación)
│   │   └── reproducibility.py        # hash de análisis
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── series_plots.py
│   │   ├── recd_plots.py
│   │   ├── ews_comparison.py
│   │   ├── domain_figures.py
│   │   └── style.py                  # Plotly theme institucional
│   ├── domains/
│   │   ├── __init__.py
│   │   ├── base.py                   # DomainAdapter ABC
│   │   ├── cardiology.py             # SDDB / RR
│   │   ├── epidemiology.py           # Dengue PR
│   │   ├── neuroscience.py           # CHB-MIT
│   │   ├── ecology.py                # Lake Mendota / LTER
│   │   └── finance.py                # S&P 500
│   ├── education/
│   │   ├── __init__.py
│   │   ├── content_loader.py         # Markdown → HTML/Streamlit
│   │   ├── glossary.py
│   │   ├── learning_path.py
│   │   └── faq.py
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── markdown_report.py
│   │   ├── pdf_report.py             # reportlab
│   │   └── templates/
│   │       ├── academic.md.j2
│   │       └── institutional.md.j2
│   └── data/
│       ├── __init__.py
│       ├── loaders.py
│       ├── preprocess.py
│       └── catalog.py
│
├── content/                          # Contenido textual (Markdown)
│   ├── fundamentos/
│   ├── matematica/
│   ├── dominios/
│   ├── learning/
│   ├── evidencia/
│   ├── docencia/
│   └── legal/
│
├── data/
│   ├── catalog/datasets.yaml
│   ├── samples/                      # Datos demo pequeños (git-tracked)
│   ├── raw/                          # No commitear
│   └── processed/
│
├── notebooks/                        # Jupyter para docencia
├── scripts/                          # Download & preprocess
├── tests/
├── docs/
│   ├── SPEC.md                       # Este documento
│   ├── ARCHITECTURE.md
│   ├── DATASETS.md
│   ├── LAB_FLOW.md
│   └── ENGINEERING.md
└── reports_out/                      # Salida de reportes del Lab
```

### 2.1 Principios de modularidad

1. **UI nunca calcula** — las páginas de Streamlit solo orquestan; la matemática vive en `src/stp/core/`.
2. **Dominios = adapters** — cada dominio implementa `DomainAdapter` (carga, preprocess, interpretación, refs).
3. **Contenido desacoplado** — Markdown en `content/`; la UI no hardcodea párrafos largos.
4. **Wrappers opcionales** — si `systemictau` o `nested-recd` están instalados, se usan; si no, cae a implementaciones puras en `stp.core`.
5. **Cache en el borde** — `@st.cache_data` / `@st.cache_resource` solo en la capa `app/`, no dentro del core.

---

## 3. Diseño detallado por página

### Paleta institucional

| Token | Hex | Uso |
|-------|-----|-----|
| `navy` | `#0D4F6B` | Primario, headers |
| `deep` | `#1A2332` | Texto |
| `teal` | `#1A8A8A` | Acentos, métricas positivas |
| `purple` | `#5B4B8A` | Nivel 3 / sinergia |
| `sand` | `#F4F1EA` | Fondos secundarios |
| `alert` | `#C45C26` | Transiciones / warnings |

Tipografía: Inter (web) / system sans en Streamlit. Figuras Plotly con template `stp_institutional`.

---

### 3.0 Home (`app/Home.py`)

**Objetivo:** primera impresión premium + routing por dominio de interés.

| Bloque | Componentes Streamlit | Notas |
|--------|----------------------|-------|
| Hero | `st.markdown` + CSS custom, logo | Título, tagline, badge DOI Zenodo |
| Value props | 3 `st.columns` con iconos | “Ordinal”, “Multiescala”, “Falsable” |
| Domain selector | `st.selectbox` o cards clickeables | Dengue · Cardio · Epilepsia · Lagos · Finanzas |
| Accesos rápidos | `st.page_link` / botones | Fundamentos, Lab, CCTP |
| Métricas sociales | `st.metric` | N papers, N dominios, N registros SDDB |
| Planes teaser | expander o strip inferior | Free / Academic / Pro |

**Estado de sesión:** `st.session_state["domain_interest"]`.

---

### 3.1 Fundamentos (`1_Fundamentos.py`)

**Layout:** sidebar TOC + main content con tabs o anchors.

| Subsección | UI | Contenido fuente |
|------------|-----|------------------|
| ¿Qué es Tau Sistémica? | markdown + diagrama conceptual | `content/fundamentos/01_tau.md` |
| Límites de EWS clásicos | comparación var/AR1 vs τ_s (demo sintética) | `02_ews_limits.md` |
| RECD Φ₁–Φ₃ | tabs por nivel + analogía muñecas rusas | `03_recd_levels.md` |
| excess3 | fórmula + interpretación | `04_excess3.md` |
| CSD y transiciones críticas | markdown + plot logístico demo | `05_csd.md` |
| Filosofía (Polo) | expander elegante, no denso | `06_filosofia.md` |

**Componentes:** `glossary_widget`, mini-plots sintéticos (`st.plotly_chart`), `st.latex`.

---

### 3.2 Matemática (`2_Matematica.py`)

| Módulo | UI | Interactividad |
|--------|-----|----------------|
| Bandt–Pompe | explicación + selector m, delay | Generar símbolos sobre serie demo |
| Cálculo τ_s | algoritmo paso a paso | Ventana W, stride |
| Breathing Window | animación/slider de W(t) | Comparar W fija vs adaptativa |
| TDA + Betti | diagrama de persistencia (si `tda` extra) | Toggle Fast/Full |
| Memoria ordinal | TE / MI de rangos | Heatmap lags |
| Surrogates | IAAFT vs phase-shuffle | Histograma nulo vs observado |

**Modos:** radio `Fast` (sin TDA, n_surr=8) / `Full` (TDA + n_surr≥50).

---

### 3.3 Dominios (`3_Dominios.py` + 3a–3e)

Cada página de dominio sigue el **mismo template pedagógico**:

```text
1. Contexto científico          (markdown)
2. Por qué fallan EWS clásicos  (markdown + cita)
3. Valor diferencial τ_s+RECD   (markdown + diagrama)
4. Dataset de ejemplo           (tabla + descarga)
5. Análisis interactivo         (Lab embebido con defaults de dominio)
6. Interpretación guiada        (expanders por métrica)
7. Referencias clave            (bib / DOI)
```

| Dominio | Page | Madurez | Dataset default |
|---------|------|---------|-----------------|
| Cardiología | `3a_` | Muy alto | SDDB RR clean (N=10) |
| Epidemiología | `3b_` | Alto | Dengue PR / DengAI sample |
| Neurociencia | `3c_` | Medio-Alto | CHB-MIT extracto o sintético |
| Ecología | `3d_` | Medio | Lake Mendota / demo eutrofización |
| Finanzas | `3e_` | Medio | S&P 500 daily sample |

---

### 3.4 Laboratorio Interactivo (`4_Laboratorio.py`)

Ver **LAB_FLOW.md** para el flujo completo. Resumen UI:

| Paso | Widgets |
|------|---------|
| 1. Datos | upload CSV / elegir sample / dominio |
| 2. Config | columnas, W, m, delay, modo Fast/Full |
| 3. Ejecutar | botón + progress bar |
| 4. Resultados | tabs: Series · τ_s · RECD · EWS · TDA · Surrogates |
| 5. Export | PDF / Markdown / JSON + hash |

---

### 3.5 Ruta de Aprendizaje (`5_Ruta_Aprendizaje.py`)

- Timeline Básico → Intermedio → Avanzado (`streamlit-extras` steppers o custom HTML).
- Artículos ordenados con checkboxes de progreso (`st.session_state`).
- Glosario searchable (`st.text_input` + filtro).
- FAQ con `st.expander` profundos.

---

### 3.6 Evidencia (`6_Evidencia.py`)

- Cards de preprints/papers (título, DOI, abstract corto, dominio).
- Tabla de estudios de caso validados (CCTP batch summary).
- Matriz comparativa: ML · TDA puro · TE clásico · τ_s+RECD.

---

### 3.7 Docencia (`7_Docencia.py`)

- Packs descargables (PDF slides outline, notebooks).
- Licencias Academic vs Commercial.
- Syllabus sugerido (4–8 semanas).

---

### 3.8 Planes (`8_Planes.py`)

| Plan | Precio (placeholder) | Features |
|------|----------------------|----------|
| **Free** | $0 | Samples, Fundamentos, Lab limitado (Fast, sin PDF branding) |
| **Academic** | $0 / verificación .edu | Full Lab, notebooks, sin watermark institucional |
| **Professional** | SaaS | Reportes branding, API futura, n_surr alto |
| **Institutional** | Cotización | SSO, multi-usuario, white-label, curricula |

v1.0: todos los planes UI-visibles; gates suaves (sin backend de pagos).

---

## 4. Flujo del Laboratorio Interactivo

```text
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐
│ 1. INGESTA  │───▶│ 2. SCHEMA    │───▶│ 3. PREPROCESS   │
│ CSV/sample  │    │ cols, time   │    │ z-score, clean  │
└─────────────┘    └──────────────┘    └────────┬────────┘
                                                 │
┌─────────────┐    ┌──────────────┐    ┌────────▼────────┐
│ 6. EXPORT   │◀───│ 5. VIZ       │◀───│ 4. PIPELINE     │
│ PDF/MD/JSON │    │ Plotly tabs  │    │ τ_s+RECD+EWS…   │
└─────────────┘    └──────────────┘    └─────────────────┘
```

### 4.1 Pipeline de análisis (orden fijo)

1. Validar shape `(T, N)` con `N ≥ 2` (multivariado mínimo).
2. Preprocess dominio-específico (p.ej. RR clean flags).
3. **τ_s** sliding window (`W`, stride) → serie + por módulo.
4. **RECD levels** Φ₁, Φ₂, Φ₃, excess3 (m, delay, d_persist, θ₃).
5. **Weighted RECD** α(λ) si hay τ_s alineado.
6. **EWS clásicos** (var, AR1, opcional DFA) por columna o proxy.
7. **Surrogates** phase-shuffle / IAAFT (n según modo).
8. **TDA** (solo Full): Betti-0/1 en cloud de símbolos o delay embedding.
9. **Memoria ordinal** (opcional): MI/TE simbólica.
10. **Repro hash** = SHA-256 de (params + data fingerprint + lib versions).

### 4.2 Modos

| Modo | n_surr | TDA | Memoria | Tiempo típico (T=5k, N=3) |
|------|--------|-----|---------|---------------------------|
| Fast | 8 | No | No | < 5 s |
| Full | 50+ | Sí | Sí | 30–120 s |

### 4.3 Salidas del Lab

- Figuras Plotly (τ_s, excess3, contribuciones Φ, comparación EWS).
- Tabla de métricas basales vs “approach” (si hay evento anotado).
- JSON de resultados + `repro_hash`.
- Reporte Markdown/PDF con branding (plan Professional+).

---

## 5. Datasets concretos

Ver `docs/DATASETS.md`. Resumen:

| Dominio | Fuente | Preprocess | Sample en repo |
|---------|--------|------------|----------------|
| Cardio | PhysioNet SDDB + `data/rr_*_clean.npz` CCTP | RR 250–2000 ms, X=[z(RR), z(\|ΔRR\|)] | Sí (subconjunto) |
| Dengue | DengAI / PR surveillance | weekly incidence + climate covariates | Sample CSV |
| EEG | CHB-MIT PhysioNet | bandpower / envelope multi-canal | Sintético + script download |
| Lagos | NTL LTER Mendota | Chl-a, DO, nutrients | Sample monthly |
| Finanzas | Yahoo / Stooq S&P500 | log-returns, realized vol | Sample daily |

---

## 6. Librerías y prácticas de ingeniería

Ver `docs/ENGINEERING.md`. Highlights:

- **Core:** numpy, scipy, numba, pandas, pydantic
- **UI:** streamlit, streamlit-extras, plotly
- **Reports:** reportlab (+ weasyprint opcional)
- **Scientific optional:** systemictau, nested-recd, ripser, wfdb
- **Tests:** pytest + smoke tests de pipeline
- **Cache:** st.cache_data en loaders y análisis; cache_resource en modelos pesados
- **Versionado:** semver; cada reporte imprime `stp.__version__` + hash

---

## 7. Conexión entre dominios (tesis unificadora)

El mismo fenómeno — **reorganización relacional ordinal** previa a una transición crítica — aparece en:

| Sistema | Variables proxy | Transición | Firma τ_s / excess3 |
|---------|-----------------|------------|---------------------|
| Corazón | RR, \|ΔRR\| | → VF | Δτ_s y Δexcess3 significativos (signo context-dependent) |
| Dengue | incidencia, clima, vector | → brote / hiper-persistencia | Aumento de acoplamiento ordinal |
| EEG | canales / bandas | → crisis | Colapso de diversidad ordinal → sinergia |
| Lago | Chl-a, nutrientes, DO | oligo → eutrófico | Pérdida de resiliencia ordinal |
| Mercado | retornos, vol | régimen de volatilidad | Sincronización de patrones de rango |

**Analogía pedagógica maestra:**  
> Antes de que el sistema “cambie de ley”, las partes dejan de moverse de forma independiente y empiezan a **co-escribir el mismo patrón ordinal**. Ese “ponerse de acuerdo en el orden” es lo que miden Φ₁–Φ₃; el reloj RECD avanza más cuando esa co-escritura se vuelve **irreducible** (Nivel 3).

---

## 8. Integración con investigación existente

| Recurso local | Uso en plataforma |
|---------------|-------------------|
| `Investigaciones/nested-recd` | Core Φ₁–Φ₃, surrogates |
| `Investigaciones/Cardiac_CCTP_Pilot` | Dominio cardio, figures, batch summary |
| `Investigaciones/Conversacion_Naturaleza_Tiempo` | Fundamentos RECD anidado |
| `systemictau` package | τ_s, accumulate_time, studio patterns |
| `Publicaciones/` | Sección Evidencia (lista DOI/preprints) |

---

## 9. Roadmap de implementación

| Fase | Entrega | Criterio de hecho |
|------|---------|-------------------|
| **P0** | Scaffold + Home + Fundamentos content | App corre; lectura completa Fundamentos |
| **P1** | Core τ_s + RECD + Lab Fast | Análisis demo end-to-end |
| **P2** | Dominio Cardiología + samples | CCTP-like plots en UI |
| **P3** | Dengue + reportes PDF | Export con hash |
| **P4** | Surrogates + EWS compare + Learning path | Paridad pedagógica |
| **P5** | TDA Full, EEG, Ecology, Finance | Cobertura multi-dominio |
| **P6** | Planes / branding / API stub | Listo comercialización |

---

## 10. Criterios de calidad (Definition of Done v1.0)

- [ ] Navegación completa 8 secciones sin errores.
- [ ] Fundamentos + Matemática con contenido peer-reviewable.
- [ ] Lab Fast ejecuta en <10 s sobre sample cardio.
- [ ] Cada análisis genera `repro_hash` estable.
- [ ] Al menos 2 dominios con dataset real sampleado.
- [ ] Reporte Markdown descargable.
- [ ] Tests smoke del core ≥ 80% de funciones públicas.
- [ ] Look & feel premium (paleta, tipografía, sin “demo genérica”).
