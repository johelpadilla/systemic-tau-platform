# Matemática del paradigma — mapa

Esta sección de la plataforma detalla los bloques computacionales. Orden pedagógico:

1. **Patrones ordinales (Bandt–Pompe)** — el alfabeto.
2. **Tau Sistémica (τ_s)** — el termómetro relacional.
3. **Ventana adaptativa (Breathing Window)** — el ritmo de observación.
4. **RECD Φ₁–Φ₃ + excess3** — el reloj y sus niveles *(ver Fundamentos)*.
5. **TDA + números de Betti (Tier 4)** — topología del cloud de estados.
6. **Memoria ordinal** — TE simbólica / MI de rangos.
7. **Surrogates** — IAAFT y phase-shuffle como nulos.

## Notación común

| Símbolo | Significado |
|---------|-------------|
| \(X \in \mathbb{R}^{T\times N}\) | Serie multivariada |
| \(m, \tau\) | Dimensión y delay Bandt–Pompe |
| \(W\), stride | Ventana y paso de τ_s |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveles de conjunción |
| excess3 | Proxy continuo de sinergia |
| \(\lambda\) | Intensidad de régimen / reorganización |
| \(\alpha_k(\lambda)\) | Pesos del ΔRECD |

## Complejidad orientativa

- Bandt–Pompe univariado: \(O(T \cdot m \log m)\) (o \(O(T)\) con m fijo=3 y numba).
- Φ₁: \(O(T \cdot N^2)\).
- Φ₂: \(O(T \cdot N^2 \cdot d)\).
- Φ₃ / excess3: \(O((T/w) \cdot w \cdot \mathrm{coste\ conteos})\); con \(m=3\), \(N\) pequeño es factible.
- Surrogates: × n_surr el coste de la métrica elegida.

## Modo Fast vs Full

| Bloque | Fast | Full |
|--------|------|------|
| τ_s + RECD | Sí | Sí |
| EWS clásicos | Sí | Sí |
| Surrogates | n=8 | n≥50 |
| TDA Betti | No | Sí |
| Memoria ordinal | No | Sí |
