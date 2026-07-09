# Guía de lectura dual — Relacional vs EWS clásicas

**Audiencia:** estudiantes en Lab y autores de informes cortos  
**Regla de oro:** un solo panel no basta para una conclusión de sistemas

---

## 1. Qué es la lectura dual

Presentar **en paralelo**:

| Columna A — Relacional (núcleo STP) | Columna B — Clásica (control) |
|------------------------------------|------------------------------|
| τ_s(t), Δτ_s | Varianza en ventana |
| excess3, Δexcess3, Φ₃ | AR(1) / autocorrelación |
| p_surr (phase-shuffle / IAAFT) | Otras EWS univariadas si aplica |
| Evento y diseño pre/post | Mismo evento / misma W si es posible |

La plataforma calcula ambos en el Lab. La **interpretación humana** declara concordancia o discordancia.

---

## 2. Cuatro patrones típicos (plantilla)

### A. Concordancia fuerte

- Relacional: |Δ| notable + p_surr bajo  
- Clásico: var y/o AR1 también se mueven hacia el evento  

**Texto modelo:**  
*“Tanto el panel relacional como el clásico señalan cambio hacia t=…; el nulo phase-shuffle no explica el Δτ_s (p=…). Interpretación acotada al diseño …”*

### B. Relacional sí, clásico ambiguo

- Relacional: señal  
- Clásico: plano o contradictorio  

**Texto modelo:**  
*“El panel univariado es ambiguo; la reorganización ordinal (Δτ_s=…, Δexcess3=…) es el hallazgo principal bajo nulo de independencia cruzada. Esto es coherente con transiciones multivariadas donde CSD univariado falla.”*

### C. Clásico sí, relacional no

- Var/AR1 suben; τ_s estable; p_surr alto  

**Texto modelo:**  
*“Hay enlentecimiento/amplitud univariada sin evidencia de reorganización ordinal cruzada en este diseño. No se reclama detección relacional.”*

### D. Casi-nulo (control)

- Como en `synthetic_ar_noise`  

**Texto modelo:**  
*“Control: |Δτ_s| pequeño; compatible con ausencia de transición diseñada.”*

---

## 3. Plantilla de párrafo para entregas (copiar y rellenar)

```
Diseño. Serie T×N = …×…; dominio = …; W=…, stride=…, m=…;
evento en t=… (o partición mitad/mitad exploratoria).
Surrogates: método=…, n=…, seed=….

Hallazgos relacionales. Δτ_s = …; mean_excess3 = …; Δexcess3 = …;
p_surr(τ_s) = ….

Hallazgos clásicos. Δvar ≈ …; comportamiento AR1: ….

Lectura dual. Concordancia / discordancia: ….
Alcance. Madurez del dominio: …; límites: no uso clínico/operativo.
Reproducibilidad. repro_hash = ….
```

---

## 4. Errores de lectura dual

| Error | Por qué falla |
|-------|----------------|
| Ocultar el panel clásico si “estorba” | Selección de resultados |
| Declarar “predicción” por un p bajo | p ≠ valor predictivo externo |
| Mezclar W distintas entre paneles sin decirlo | Incomparabilidad |
| Usar demo sintético como evidencia de dominio real | Categoría de claim incorrecta |
| Ignorar signo context-dependent | Δ negativo puede ser reorganización real |

---

## 5. Rúbrica rápida (0–2 cada ítem)

1. Pregunta científica explícita  
2. Diseño (evento / partición) declarado  
3. Métricas relacionales completas  
4. Panel clásico reportado  
5. Nulos y n_surr  
6. Conclusión acotada + hash  

**Máximo 12.** Una entrega de Lab decente ≥ 9.

---

*Guía de lectura dual STP · pegar en el LMS junto al syllabus.*
