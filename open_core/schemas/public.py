"""Small public data model; it deliberately contains no provider or runtime controls."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class ProcessEvent:
    event_id: str
    sequence: int
    kind: Literal["diagnosis", "checkpoint", "intervention", "behavior", "verification"]
    public_projection: str


@dataclass(frozen=True)
class OptimizationTarget:
    target_id: str
    diagnosis: str
    observable_success_condition: str


@dataclass(frozen=True)
class TreatmentOutcome:
    branch: Literal["generic", "treatment"]
    target_resolved: bool
    verified_completion: bool
    strong_mechanism_trace: bool


@dataclass(frozen=True)
class CausalPair:
    pair_id: str
    checkpoint_id: str
    target: OptimizationTarget
    generic: TreatmentOutcome
    treatment: TreatmentOutcome

