# Matemática práctica — Bandt–Pompe, τ_s y RECD

**Audiencia:** quien ya leyó la guía rápida y va al sandbox de Matemática / Lab  
**Objetivo:** poder calcular e interpretar sin saltarse el alfabeto ordinal

---

## 1. Orden de aprendizaje (no salte pasos)

| # | Bloque | Una frase | Dónde |
|---|--------|-----------|--------|
| 1 | Bandt–Pompe | m! patrones de orden local | Matemática (sandbox) |
| 2 | τ_s | Termómetro relacional en ventanas | Lab |
| 3 | Φ₁–Φ₃ + excess3 | Reloj anidado y sinergia | Fundamentos + Lab |
| 4 | EWS clásicas | Panel univariado de control | Lab |
| 5 | Surrogates | Nulos de dependencia cruzada | Lab (n_surr) |
| 6 | Breathing / memoria / TDA | Extensiones operativas del Lab | Lab · casillas / modo Full |

**Consejo:** si no puede dibujar Bandt–Pompe en una pizarra, no interprete excess3.

---

## 2. Notación

| Símbolo | Significado | Típico v1.0 |
|---------|-------------|-------------|
| \(X\in\mathbb{R}^{T\times N}\) | Serie multivariada | N≥2 |
| \(m,\tau\) | Dimensión y delay ordinal | m=3, delay=1 |
| \(W\), stride | Ventana y paso | ver presets |
| \(\Phi_1,\Phi_2,\Phi_3\) | Niveles de conjunción | [0,1] / binario |
| excess3 | Sinergia continua | primario en ruido |
| \(\theta_3\) | Umbral de Φ₃ | 0.08 cardio; ~0.10 otros |
| \(\lambda\) | Intensidad de reorganización | ligada a \|τ_s\| |

---

## 3. Bandt–Pompe en 90 segundos

Para una ventana de \(m\) puntos con delay \(\tau\):

1. Tome \(x_t, x_{t+\tau},\ldots,x_{t+(m-1)\tau}\).  
2. Ordénelos: el **patrón de rangos** es un símbolo en \(\{0,\ldots,m!-1\}\).  
3. Con \(m=3\) hay **6** símbolos.

### Propiedad clave

Invariancia a transformaciones **estrictamente monótonas** (cambiar unidades o “estirar” la señal no cambia el orden). Por eso el paradigma es robusto a escalas distintas entre canales — tras un preprocess honesto.

### Ejercicio de pizarra

Serie: `3, 1, 4, 2` con m=3, delay=1.

- Tripleta (3,1,4) → ordenar valores → patrón de permutación.  
- Tripleta (1,4,2) → otro símbolo.  
Cuente frecuencias en una ventana más larga en el sandbox de la app.

---

## 4. De símbolos a τ_s (intuición operativa)

1. Cada canal se simboliza (Bandt–Pompe).  
2. En la ventana se mide **coherencia / reorganización** entre canales (no solo entropía univariada).  
3. Se obtiene \(\tau_s(t)\) a lo largo del tiempo.  
4. Con un **evento** marcado se calcula Δ pre/post; si no, 1ª vs 2ª mitad.

### Controles mentales

- **Control positivo:** logísticos acoplados con switch → |Δτ_s| grande.  
- **Control casi-nulo:** AR independientes → |Δτ_s| pequeño.  
- Si su demo “aplicado” se parece al AR, no force una narrativa de reorganización.

---

## 5. RECD y excess3 (fórmulas en palabras)

### Φ₁

Fracción (normalizada) de pares de variables con el **mismo símbolo** en el tiempo t. Base estadística; insuficiente sola.

### Φ₂

Relaciones de a pares (p.ej. EQ/GT/LT) que **persisten** al menos \(d\) pasos (típico d=4). Hábitos, no destellos.

### excess3

Proxy continuo de **sinergia irreducible**: hay estructura conjunta que no se reduce a pares independientes. Es el continuo que alimenta la decisión de Φ₃.

### Φ₃

1 si excess3 > θ₃; 0 si no. En series ruidosas puede quedarse apagado mientras excess3 se mueve: **reporte el continuo**.

### ΔRECD

Acumulación de ticks de reorganización modulados por el régimen. Opera la distinción Chronos (índice) vs Kairos (tiempo con peso de evento).

---

## 6. Surrogates — matemática del nulo

**Phase-shuffle independiente por canal**

1. FFT del canal.  
2. Aleatorizar fases.  
3. IFFT → misma densidad espectral aproximada, dependencia cruzada destruida.

Si el Δ de los datos es extremo respecto a la distribución de Δ en surrogates, obtiene p_surr bajo: evidencia de que la estructura **cruzada** importa.

**IAAFT** itera para ajustar también el histograma de amplitudes; más costoso; útil en modo full.

---

## 7. Checklist numérico antes de un claim

- [ ] N ≥ 2 (o proxy documentado)  
- [ ] W y stride justificados (preset o sensibilidad)  
- [ ] m, delay fijados y reportados  
- [ ] Evento o partición exploratoria **declarada**  
- [ ] Δτ_s y Δexcess3 con signo y magnitud  
- [ ] p_surr con n_surr y método  
- [ ] Panel EWS en paralelo  
- [ ] Hash y Methods exportados  

---

## 8. Errores matemáticos frecuentes

| Error | Corrección |
|-------|------------|
| Interpretar τ_s como correlación de Pearson | Es ordinal-relacional en ventanas |
| Publicar solo Φ₃ | Preferir excess3 + Φ₃ |
| n_surr = 2 para un paper | Usar decenas y sensibilidad a seed |
| Comparar dominios con W distintos sin decirlo | La escala temporal del reloj cambia |
| Tratar demos sintéticos como cohorte | Ground truth de diseño ≠ evidencia de campo |

---

*Handout de matemática práctica STP · usar junto al sandbox de la página Matemática.*
