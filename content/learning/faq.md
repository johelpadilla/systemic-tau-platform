# Preguntas frecuentes (respuestas profundas)

Estas respuestas están escritas para **malentendidos reales** de posgrado y de revisión por pares — no para un FAQ de marketing.

---

## A. Conceptos

### ¿Tau Sistémica es solo un Kendall tau con marketing?

No. El parentesco con estadísticas de rangos (Kendall y afines) es real en el **sustrato ordinal**, pero el objeto de τ_s es la **dinámica de reorganización del acoplamiento** en ventanas, a menudo multiescala y acoplada al RECD. Un coeficiente de correlación de rangos estático no define un reloj ni niveles Φ₁–Φ₃.

### ¿En qué se diferencia de Transfer Entropy?

| | Transfer Entropy | τ_s + RECD / excess3 |
|--|------------------|----------------------|
| Pregunta | ¿Cuánta información de A mejora la predicción de B? | ¿Cómo se reorganiza la estructura ordinal conjunta y avanza el reloj? |
| Dirección | Explícitamente direccional | Relacional / sinérgica (no es un grafo causal) |
| Uso en v1.0 | Horizonte Full | Núcleo del Lab |

Son **complementarios**. No sustituya uno por el otro en un paper sin justificar la pregunta.

### ¿Por qué Bandt–Pompe y no SAX u otros símbolos?

Por parsimonia, invariancia monótona, y ecosistema maduro (entropía de permutación, papers del paradigma). SAX u otros alfabetos son extensiones posibles; **no** son el estándar del piloto CCTP ni del núcleo v1.0.

### ¿Qué es “signo context-dependent”?

Significa que **Δτ_s o Δexcess3 pueden subir o bajar** hacia un evento según el régimen (p.ej. FA, pacing, fase de un brote). La evidencia se juega en:

1. magnitud del cambio,  
2. concordancia entre métricas,  
3. p-valores bajo surrogates,  
4. narrativa clínica/epidemiológica,

no en un letrero universal “siempre positivo = malo”.

---

## B. Datos y práctica

### ¿Puedo usarlo con una sola variable?

El núcleo es multivariado (N≥2). Si solo tiene una serie, la plataforma construye un proxy  
\(X=[z(x), z(|\Delta x|)]\) (patrón CCTP). Es un compromiso **legítimo y explícito**, no magia: está haciendo visible la relación nivel–variación.

### ¿Qué ventana W debo usar?

Empiece por el **preset de dominio** (cardio: 101; dengue/sintético: ~13). Luego:

- W demasiado pequeña → ruido, p-valores inestables.  
- W demasiado grande → suaviza la transición y “llega tarde”.  
Documente W en el reporte; el hash la incluye.

### ¿Cuántos surrogates bastan?

| Uso | n_surr orientativo |
|-----|--------------------|
| Clase / demo | 4–8 (Fast) |
| Exploración seria | 20–50 |
| Resultado a citar | ≥50 y sensibilidad a seed |

Phase-shuffle **preserva espectros por canal** y **rompe dependencia cruzada**: es el nulo natural para “¿la señal es realmente relacional?”.

### ¿Cómo leo p_surr juntos con Δ?

- **Δ grande + p bajo:** candidato a efecto relacional.  
- **Δ grande + p alto:** no reclame detección; revise preprocess y W.  
- **Δ pequeño + p bajo:** efecto pequeño pero estable — interprete con cautela clínica.  
- **Nunca** publique solo el p sin el tamaño del efecto y el contexto.

---

## C. Evidencia y ética

### ¿Esto predice la muerte súbita o un brote de dengue?

**No como dispositivo clínico/operativo certificado.** Es un marco de investigación y docencia. Cualquier uso prospectivo exige validación externa, calibración de umbrales y gobernanza ética.

### ¿Qué cubre el núcleo actual?

- Pipeline completo τ_s + RECD + EWS + surrogates + hash.  
- Piloto **CCTP/SDDB N=10** con hallazgos documentados (panel clásico ambiguo; relacional significativo; concordancia 8/10).  
- Fundamentos, glosario, dominios, Lab y syllabus de 6 semanas.  
- Samples y generadores para reproducir la *lógica* del análisis sin PhysioNet.

Detalle: **Alcance del núcleo** (Ruta de aprendizaje) o el expander en Home.

### ¿Qué debo citar?

1. El paper/preprint del **dominio** que use (p.ej. CCTP para cardio).  
2. El software (`systemictau`, `nested-recd`, esta plataforma v1.0).  
3. El dataset original (PhysioNet, LTER, DengAI, etc.).  
4. El **repro_hash** del Lab si reporta un número concreto de una corrida.

---

## D. Producto y límites de software

### ¿Por qué a veces Φ₃ “no se enciende”?

Porque es un **indicador binario** con umbral θ₃. En datos ruidosos el continuo **excess3** puede moverse con claridad mientras Φ₃ permanece en cero. En CCTP la métrica primaria es mean_excess3 / Δexcess3.

### ¿TDA y Breathing Window están listos?

**Sí, como extensiones operativas del Lab** (v1.0+):

| Extensión | Qué hace en el Lab | Backend |
|-----------|--------------------|---------|
| **Breathing window** | W se adapta a la volatilidad local al calcular τ_s | Nativo (siempre) |
| **TDA / Betti** | Curvas β₀/β₁ en ventanas sobre cloud de delay-embedding | `ripser` si `pip install …[tda]`; si no, **1-skeleton Vietoris–Rips** (NumPy/SciPy) |
| **Memoria ordinal** | MI simbólica lag-1 y cross-MI | Nativo |

**Cómo activarlos:** modo **Full** (casillas activas por defecto) o marque las casillas en modo Fast. Pestaña de resultados **Extensiones**. CLI: `--breathing --tda`.

**Qué no son:** no sustituyen τ_s + RECD + EWS + surrogates. Un claim principal de tesis **no** debería basarse solo en β₁ del proxy pedagógico. El núcleo sigue siendo la lectura dual ordinal.

### ¿Necesito instalar ripser?

No es obligatorio. Sin ripser el Lab usa un proxy de Betti del 1-esqueleto VR (componentes + número ciclomático). Con `pip install systemic-tau-platform[tda]` se usa ripser cuando está disponible.

### ¿Los planes Academic/Professional están activos?

La UI de planes **no forma parte del núcleo educativo v1.0**. En ejecución local el Lab y los materiales descargables están disponibles sin backend de pagos. No confunda posicionamiento comercial con limitación científica del código local.

---

## E. Dominios nuevos y pedagogía

### ¿Por qué hay demos de “aula”, “polarización” o “sequía”?

Porque STP es software **pedagógico**: sirven para practicar la misma gramática ordinal en sistemas familiares o clásicos (CSD), con **ground truth de diseño**. No son evidencia de campo ni productos predictivos.

### ¿Cuál demo uso el primer día de clase?

1. `synthetic_coupled_logistic` (señal fuerte).  
2. `synthetic_ar_noise` (casi-nulo).  
3. Luego un dominio aplicado **con disclaimer de madurez** (p.ej. dengue-like o education_cohort).

### ¿Dónde descargo PDF/Markdown para el LMS?

Página **Materiales** de la app: guía rápida, manual, teoría, cheat-sheet, checklist, syllabus, FAQ, glosario, packs estudiante/docente.
