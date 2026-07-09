"""Domain adapters."""

from __future__ import annotations

import numpy as np
import pandas as pd

from stp.domains import get_adapter


def test_cardiology_adapter_z_cols():
    df = pd.DataFrame(
        {
            "z_rr": np.random.randn(100),
            "z_abs_drr": np.random.randn(100),
            "noise": np.random.randn(100),
        }
    )
    b = get_adapter("cardiology").prepare(df)
    assert b.X.shape == (100, 2)
    assert b.domain == "cardiology"


def test_epidemiology_adapter():
    df = pd.DataFrame(
        {
            "cases": np.arange(50, dtype=float),
            "rain": np.random.rand(50) * 10,
            "temp": 25 + np.random.randn(50),
        }
    )
    b = get_adapter("epidemiology").prepare(df, event_index=30)
    assert b.event_index == 30
    assert b.X.shape[1] >= 2


def test_finance_close_to_ret():
    df = pd.DataFrame({"close": 100 + np.cumsum(np.random.randn(80) * 0.5)})
    b = get_adapter("finance").prepare(df)
    assert b.X.shape[1] == 2


def test_climate_adapter():
    df = pd.DataFrame(
        {
            "temp_anom": np.random.randn(60),
            "precip": np.abs(np.random.randn(60)),
            "soil_moisture": np.random.rand(60),
        }
    )
    b = get_adapter("climate").prepare(df, event_index=40)
    assert b.domain == "climate"
    assert b.X.shape == (60, 3)
    assert b.event_index == 40


def test_education_adapter():
    df = pd.DataFrame(
        {
            "engagement": np.random.rand(40),
            "peer_sync": np.random.rand(40),
            "cognitive_load": np.random.rand(40),
        }
    )
    b = get_adapter("education").prepare(df)
    assert b.domain == "education"
    assert b.X.shape[1] == 3
