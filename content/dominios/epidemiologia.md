# Dominio: Epidemiología — Dengue e hiper-persistencia

### Objetivos de aprendizaje
1. Transferir la gramática τ_s + RECD de cardio a un sistema socio-ecológico.
2. Explicar por qué var/AR1 confunden estacionalidad con proximidad a brote.
3. Formular una hipótesis falsable sobre coherencia ordinal cases–clima.

**Madurez empírica en v1.0:** ★★★★☆ — preprints y narrativa madura; la cohorte estrella de la plataforma sigue siendo CCTP.

---

## 1. Contexto científico

El **dengue** es un sistema socio-ecológico forzado por clima, vector (*Aedes*), inmunidad y movilidad humana. Las series de incidencia semanal muestran **brotes**, mesetas y a veces **hiper-persistencia**: el sistema se queda “pegado” en regímenes de transmisión elevada más de lo que un modelo simple de ruido predeciría.

Puerto Rico y series tipo **DengAI** (San Juan / Iquitos) son laboratorios naturales para early warning epidemiológico.

## 2. Por qué fallan o se quedan cortas las EWS clásicas

- La incidencia es **discreta, ruidosa y estacional**; var y AR1 confunden estacionalidad con proximidad a brote.
- El “sistema” no es solo `cases(t)`: es el **acoplamiento** cases–clima–vector.
- Umbrales univariados (percentiles de casos) alertan **tarde** o con muchos falsos positivos.
- Modelos ML predictivos pueden acertar el número y **opacar** el mecanismo de reorganización.

## 3. Valor diferencial de τ_s + RECD

| Aporte | Contenido |
|--------|-----------|
| Multivariado ordinal | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Hiper-persistencia ordinal | Lectura vía Φ₂ (relaciones que se sostienen) y capas de persistencia del marco Tau |
| RECD | “Reloj” del brote: ticks cuando la configuración conjunta se vuelve sinérgica |
| Comparabilidad | Mismo lenguaje que en cardiología/ecología → ciencia de sistemas, no silo epidemiológico |

## 4. Dataset de ejemplo

- DengAI San Juan weekly (sample en plataforma).
- Variables: cases, temperatura, precipitación (z-score).
- Anotación pedagógica de ventanas de brote (percentil alto o etiquetas históricas).

## 5. Interpretación

- Buscar **aumento de coherencia ordinal** cases–clima **antes** del pico de incidencia.
- excess3 alto sostenido ≈ régimen de transmisión con estructura conjunta rígida.
- Siempre contrastar con estacionalidad (nulls estacionales / surrogates).

## 6. Referencias

- Preprints dengue Tau/RECD del autor (2025–2026).
- DengAI DrivenData; literatura de early warning en enfermedades vectoriales.
