# Dominio: Cardiología computacional — pre-FV y SDDB

### Objetivos de aprendizaje
1. Explicar por qué var/AR1 pueden ser ambiguos antes de una FV.
2. Describir el proxy \(X=[z(\mathrm{RR}), z(|\Delta\mathrm{RR}|)]\) y los presets CCTP.
3. Aplicar el protocolo de **lectura dual** a un caso cardio-like o sample SDDB.

**Madurez empírica en v1.0:** ★★★★★ (máxima de la plataforma) — piloto CCTP N=10.

---

## 1. Contexto científico

La **muerte súbita cardíaca** por **fibrilación ventricular (FV)** sigue siendo difícil de anticipar desde el ECG de superficie. Los Holter de la *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) son uno de los pocos recursos públicos con horas de dinámica pre-evento y onset de FV documentado.

El **Cardiac Critical Transitions Protocol (CCTP)** aplica Tau Sistémica y RECD ordinal a series de **intervalos RR** para caracterizar la reorganización relacional de la dinámica de frecuencia cardíaca **antes** de FV espontánea.

**Pregunta guía:** no “¿sube la varianza?”, sino “¿se reorganiza la relación entre el nivel de RR y su variación batido a batido?”.

---

## 2. Por qué las métricas clásicas son insuficientes aquí

En la cohorte CCTP (N=10 registros de alta calidad):

| Hallazgo | Implicación |
|----------|-------------|
| Varianza de RR suele **aumentar** | Firma “tipo CSD” presente |
| AR(1) con frecuencia **disminuye** | CSD ingenuo falla |
| Pacing intermitente / FA en algunos registros | El “ruido” es contexto clínico, no basura a borrar ciegamente |

Interpretar solo var/AR1 produce lecturas confusas o **falsos negativos conceptuales**.

---

## 3. Valor diferencial de τ_s + RECD

| Ingrediente | Rol en CCTP | En el Lab v1.0 |
|-------------|-------------|----------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Multivariado mínimo fisiológicamente motivado | Auto si sube 1 columna; cardio-like lo simula |
| τ_s (W=101, stride=5) | Acoplamiento ordinal nivel–variabilidad | Preset `cardiology` |
| Φ₁–Φ₃ + **excess3** | Estructura simbólica; excess3 primario | Tab RECD + métricas |
| Phase-shuffle | Nulo de dependencia cruzada | Slider n surrogates |
| Signo context-dependent | Reorganización, no dogma de signo | Interpretar Δ + p + contexto |

**Hallazgo clave del piloto (documentado):**  
Δτ_s y Δexcess3 son significativos en la mayoría de registros bajo surrogates, con **concordancia de signo en 8/10** casos, incluso cuando el panel clásico es ambiguo.

---

## 4. Dataset de ejemplo en la plataforma

| Recurso | Función en el Lab |
|---------|-------------------|
| Sample `sddb_rr_38_demo.csv` | Señal fuerte / caso de referencia |
| Sample `sddb_rr_51_demo.csv` | Pacing intermitente — flags de calidad y límites del preset |
| Generador **Cardio-like demo** | Flujo CCTP sin depender de PhysioNet |

Columnas típicas: `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`. Evento: índice de onset de FV (`vfon`) cuando está disponible.

---

## 5. Interpretación guiada (checklist)

1. **Calidad:** ¿hay interpolación excesiva, pacing, artefactos?  
2. **Panel relacional:** τ_s basal vs approach; mean excess3 y Δ.  
3. **Nulos:** p de phase-shuffle para Δτ_s (y, si se calcula, excess3).  
4. **Panel clásico:** var y AR1 — ¿confirman, callan o contradicen?  
5. **Concordancia:** ¿τ_s y excess3 se mueven juntos?  
6. **Frase de cierre acotada:** p.ej. *“Reorganización relacional significativa con panel clásico ambiguo (var↑, AR1↓); no implica dispositivo de alarma clínica.”*

---

## 6. Ejercicio de 20 minutos

1. Lab → **Cardio-like demo** → preset cardiology → Fast, n_surr=8.  
2. Anote en tabla: Δτ_s, mean excess3, Δexcess3, p_surr, var/AR1 cualitativo.  
3. Escriba 4 líneas de interpretación con lectura dual.  
4. (Opcional) Suba sample 38 vs 51 y compare dificultad.

---

## 7. Referencias

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).  
- Goldberger et al., PhysioNet / SDDB.  
- Greenwald (1986) — base del SDDB.  
- En plataforma: **Evidencia** + **Alcance del núcleo** (Ruta de aprendizaje).
