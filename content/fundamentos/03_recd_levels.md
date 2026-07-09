# RECD: tres niveles de conjunciones ordinales (Φ₁, Φ₂, Φ₃)

## ¿Qué es el RECD?

El **Reloj Extramental Discreto (RECD)** postula que el tiempo extramental no es un continuo absoluto newtoniano (*Chronos*), sino una **secuencia discreta y fractal de conjunciones ordinales** que emerge en el rango caótico (\(|\tau_s| < 0.41\)), gobernada por la constante de Feigenbaum (\(\delta \approx 4.6692016\)).

Esta construcción es jerárquica y escalonada en **cuatro niveles ontológicos principales** (Nivel 0 a Nivel 3). Cada nivel superior **añade irreductibilidad**: no niega el inferior; lo engloba y emerge a partir de este sin requerir sustrato temporal externo.

---

## Nivel 0 — Micro-conjunciones locales

**Idea:** Corresponde a las concordancias ordinales elementales entre pares de componentes del sistema.
- Fórmulación: \( C_{ij}^{(0)} = \tau_k(r_i, r_j) \)
- En este nivel **aún no existe el tiempo**; solo existen relaciones ordinales atemporales.

---

## Nivel 1 — Conjunciones Sistémicas (Φ₁)

**Idea:** ¿Comparten dos o más variables el **mismo símbolo ordinal** en el mismo instante?

Tras embedding de Bandt–Pompe (dimensión \(m\), retardo \(\tau\)), cada variable \(i\) produce un símbolo \(\pi_t^{(i)}\) (una de \(m!\) permutaciones).

\[
\Phi_1(t) = \frac{2}{N(N-1)} \sum_{i < j} \mathbf{1}\!\left(\pi_t^{(i)} = \pi_t^{(j)}\right)
\]

- Rango: \([0,1]\).
- Interpretación: fracción de pares “en el mismo patrón de orden”.
- Ontología: Solo cuando la conjunción sistémica entra en rango caótico (\(|\tau_s| < 0.41\)) se activa la **primera conjunción temporal** \(t_1\) (el primer "tic" del reloj extramental).

**Analogía:** Varios músicos tocan la misma figura rítmica en el mismo compás, por azar o por acoplamiento débil.

---

## Nivel 2 — Jerarquía de escalas ordinales (Φ₂)

**Idea:** no basta la igualdad puntual; importa una **relación** (igual, mayor, menor entre símbolos) que **persiste** al menos \(d\) pasos.

Para cada par \((i,j)\):

1. Codificar la relación \(R_t^{ij} \in \{\mathrm{EQ},\mathrm{GT},\mathrm{LT}\}\).
2. En una ventana retrospectiva de longitud \(d\), medir si la relación actual domina (fracción ≥ umbral, p.ej. 0.75).
3. Agregar y normalizar por número de pares → \(\Phi_2(t)\).

- Parámetro típico: \(d = 4\).
- Ontología: Cada nueva conjunción sistémica genera una renormalización completa del sistema. Los intervalos entre "tics" se comprimen exponencialmente según la constante de Feigenbaum: \(\Delta t_k = (1/\delta^k) \times (1/|\tau_s|)\). Es una estructura **fractal-estocástica**.

**Analogía:** No solo coinciden en un compás; mantienen un **liderazgo o espejo rítmico** durante varios compases.

---

## Nivel 3 — Tiempo emergente global (Φ₃)

**Idea:** aparece una configuración conjunta que **no se reduce** a coincidencias ni a pares persistentes. Es un proxy computable de **sinergia / irreductibilidad**.

Operacionalmente (ventana local de símbolos):

1. Entropía conjunta de la tupla \((\pi^1,\ldots,\pi^N)\).
2. Entropías marginales y MI pairwise promedio.
3. **Exceso sinérgico** ≈ correlación total − contribución explicable por pares.
4. Opcional: *joint surprise* (configuraciones más frecuentes de lo esperado bajo independencia).

\[
\texttt{excess3}(t) \approx \text{combinación de sinergia y sorpresa conjunta}
\]

\[
\Phi_3(t) = \mathbf{1}\{\texttt{excess3}(t) > \theta_3\}
\]

- θ₃ típico: ~0.10 en sintéticos; **0.08** recalibrado en RR cardíaco ruidoso.
- En fisiología real, el **exceso continuo (excess3)** suele ser más robusto que la tasa binaria de “alto Nivel 3”.

**Analogía:** la orquesta no solo se coordina por pares: emerge un **gesto colectivo** (un “instante” con identidad propia) que no se deduce de cada atril por separado.

---

## Acumulación del reloj y pesos por régimen

El tiempo extramental completo se construye como la suma jerárquica mediante la ecuación de recurrencia:
\[
t_{k+1} = t_k + g(\tau_s(t_k)) \cdot \Delta t_k
\]

donde \(g(\tau_s)\) es la **función de compuerta universal**. Este nivel es el único observable macroscópicamente.

Comportamiento cualitativo de la función de compuerta \(g(\tau_s)\):

| Régimen | Valor \(g(\tau_s)\) | Efecto Ontológico |
|---------|---------------------|-------------------|
| Orden / Estabilidad (\(\tau_s \ge +0.50\)) | +1 | Avance estable y predecible (*Chronos*). |
| Rango Caótico (\(\|\tau_s\| < 0.41\)) | (δ-1)/δ × (0.41 - \|\tau_s\|) / 0.41 | Avance continuo pero fractal-estocástico (*Kairos*). |
| Antisincronización (\(\tau_s \le -0.41\)) | -1 | Detención o retrocausalidad local (anti-cronología). |

**Tesis central:** La jerarquía ontológica demuestra que el tiempo extramental es una propiedad **emergente de orden superior**, construida de abajo hacia arriba a partir de correlaciones ordinales en el rango caótico, refutando el tiempo absoluto newtoniano.

---

## Tabla resumen

| Nivel | Nombre | Qué mide | Proxy numérico | Peso ontológico |
|-------|--------|----------|----------------|-----------------|
| 1 | Coincidencia | Igualdad de símbolos | Φ₁ ∈ [0,1] | Bajo |
| 2 | Relación persistente | Relaciones estables ≥ d | Φ₂ ∈ [0,1] | Medio |
| 3 | Emergencia | Sinergia irreducible | excess3, Φ₃ | Alto |

## Hipótesis falsables (diseño experimental)

1. **H1:** Φ₃ / excess3 aumentan (en magnitud o frecuencia) en regímenes post-umbral vs basales.
2. **H2:** La contribución relativa del Nivel 3 crece con λ.
3. **H3:** Los grandes ticks de ΔRECD se alinean con transiciones conocidas mejor que un reloj solo-Φ₁.
4. **H4:** En surrogates que destruyen dependencia cruzada, Φ₂ y Φ₃ colapsan hacia ruido.

Estas hipótesis estructuran tanto el Lab de la plataforma como los papers CCTP y de tiempo anidado.
