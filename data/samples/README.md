# Sample datasets

| File | Origin | License note |
|------|--------|--------------|
| `sddb_rr_38_demo.csv` | Derived RR from PhysioNet SDDB record 38 (CCTP export) | Cite PhysioNet + SDDB; educational derived export, not raw `.dat` |
| `sddb_rr_51_demo.csv` | Derived RR from PhysioNet SDDB record 51 | Same as above |

Synthetic series are generated at runtime by `stp.data.generators` (no files here).

Re-export helper (requires local CCTP tree):

```bash
python scripts/export_sddb_samples.py --records 38,51
```
