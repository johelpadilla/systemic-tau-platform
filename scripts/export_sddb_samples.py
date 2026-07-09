#!/usr/bin/env python3
"""Export CCTP clean RR npz files to platform sample CSVs.

Usage:
  python scripts/export_sddb_samples.py \\
    --cctp-dir ~/grok-safe/Investigaciones/Cardiac_CCTP_Pilot \\
    --records 38,51
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def export_record(npz_path: Path, out_csv: Path) -> None:
    data = np.load(npz_path)
    # Flexible key detection
    keys = list(data.keys())
    rr = None
    for k in ("rr", "rr_ms", "RR", "rr_clean"):
        if k in data:
            rr = np.asarray(data[k], dtype=float).ravel()
            break
    if rr is None:
        # take first array
        rr = np.asarray(data[keys[0]], dtype=float).ravel()

    drr = np.abs(np.diff(rr, prepend=rr[0]))
    z_rr = (rr - rr.mean()) / (rr.std() + 1e-12)
    z_drr = (drr - drr.mean()) / (drr.std() + 1e-12)
    df = pd.DataFrame(
        {
            "t_beat": np.arange(len(rr)),
            "rr_ms": rr,
            "abs_drr": drr,
            "z_rr": z_rr,
            "z_abs_drr": z_drr,
        }
    )
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv} ({len(df)} rows)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--cctp-dir",
        type=Path,
        default=Path.home() / "grok-safe/Investigaciones/Cardiac_CCTP_Pilot",
    )
    ap.add_argument("--records", default="38,51")
    ap.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "samples",
    )
    args = ap.parse_args()
    for rec in args.records.split(","):
        rec = rec.strip()
        npz = args.cctp_dir / "data" / f"rr_{rec}_clean.npz"
        if not npz.exists():
            print(f"Skip missing {npz}")
            continue
        export_record(npz, args.out_dir / f"sddb_rr_{rec}.csv")


if __name__ == "__main__":
    main()
