# El concepto de “exceso de Nivel 3” (excess3)

## Definición

**excess3** es un **proxy continuo de sinergia ordinal irreducible** en una ventana local de símbolos multivariados. Responde a la pregunta:

> ¿Cuánta estructura conjunta hay **por encima** de lo que explicarían las variables por separado y las interacciones de a pares?

No es un test de causalidad. Es un **medidor de irreductibilidad simbólica** alineado con la ontología del Nivel 3 del RECD.

## Construcción (esquema)

Dada la matriz de símbolos \(S \in \{0,\ldots,m!-1\}^{T \times N}\) (Bandt–Pompe):

1. En una ventana de longitud \(w\):
   - Estimar \(H(\pi^1,\ldots,\pi^N)\) (entropía conjunta).
   - Estimar \(\sum_i H(\pi^i)\) (marginales).
   - Estimar MI promedio de pares.
2. Correlación total aproximada: \(TC \approx \sum_i H_i - H_{\mathrm{joint}}\).
3. Restar una contribución pairwise (heurística transparente) → **sinergia residual**.
4. (Opcional) Añadir **joint surprise**: configuraciones conjuntas más frecuentes de lo esperado bajo independencia de marginales.
5. Combinar (p.ej. \(0.6\cdot\mathrm{syn} + 0.4\cdot\mathrm{surprise}\)) → **excess3(t)**.

La versión binaria del Nivel 3 es simplemente:

\[
\Phi_3(t) = \mathbf{1}\{\mathrm{excess3}(t) > \theta_3\}
\]

## Por qué preferir el continuo en datos reales

En el piloto cardíaco CCTP (RR ruidoso, N=10 registros SDDB):

- excess3 basal ≈ 0.30–0.35; en approach puede subir hacia ~0.43 (ej. registro 38).
- Con umbrales altos, la **tasa** de “alto Nivel 3” puede quedarse en cero aunque el **delta de excess3** sea altamente significativo.
- Por eso la métrica primaria de paper es **mean_excess3** (y su Δ), no solo `high_level3_rate`.

**Regla pedagógica de la plataforma:**

| Situación | Usar |
|-----------|------|
| Series sintéticas limpias | Φ₃ binario + excess3 |
| Fisiología / campo ruidoso | **excess3 continuo** como primario |
| Reportes institucionales | ambos + intervalo / p de surrogates |

## Interpretación de signos y deltas

Al igual que τ_s, el **signo de Δexcess3** es **context-dependent**:

- Un aumento puede indicar **emergencia de configuración conjunta** pre-transición.
- Una disminución puede indicar **colapso o simplificación** de la estructura sinérgica (p.ej. regímenes paced o terminales distintos).

Lo científicamente relevante en CCTP no es “siempre sube”, sino:

1. **Magnitud del cambio** basal → approach.
2. **Concordancia de signo** con Δτ_s.
3. **Significancia** frente a phase-shuffle surrogates (que preservan espectros univariados y rompen dependencia cruzada).

## Analogía

Si Φ₁ es “cantar la misma nota” y Φ₂ es “mantener un dúo estable”, excess3 es el residual de una **polifonía** que no se puede factorizar en solos ni en dúos. Cuando ese residual cambia de forma sostenida, el sistema está reescribiendo su **gramática conjunta**.

## Relación con otros enfoques

| Enfoque | Cercanía a excess3 | Diferencia |
|---------|-------------------|------------|
| Transfer Entropy clásica | Media | TE es direccional y suele ser real-valued, no necesariamente ordinal anidada |
| Total correlation / PID | Alta | excess3 es un proxy quirúrgico orientado a RECD, no una descomposición PID completa |
| TDA (Betti) | Complementaria | TDA ve topología del cloud; excess3 ve sinergia simbólica temporal |
| ML features | Baja | excess3 es interpretable y falsable con surrogates |

## Parámetros recomendados (v1.0 plataforma)

| Dominio | θ₃ | w_φ | Notas |
|---------|-----|-----|-------|
| Cardio RR | 0.08 | 101 | recalibrado CCTP |
| Dengue semanal | 0.10 | 13 | default teórico |
| Sintéticos | 0.10 | 13 | Feigenbaum sweeps |
| EEG bandpower | 0.08–0.12 | explorar | alta sensibilidad al preprocess |
