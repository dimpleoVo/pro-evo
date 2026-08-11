"""Deterministic aggregation over sanitized same-checkpoint evidence."""
from __future__ import annotations

from pathlib import Path
import json
from typing import Any


REQUIRED_CHAIN = (
    "public_failure",
    "process_diagnosis",
    "pre_revision_checkpoint",
    "same_checkpoint_branches",
    "target_guided_intervention",
    "observable_behavior_divergence",
    "post_treatment_revision",
    "public_reverification",
)


def load_pairs(path: str | Path) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    pairs = data["matched_pairs"]
    for pair in pairs:
        if pair["generic"]["checkpoint_id"] != pair["treatment"]["checkpoint_id"]:
            raise ValueError(f"{pair['pair_id']} is not same-checkpoint")
    return pairs


def aggregate_pairs(pairs: list[dict[str, Any]]) -> dict[str, int | bool]:
    generic = [pair["generic"] for pair in pairs]
    treatment = [pair["treatment"] for pair in pairs]
    strong = sum(
        all(step in pair["treatment"]["public_chain"] for step in REQUIRED_CHAIN)
        and pair["treatment"]["target_resolved"]
        and pair["treatment"]["verified_completion"]
        for pair in pairs
    )
    return {
        "matched_pair_count": len(pairs),
        "g_target_resolution": sum(x["target_resolved"] for x in generic),
        "t_target_resolution": sum(x["target_resolved"] for x in treatment),
        "g_verified_completion": sum(x["verified_completion"] for x in generic),
        "t_verified_completion": sum(x["verified_completion"] for x in treatment),
        "strong_mechanism_trace_count": strong,
        "public_only": True,
        "private_cot_used": False,
    }

