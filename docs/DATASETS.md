# Datasets — Systemic Tau Platform

Guía operativa: **qué bajar, cómo preprocesar, qué meter en el repo**.

---

## Política de datos

| Nivel | Qué incluye | Git |
|-------|-------------|-----|
| **Samples** | Series cortas o agregadas para demo (< 2 MB c/u) | Sí (`data/samples/`) |
| **Processed** | Series limpias listas para análisis | No (script regenera) |
| **Raw** | Descargas originales (PhysioNet, LTER, etc.) | No |

Siempre documentar **licencia de uso** del dataset original y citar DOI.

---

## 1. Cardiología — SDDB (prioridad máxima)

### Fuente
- **Sudden Cardiac Death Holter Database (SDDB)**  
  PhysioNet: https://physionet.org/content/sddb/1.0.0/  
  DOI: 10.13026/C2W306  
- Pipeline ya validado en:  
  `~/grok-safe/Investigaciones/Cardiac_CCTP_Pilot/`

### Cohorte analítica (N=10)
```
30, 31, 32, 35, 36, 38, 45, 47, 50, 51
```

### Preprocess (CCTP)
1. `wfdb.rdann` — preferir `.atr`, fallback `.ari`.
2. RR (ms) = `diff(samples)/fs * 1000` (fs=250).
3. Filtrar `250 < RR < 2000`; interpolar outliers linealmente.
4. Metadata: `n_beats`, `interp_frac`, `cv_rr`, `pacing_detected`.
5. Proxy multivariado:
   ```text
   X = [zscore(RR), zscore(|ΔRR|)]
   ```

### Parámetros paper
| Parámetro | Valor |
|-----------|--------|
| W_τ | 101 beats |
| stride | 5 |
| m | 3 |
| delay | 1 |
| θ₃ | 0.08 |
| high_thresh | 0.65 |
| surrogates | phase-shuffle, n=8 |

### Sample para la plataforma
- Exportar 1–2 registros (p.ej. **38** y **51**) como CSV:
  ```text
  t_beat, rr_ms, abs_drr, z_rr, z_abs_drr, phase
  ```
- Incluir `vfon_index` en sidecar YAML.
- Script: `scripts/export_sddb_samples.py` (lee npz del piloto CCTP).

### Licencia / cita
Goldberger et al. 2000; Greenwald 1986; Padilla CCTP Zenodo 10.5281/zenodo.21270699.

---

## 2. Epidemiología — Dengue Puerto Rico / DengAI

### Fuentes sugeridas
1. **DengAI** (DrivenData) — series semanales de San Juan e Iquitos  
   https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/
2. Datos internos / vigilancia PR (si disponibles bajo NDA) — no commitear PII.
3. Ya existe en ecosistema local:  
   `Gemini/systemictau/data/datos_dengai_completo.csv`

### Preprocess
1. Agregar a **semana epidemiológica** (ISO week).
2. Variables mínimas:
   - `cases` (incidencia)
   - `temp_avg`, `precip`, `humidity` (si hay)
   - opcional: índice de vegetación / Aedes proxy
3. Imputar gaps cortos (≤2 sem) con interpolación; marcar gaps largos.
4. Proxy multivariado ejemplo:
   ```text
   X = [z(cases), z(temp), z(precip)]  # o cases + lagged cases
   ```
5. Anotar ventanas de **brote** (percentil 90 de cases o etiquetas conocidas).

### Sample
- `data/samples/dengue_sj_weekly.csv` (San Juan, ~5–10 años).
- Sidecar: `dengue_sj_meta.yaml` con definición de brotes.

### Cita
DengAI challenge; papers dengue Tau/RECD del autor (preprints 2025–2026).

---

## 3. Neurociencia — CHB-MIT Scalp EEG

### Fuente
- CHB-MIT Scalp EEG Database (PhysioNet)  
  https://physionet.org/content/chbmit/1.0.0/  
  DOI: 10.13026/C2K01R

