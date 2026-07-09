# Changelog

All notable changes to Systemic Tau Platform are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] — 2026-07-09

### Added
- Full educational Streamlit app (Home + 9 pages): Fundamentos, Matemática, Dominios, Laboratorio, Ruta, Evidencia, Docencia, Materiales, About & Legal.
- Core pipeline: τ_s, RECD (Φ₁–Φ₃, excess3), classical EWS, phase-shuffle + IAAFT surrogates, repro hash.
- Lab extensions: breathing window, ordinal memory, TDA Betti (ripser optional / VR fallback).
- Multi-domain catalog + adapters; deep-links Domain/Ruta → Lab.
- i18n: Spanish (source), English, French — UI catalogs + educational content.
- Downloadable handouts / packs; CLI `stp analyze` / `stp serve`.
- Public-readiness: disclaimer & privacy banners, Lab anti-abuse caps, `st.navigation` localized labels.
- Docker image, Streamlit production config, GitHub Actions CI + AppTest smoke script.
- OSS docs: CONTRIBUTING, SECURITY, DEPLOY, this changelog.

### Security
- Public Lab caps: CSV rows/columns/MB, surrogate count; maxUploadSize 15 MB.
- Upload privacy notice (session-only processing).

### Fixed
- Safe multipage `page_link` outside full Streamlit multipage sessions.
- `set_page_config` under `st.navigation` (safe wrapper).

## [1.0.0-pre-launch-freeze] — 2026-07-09

Baseline snapshot before public-readiness work. Tag: `v1.0.0-pre-launch-freeze`.
Restore: `git checkout v1.0.0-pre-launch-freeze` or sibling freeze tarball.
