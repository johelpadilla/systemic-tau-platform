"""Template-based dual-reading interpretation (no LLM). Language-aware via stp.i18n."""

from __future__ import annotations

from typing import Any

from stp.i18n.core import get_lang, t


def interpret_dual_reading(
    metrics: dict[str, Any],
    surrogate_stats: dict[str, Any] | None = None,
    event_index: int | None = None,
    domain: str = "generic",
    lang: str | None = None,
) -> dict[str, Any]:
    """
    Build structured interpretation bullets from pipeline metrics.

    Returns title, summary, bullets, caution, flags.
    """
    lang = lang or get_lang()
    surr = (surrogate_stats or {}).get("tau_s", {})
    d_tau = float(metrics.get("delta_tau_s", 0.0))
    d_ex = float(metrics.get("delta_excess3", 0.0))
    mean_ex = float(metrics.get("mean_excess3", 0.0))
    p = surr.get("p_value")
    p_val = float(p) if p is not None else None

    flags: list[str] = []
    bullets: list[str] = []

    def _mag(v: float) -> str:
        a = abs(v)
        if a < 0.02:
            return t("interp.mag_small", lang=lang)
        if a < 0.08:
            return t("interp.mag_mod", lang=lang)
        return t("interp.mag_large", lang=lang)

    if d_tau > 0:
        direction = t("interp.dir_up", lang=lang)
    elif d_tau < 0:
        direction = t("interp.dir_down", lang=lang)
    else:
        direction = t("interp.dir_flat", lang=lang)

    bullets.append(
        t(
            "interp.bullet_dtau",
            lang=lang,
            d_tau=d_tau,
            mag=_mag(d_tau),
            direction=direction,
        )
    )

    if d_ex > 0:
        trend = t("interp.trend_up", lang=lang)
    elif d_ex < 0:
        trend = t("interp.trend_down", lang=lang)
    else:
        trend = t("interp.trend_flat", lang=lang)

    bullets.append(
        t(
            "interp.bullet_excess",
            lang=lang,
            mean_ex=mean_ex,
            d_ex=d_ex,
            mag=_mag(d_ex),
            trend=trend,
        )
    )

    if p_val is not None:
        if p_val <= 0.05 and abs(d_tau) >= 0.02:
            flags.append("surrogate_reject")
            bullets.append(t("interp.surr_reject", lang=lang, p=p_val))
        elif p_val <= 0.10:
            flags.append("surrogate_marginal")
            bullets.append(t("interp.surr_marginal", lang=lang, p=p_val))
        else:
            flags.append("surrogate_null")
            bullets.append(t("interp.surr_null", lang=lang, p=p_val))
    else:
        bullets.append(t("interp.surr_off", lang=lang))

    if event_index is not None:
        bullets.append(t("interp.event_on", lang=lang, t=event_index))
        flags.append("event_split")
    else:
        bullets.append(t("interp.event_off", lang=lang))

    domain_key = f"interp.dom_{domain}"
    domain_note = t(domain_key, lang=lang)
    if domain_note == domain_key:
        domain_note = t("interp.dom_generic", lang=lang)

    if metrics.get("tda"):
        db0 = float(metrics.get("delta_beta0", 0.0))
        db1 = float(metrics.get("delta_beta1", 0.0))
        backend = metrics.get("tda_backend", "vr_skeleton")
        bullets.append(
            t("interp.tda_bullet", lang=lang, backend=backend, db0=db0, db1=db1)
        )
        if abs(db0) >= 0.5 or abs(db1) >= 0.5:
            flags.append("tda_shift")
    if metrics.get("breathing"):
        bullets.append(t("interp.breathing_bullet", lang=lang))
        flags.append("breathing")

    same_sign = (d_tau * d_ex) > 0 and abs(d_tau) >= 0.02 and abs(d_ex) >= 0.01
    p_part = t("interp.p_part", lang=lang, p=p_val) if p_val is not None else ""
    if same_sign:
        flags.append("sign_concordance")
        summary = t(
            "interp.summary_concord",
            lang=lang,
            d_tau=d_tau,
            d_ex=d_ex,
            p_part=p_part,
        )
    elif abs(d_tau) < 0.02 and abs(d_ex) < 0.01:
        flags.append("quiet")
        summary = t("interp.summary_quiet", lang=lang)
    else:
        flags.append("mixed_panel")
        summary = t(
            "interp.summary_mixed",
            lang=lang,
            d_tau=d_tau,
            d_ex=d_ex,
        )

    caution = domain_note + t("interp.caution_tail", lang=lang)

    return {
        "title": t("interp.title", lang=lang),
        "summary": summary,
        "bullets": bullets,
        "caution": caution,
        "flags": flags,
        "domain": domain,
        "lang": lang,
    }


