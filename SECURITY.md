# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅        |
| < 1.0   | ❌        |

## Reporting a vulnerability

**Do not open a public GitHub issue for security vulnerabilities or exploit details.**

Email: **johel.padilla@upr.edu**  
Subject prefix: `[STP SECURITY]`

Please include:
- Affected component (Lab upload, CLI, Docker, etc.)
- Steps to reproduce
- Impact assessment
- Whether a fix is already known

We aim to acknowledge reports within **7 days** and provide a remediation plan or status update within **30 days** for confirmed issues.

## Scope notes

- The public web Lab is an **educational demo**. Treat uploaded CSVs as untrusted input; caps limit resource exhaustion but are not a sandbox.
- Do not upload secrets, PHI/PII, or credentials to public deployments.
- Optional scientific packages (`ripser`, `wfdb`, etc.) are out of band; report issues upstream when the root cause is external.
