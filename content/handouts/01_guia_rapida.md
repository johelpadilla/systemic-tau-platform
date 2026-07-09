# Systemic Tau Platform — Guía rápida (1 página)

**Audiencia:** primera sesión · estudiante · visitante  
**Tiempo estimado:** 15–20 minutos  
**Versión de plataforma:** v1.0

---

## ¿Qué hace esta plataforma?

Ayuda a **enseñar, calcular y documentar** un análisis de **reorganización relacional ordinal** (τ_s + RECD) frente a las *early warning signals* clásicas (var, AR1, …).

No es un dispositivo clínico ni un sistema de trading.

---

## Ruta en 5 clics

| Paso | Dónde | Qué hacer |
|------|--------|-----------|
| 1 | **Home** | Leer el alcance del núcleo (qué está listo y qué no). |
| 2 | **Fundamentos** | τ_s vs EWS; RECD y excess3. |
| 3 | **Matemática** | Sandbox Bandt–Pompe (m=3 → 6 símbolos). |
| 4 | **Laboratorio** | Cargar un demo del catálogo → Analizar → Exportar. |
| 5 | **Evidencia** | Ver el ancla empírica CCTP/SDDB (no generalizar a ciegas). |

---

## Su primer experimento (recomendado)

1. Abra **Laboratorio**.
2. Catálogo → `synthetic_coupled_logistic` (switch de acoplamiento conocido).
3. Dominio: **Sintético** · modo **Fast** · surrogates 4–8.
4. Observe: Δτ_s grande vs el control `synthetic_ar_noise` (casi nulo).
5. Descargue el reporte **Markdown** y copie el **hash** de reproducibilidad.

**Pregunta de cierre:** ¿El Δ se mantiene extremo frente a phase-shuffle?

---

## Controles mentales (antes de interpretar)

- **N ≥ 2 variables** (o proxy RR + |ΔRR| como en CCTP).
- **Preset de dominio** antes de retocar W a mano.
- **Lectura dual:** τ_s/RECD **y** panel EWS clásico.
- **p_surr sin tamaño de efecto** no se publica solo.
- **Signo context-dependent:** subir o bajar puede ser informativo según el régimen.

---

## Documentos para profundizar

| Documento | Uso |
|-----------|-----|
| Manual de usuario | Operación completa del Lab y CLI |
| Teoría τ_s + RECD | Marco conceptual |
| Cheat-sheet del Lab | Parámetros y lectura en una hoja |
| FAQ | Malentendidos de posgrado y revisión |
| Checklist de análisis | Entrega de práctica / paper corto |

---

## CLI (opcional)

```bash
stp serve
stp analyze datos.csv --domain cardiology -o reporte.md --json resultado.json
```

---

*Material docente STP · uso académico con citación · no sustituye validación externa.*
