# Operational extensions — Breathing Window and TDA / Betti

**Status:** **operational** in the STP Lab (not “under development”).

| Layer | Pieces | Role |
|-------|--------|------|
| **Core** | τ_s, RECD, EWS, surrogates, hash | Main claim |
| **Extensions** | Breathing window, TDA β₀/β₁, ordinal memory | Complement / contrast |

The Lab **does not depend** on TDA or breathing. When enabled, they appear in the **Extensions** tab, report, and Methods.

## Breathing
Higher local volatility → shorter W for τ_s. Enable checkbox or Full mode; read W(t).

## TDA
Sliding Betti-0/1 on delay-embedded clouds. ripser if installed; else VR 1-skeleton.

## CLI
```bash
stp analyze data.csv --mode full
# or
stp analyze data.csv --breathing --tda
```
