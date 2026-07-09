"""Data generators and catalog."""

from stp.data.catalog import list_datasets, load_catalog, load_dataset
from stp.data.generators import (
    GENERATOR_REGISTRY,
    ar_noise,
    cardiac_like_rr,
    climate_like,
    coupled_logistic,
    dengue_like,
    ecology_like,
    education_like,
    eeg_like,
    finance_like,
    sleep_like,
    social_like,
)

__all__ = [
    "GENERATOR_REGISTRY",
    "ar_noise",
    "cardiac_like_rr",
    "climate_like",
    "coupled_logistic",
    "dengue_like",
    "ecology_like",
    "education_like",
    "eeg_like",
    "finance_like",
    "list_datasets",
    "load_catalog",
    "load_dataset",
    "sleep_like",
    "social_like",
]
