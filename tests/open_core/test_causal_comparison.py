from pathlib import Path
from open_core.causal import aggregate_pairs, load_pairs


ROOT = Path(__file__).resolve().parents[2]


def test_gate22_aggregate_is_the_public_claim():
    actual = aggregate_pairs(load_pairs(ROOT / "evidence/gate22/summary.json"))
    assert actual == {
        "matched_pair_count": 3,
        "g_target_resolution": 0,
        "t_target_resolution": 3,
        "g_verified_completion": 0,
        "t_verified_completion": 3,
        "strong_mechanism_trace_count": 3,
        "public_only": True,
        "private_cot_used": False,
    }

