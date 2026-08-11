from pathlib import Path
from open_core.causal import load_pairs


ROOT = Path(__file__).resolve().parents[2]


def test_each_public_pair_has_one_pre_revision_checkpoint():
    pairs = load_pairs(ROOT / "evidence/gate22/summary.json")
    assert len(pairs) == 3

