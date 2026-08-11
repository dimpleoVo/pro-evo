from __future__ import annotations

from pathlib import Path
from open_core.causal import aggregate_pairs, load_pairs


def replay_gate22(repo_root: str | Path) -> dict:
    root = Path(repo_root)
    pairs = load_pairs(root / "evidence/gate22/summary.json")
    return aggregate_pairs(pairs)

