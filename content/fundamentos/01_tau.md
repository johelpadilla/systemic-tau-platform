# ¿Qué es Tau Sistémica?

**Tau Sistémica** (τ_s) es una métrica **ordinal y relacional** diseñada para detectar **reorganizaciones de acoplamiento** entre variables de un sistema complejo **antes o durante** una transición de régimen.

A diferencia de las señales de alerta temprana (EWS) clásicas —varianza, autocorrelación de lag-1, recuperación lenta—, τ_s no pregunta *“¿cuánto se mueve cada variable?”* sino:

> **¿Cómo cambia la estructura de orden compartida entre las variables del sistema?**

## Definición conceptual

Sea un sistema multivariado \(X(t) \in \mathbb{R}^{T \times N}\) con \(N \geq 2\) componentes observables (por ejemplo: intervalo RR y su variación batido a batido; incidencia de dengue y temperatura; bandas de potencia EEG).

En una ventana deslizante de longitud \(W\), Tau Sistémica resume el **grado de coherencia ordinal cruzada** (y sus cambios) entre las series. Operacionalmente se construye a partir de:

1. **Patrones de rango** (ordenamientos locales o rangos de Kendall dentro de la ventana).
2. **Contrastes entre módulos** o pares de variables (acoplamiento vs anti-sincronización).
3. **Umbrales universales (Universalidad de Feigenbaum)**: El grado de acoplamiento no se interpreta arbitrariamente. La métrica se rige por umbrales derivados estadísticamente y regidos por la constante universal de Feigenbaum (\(\delta \approx 4.6692\)):
   - \(\tau_s \ge +0.50\): **Estabilidad y Sincronización** (Orden emergente).
   - \(|\tau_s| < 0.41\): **Rango Caótico Genuino** (Máxima sensibilidad a condiciones iniciales y volatilidad ordinal).
   - \(\tau_s \le -0.41\): **Antisincronización Fuerte** (Divergencia en antifase, abriendo posibilidad de retrocausalidad local).

El resultado es una serie temporal \(\tau_s(t)\) que **acelera, se invierte o se estabiliza** según el sistema se reorganice — no necesariamente según la varianza suba. Las componentes del sistema colapsan estadísticamente en el rango \(|\tau_s| < 0.41\), marcando el nacimiento fractal del tiempo sistémico.

## Por qué “sistémica”

El adjetivo *sistémica* enfatiza tres compromisos metodológicos:

| Compromiso | Significado |
|------------|-------------|
| **Relacional** | La señal vive entre variables, no dentro de una sola. |
| **Ordinal** | Usa orden e igualdad de rangos; es robusta a monótonas no lineales y a unidades. |
| **Multiescala** | Puede agregarse en capas (local / media / global) sin promediar linealmente la ontología del sistema. |

## Analogía pedagógica

Imagine una orquesta. Las EWS clásicas miden si **cada músico toca más fuerte o más despacio** (amplitud, autocorrelación). Tau Sistémica pregunta si **dejan de leer partituras independientes y empiezan a coordinar el mismo patrón rítmico** — aunque el volumen total no cambie, o incluso baje.

En un corazón previo a fibrilación ventricular, en un brote de dengue o en un lago que se eutrofiza, esa “coordinación del orden” es a menudo la firma más informativa de que el sistema está **cambiando de ley**, no solo de ruido.

## Qué no es Tau Sistémica

- No es un clasificador de machine learning opaco.
- No sustituye el juicio clínico, epidemiológico o ecológico.
- No asume *critical slowing down* univariado como única vía a la transición.
- No es una medida de “caos” en el sentido popular: es una medida de **reorganización relacional**, modulable por régimen.

## Lectura mínima recomendada

1. Fundamentos del marco topológico/ordinal de early warning (paper *Systemic Tau: Foundations*).
2. Aplicación cardíaca CCTP/SDDB (τ_s + RECD antes de FV espontánea).
3. *Síntesis Magna del Tau Sistémico* — capas ontológicas 1–3.
