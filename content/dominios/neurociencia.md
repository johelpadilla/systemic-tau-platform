# Dominio: Neurociencia — crisis epilépticas (CHB-MIT)

## 1. Contexto

Las **crisis epilépticas** son transiciones de régimen en dinámica cortical. El EEG multicanal es el prototipo de sistema donde:

- hay muchas variables (canales/bandas),
- el evento está anotado,
- el interés clínico es el **pre-ictal**.

CHB-MIT (PhysioNet) ofrece registros pediátricos con anotaciones de crisis.

## 2. Límites de EWS clásicas

- Un solo canal puede no mostrar CSD claro.
- Artefactos y sueño confunden var/AR1.
- La transición es **espacialmente distribuida**: la firma está en la **sincronización de patrones**, no solo en la potencia de un canal.

## 3. Aporte Tau + RECD

- Multivariado: bandpowers o envelopes de 4–8 canales/bandas.
- Φ₁–Φ₃ capturan **co-ordenación simbólica** pre-ictal.
- excess3 como proxy de configuración de red irreducible.
- Comparación con TE clásica y con índices de sincronización estándar (PLV, etc.) en modo Full.

## 4. Dataset

- Extracto procesado o sintético pre-ictal-like (el raw CHB-MIT no se redistribuye completo).
- Scripts de descarga bajo ToS PhysioNet.

## 5. Madurez

**Medio-Alto** en la plataforma v1: pipeline listo; evidencia empírica en curso de consolidación (menos madura que CCTP).

## 6. Referencias

- CHB-MIT PhysioNet; literatura de seizure prediction; marco ordinal del paradigma.
