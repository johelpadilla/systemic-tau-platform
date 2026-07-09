# Frequently asked questions (deep answers)

These answers target real graduate-level and peer-review misunderstandings — not marketing FAQ.

---

## A. Concepts

### Is Systemic Tau just Kendall tau with marketing?

No. Kinship with rank statistics is real in the **ordinal substrate**, but the object of τ_s is the **dynamics of coupling reorganization** in windows, often multi-scale and tied to RECD. A static rank correlation does not define a clock or Φ₁–Φ₃ levels.

### How does it differ from Transfer Entropy?

| | Transfer Entropy | τ_s + RECD / excess3 |
|--|------------------|----------------------|
| Question | How much does A improve prediction of B? | How does joint ordinal structure reorganize and advance the clock? |
| Direction | Explicitly directional | Relational / synergistic (not a causal graph) |
| Use in v1.0 | Full-horizon | Lab core |

They are **complementary**. Do not substitute one for the other in a paper without justifying the question.

### Why Bandt–Pompe rather than SAX or other symbols?

Parsimony, monotone invariance, and a mature ecosystem (permutation entropy, paradigm papers). SAX and other alphabets are possible extensions; they are **not** the CCTP pilot standard nor the v1.0 core.

### What is “context-dependent sign”?

It means **Δτ_s or Δexcess3 may rise or fall** toward an event depending on regime (e.g. AF, pacing, outbreak phase). Evidence is played on: (1) change magnitude, (2) concordance among metrics, (3) surrogate p-values, (4) domain narrative — not a universal “always positive = bad” sign.

---

## B. Data and practice

### Can I use a single variable?

The core is multivariate (N≥2). With one series, the platform builds the proxy  
X=[z(x), z(|Δx|)]. That is a legitimate educational bridge, not a free pass for every univariate claim.

### How many surrogates?

Fast mode: few (exploration). Full: more. Report n, method (phase-shuffle / IAAFT), seed, and the event cut.

### What about TDA and Breathing Window?

Operational Lab **extensions**. Enable in Full or via checkboxes; read them in the Extensions tab. They do **not** replace τ_s + RECD + EWS + surrogates.

---

## C. Ethics and citation

### Can I claim clinical or operational readiness?

No for v1.0 product claims. Cardiology is the empirical anchor (CCTP/SDDB); other domains prioritize pedagogy and transfer. Scope every claim.

### How should I cite?

Cite the empirical paper/pilot for cardiac claims; for demos, state “pedagogical synthetic / domain-like demo” and ship Methods + repro hash.
