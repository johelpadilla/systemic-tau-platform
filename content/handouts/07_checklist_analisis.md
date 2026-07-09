# Checklist de análisis — entrega Lab / informe corto

Marque cada ítem antes de enviar. Si un ítem no aplica, escriba **N/A** y justifique en una línea.

---

## A. Pregunta y alcance

- [ ] Pregunta científica en una frase (reorganización relacional, no “predecir X”)  
- [ ] Dominio y **madurez empírica** declarados  
- [ ] Se distingue demo sintético vs datos reales  
- [ ] Límites éticos (no clínico / no operativo) mencionados  

## B. Datos

- [ ] Fuente (catálogo ID / CSV / PhysioNet / …)  
- [ ] Dimensiones T × N  
- [ ] Variables usadas y por qué (adapter / teoría)  
- [ ] Preprocess (z-score, proxy RR–|ΔRR|, missing, …)  
- [ ] Licencia / ToS de terceros respetada  

## C. Diseño

- [ ] Evento marcado **o** partición exploratoria declarada  
- [ ] Preset de dominio o justificación de W, stride, m, θ₃  
- [ ] Seed de surrogates fijada  
- [ ] Modo fast/full y n_surr acordes al claim  

## D. Resultados numéricos

- [ ] Δτ_s (signo + magnitud)  
- [ ] mean_excess3 y Δexcess3  
- [ ] p_surr y método (phase-shuffle / IAAFT)  
- [ ] Al menos un EWS clásico en paralelo  
- [ ] Figuras: series+evento, τ_s, RECD/excess3, EWS  

## E. Interpretación

- [ ] Lectura dual (concordancia / discordancia)  
- [ ] No se sobreinterpreta Φ₃ si excess3 es la señal  
- [ ] Signo context-dependent considerado  
- [ ] Comparación con control (AR o basal) si aplica  

## F. Reproducibilidad y entrega

- [ ] `repro_hash` copiado  
- [ ] Export Markdown  
- [ ] Export JSON (si el curso lo pide)  
- [ ] Párrafo Methods  
- [ ] Citas: software + dataset + paper de dominio  

---

## Autoevaluación (opcional)

| Criterio (0–2) | Nota |
|----------------|------|
| Pregunta y alcance | |
| Datos y diseño | |
| Métricas + nulos | |
| Lectura dual | |
| Escritura acotada | |
| Hash / exports | |
| **Total /12** | |

---

*Checklist STP v1.0 · imprimible*