def methods_paragraph(
    params: Any,
    domain: str = "generic",
    event_index: int | None = None,
    surrogate_method: str = "phase_shuffle",
    n: int | None = None,
    repro_hash: str = "",
    lang: str | None = None,
) -> str:
    """Copy-ready Methods block. Scientific English is standard for Methods;
    FR/ES provide equivalent formal prose when UI language is set.
    """
    lang = lang or get_lang()
    p = params
    n = n if n is not None else getattr(p, "n_surrogates", 0)

    if lang == "es":
        split = (
            f"índice de evento t={event_index}"
            if event_index is not None
            else "partición temporal (1ª vs 2ª mitad de la serie de métricas)"
        )
        extras = []
        if getattr(p, "include_breathing", False):
            extras.append(
                f"Ventanas breathing adaptativas mapearon la volatilidad local a W impar ∈"
                f"[≈{max(5, p.window // 4)},{p.window}] para τ_s (mayor volatilidad → W más corta)."
            )
        if getattr(p, "include_tda", False):
            extras.append(
                "TDA en ventanas sobre nubes de puntos con embedding de retardos reportó curvas "
                "Betti-0/1 (ripser si está instalado; si no, proxy 1-esqueleto Vietoris–Rips)."
            )
        if getattr(p, "include_memory", False):
            extras.append(
                "Se computó memoria ordinal (MI simbólica lag-1 y cross-MI) como extensión."
            )
        extra_txt = (" " + " ".join(extras)) if extras else ""
        return (
            f"Las series multivariadas se estandarizaron (z-score) por canal. Systemic Tau (τ_s) se "
            f"computó como la media de Kendall-τ por pares en ventanas deslizantes (W={p.window}, "
            f"stride={p.stride}"
            f"{', breathing=on' if getattr(p, 'include_breathing', False) else ''}). "
            f"RECD ordinal anidado (Bandt–Pompe m={p.m}, delay={p.delay}, persistencia d={p.d_persist}, "
            f"θ₃={p.theta3}) produjo Φ₁–Φ₃, excess3 continuo y T_recd acumulado. "
            f"EWS clásicas (varianza, AR(1)) usaron el mismo W/stride base. "
            f"Nulos: surrogates independientes {surrogate_method} (n={n}, seed={p.seed}) "
            f"sobre el contraste Δτ_s definido por {split}.{extra_txt} "
            f"Preset de dominio: {domain}. "
            f"Hash de reproducibilidad (SHA-256): {repro_hash or '—'}. "
            f"Software: Systemic Tau Platform v1.0 (núcleo educativo + extensiones opcionales)."
        )

    if lang == "fr":
        split = (
            f"indice d’événement t={event_index}"
            if event_index is not None
            else "partition temporelle (1re vs 2e moitié de la série de métriques)"
        )
        extras = []
        if getattr(p, "include_breathing", False):
            extras.append(
                f"Des fenêtres breathing adaptatives ont mappé la volatilité locale sur W impair ∈"
                f"[≈{max(5, p.window // 4)},{p.window}] pour τ_s (volatilité plus élevée → W plus courte)."
            )
        if getattr(p, "include_tda", False):
            extras.append(
                "La TDA par fenêtres sur des nuages de points à plongement de retards a rapporté des "
                "courbes Betti-0/1 (ripser si installé ; sinon proxy 1-squelette Vietoris–Rips)."
            )
        if getattr(p, "include_memory", False):
            extras.append(
                "La mémoire ordinale (MI symbolique lag-1 et cross-MI) a été calculée comme extension."
            )
        extra_txt = (" " + " ".join(extras)) if extras else ""
        return (
            f"Les séries multivariées ont été standardisées (z-score) par canal. Le Systemic Tau (τ_s) "
            f"a été calculé comme la moyenne des Kendall-τ par paires dans des fenêtres glissantes "
            f"(W={p.window}, stride={p.stride}"
            f"{', breathing=on' if getattr(p, 'include_breathing', False) else ''}). "
            f"Le RECD ordinal emboîté (Bandt–Pompe m={p.m}, delay={p.delay}, persistance d={p.d_persist}, "
            f"θ₃={p.theta3}) a produit Φ₁–Φ₃, excess3 continu et T_recd cumulé. "
            f"Les EWS classiques (variance, AR(1)) ont utilisé le même W/stride de base. "
            f"Nuls : surrogates indépendants {surrogate_method} (n={n}, seed={p.seed}) "
            f"sur le contraste Δτ_s défini par {split}.{extra_txt} "
            f"Preset de domaine : {domain}. "
            f"Hash de reproductibilité (SHA-256) : {repro_hash or '—'}. "
            f"Logiciel : Systemic Tau Platform v1.0 (noyau éducatif + extensions optionnelles)."
        )

    # English (default scientific Methods prose)
    split = (
        f"event index t={event_index}"
        if event_index is not None
        else "temporal split (first vs second half of the metric series)"
    )
    extras = []
    if getattr(p, "include_breathing", False):
        extras.append(
            f"Adaptive breathing windows mapped local volatility to odd W∈[≈{max(5, p.window // 4)},{p.window}] "
            f"for τ_s (higher volatility → shorter W)."
        )
    if getattr(p, "include_tda", False):
        extras.append(
            "Sliding-window TDA on delay-embedded point clouds reported Betti-0/1 curves "
            "(ripser if installed, else Vietoris–Rips 1-skeleton proxy)."
        )
    if getattr(p, "include_memory", False):
        extras.append(
            "Ordinal memory (symbolic MI lag-1 and cross-MI) was computed as an extension."
        )
    extra_txt = (" " + " ".join(extras)) if extras else ""

    return (
        f"Multivariate series were z-scored per channel. Systemic Tau (τ_s) was computed as the "
        f"mean pairwise Kendall-τ in sliding windows (W={p.window}, stride={p.stride}"
        f"{', breathing=on' if getattr(p, 'include_breathing', False) else ''}). "
        f"Nested ordinal RECD (Bandt–Pompe m={p.m}, delay={p.delay}, persistence d={p.d_persist}, "
        f"θ₃={p.theta3}) produced Φ₁–Φ₃, continuous excess3 and cumulative T_recd. "
        f"Classical EWS (variance, AR(1)) used the same base W/stride for comparison. "
        f"Null models used independent {surrogate_method} surrogates (n={n}, seed={p.seed}) "
        f"on the Δτ_s contrast defined by {split}.{extra_txt} "
        f"Analysis domain preset: {domain}. "
        f"Reproducibility hash (SHA-256): {repro_hash or '—'}. "
        f"Software: Systemic Tau Platform v1.0 (educational core + optional extensions)."
    )
