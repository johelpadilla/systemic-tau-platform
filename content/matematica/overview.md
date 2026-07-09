# Matemática del paradigma — mapa

### Objetivos de esta sección
1. Ordenar los bloques computacionales de lo más simple a lo más costoso.
2. Saber qué corre en modo **Fast** vs **Full** en v1.0.
3. Conectar cada fórmula con un widget del Lab o del sandbox.

---

## 1. Orden de aprendizaje (no salte pasos)

| # | Bloque | Idea en una frase | Dónde practicarlo |
|---|--------|-------------------|-------------------|
| 1 | **Bandt–Pompe** | Alfabeto de m! patrones de orden local | Sandbox abajo |
| 2 | **τ_s** | Termómetro de reorganización relacional en ventanas | Demo + Lab |
| 3 | **RECD Φ₁–Φ₃ + excess3** | Reloj anidado y sinergia | Fundamentos + Lab |
| 4 | **EWS clásicas** | Panel univariado de control | Lab tab EWS |
| 5 | **Surrogates** | Nulos que rompen dependencia cruzada | Lab n_surr |
| 6 | **Breathing Window** | W que se adapta al régimen | Lab · extensión operativa |
| 7 | **TDA / Betti** | Topología del cloud de estados (β₀/β₁) | Lab · extensión (ripser opcional) |
| 8 | **Memoria ordinal** | MI simbólica / cross-MI | Lab · extensión |

**Consejo:** si no puede dibujar Bandt–Pompe en una pizarra, no interprete excess3. El sandbox existe para eso.

---

## 2. Notación común

| Símbolo | Significado | Valor típico v1.0 |
|---------|-------------|-------------------|
| \(X \in \mathbb{R}^{T\times N}\) | Serie multivariada | N≥2 (o proxy bivariado) |
| \(m, \tau\) | Dimensión y delay Bandt–Pompe | m=3, delay=1 |
| \(W\), stride | Ventana y paso de τ_s | cardio 101/5; sintético 13/1 |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveles de conjunción | [0,1] / binario |
| excess3 | Proxy continuo de sinergia | primario en ruido real |
| \(\theta_3\) | Umbral de Φ₃ | 0.08 cardio; 0.10 default |
| \(\lambda\) | Intensidad de reorganización | ligada a \|τ_s\| |
| \(\alpha_k(\lambda)\) | Pesos del ΔRECD | cambian con el régimen |

---

## 3. Bandt–Pompe en 60 segundos

Para una ventana de m puntos con delay τ:

1. Tome \(x_t, x_{t+\tau}, \ldots, x_{t+(m-1)\tau}\).  
2. Ordénelos; el **patrón de rangos** es un símbolo en \(\{0,\ldots,m!-1\}\).  
3. Con m=3 hay **6** símbolos posibles — un alfabeto pequeño y potente.

**Por qué importa:** Φ₁–Φ₃ y muchas entropías de permutación viven en ese alfabeto. Es invariante a transformaciones monótonas (cambiar unidades o “estirar” la señal no cambia el orden).

En el sandbox de esta página: mueva **m** y vea cómo el histograma se reparte en m! bins.

---

## 4. De símbolos a τ_s y RECD (pipeline v1.0)

```text
X (T×N)  →  z-score por canal
         →  τ_s(t) en ventanas W, stride
         →  símbolos BP → Φ₁, Φ₂, excess3, Φ₃
         →  EWS clásicas (var, AR1, …) en paralelo
         →  phase-shuffle × n_surr → p de Δmétrica
         →  hash SHA-256 de params + métricas
```

**Proxy univariado (CCTP):** si solo hay una serie \(x\), v1.0 construye  
\(X = [z(x),\, z(|\Delta x|)]\) — nivel y variación batido a batido. Es un compromiso explícito, no magia.

---

## 5. Complejidad orientativa (para no sorprenderse)

| Bloque | Orden de coste |
|--------|----------------|
| Bandt–Pompe univariado | \(O(T \cdot m \log m)\) (m fijo=3 es barato) |
| Φ₁ | \(O(T \cdot N^2)\) |
| Φ₂ | \(O(T \cdot N^2 \cdot d)\) |
| excess3 | crece con ventanas de conteo; N pequeño y m=3 es factible |
| Surrogates | × n_surr el coste de la métrica |

---

## 6. Modo Fast vs Full

| Bloque | Fast (docencia / exploración) | Full (paper-like) |
|--------|-------------------------------|-------------------|
| τ_s + RECD | Sí | Sí |
| EWS clásicas | Sí | Sí |
| Surrogates | n≈8 | n≥50 (recomendado) |
| TDA Betti | Opcional (casilla) | Sí (default Full; ripser o VR skeleton) |
| Breathing | Opcional (casilla) | Sí (default Full) |
| Memoria ordinal | No | Sí (extra) |

**Regla operativa:** explore en Fast; confirme en Full antes de citar un p-valor.

---

## 7. Qué demuestra la demo de logísticos acoplados

Los mapas logísticos con **switch de acoplamiento** a mitad de serie son el “laboratorio de juguete” ideal:

- Hay un **cambio de régimen conocido** ( Chronos: t = T/2 ).  
- Puede ver si τ_s y excess3 **reaccionan** al switch.  
- Puede contrastar con var/AR1 (a veces claros, a veces no).  
- Puede comprobar que el **hash** cambia si cambia seed/params.

Eso entrena la misma lectura que luego aplicará a Holter o dengue, donde el “ground truth” es clínico o epidemiológico, no sintético.
