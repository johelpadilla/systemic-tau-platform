# Alcance del núcleo

Qué calcula y documenta *Systemic Tau Platform*, y con qué límites de interpretación.

---

## 1. Tres hilos unificados

| Hilo | Qué resuelve | Dónde se trabaja |
|------|--------------|------------------|
| **Tau Sistémica (τ_s)** | Medir *reorganización relacional* (no solo “más varianza”) | Fundamentos · Matemática · Lab |
| **RECD ordinal anidado** | Reloj interno del sistema vía Φ₁–Φ₃ y excess3 | Fundamentos · Lab · Evidencia |
| **Falsabilidad operativa** | Surrogates, panel EWS clásicas, hash de corrida | Lab · reportes |

**Idea central:**

> Las EWS clásicas (var, AR1) no están “mal”: están **incompletas** cuando la transición es una reorganización de *relaciones* entre variables.  
> τ_s + RECD **completan el panel de instrumentos**, con interpretación y nulos.

---

## 2. Contenido de la plataforma

### 2.1 Módulos navegables

- **Fundamentos** en seis bloques: τ_s, límites de EWS, RECD Φ₁–Φ₃, excess3, CSD, filosofía operativa.
- **Matemática** con sandbox Bandt–Pompe y demo de pipeline en logísticos acoplados.
- **Dominios** con madurez empírica explícita (cardio &gt; dengue &gt; neuro/eco/clima/educación/sueño/social/finanzas).
- **Ruta de aprendizaje** Básico → Intermedio → Avanzado con checklist.
- **FAQ y glosario** orientados a malentendidos reales (signo context-dependent, N=1, “¿predice la muerte?”).

### 2.2 Evidencia de referencia

- Piloto **CCTP/SDDB (N=10)**: Δτ_s y Δexcess3, phase-shuffle, concordancia de signo **8/10**.
- Preprints y síntesis (Zenodo) enlazados en **Evidencia**.
- Matriz de comparación con EWS clásicas, ML, TDA y Transfer Entropy.

### 2.3 Curso corto (6 semanas)

- Syllabus sugerido semana a semana en **Docencia**.
- Separación de licencias académico / comercial / datos de terceros.
- Alineación con `systemictau` y `nested-recd`.

---

## 3. Pipeline científico (`src/stp/` · Laboratorio)

| Capacidad | Estado | Notas |
|-----------|--------|-------|
| Bandt–Pompe / símbolos ordinales | Operativo | Alfabeto de m! patrones |
| τ_s en ventana deslizante | Operativo | Termómetro relacional |
| Φ₁, Φ₂, Φ₃ + excess3 | Operativo | Reloj anidado; excess3 preferido en ruido real |
| EWS clásicas (var, AR1, …) | Operativo | Panel univariado para lectura dual |
| Phase-shuffle surrogates | Operativo | Nulo que rompe dependencia cruzada |
| Generadores sintéticos | Operativo | Logísticos, AR, cardio-like RR |
| Proxy univariado → bivariado | Operativo | \(X=[z(x), z(\|Δx\|)]\) como en CCTP |
| Presets por dominio | Operativo | W, stride, θ₃ (p.ej. cardio W=101, θ₃=0.08) |
| Reporte Markdown + hash SHA-256 | Operativo | Reproducibilidad de la corrida |
| Samples SDDB demo (38, 51) | Operativo | `data/samples/` |
| TDA / Breathing Window / memoria | Operativo (extensión Lab) | Casillas + pestaña Extensiones; no sustituyen el núcleo |

---

## 4. Resultados que el Lab ayuda a redescubrir

1. **En pre-FV (SDDB), el panel clásico es ambiguo:** var suele subir; AR1 a menudo baja. El CSD “de libro” no basta.
2. **El panel relacional sigue viendo señal:** Δτ_s y Δexcess3, con surrogates, capturan reorganización.
3. **El signo no es un dogma:** reorganización puede aumentar o colapsar estructura sinérgica según contexto (FA, pacing, fase terminal).
4. **excess3 continuo &gt; Φ₃ binario en datos ruidosos:** umbrales altos pueden dejar tasa de “alto Nivel 3” en cero aunque el delta sea significativo.
5. **La misma gramática cruza dominios:** corazón, dengue, EEG, lagos, clima, aula, polarización, sueño, finanzas — distinta madurez empírica, misma ontología metodológica (énfasis pedagógico, no promesas comerciales).

---

## 5. Sesión de 90–120 minutos

| Minutos | Actividad | Objetivo |
|---------|-----------|----------|
| 0–15 | Home + este documento | Orientar el alcance del núcleo |
| 15–35 | Fundamentos: τ_s + límites EWS | Formular la pregunta relacional |
| 35–50 | Fundamentos: RECD + excess3 | Distinguir Φ₁ / Φ₂ / Φ₃ |
| 50–70 | Matemática: sandbox BP + demo | Ver el alfabeto y una corrida |
| 70–100 | Lab: sintético → cardio-like | Interpretar Δτ_s, excess3, p_surr, EWS |
| 100–120 | Evidencia + FAQ | Citar con rigor; evitar overclaim |

---

## 6. Límites de interpretación

- **No es** un dispositivo clínico certificado ni un sistema de alarma hospitalaria.
- **No predice** de forma operativa la muerte súbita ni un brote de dengue.
- **No sustituye** validación externa, calibración de umbrales ni gobernanza ética.
- **TDA / Breathing** están **operativos como extensión** del Lab (no como núcleo de claims). API SaaS de pagos no forma parte del núcleo educativo.
- Los **dominios no cardio** tienen presets y pedagogía listos; la cohorte de referencia sigue siendo CCTP/SDDB.

---

## 7. Cómo citar

1. Preprint / paper del **dominio** que use (p.ej. CCTP para cardio).  
2. Software: `systemictau`, `nested-recd`, *Systemic Tau Platform*.  
3. Dataset original (PhysioNet SDDB, LTER, DengAI, …).  
4. Hash de reproducibilidad del Lab si reporta un resultado numérico concreto.

---

## 8. Cierre

> Se puede **definir**, **calcular**, **comparar con EWS**, **nular con surrogates** y **documentar con hash**.  
> El trabajo del investigador es **interpretar con contexto** y **validar fuera de la cohorte piloto**.
