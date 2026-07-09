# El problema de las métricas clásicas de Early Warning Signals

### Objetivos de este módulo
1. Recordar *por qué* var y AR1 fueron una buena idea (CSD).
2. Enumerar cinco fallos prácticos en sistemas vivos multivariados.
3. Adoptar la postura de la plataforma: **panel dual**, no “EWS malas vs buenas”.

---

## 1. La promesa legítima de las EWS clásicas

La teoría de **transiciones críticas** predice que, al acercarse a un punto de bifurcación, muchos sistemas exhiben *critical slowing down* (CSD): la recuperación ante perturbaciones se vuelve más lenta. En series univariadas eso se traduce a menudo en:

| Métrica | Firma esperada cerca de la transición |
|---------|----------------------------------------|
| Varianza | ↑ aumento |
| Autocorrelación lag-1 (AR1) | ↑ acercándose a 1 |
| Espectro de potencias | más energía en bajas frecuencias |
| DFA / Hurst | mayor memoria de largo alcance |

Estas métricas han sido útiles en ecología, clima y modelos sintéticos. El problema aparece en **sistemas vivos reales, ruidosos y multivariados** — el terreno natural de Tau/RECD.

**Idea a retener:** el CSD es un *mecanismo elegante*, no una *ley universal de los datos clínicos*.

---

## 2. Dónde fallan en la práctica (cinco lecciones)

### 2.1 Asunción de univariado / CSD simple

Muchas transiciones biológicas **no** se comportan como un único potencial con un parámetro de control que se desliza suavemente. El corazón, el cerebro o una epidemia reorganizan **redes de relaciones**. La varianza de una sola serie puede subir, bajar o no moverse, mientras la **estructura cruzada** sí cambia.

### 2.2 Signos invertidos o no informativos (caso CCTP)

En el piloto CCTP sobre Holter pre-FV (SDDB, N=10 de alta calidad):

- La **varianza** tiende a subir (firma “clásica”).
- El **AR(1)** con frecuencia **baja** — opuesto al CSD ingenuo.
- τ_s y excess3 capturan la **dirección de la reorganización relacional**, que es **context-dependent**.

Interpretar “AR1 no subió ⇒ no hay alerta” sería un **falso negativo metodológico**.

### 2.3 Sensibilidad a escala y monótonas

Métricas basadas en momentos dependen de la escala y de transformaciones. Las medidas **ordinales** son invariantes a transformaciones monótonas y se alinean con “patrón de orden”.

### 2.4 Ruido, pacing y patología

En ECG real hay pacing intermitente, FA, artefactos de anotación. Las EWS univariadas reaccionan a todo eso. Un marco relacional + flags de calidad permite **retener** casos difíciles sin destruir la señal (como en CCTP, p.ej. registro 51).

### 2.5 Falta de teoría del “tiempo del sistema”

Las EWS clásicas viven en el reloj del laboratorio (segundos, semanas). No modelan el **tiempo interno**: cuándo “avanza” un instante significativo de reorganización. El **RECD** ataca ese vacío (siguiente módulo).

---

## 3. Tabla comparativa

| Criterio | EWS clásicas | Tau Sistémica + RECD |
|----------|--------------|----------------------|
| Unidad de análisis | Univariada (típica) | Multivariada / relacional |
| Observables | Momentos, correlaciones lineales | Patrones ordinales, conjunciones |
| Hipótesis de vía | CSD genérico | Reorganización relacional (signo contextual) |
| Tiempo | Cronológico externo | RECD (tiempo extramental discreto) |
| Validación nula | Bootstrap simple | Surrogates de fase / IAAFT |
| Interpretabilidad | Media–alta | Alta (Φ₁–Φ₃, excess3) cuando se domina la gramática |

---

## 4. Protocolo de lectura dual (v1.0 Lab)

Cuando abra el Laboratorio, **no elija un bando**. Haga esto:

1. **Panel clásico:** ¿var sube? ¿AR1 sube o baja?  
2. **Panel relacional:** ¿Δτ_s y Δexcess3 son grandes y significativos bajo surrogates?  
3. **Concordancia:** ¿τ_s y excess3 se mueven en el mismo sentido? (en CCTP: 8/10)  
4. **Contexto:** pacing, FA, estacionalidad, artefactos.  
5. **Conclusión acotada:** “reorganización relacional con panel clásico ambiguo” es un resultado científico legítimo.

---

## 5. Mensaje clave

> Las EWS clásicas no están “mal”: están **incompletas** para sistemas donde la transición es una **reorganización de relaciones**, no solo un enlentecimiento de una variable.

Tau Sistémica y RECD no reemplazan la física de las bifurcaciones; **completan el panel de instrumentos** con observables alineados a esa reorganización.

### Pregunta de contraste
*Si en un Holter pre-FV la varianza sube y el AR1 baja, ¿qué hipótesis formula usted antes de mirar τ_s?*  
Dirección esperada: no descartar transición; sospechar vía no-CSD o multivariada; ir al panel relacional y a nulos.
