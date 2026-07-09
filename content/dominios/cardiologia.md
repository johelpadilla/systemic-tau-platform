# Dominio: Cardiología computacional — pre-FV y SDDB

## 1. Contexto científico

La **muerte súbita cardíaca** por **fibrilación ventricular (FV)** sigue siendo difícil de anticipar desde el ECG de superficie. Los Holter de la *Sudden Cardiac Death Holter Database* (SDDB, PhysioNet) son uno de los pocos recursos públicos con horas de dinámica pre-evento y onset de FV documentado.

El **Cardiac Critical Transitions Protocol (CCTP)** aplica Tau Sistémica y RECD ordinal a series de **intervalos RR** para caracterizar la reorganización relacional de la dinámica de frecuencia cardíaca **antes** de FV espontánea.

## 2. Por qué las métricas clásicas son insuficientes

En la cohorte CCTP (N=10 registros de alta calidad):

- La **varianza** de RR suele aumentar (firma “tipo CSD”).
- El **AR(1)** con frecuencia **disminuye** — un comportamiento de *anti-persistencia* directamente opuesto a la expectativa ingenua del *critical slowing down*.
- Interpretar solo var/AR1 produce lecturas confusas o falsos negativos conceptuales, dado que las dinámicas previas a la FV no siguen un único atractor, sino que presentan divergencias bruscas.
- Hay **pacing intermitente** y ruido sináptico inherente (con niveles de ruido hasta del 20%). Este ruido no es un mero "error a borrar", sino que el Tau Sistémico demuestra una **invarianza topológica** y robustez que las métricas clásicas no poseen.

## 3. Valor diferencial de τ_s + RECD

| Ingrediente | Rol en CCTP |
|-------------|-------------|
| Proxy \(X = [z(\mathrm{RR}),\, z(\|\Delta\mathrm{RR}\|)]\) | Multivariado mínimo fisiológicamente motivado |
| τ_s (W=101, stride=5) | Acoplamiento ordinal entre nivel y variabilidad batido-a-batido |
| Φ₁–Φ₃ + **excess3** | Descomposición de estructura simbólica; excess3 como primario |
| Phase-shuffle surrogates | Nulo que preserva espectros y rompe dependencia cruzada |
| Signo context-dependent | Reorganización, no “siempre sube la métrica” |

**Hallazgos clave del CCTP (validación empírica):** 
1. Δτ_s y Δexcess3 son significativos bajo surrogates *phase-shuffle* (que destruyen la dependencia cruzada preservando el espectro de frecuencias).
2. Se observó una **tasa de falsos positivos 3.8 veces menor** y una ventana de alerta temprana **2.3 veces mayor** en comparación con el exponente de Lyapunov local y el coeficiente de Pearson.
3. El reloj extramental en el corazón presentó una emergencia espontánea con una **dimensión fractal constante de ≈1.98**.

## 4. Dataset de ejemplo

- **Fuente:** PhysioNet SDDB + RR limpios del repositorio CCTP.
- **Sample plataforma:** registros 38 (señal fuerte) y 51 (pacing intermitente).
- **Columnas:** `rr_ms`, `abs_drr`, `z_rr`, `z_abs_drr`.
- **Evento:** índice de onset de FV (`vfon`) cuando está disponible.

## 5. Interpretación guiada

1. Inspeccionar calidad: `interp_frac`, flags de pacing.
2. Mirar τ_s en ventana basal vs approach (~3 h pre-evento).
3. Mirar mean excess3 y su Δ (no solo Φ₃ binario).
4. Contrastar con var y AR1 (tab EWS).
5. Exigir p de surrogates antes de reclamar “alerta”.

## 6. Referencias

- Padilla-Villanueva — CCTP/SDDB (Zenodo 10.5281/zenodo.21270699).
- Goldberger et al., PhysioNet / SDDB.
- Greenwald (1986) — base del SDDB.
