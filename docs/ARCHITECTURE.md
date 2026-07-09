# Arquitectura técnica (resumen)

Ver el árbol completo y contratos en [`SPEC.md`](SPEC.md) y [`ENGINEERING.md`](ENGINEERING.md).

```text
Usuario
  │
  ▼
app/  (Streamlit multipage)
  │  session_state, cache, widgets
  ▼
src/stp/
  ├── education/   ← content/*.md, glossary
  ├── domains/     ← adapters por dominio
  ├── core/        ← ordinal, tau_s, recd, ews, surrogates, pipeline
  ├── visualization/
  ├── reports/
  └── data/
  │
  ▼ (opcional)
nested-recd / systemictau   ← paridad paper si instalados
```

**Regla:** la UI no implementa matemática; el core no importa Streamlit.
