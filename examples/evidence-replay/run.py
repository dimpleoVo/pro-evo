#!/usr/bin/env python3
"""Run the credential-free public Gate22 replay."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from open_core.replay import replay_gate22

result = replay_gate22(ROOT)
print("Gate22 public evidence replay")
for key in (
    "matched_pair_count", "g_target_resolution", "t_target_resolution",
    "g_verified_completion", "t_verified_completion",
    "strong_mechanism_trace_count", "public_only", "private_cot_used",
):
    print(f"{key} = {result[key]}")

