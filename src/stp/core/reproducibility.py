"""Reproducibility hashes for analysis runs."""

from __future__ import annotations

import hashlib
import json
from typing import Any

import numpy as np

from stp import __version__


def data_fingerprint(X: np.ndarray) -> str:
    X = np.ascontiguousarray(np.asarray(X, dtype=np.float64))
    h = hashlib.sha256()
    h.update(str(X.shape).encode())
    h.update(X.tobytes())
    return h.hexdigest()[:16]


def repro_hash(params: dict[str, Any], X: np.ndarray, extra: dict | None = None) -> str:
    payload = {
        "params": params,
        "data_fp": data_fingerprint(X),
        "stp_version": __version__,
        "numpy": np.__version__,
        "extra": extra or {},
    }
    raw = json.dumps(payload, sort_keys=True, default=str)
    return hashlib.sha256(raw.encode()).hexdigest()
