# Dominio: Epidemiología — Dengue e hiper-persistencia

## 1. Contexto científico

El **dengue** es un sistema socio-ecológico forzado por clima, vector (*Aedes*), inmunidad y movilidad humana. Las series de incidencia semanal muestran **brotes**, mesetas y a veces **hiper-persistencia**: el sistema se queda “pegado” en regímenes de transmisión elevada más de lo que un modelo simple de ruido predeciría.

Puerto Rico y series tipo **DengAI** (San Juan / Iquitos) son laboratorios naturales para early warning epidemiológico.

## 2. Por qué fallan o se quedan cortas las EWS clásicas

- La incidencia es **discreta, ruidosa y estacional**; la varianza y el AR(1) confunden estacionalidad con proximidad a brote.
- El “sistema” no es unilineal: requiere integrar **modelos de orden fraccionario** (donde la memoria de huevos quiescentes retrasa el sistema) o evaluar explícitamente el acoplamiento *casos–clima–vector*.
- Umbrales univariados fallan sistemáticamente ante el ruido biológico urbano.
- Los modelos predictivos ML o SEIR clásicos (orden entero) sufren por el "olvido", opacando los verdaderos puntos de bifurcación y de reorganización relacional profunda.

## 3. Valor diferencial de τ_s + RECD

| Aporte | Contenido |
|--------|-----------|
| Multivariado ordinal | \(X = [z(\mathrm{cases}), z(\mathrm{temp}), z(\mathrm{precip}), \ldots]\) |
| Hiper-persistencia | Captura los retardos fraccionarios debidos a la latencia/memoria biológica del vector. |
| Antisincronización Vectorial | Capacidad única de detectar divergencia en antifase (\(\tau_s \le -0.41\)) entre el clima favorable y poblaciones diezmadas por fumigación. |
| RECD (Reloj Epidémico) | Reemplaza el tiempo cronológico por un **tiempo epidemiológico efectivo**; "ticks" asimétricos marcan la reorganización y permiten predicciones adelantadas (4-6 semanas). |

## 4. Dataset de ejemplo

- DengAI San Juan weekly (sample en plataforma).
- Variables: cases, temperatura, precipitación (z-score).
- Anotación pedagógica de ventanas de brote (percentil alto o etiquetas históricas).

## 5. Interpretación

- Buscar el ingreso al **rango caótico genuino (\(|\tau_s| < 0.41\))**, el cual estadísticamente **precede los picos poblacionales con una anticipación de 4-6 semanas**.
- Identificar regímenes de **sincronización fuerte (\(\tau_s \ge +0.50\))**, característicos de los periodos post-intervención vectorial estable.
- Estudiar periodos de **antisincronización (\(\tau_s \le -0.41\))**, donde se da la *retrocausalidad local*: el clima sube la presión, pero la densidad larvaria se reduce forzadamente, invirtiendo temporalmente el reloj epidemiológico.
- Contrastar empíricamente que la imputación de datos faltantes en áreas marginales no destruye las invariantes ordinales.

## 6. Referencias

- Preprints dengue Tau/RECD del autor (2025–2026).
- DengAI DrivenData; literatura de early warning en enfermedades vectoriales.
