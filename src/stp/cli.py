"""CLI: analyze CSV and launch Streamlit lab."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd


def _ensure_src_path() -> Path:
    root = Path(__file__).resolve().parents[2]
    src = root / "src"
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))
    return root


def cmd_analyze(args: argparse.Namespace) -> int:
    _ensure_src_path()
    from stp.config.settings import AnalysisParams, DOMAIN_PRESETS
    from stp.core.pipeline import result_to_jsonable, run_analysis
    from stp.reports.markdown_report import render_markdown_report

    path = Path(args.input)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    df = pd.read_csv(path)
    num = df.select_dtypes(include=[np.number])
    if args.columns:
        cols = [c.strip() for c in args.columns.split(",") if c.strip()]
        cols = [c for c in cols if c in num.columns]
    else:
        cols = list(num.columns)[: min(3, num.shape[1])]
    if not cols:
        print("No numeric columns found.", file=sys.stderr)
        return 1
    X = num[cols].to_numpy(dtype=float)

    preset = DOMAIN_PRESETS.get(args.domain, DOMAIN_PRESETS["synthetic"])
    params = AnalysisParams(
        window=args.window or int(preset["window"]),
        stride=args.stride or int(preset["stride"]),
        m=args.m or int(preset.get("m", 3)),
        theta3=args.theta3 if args.theta3 is not None else float(preset["theta3"]),
        n_surrogates=args.surrogates,
        mode=args.mode,
        seed=args.seed,
        include_ews=True,
        include_breathing=args.breathing or args.mode == "full",
        include_tda=args.tda or args.mode == "full",
        include_memory=args.memory or args.mode == "full",
        surrogate_method=args.surrogate_method,
    )
    result = run_analysis(
        X,
        params,
        event_index=args.event,
        domain=args.domain,
        variables=cols,
    )

    out = Path(args.out) if args.out else path.with_suffix(".stp_report.md")
    out.write_text(render_markdown_report(result, domain=args.domain), encoding="utf-8")
    print(f"Wrote {out}")
    print(f"repro_hash={result.repro_hash}")
    print(f"delta_tau_s={result.metrics['delta_tau_s']:.6f}")
    print(f"delta_excess3={result.metrics['delta_excess3']:.6f}")
    if args.json:
        jpath = Path(args.json)
        jpath.write_text(json.dumps(result_to_jsonable(result), indent=2), encoding="utf-8")
        print(f"Wrote {jpath}")
    return 0


def cmd_serve(args: argparse.Namespace) -> int:
    root = _ensure_src_path()
    app = root / "app" / "Home.py"
    import os
    import subprocess

    env = os.environ.copy()
    env["PYTHONPATH"] = str(root / "src") + os.pathsep + env.get("PYTHONPATH", "")
    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(app),
        "--server.port",
        str(args.port),
    ]
    return subprocess.call(cmd, env=env, cwd=str(root))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="stp", description="Systemic Tau Platform CLI")
    sub = parser.add_subparsers(dest="command")

    p_an = sub.add_parser("analyze", help="Run pipeline on a CSV")
    p_an.add_argument("input", help="Input CSV path")
    p_an.add_argument("-o", "--out", help="Markdown report path")
    p_an.add_argument("--json", help="Optional JSON export path")
    p_an.add_argument("--domain", default="synthetic")
    p_an.add_argument("--columns", help="Comma-separated numeric columns")
    p_an.add_argument("--event", type=int, default=None, help="Event index")
    p_an.add_argument("--mode", choices=["fast", "full"], default="fast")
    p_an.add_argument("--window", type=int, default=None)
    p_an.add_argument("--stride", type=int, default=None)
    p_an.add_argument("--m", type=int, default=None)
    p_an.add_argument("--theta3", type=float, default=None)
    p_an.add_argument("--surrogates", type=int, default=8)
    p_an.add_argument("--surrogate-method", default="phase_shuffle", choices=["phase_shuffle", "iaaft"])
    p_an.add_argument("--seed", type=int, default=42)
    p_an.add_argument("--breathing", action="store_true", help="Adaptive breathing window for τ_s")
    p_an.add_argument("--tda", action="store_true", help="Sliding Betti-0/1 curves (TDA extension)")
    p_an.add_argument("--memory", action="store_true", help="Ordinal memory profiles")
    p_an.set_defaults(func=cmd_analyze)

    p_sv = sub.add_parser("serve", help="Launch Streamlit Lab")
    p_sv.add_argument("--port", type=int, default=8501)
    p_sv.set_defaults(func=cmd_serve)

    p_lab = sub.add_parser("lab", help="Alias for serve")
    p_lab.add_argument("--port", type=int, default=8501)
    p_lab.set_defaults(func=cmd_serve)

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(0)
    code = args.func(args)
    sys.exit(code or 0)


def run_streamlit() -> None:
    main(["serve"])


if __name__ == "__main__":
    main()
