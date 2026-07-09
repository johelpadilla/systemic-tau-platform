"""Markdown report generation."""

from __future__ import annotations

from datetime import datetime, timezone

from stp.core.pipeline import AnalysisResult


def render_markdown_report(
    result: AnalysisResult,
    title: str = "Systemic Tau Platform — Analysis Report",
    domain: str = "generic",
) -> str:
    m = result.metrics
    p = result.params
    surr = result.surrogate_stats.get("tau_s", {})
    lines = [
        f"# {title}",
        "",
        f"**Generated (UTC):** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Domain:** {domain}",
        f"**Reproducibility hash:** `{result.repro_hash}`",
        f"**STP version:** {result.lib_versions.get('stp', '?')}",
        "",
        "## Parameters",
        "",
        f"- mode: `{p.mode}`",
        f"- window: `{p.window}`, stride: `{p.stride}`",
        f"- m: `{p.m}`, delay: `{p.delay}`, d_persist: `{p.d_persist}`",
        f"- θ₃: `{p.theta3}`, n_surrogates: `{p.n_surrogates}`, seed: `{p.seed}`",
        "",
        "## Key metrics",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| mean τ_s | {m.get('mean_tau_s', float('nan')):.6f} |",
        f"| Δτ_s (2nd half − 1st) | {m.get('delta_tau_s', float('nan')):.6f} |",
        f"| mean excess3 | {m.get('mean_excess3', float('nan')):.6f} |",
        f"| Δexcess3 | {m.get('delta_excess3', float('nan')):.6f} |",
        f"| final T_recd | {m.get('final_T_recd', float('nan')):.4f} |",
        "",
    ]
    if surr:
        lines += [
            "## Surrogates (τ_s)",
            "",
            f"- observed Δ: `{surr.get('observed_delta', float('nan')):.6f}`",
            f"- p-value (phase-shuffle): `{surr.get('p_value', float('nan')):.4f}`",
            f"- n: `{surr.get('n', 0)}`",
            "",
        ]
    lines += [
        "## Interpretation notes",
        "",
        "- Δ metrics use a simple temporal split (first vs second half) when no event index is provided.",
        "- Sign of Δτ_s / Δexcess3 is **context-dependent**; interpret with domain knowledge and quality flags.",
        "- Classical EWS (var, AR1) are comparative panels, not substitutes for ordinal relational metrics.",
        "",
        "---",
        "*Systemic Tau Platform — Paradigma Tau Sistémico: De la Teoría a la Práctica*",
        "",
    ]
    return "\n".join(lines)
