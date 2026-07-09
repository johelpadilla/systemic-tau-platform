# Teoría — Tau Sistémica, RECD y lectura dual

**Audiencia:** posgrado · docentes · lectores de papers del paradigma  
**Uso:** handout de teoría (complementa Fundamentos en la app)  
**Versión:** v1.0

---

## 1. La pregunta científica

Las *early warning signals* (EWS) clásicas, motivadas por *critical slowing down* (CSD), preguntan en lo esencial:

> ¿Cuánto se mueve cada variable? ¿Se vuelve más lenta la recuperación?

**Tau Sistémica (τ_s)** pregunta otra cosa:

> **¿Cómo se reorganiza la estructura de orden compartida entre las variables del sistema?**

En sistemas vivos y socio-ecológicos la transición suele ser un **cambio de ley relacional**, no solo un enlentecimiento univariado. Por eso τ_s es **ordinal** y **relacional**.

### Qué no es τ_s

| Confusión frecuente | Aclaración |
|---------------------|------------|
| “Es Kendall-tau con marketing” | Comparte sustrato de rangos, pero opera en **ventanas**, multivariado, y se acopla al reloj RECD. |
| “Es causalidad / TE” | No es Transfer Entropy. TE pregunta predicción direccional; τ_s pregunta reorganización relacional. |
| “Predice muerte / brote / crisis” | Marco de investigación y docencia; no dispositivo certificado. |

---

## 2. Observables y ventana

Sea \(X \in \mathbb{R}^{T \times N}\) con \(N \ge 2\) (o un proxy bivariado legítimo, p.ej. \(z(\mathrm{RR}),\, z(|\Delta\mathrm{RR}|)\) en el patrón CCTP).

En una ventana de longitud \(W\) con paso `stride`:

1. Se construyen **patrones de orden** (Bandt–Pompe / rangos).  
2. Se resume la **coherencia ordinal cruzada** en un escalar \(\tau_s(t)\).  
3. La trayectoria \(\tau_s(t)\) puede acelerar, invertirse o estabilizarse cuando el sistema se reorganiza — **no necesariamente** cuando sube la varianza.

### Parámetros típicos (presets v1.0)

| Dominio | W | stride | θ₃ (orientativo) |
|---------|---|--------|------------------|
| Cardiología | 101 | 5 | 0.08 |
| Epidemiología | 13 | 1 | 0.10 |
| Neurociencia / sueño | 51 | 2 | 0.10 |
| Ecología / clima / social / finanzas | 21–25 | 1 | 0.10 |
| Educación (cohorte) | 17 | 1 | 0.10 |
| Sintético | 31 | 2 | 0.10 |

Documente siempre W; el hash de reproducibilidad la incluye.

---

## 3. RECD — reloj extramental discreto

**RECD** formaliza un tiempo emergente del sistema (*Kairos*) distinto del índice del CSV (*Chronos*).

### Niveles de conjunción ordinal

| Nivel | Idea | Trampa |
|-------|------|--------|
| **Φ₁** | Coincidencia de símbolos entre pares en \(t\) | Alto Φ₁ ≠ emergencia |
| **Φ₂** | Persistencia de relaciones de a pares (≥ d pasos) | “Hábito” relacional, no solo destello |
| **Φ₃** | Indicador binario de sinergia sobre umbral θ₃ | En ruido puede quedarse en 0 |
| **excess3** | Proxy **continuo** de sinergia irreducible | Métrica primaria en CCTP |

En datos reales ruidosos, **mean_excess3 / Δexcess3** suelen ser más informativos que el bit Φ₃.

El avance del reloj (ΔRECD) se modula por la intensidad de reorganización λ (ligada en la práctica a \(|\tau_s|\) y al régimen).

---

## 4. Surrogates — el nulo relacional

Para preguntar *“¿el Δ es realmente relacional?”* se usan nulos que:

- **Phase-shuffle (default):** preserva espectros por canal y **rompe dependencia cruzada**.  
- **IAAFT (opcional):** nulo más estricto en amplitud/espectro.

Lectura conjunta:

| Δ (efecto) | p_surr | Lectura docente |
|------------|--------|-----------------|
| Grande | Bajo (p.ej. ≤0.05) | Candidato a estructura relacional residual |
| Grande | Alto | No reclame detección; revise W y preprocess |
| Pequeño | Bajo | Efecto pequeño pero estable — cautela de dominio |
| Pequeño | Alto | Compatible con nulo; útil como control |

**Nunca** publique solo el p-valor sin tamaño de efecto, diseño y madurez del dominio.

---

## 5. Lectura dual (obligatoria en docencia)

Todo resultado serio se presenta en **dos columnas mentales**:

1. **Panel relacional:** τ_s, RECD, excess3, p_surr.  
2. **Panel clásico:** var, AR1 u otras EWS univariadas en paralelo.

### Por qué

- Las EWS clásicas pueden ser ambiguas cuando la transición es multivariada.  
- τ_s puede moverse cuando var/AR1 no “alertan” — y al revés.  
- La ciencia útil declara **concordancia o discordancia**, no esconde el panel incómodo.

### Signo context-dependent

Δτ_s o Δexcess3 pueden **subir o bajar** hacia un evento según el régimen (FA, pacing, fase de brote, tipo de sequía, crisis de cohorte). La evidencia se juega en magnitud, concordancia, nulos y narrativa de dominio — no en un letrero universal “positivo = malo”.

---

## 6. Madurez empírica (v1.0)

| Nivel | Dominios / materiales | Implicación |
|-------|----------------------|-------------|
| Ancla | Cardiología CCTP / SDDB (piloto documentado) | Claims más fuertes, aún de investigación |
| Transferencia alta | Epidemiología (narrativa + demos) | Hipótesis transferibles, validar fuera |
| Sandbox pedagógico | Clima, educación, social, sueño, finanzas, sintéticos | Ground truth de **diseño**; enseñan el método |

**Regla de oro:** no venda la fuerza del piloto cardio como si fuera validación de polarización social o de trading.

---

## 7. Reproducibilidad

Cada corrida del Lab genera un **repro_hash** (SHA-256) que sella parámetros y huella de los datos. Para citar un número:

1. Paper/preprint del dominio.  
2. Software (STP v1.0 / librerías alineadas).  
3. Dataset original y licencia.  
4. Hash de la corrida + Methods exportados.

---

## 8. Glosario mínimo

- **τ_s** — termómetro de reorganización relacional ordinal.  
- **RECD** — reloj de ticks de reorganización.  
- **excess3** — sinergia ordinal continua.  
- **Bandt–Pompe** — alfabeto de m! patrones de orden (m=3 → 6).  
- **EWS** — señales tempranas univariadas (control).  
- **CSD** — *critical slowing down* (marco clásico).

Glosario completo: handout *Glosario* o página Ruta de aprendizaje.

---

## 9. Lecturas de contexto (no exhaustivo)

- Bandt & Pompe — ordinal patterns / permutation entropy.  
- Literatura CSD / critical transitions (Scheffer y afines).  
- Papers/preprints del dominio que use (p.ej. CCTP en cardiología).  
- Documentación de datasets (PhysioNet SDDB, etc.).

---

*Handout teórico STP · para imprimir o adjuntar al LMS · complementa la app, no la sustituye.*
