# Preguntas frecuentes (respuestas profundas)

## ¿Tau Sistémica es solo un Kendall tau con marketing?

No. El parentesco con estadísticas de rangos (Kendall y afines) es real en el **sustrato ordinal**, pero el objeto de τ_s es la **dinámica de reorganización del acoplamiento** en ventanas, a menudo multiescala y acoplada al RECD. Un coeficiente de correlación de rangos estático no define un reloj ni niveles Φ₁–Φ₃.

## ¿Por qué el signo de Δτ_s / Δexcess3 no es siempre positivo?

Porque la métrica mide **reorganización**, no “proximidad a un umbral en un potencial 1D”. En FV, FA o pacing, el sistema puede **ganar o perder** estructura sinérgica según el contexto. La evidencia se juega en **magnitud + surrogates + concordancia**, no en un signo universal.

## ¿Puedo usarlo con una sola variable?

El núcleo es multivariado (N≥2). Si solo tiene una serie, la plataforma puede construir un proxy \(X=[z(x), z(|\Delta x|)]\) (patrón CCTP). Es un compromiso legítimo, no magia: está haciendo explícita la relación nivel–variación.

## ¿Esto predice la muerte súbita o un brote de dengue?

**No como dispositivo clínico/operativo certificado.** Es un marco de investigación y docencia. Cualquier uso prospectivo exige validación externa, calibración de umbrales y gobernanza ética.

## ¿En qué se diferencia de Transfer Entropy?

TE estima **flujo de información direccional**. RECD/excess3 estiman **niveles de conjunción ordinal y sinergia** orientados a un reloj emergente. Son complementarios: el Lab Full puede mostrar ambos.

## ¿Por qué Bandt–Pompe y no SAX u otros símbolos?

Por parsimonia, invariancia monótona, y ecosistema maduro (entropía de permutación, papers del paradigma). SAX u otros alfabetos son extensiones posibles; no son el estándar del piloto CCTP.

## ¿Qué debo citar?

1. El paper/preprint del dominio que use (p.ej. CCTP para cardio).
2. El software (`systemictau`, `nested-recd`, esta plataforma).
3. El dataset original (PhysioNet, LTER, etc.).
