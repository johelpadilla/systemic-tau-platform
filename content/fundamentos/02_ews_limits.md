# El problema de las métricas clásicas de Early Warning Signals

## La promesa de las EWS clásicas

La teoría de **transiciones críticas** predice que, al acercarse a un punto de bifurcación, muchos sistemas exhiben *critical slowing down* (CSD): la recuperación ante perturbaciones se vuelve más lenta. En series temporales univariadas, eso se traduce a menudo en:

| Métrica | Firma esperada cerca de la transición |
|---------|----------------------------------------|
| Varianza | ↑ aumento |
| Autocorrelación lag-1 (AR1) | ↑ acercándose a 1 |
| Espectro de potencias | más energía en bajas frecuencias |
| DFA / Hurst | mayor memoria de largo alcance |

Estas métricas han sido útiles en ecología, clima y algunos modelos sintéticos. El problema aparece en **sistemas vivos reales, ruidosos y multivariados**.

## Dónde fallan en la práctica

### 1. Asunción de univariado / CSD simple

Muchas transiciones biológicas **no** se comportan como un único potencial con un parámetro de control que se desliza suavemente. El corazón, el cerebro o una epidemia reorganizan **redes de relaciones**. La varianza de una sola serie puede subir, bajar o no moverse, mientras la **estructura cruzada** sí cambia.

### 2. Signos invertidos o no informativos

En el piloto CCTP sobre Holter pre-FV (SDDB):

- La **varianza** tiende a subir (firma “clásica”).
- El **AR(1)** con frecuencia **baja** — opuesto al CSD ingenuo.
- τ_s y excess3 capturan la **dirección de la reorganización relacional**, que es **context-dependent** (no siempre el mismo signo).

Interpretar “AR1 no subió ⇒ no hay alerta” sería un falso negativo metodológico.

### 3. Sensibilidad a no linealidades monótonas y a escala

Métricas basadas en momentos (media, var) dependen de la escala y de transformaciones. Las medidas **ordinales** son invariantes a transformaciones monótonas y se alinean mejor con la idea de “patrón de orden” del sistema.

### 4. Confusión entre ruido, pacing y patología

En ECG real hay pacing intermitente, FA, artefactos de anotación. Las EWS univariadas reaccionan a todo eso. Un marco relacional + flags de calidad permite **retener** casos difíciles sin destruir la señal (como en CCTP).

### 5. Falta de teoría de “tiempo del sistema”

Las EWS clásicas viven en el tiempo del reloj del laboratorio (segundos, semanas). No modelan el **tiempo interno** del sistema: cuándo “avanza” un instante significativo de reorganización. El RECD ataca precisamente ese vacío.

## Tabla comparativa (pedagógica)

| Criterio | EWS clásicas | Tau Sistémica + RECD |
|----------|--------------|----------------------|
| Unidad de análisis | Univariada (típica) | Multivariada / relacional |
| Observables | Momentos, correlaciones lineales | Patrones ordinales, conjunciones |
| Hipótesis de vía | CSD genérico | Reorganización relacional (signo contextual) |
| Tiempo | Cronológico externo | RECD (tiempo extramental discreto) |
| Validación nula | Bootstrap simple | Surrogates de fase / IAAFT que rompen dependencia cruzada |
| Interpretabilidad | Media | Alta (Φ₁–Φ₃, excess3) |

## Mensaje clave

> Las EWS clásicas no están “mal”: están **incompletas** para sistemas donde la transición es una **reorganización de relaciones**, no solo un enlentecimiento de una variable.

Tau Sistémica y RECD no reemplazan la física de las bifurcaciones; **completan el panel de instrumentos** con observables alineados a esa reorganización.
