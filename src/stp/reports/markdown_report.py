"""Markdown report generation + Methods block (language-aware)."""

from __future__ import annotations

from datetime import datetime, timezone

from stp.core.pipeline import AnalysisResult
from stp.i18n.core import get_lang, t


def render_markdown_report(
    result: AnalysisResult,
    title: str | None = None,
    domain: str | None = None,
    lang: str | None = None,
) -> str:
    lang = lang or get_lang()
    title = title or t("report.title", lang=lang)
    m = result.metrics
    p = result.params
    domain = domain or result.domain or "generic"
    surr = result.surrogate_stats.get("tau_s", {})
    interp = result.interpretation or {}
    lines = [
        f"# {title}",
        "",
        f"**{t('report.generated', lang=lang)}:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}",
        f"**{t('report.domain', lang=lang)}:** {domain}",
        f"**{t('report.repro', lang=lang)}:** `{result.repro_hash}`",
        f"**{t('report.version', lang=lang)}:** {result.lib_versions.get('stp', '?')}",
        "",
        f"## {t('report.params', lang=lang)}",
        "",
        f"- mode: `{p.mode}`",
        f"- window: `{p.window}`, stride: `{p.stride}`",
        f"- m: `{p.m}`, delay: `{p.delay}`, d_persist: `{p.d_persist}`",
        f"- θ₃: `{p.theta3}`, n_surrogates: `{p.n_surrogates}`, seed: `{p.seed}`",
        f"- surrogate_method: `{p.surrogate_method}`",
        f"- breathing: `{p.include_breathing}`, tda: `{p.include_tda}`, ordinal_memory: `{p.include_memory}`",
        f"- event_index: `{result.event_index}`",
        f"- tda_backend: `{result.lib_versions.get('tda_backend', 'off')}`",
        "",
        f"## {t('report.metrics', lang=lang)}",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| mean τ_s | {m.get('mean_tau_s', float('nan')):.6f} |",
        f"| Δτ_s | {m.get('delta_tau_s', float('nan')):.6f} |",
        f"| mean excess3 | {m.get('mean_excess3', float('nan')):.6f} |",
        f"| Δexcess3 | {m.get('delta_excess3', float('nan')):.6f} |",
        f"| final T_recd | {m.get('final_T_recd', float('nan')):.4f} |",
        "",
    ]
    if p.include_tda and m.get("mean_beta0") is not None:
        lines += [
            f"### {t('report.extensions', lang=lang)} — TDA (Betti)",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| mean β₀ | {m.get('mean_beta0', float('nan')):.4f} |",
            f"| mean β₁ | {m.get('mean_beta1', float('nan')):.4f} |",
            f"| Δβ₀ | {m.get('delta_beta0', float('nan')):.4f} |",
            f"| Δβ₁ | {m.get('delta_beta1', float('nan')):.4f} |",
            f"| backend | {m.get('tda_backend', '—')} |",
            "",
        ]
    if p.include_breathing:
        lines += [
            f"### {t('report.extensions', lang=lang)} — Breathing",
            "",
            "τ_s · W adaptive (Methods).",
            "",
        ]
    if surr:
        lines += [
            "## Surrogates (τ_s)",
            "",
            f"- method: `{surr.get('method', p.surrogate_method)}`",
            f"- observed Δ: `{surr.get('observed_delta', float('nan')):.6f}`",
            f"- p-value: `{surr.get('p_value', float('nan')):.4f}`",
            f"- n: `{surr.get('n', 0)}`",
            "",
        ]
    if interp:
        lines += [
            f"## {t('report.interpretation', lang=lang)}",
            "",
            f"**{interp.get('summary', '')}**",
            "",
        ]
        for b in interp.get("bullets") or []:
            lines.append(f"- {b}")
        lines += ["", f"_{interp.get('caution', '')}_", ""]

    lines += [
        f"## {t('report.methods', lang=lang)}",
        "",
        result.methods_text or "_—_",
        "",
        "---",
        "*Systemic Tau Platform*",
        "",
    ]
    return "\n".join(lines)


def render_methods_only(result: AnalysisResult) -> str:
    return (result.methods_text or "").strip() + "\n"
