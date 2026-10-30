"""Helpers for the CircuitNet-N28 congestion data (Day 6)."""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

# Example file name: 4489-RISCY-FPU-a-1-c20-u0.85-m4-p1-f0
# Fields (names inferred from the paper's knobs; confirm against the dataset docs):
#   sample_id, design, placement_idx, clock (period in ns), util, macros, power_mesh, filler
# One sample in the dataset has "mNone" for the macros field, so macros may be missing.
SAMPLE_PATTERN = re.compile(
    r"^(?P<sample_id>\d+)-(?P<design>.+?)-(?P<placement_idx>\d+)"
    r"-c(?P<clock>\d+)-u(?P<util>\d+(?:\.\d+)?)-m(?P<macros>\d+|None)"
    r"-p(?P<power_mesh>\d+)-f(?P<filler>\d+)(?:\.npy)?$"
)


def parse_sample_name(name: str) -> dict | None:
    """Return the fields of a sample file name, or None if it does not match."""
    m = SAMPLE_PATTERN.match(name)
    if m is None:
        return None
    d = m.groupdict()
    return {
        "sample_id": int(d["sample_id"]),
        "design": d["design"],
        "placement_idx": int(d["placement_idx"]),
        "clock": int(d["clock"]),
        "util": float(d["util"]),
        "macros": None if d["macros"] == "None" else int(d["macros"]),
        "power_mesh": int(d["power_mesh"]),
        "filler": int(d["filler"]),
    }


def build_metadata(names: list[str]) -> tuple[pd.DataFrame, list[str]]:
    """Parse many names. Returns (table, names that failed to parse)."""
    rows, failed = [], []
    for n in names:
        parsed = parse_sample_name(n)
        if parsed is None:
            failed.append(n)
        else:
            parsed["file"] = n
            rows.append(parsed)
    return pd.DataFrame(rows), failed


def label_stats(a: np.ndarray) -> dict:
    """Per-map statistics used in the EDA."""
    return {
        "shape": a.shape,
        "min": float(a.min()),
        "max": float(a.max()),
        "mean": float(a.mean()),
        "frac_gt1": float((a > 1).mean()),
        "frac_eq1": float(np.isclose(a, 1.0).mean()),
        "frac_nonzero": float((a > 0).mean()),
    }
