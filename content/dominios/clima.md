# Dominio: Clima e hidrología — sequía y regímenes hidro-climáticos

### Objetivos de aprendizaje
1. Conectar la literatura clásica de **umbrales críticos** (CSD) con observables **ordinales multivariados**.
2. Distinguir un cambio de nivel (más calor) de una **reorganización relacional** temp–precip–suelo.
3. Formular una hipótesis falsable sobre el latente de sequía sin pretender un modelo de predicción operativa.

**Madurez empírica en v1.0:** ★★★☆☆ — pedagogía fuerte y puente con CSD; no es un producto de forecast climático.

---

## 1. Contexto científico

Sequías y flips hidro-climáticos se estudian con indicadores de temperatura, precipitación y humedad del suelo. La pregunta clásica de *early warning* es: ¿el sistema se acerca a un régimen seco irreversible? La pregunta de τ_s es distinta y complementaria: **¿cómo se reordenan las relaciones** entre esas variables cuando aparece un forzado compartido (latente de sequía)?

## 2. Por qué no basta el panel clásico

- La estacionalidad confunde var/AR1.
- Un solo índice de sequía colapsa la estructura multivariada.
- El “evento” a menudo es un **régimen**, no un instante puntual.

## 3. Valor de τ_s + RECD

| Aporte | Contenido |
|--------|-----------|
| Triada climática | \(X = [\mathrm{temp}, \mathrm{precip}, \mathrm{soil}]\) |
| Reorganización | El latente de sequía acopla canales que antes eran casi estacionales e independientes |
| Comparabilidad | Mismo lenguaje que lagos (ecología) y brotes (epidemiología) |

## 4. Dataset de ejemplo

- `climate_drought_demo`: sintético con evento marcado (inicio del régimen seco).
- Ground truth de diseño: latente compartido post-evento (no datos satelitales reales en v1.0).

## 5. Madurez y ética de uso

**Media — énfasis docente.** Sirve para enseñar transferencia metodológica y lectura dual, no para alertas oficiales de sequía.

## 6. Referencias de contexto

- Scheffer et al., critical transitions / CSD.
- Literatura de drought indices (SPI, SPEI) como contraste univariado.
