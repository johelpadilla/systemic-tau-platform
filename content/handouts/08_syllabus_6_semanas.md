# Systemic Tau Platform — Syllabus 6 semanas

**Competencia de salida:** definir, calcular, comparar, nular y documentar un análisis τ_s + RECD, acotando la conclusión frente a EWS clásicas y a la madurez del dominio.

---

## Semanas

| Semana | Tema | Actividad Lab | Ancla en la app |
|--------|------|---------------|-----------------|
| 1 | EWS clásicas y límites | var/AR1 en sintético; 1 pág. crítica | Fundamentos · EWS |
| 2 | Bandt–Pompe y τ_s | Sandbox m=3; logísticos acoplados; hash | Matemática + Lab |
| 3 | RECD y excess3 | Panel RECD; por qué el continuo | Fundamentos 3–4 |
| 4 | Cardiología CCTP | RR-38/51 o cardio-like; lectura dual | Dominios + Evidencia |
| 5 | Transferencia de dominio | Elegir **uno**: dengue, ecología, clima, educación o sueño | Dominios + Lab |
| 6 | Surrogates, reportes, ética | Export MD+JSON+Methods; límites; peer review con rúbrica | Lab + Materiales |

---

## Rúbrica Lab (6 criterios × 0–2 = 12)

1. Pregunta científica  
2. Parámetros y preset de dominio  
3. Δτ_s · excess3 · p_surr  
4. EWS clásicas en paralelo  
5. Conclusión acotada  
6. Hash de la corrida  

**Umbral sugerido de aprobación de la práctica:** ≥ 9/12.

---

## Datasets demo (catálogo)

**Controles**

- `synthetic_coupled_logistic` — positivo  
- `synthetic_ar_noise` — casi-nulo  

**Ancla**

- `sddb_rr_38_demo`, `sddb_rr_51_demo` (si están en `data/samples/`)  
- `cardiac_like_demo`  

**Transferencia / pedagogía**

- `dengue_like_demo`, `eeg_like_demo`, `ecology_like_demo`  
- `climate_drought_demo`, `education_cohort_demo`  
- `social_polarization_demo`, `sleep_fragmentation_demo`  
- `finance_like_demo` (solo transferencia metodológica)

---

## Materiales descargables (página Materiales)

- Guía rápida  
- Manual de usuario  
- Teoría τ_s + RECD  
- Matemática práctica  
- Cheat-sheet del Lab  
- Lectura dual  
- Checklist de análisis  
- FAQ  
- Glosario  
- Ética y alcance  
- Pack estudiante / Pack docente  

---

## CLI

```bash
stp analyze data.csv --domain cardiology -o report.md --json result.json
stp serve
```

---

## Evaluación formativa sugerida

| Momento | Producto |
|---------|----------|
| Semana 2 | Captura Lab + hash de logísticos vs AR |
| Semana 4 | Informe dual 2–3 págs. cardio |
| Semana 5 | Mini-informe de transferencia (1 dominio) |
| Semana 6 | Portfolio: MD + JSON + Methods + checklist firmado |

---

## Notas para el docente

- Priorice **pedagogía y falsación** sobre promesas de producto.  
- No use la demo de finanzas o social como promesa predictiva.  
- El piloto CCTP es el ancla; el resto es sandbox con ground truth de diseño.  
- Dedique tiempo explícito a **controles** (semana 2) antes de dominios aplicados.

---

*Syllabus STP v1.0 · uso académico con citación*
