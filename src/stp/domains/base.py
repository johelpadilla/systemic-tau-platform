"""Domain adapter ABC + helpers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class DomainBundle:
    """Prepared analysis matrix + metadata."""

    X: np.ndarray
    domain: str
    variables: list[str]
    event_index: int | None = None
    event_label: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)
    source: str = ""


class DomainAdapter(ABC):
    domain: str = "generic"
    label: str = "Generic"
    suggested_columns: list[str] = []
    default_params: dict[str, Any] = {}

    @abstractmethod
    def prepare(self, df: pd.DataFrame, **kwargs) -> DomainBundle:
        ...

    def hint(self) -> str:
        return f"Dominio {self.label}: use columnas numéricas y marque el evento si existe."


def select_numeric(df: pd.DataFrame, cols: list[str] | None = None) -> pd.DataFrame:
    num = df.select_dtypes(include=[np.number])
    if cols:
        keep = [c for c in cols if c in num.columns]
        if keep:
            return num[keep]
    return num
