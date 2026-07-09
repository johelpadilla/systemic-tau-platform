# RECD: tres niveles de conjunciones ordinales (Φ₁, Φ₂, Φ₃)

### Objetivos de este módulo
1. Explicar *Chronos* vs *Kairos* sin metáfora vacía.
2. Definir Φ₁, Φ₂ y Φ₃ como **muñecas rusas** (anidamiento).
3. Enunciar hipótesis falsables H1–H4 que el Lab puede ilustrar.

---

## 1. ¿Qué es el RECD?

El **Reloj Extramental Discreto (RECD)** formaliza la idea de que el **tiempo relevante del sistema** no es un parámetro externo homogéneo (*Chronos*), sino una **métrica emergente** generada por eventos de reorganización estructural (*Kairos*).

| Concepto | En la vida cotidiana | En los datos |
|----------|----------------------|--------------|
| **Chronos** | Segundos del reloj de pared | Índice \(t\) del CSV / Holter |
| **Kairos** | “El momento en que cambió el partido” | Tick de ΔRECD con peso de reorganización |

En su versión operacional ordinal (implementada en `nested-recd` y en el piloto CCTP), el avance del reloj se construye a partir de **conjunciones ordinales anidadas**:

\[
\text{Nivel 3} \;\supset\; \text{Nivel 2} \;\supset\; \text{Nivel 1}
\]

Cada nivel superior **añade irreductibilidad**: no niega el inferior; lo engloba y exige más estructura.

---

## 2. Nivel 1 — Coincidencia (Φ₁)

**Pregunta:** ¿Comparten dos o más variables el **mismo símbolo ordinal** en el mismo instante?

Tras embedding de Bandt–Pompe (dimensión \(m\), retardo \(\tau\)), cada variable \(i\) produce un símbolo \(\pi_t^{(i)}\) (una de \(m!\) permutaciones).

\[
\Phi_1(t) = \frac{2}{N(N-1)} \sum_{i < j} \mathbf{1}\!\left(\pi_t^{(i)} = \pi_t^{(j)}\right)
\]

| Propiedad | Valor |
|-----------|--------|
| Rango | \([0,1]\) |
| Interpretación | Fracción de pares “en el mismo patrón de orden” |
| Ontología | Coincidencia estadística — necesaria, no suficiente |

**Analogía:** varios músicos tocan la misma figura rítmica en el mismo compás, por azar o por acoplamiento débil.

**Trampa de interpretación:** Φ₁ alto *solo* no prueba “emergencia”. Puede ser ruido compartido o un patrón trivial.

---

## 3. Nivel 2 — Relación persistente (Φ₂)

**Pregunta:** ¿Hay una **relación** (igual, mayor, menor entre símbolos) que **persiste** al menos \(d\) pasos?

Para cada par \((i,j)\):

1. Codificar la relación \(R_t^{ij} \in \{\mathrm{EQ},\mathrm{GT},\mathrm{LT}\}\).
2. En una ventana retrospectiva de longitud \(d\), medir si la relación actual domina (p.ej. fracción ≥ 0.75).
3. Agregar y normalizar por número de pares → \(\Phi_2(t)\).

| Propiedad | Valor |
|-----------|--------|
| Parámetro típico | \(d = 4\) |
| Ontología | Estructura relacional *mantenida* — un hábito del sistema |

**Analogía:** no solo coinciden en un compás; mantienen un **liderazgo o espejo rítmico** durante varios compases.

En epidemiología, Φ₂ ayuda a pensar la **hiper-persistencia** de regímenes de transmisión.

---

## 4. Nivel 3 — Emergencia / co-actualización (Φ₃)

**Pregunta:** ¿Aparece una configuración conjunta **irreducible** a coincidencias y a pares?

Operacionalmente (ventana local de símbolos):

1. Entropía conjunta de la tupla \((\pi^1,\ldots,\pi^N)\).
2. Entropías marginales y MI pairwise promedio.
3. **Exceso sinérgico** ≈ correlación total − contribución explicable por pares.
4. Opcional: *joint surprise* vs independencia.

\[
\texttt{excess3}(t) \approx \text{combinación de sinergia y sorpresa conjunta}
\]

\[
\Phi_3(t) = \mathbf{1}\{\texttt{excess3}(t) > \theta_3\}
\]

| Parámetro | Valor típico v1.0 |
|-----------|-------------------|
| θ₃ sintéticos / dengue | ~0.10 |
| θ₃ RR cardíaco (CCTP) | **0.08** (recalibrado) |

**Regla de oro de la plataforma:** en fisiología ruidosa, el **exceso continuo (excess3)** suele ser más robusto que la tasa binaria de “alto Nivel 3”. El módulo siguiente lo detalla.

**Analogía:** la orquesta no solo se coordina por pares: emerge un **gesto colectivo** que no se deduce de cada atril por separado.

---

## 5. Acumulación del reloj y pesos por régimen

\[
\Delta \mathrm{RECD}(t) = \alpha_1(\lambda)\,\Phi_1 + \alpha_2(\lambda)\,\Phi_2 + \alpha_3(\lambda)\,\Phi_3
\]

donde \(\lambda(t)\) mide la **intensidad de reorganización**, a menudo ligada a \(|\tau_s|\).

| Régimen | α₁ (Nivel 1) | α₂, α₃ (Niveles 2–3) |
|---------|--------------|----------------------|
| Ordenado / estable | alto | relativamente bajos |
| Reorganización fuerte (λ↑) | decae | crecen (esp. α₃) |

**Tesis central:** cerca de transiciones, el reloj no solo “corre más”; **cambia de composición ontológica** — gana peso el Nivel 3.

---

## 6. Tabla resumen (chuleta)

| Nivel | Nombre | Qué mide | Proxy | Peso ontológico |
|-------|--------|----------|-------|-----------------|
| 1 | Coincidencia | Igualdad de símbolos | Φ₁ ∈ [0,1] | Bajo |
| 2 | Relación persistente | Relaciones estables ≥ d | Φ₂ ∈ [0,1] | Medio |
| 3 | Emergencia | Sinergia irreducible | excess3, Φ₃ | Alto |

---

## 7. Hipótesis falsables (diseño experimental)

Estas hipótesis estructuran el Lab y los papers de tiempo anidado / CCTP:

1. **H1:** Φ₃ / excess3 aumentan (magnitud o frecuencia) en regímenes post-umbral vs basales.  
2. **H2:** La contribución relativa del Nivel 3 crece con λ.  
3. **H3:** Los grandes ticks de ΔRECD se alinean con transiciones conocidas mejor que un reloj solo-Φ₁.  
4. **H4:** En surrogates que destruyen dependencia cruzada, Φ₂ y Φ₃ colapsan hacia ruido.

### Cómo “verlas” en v1.0
- **H1 / H4:** Lab con surrogates phase-shuffle; compare mean excess3 y p_surr.  
- **H2 / H3:** lectura de paneles RECD + τ_s en sintético con switch y en cardio-like.

### Puente al siguiente módulo
Si Φ₃ binario “no se enciende” pero excess3 se mueve, **no concluya que no hay Nivel 3**: lea el módulo **excess3**.
