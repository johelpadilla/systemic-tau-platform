# ¿Qué es Tau Sistémica?

### Objetivos de este módulo
1. Formular la pregunta científica que τ_s responde (y la que *no* responde).
2. Distinguir métricas de *amplitud* (var, AR1) de métricas *ordinal-relacionales*.
3. Poder explicar τ_s a un colega en menos de dos minutos con una analogía sólida.

---

## 1. La pregunta que abre el paradigma

**Tau Sistémica** (τ_s) es una métrica **ordinal y relacional** diseñada para detectar **reorganizaciones de acoplamiento** entre variables de un sistema complejo **antes o durante** una transición de régimen.

Las EWS clásicas preguntan, en esencia:

> *¿Cuánto se mueve cada variable? ¿Se está volviendo más lenta al recuperarse?*

τ_s pregunta otra cosa:

> **¿Cómo cambia la estructura de orden compartida entre las variables del sistema?**

Esa diferencia no es cosmética: en sistemas vivos (corazón, epidemia, lago, red neuronal) la transición a menudo es un **cambio de ley relacional**, no un simple enlentecimiento univariado.

---

## 2. Definición conceptual (nivel investigador)

Sea un sistema multivariado \(X(t) \in \mathbb{R}^{T \times N}\) con \(N \geq 2\) componentes observables. Ejemplos reales en esta plataforma:

| Dominio | Ejemplo de \(X\) |
|---------|------------------|
| Cardiología CCTP | \(z(\mathrm{RR})\), \(z(\|\Delta\mathrm{RR}\|)\) |
| Dengue | cases, temperatura, precipitación (z-score) |
| EEG | potencias de banda o canales seleccionados |
| Sintético | mapas logísticos acoplados con switch de régimen |

En una **ventana deslizante** de longitud \(W\), τ_s resume el **grado de coherencia ordinal cruzada** (y sus cambios) entre las series. Operacionalmente se construye a partir de:

1. **Patrones de rango** (ordenamientos locales / rangos de Kendall en la ventana).
2. **Contrastes entre módulos o pares** (acoplamiento vs anti-sincronización).
3. **Normalización** a una escala interpretable en el tiempo de la serie.

El resultado es una trayectoria \(\tau_s(t)\) que **acelera, se invierte o se estabiliza** cuando el sistema se reorganiza — **no necesariamente** cuando la varianza sube.

### Qué mirar en el Lab

| Observación | Lectura |
|-------------|---------|
| τ_s estable en basal | Régimen relacional “en ley” |
| Cambio sostenido basal → approach | Candidato a reorganización |
| Δτ_s grande + p_surr bajo | El cambio no se explica por dependencia cruzada nula (phase-shuffle) |
| Δτ_s grande pero p_surr alto | Cuidado: puede ser compatible con nulo espectral |

---

## 3. Por qué se llama “sistémica”

| Compromiso | Significado | Si se viola… |
|------------|-------------|--------------|
| **Relacional** | La señal vive *entre* variables | Se confunde con univariado disfrazado |
| **Ordinal** | Usa orden e igualdad de rangos; robusta a monótonas y a unidades | Se reintroduce dependencia de escala |
| **Multiescala / capas** | Puede articularse con RECD y capas ontológicas | Se colapsa todo a un único número sin gramática |

---

## 4. Analogía (orquesta)

Imagine una orquesta:

- **EWS clásicas** miden si cada músico toca más fuerte o más despacio (amplitud, autocorrelación).
- **τ_s** pregunta si dejan de leer partituras independientes y empiezan a **coordinar el mismo patrón de orden** — aunque el volumen total no cambie, o incluso baje.

En un corazón previo a fibrilación ventricular, en un brote de dengue o en un lago que se eutrofiza, esa “coordinación del orden” es a menudo la firma más informativa de que el sistema está **cambiando de ley**, no solo de ruido.

**Ejercicio mental:** ¿puede haber transición clínica real con AR1 que *baja*? Sí — y el piloto CCTP lo documenta. Ahí τ_s + excess3 no son un lujo: son el panel que sigue teniendo sentido.

---

## 5. Qué no es Tau Sistémica

- No es un clasificador de machine learning opaco.
- No sustituye el juicio clínico, epidemiológico o ecológico.
- No asume *critical slowing down* univariado como única vía a la transición.
- No es “caos” en el sentido popular: es **reorganización relacional**, modulable por régimen.
- No es un Kendall tau estático con marketing (véase FAQ): el objeto es la **dinámica de reorganización** acoplada al RECD.

---

## 6. Mini-síntesis (para el examen / el paper)

> **τ_s** = termómetro de *cómo se reordenan las relaciones ordinales* del sistema en el tiempo.  
> Se interpreta junto a **EWS clásicas** (panel univariado) y a **RECD/excess3** (reloj y sinergia).  
> La unidad de evidencia no es un pico aislado: es **Δ + contexto + surrogates + concordancia**.

### Lectura mínima recomendada
1. *Systemic Tau: Foundations…* (marco ordinal de early warning).  
2. CCTP/SDDB (aplicación cardíaca pre-FV).  
3. *Síntesis Magna del Tau Sistémico* (capas ontológicas).  
4. En esta plataforma: módulo **Límites EWS** → **RECD** → **excess3**.
