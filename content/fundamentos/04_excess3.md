# El concepto de “exceso de Nivel 3” (excess3)

### Objetivos de este módulo
1. Definir excess3 como *proxy continuo* de sinergia ordinal irreducible.
2. Explicar por qué en datos reales se prefiere al Φ₃ binario.
3. Interpretar **signos y deltas** sin dogma (“siempre sube”).

---

## 1. Definición

**excess3** es un **proxy continuo de sinergia ordinal irreducible** en una ventana local de símbolos multivariados. Responde a:

> ¿Cuánta estructura conjunta hay **por encima** de lo que explicarían las variables por separado y las interacciones de a pares?

No es un test de causalidad. Es un **medidor de irreductibilidad simbólica** alineado con la ontología del Nivel 3 del RECD.

---

## 2. Construcción (esquema transparente)

Dada la matriz de símbolos \(S \in \{0,\ldots,m!-1\}^{T \times N}\) (Bandt–Pompe):

1. En una ventana de longitud \(w\):
   - Estimar \(H(\pi^1,\ldots,\pi^N)\) (entropía conjunta).
   - Estimar \(\sum_i H(\pi^i)\) (marginales).
   - Estimar MI promedio de pares.
2. Correlación total aproximada: \(TC \approx \sum_i H_i - H_{\mathrm{joint}}\).
3. Restar una contribución pairwise (heurística transparente) → **sinergia residual**.
4. (Opcional) Añadir **joint surprise**: configuraciones conjuntas más frecuentes de lo esperado bajo independencia.
5. Combinar (p.ej. \(0.6\cdot\mathrm{syn} + 0.4\cdot\mathrm{surprise}\)) → **excess3(t)**.

La versión binaria del Nivel 3 es:

\[
\Phi_3(t) = \mathbf{1}\{\mathrm{excess3}(t) > \theta_3\}
\]

**Pedagogía:** excess3 es el *termómetro*; Φ₃ es un *termostato* con umbral. En series ruidosas el termómetro es más fiel.

---

## 3. Por qué preferir el continuo en datos reales (lección CCTP)

En el piloto cardíaco CCTP (RR ruidoso, N=10 registros SDDB):

- excess3 basal ≈ 0.30–0.35; en approach puede subir hacia ~0.43 (ej. registro 38).
- Con umbrales altos, la **tasa** de “alto Nivel 3” puede quedarse en cero aunque el **delta de excess3** sea altamente significativo.
- Por eso la métrica primaria de paper es **mean_excess3** (y su Δ), no solo `high_level3_rate`.

| Situación | Usar |
|-----------|------|
| Series sintéticas limpias | Φ₃ binario + excess3 |
| Fisiología / campo ruidoso | **excess3 continuo** como primario |
| Reportes / docencia | ambos + p de surrogates + contexto |

---

## 4. Interpretación de signos y deltas

Al igual que τ_s, el **signo de Δexcess3** es **context-dependent**:

| Patrón | Lectura posible (hipótesis, no dogma) |
|--------|----------------------------------------|
| excess3 ↑ hacia el evento | Emergencia de configuración conjunta / rigidificación sinérgica |
| excess3 ↓ hacia el evento | Colapso o simplificación de la estructura sinérgica (p.ej. ciertos regímenes paced o terminales) |
| Δ grande, p_surr bajo | Cambio difícil de explicar con nulo de independencia cruzada |
| Δ grande, p_surr alto | No reclamar “alerta”; revisar W, m, calidad, dominio |

Lo científicamente relevante en CCTP no es “siempre sube”, sino:

1. **Magnitud del cambio** basal → approach.  
2. **Concordancia de signo** con Δτ_s (8/10 en el piloto).  
3. **Significancia** frente a phase-shuffle surrogates.

---

## 5. Analogía

Si Φ₁ es “cantar la misma nota” y Φ₂ es “mantener un dúo estable”, excess3 es el residual de una **polifonía** que no se puede factorizar en solos ni en dúos. Cuando ese residual cambia de forma sostenida, el sistema está reescribiendo su **gramática conjunta**.

---

## 6. Relación con otros enfoques

| Enfoque | Cercanía a excess3 | Diferencia clave |
|---------|-------------------|------------------|
| Transfer Entropy | Media | TE es direccional; excess3 es sinergia conjunta orientada a RECD |
| Total correlation / PID | Alta | excess3 es un proxy quirúrgico, no PID completa |
| TDA (Betti) | Complementaria | TDA ve topología del cloud; excess3 ve sinergia simbólica temporal |
| Features ML | Baja | excess3 es interpretable y falsable con surrogates |

---

## 7. Parámetros recomendados (v1.0)

| Dominio | θ₃ | Notas |
|---------|-----|-------|
| Cardio RR | 0.08 | recalibrado CCTP |
| Dengue semanal | 0.10 | default teórico |
| Sintéticos | 0.10 | demos Lab |
| EEG bandpower | 0.08–0.12 | explorar preprocess |

### Ejercicio en el Lab
1. Ejecute **cardio-like** en modo fast.  
2. Anote Δτ_s, mean excess3, Δexcess3, p_surr.  
3. Abra el tab EWS: ¿var y AR1 cuentan la misma historia?  
4. Escriba en una frase: *“El panel relacional dice X; el clásico dice Y; la conclusión es Z.”*
