# Licenses and use

## Platform software

- **MIT** license (see `LICENSE` at the repository root).
- Author: Johel Padilla-Villanueva (ORCID [0000-0002-5797-6931](https://orcid.org/0000-0002-5797-6931)).
- Repository: https://github.com/johelpadilla/systemic-tau-platform
- Contact: johel.padilla@upr.edu

## Third-party data and included demos

| Source | What STP ships | Condition |
|--------|----------------|-----------|
| PhysioNet **SDDB** | Demo CSVs `sddb_rr_38_demo.csv`, `sddb_rr_51_demo.csv` — **derived/processed RR** for teaching (not raw `.dat` files) | Follow [PhysioNet ToS / data use agreements](https://physionet.org/); **cite** SDDB and the domain paper; do not present demos as clinical diagnosis |
| STP synthetic generators | Logistic / AR / dengue-like / EEG-like / etc. | MIT via this software; free use with platform citation |
| DengAI / open challenges | Mentions / educational pipelines only | Per challenge license |
| NTL LTER | Cite data papers; respect use policy | Do not repackage raw data without permission |
| Market prices | Synthetic volatility demos | Educational use; no proprietary feeds |

### PhysioNet / SDDB — explicit note

Demo CSVs are **not** a redistribution of the full SDDB database. They are cleaned RR exports for reproducing the Lab flow and the CCTP pilot grammar. Anyone publishing results must:

1. Cite PhysioNet and the relevant SDDB reference.
2. Cite the CCTP preprint/paper or domain paper used.
3. Not claim equivalence to credentialed PhysioNet access or clinical use.

## Privacy of web Lab uploads

- Processed in **session** (Streamlit process memory).
- **No** upload database in v1.0.
- **No** model retraining on user data.
- Do not upload PHI/PII or secrets to public deployments.

## Minimum citation

When publishing results obtained with the platform, cite:

1. The domain preprint/paper.
2. This platform: *Systemic Tau Platform* v1.0 (MIT), https://github.com/johelpadilla/systemic-tau-platform
3. The original dataset (e.g. PhysioNet SDDB).
4. Optional: `systemictau` / `nested-recd` if used as the engine.

## Disclaimer

Not a medical device. Not investment advice. Not a diagnostic system. Results require independent scientific validation before operational use.
