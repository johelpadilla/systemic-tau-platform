# Extensions opérationnelles — Breathing Window et TDA / Betti

**État :** **opérationnel** dans le Lab STP (pas « en développement »).

| Couche | Pièces | Rôle |
|-------|--------|------|
| **Noyau** | τ_s, RECD, EWS, surrogates, hash | Claim principale |
| **Extensions** | Breathing window, TDA β₀/β₁, mémoire ordinale | Complément / contraste |

Le Lab **ne dépend pas** du TDA ni du breathing. Lorsqu’ils sont activés, ils apparaissent dans l’onglet **Extensions**, le rapport et les Methods.

## Breathing
Plus de volatilité locale → W plus courte pour τ_s. Case ou mode Full ; lisez W(t).

## TDA
Betti-0/1 glissants sur nuages à plongement de retards. ripser si installé ; sinon 1-squelette VR.

## CLI
```bash
stp analyze data.csv --mode full
# ou
stp analyze data.csv --breathing --tda
```
