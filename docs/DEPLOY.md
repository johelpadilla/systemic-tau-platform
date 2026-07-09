# Deploy guide

## Recommended: Streamlit Community Cloud (fastest)

1. Push this repo to GitHub (`johelpadilla/systemic-tau-platform`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select the repo, branch `main`.
4. **Main file path:** `app/streamlit_app.py`
5. Python version: 3.11 if available.
6. Deploy. Free tier is suitable for educational demo traffic.

Notes:
- `packages.txt` is present (empty) for future system deps.
- `.streamlit/config.toml` sets `maxUploadSize = 15` and disables usage stats.
- Heavy Full + IAAFT jobs should use local CLI (`stp analyze`), not the public Lab.

## Docker

```bash
docker build -t systemic-tau-platform .
docker run --rm -p 8501:8501 systemic-tau-platform
# open http://localhost:8501
```

Healthcheck hits `/_stcore/health`.

## Local production-like

```bash
pip install -r requirements.txt && pip install -e .
streamlit run app/streamlit_app.py --server.port 8501 --server.headless true
```

## Environment

| Variable | Effect |
|----------|--------|
| `STP_LANG` | Default language (`es`, `en`, `fr`) before session override |
| `PYTHONPATH` | Should include `src` if not installed editable |

## Rollback

- Git tag: `v1.0.0-pre-launch-freeze` (pre public-readiness)
- Git tag: `v1.0.0` (this release)
- Sibling tarball: `systemic-tau-platform-freeze-prelaunch-*.tar.gz` next to the repo parent