### Preprocess (v1 simplificado)
1. Seleccionar 1–2 sujetos con crisis bien anotadas (p.ej. chb01).
2. Extraer ventana: **30–60 min pre-ictal + ictal**.
3. Features por canal o por banda (delta/theta/alpha/beta):
   - potencia de banda (Welch), o
   - envelope Hilbert de un canal de referencia.
4. Multivariado: N=4–8 series de bandpower.
5. Downsample temporal a 1–4 Hz efectivo para τ_s (no analizar a 256 Hz crudo en Streamlit).

### Sample
- Por tamaño: **solo extracto procesado** (~50k filas max) o serie sintética “pre-ictal-like”.
- Script download: `scripts/download_chbmit_sample.py` (requiere `wfdb`).

### Licencia
PhysioNet credentialed access — documentar en UI que el usuario debe aceptar ToS.

---

## 4. Ecología — Lagos eutrofizados

### Fuentes
1. **NTL LTER — Lake Mendota** (Wisconsin)  
   https://lter.limnology.wisc.edu/  
   Chlorophyll-a, nutrients, DO, Secchi.
2. Lake Washington / otros LTER con transición documentada.

### Preprocess
1. Series mensuales o semanales de:
   - `chla`, `tp` (fósforo total), `tn`, `do_bottom`, `temp`
2. Alinear estacionalidad (deseasonalize opcional para EWS clásicos; **no** deseasonalize ciegamente para ordinal — documentar ambos modos).
3. Marcar régimen oligotrófico vs eutrófico si hay umbral histórico de Chl-a.

### Sample
- `data/samples/mendota_monthly.csv` (variables clave, ~20–30 años si público).

### Cita
NTL LTER data papers; Scheffer et al. sobre critical transitions en lagos.

---

## 5. Finanzas — S&P 500 (opcional avanzado)

### Fuente
- Stooq / Yahoo Finance: `^GSPC` daily.
- VIX opcional como segunda variable de estrés.

### Preprocess
1. `log_return = log(P_t / P_{t-1})`
2. `realized_vol` = rolling std 21d de returns.
3. Proxy:
   ```text
   X = [z(log_return), z(realized_vol)]
   ```
4. Eventos de régimen: 2008, 2020-COVID, 2022 (para anotación pedagógica).

### Sample
- `data/samples/sp500_daily_sample.csv` (últimos ~5–10 años).

### Disclaimer UI
> Análisis educativo de dinámica de regímenes. **No es consejo de inversión.**

---

## Catálogo YAML (`data/catalog/datasets.yaml`)

```yaml
datasets:
  sddb_rr_38:
    domain: cardiology
    title: "SDDB Record 38 — RR clean"
    path: samples/sddb_rr_38.csv
    maturity: very_high
    license: "PhysioNet + CCTP analysis code"
    variables: [z_rr, z_abs_drr]
    event_col: null
    event_index: null  # fill from meta
    default_params:
      window: 101
      stride: 5
      m: 3
      theta3: 0.08

  dengue_sj:
    domain: epidemiology
    title: "Dengue San Juan weekly"
    path: samples/dengue_sj_weekly.csv
    maturity: high
    license: "DengAI / public challenge"
    variables: [cases_z, temp_z, precip_z]
    default_params:
      window: 13
      stride: 1
      m: 3
      theta3: 0.10
```

---

## Scripts de adquisición

| Script | Función |
|--------|---------|
| `scripts/export_sddb_samples.py` | Desde CCTP npz → CSV sample |
| `scripts/prepare_dengai.py` | DengAI → weekly multivariado |
| `scripts/download_chbmit_sample.py` | EEG extracto |
| `scripts/prepare_mendota.py` | LTER → monthly |
| `scripts/prepare_sp500.py` | Precios → returns/vol |
| `scripts/build_synthetic_demos.py` | Series sintéticas (logístico, acoplados) |

---

## Checklist de calidad por dataset

- [ ] Shape documentado `(T, N)` con N≥2
- [ ] Sin NaN residuales (o máscara explícita)
- [ ] Units y frecuencia temporal
- [ ] Evento de transición (si aplica) con índice
- [ ] Licencia y cita en UI
- [ ] Sample < 2 MB
- [ ] Fingerprint SHA-256 en `datasets.yaml`
