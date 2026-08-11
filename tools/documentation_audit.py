#!/usr/bin/env python3
"""Offline audit for bilingual public documentation and shared figures."""
from __future__ import annotations

import json
from pathlib import Path
import re


EN_SECTIONS = (
    "Why Pro-Evo",
    "How to Read This Repository",
    "Strong Mechanism Attribution and Corrective Optimization Validation",
    "Same-Checkpoint Causal Validation",
    "Initial Target-Guided Recovery Validation: A Null Result",
    "Outcome-Level Causal Optimization Validation",
    "Open Core and Public Evidence Boundary",
    "Replay the Public Evidence",
    "Research Integrity and Scope Note",
    "License",
)
ZH_SECTIONS = (
    "为什么需要 Pro-Evo",
    "如何阅读本仓库",
    "Strong Mechanism Attribution and Corrective Optimization Validation",
    "Same-Checkpoint Causal Validation",
    "Initial Target-Guided Recovery Validation：一次真实的 Null Result",
    "Outcome-Level Causal Optimization Validation",
    "Open Core and Public Evidence Boundary",
    "Replay Public Evidence",
    "Research Integrity and Scope Note",
    "License",
)
EXPECTED_FIGURES = {
    "figures/evaluation-to-optimization.svg",
    "figures/strong-mechanism-result.svg",
    "figures/same-checkpoint-causal-design.svg",
    "figures/scientific-progression.svg",
    "figures/public-private-boundary.svg",
}


def _figures(text: str) -> set[str]:
    return set(re.findall(r"!\[[^]]*]\((figures/[^)]+\.svg)\)", text))


def _broken_relative_links(path: Path, text: str) -> list[str]:
    links = re.findall(r"(?<!!)\[[^]]*]\(([^)#]+)(?:#[^)]+)?\)", text)
    return sorted(link for link in links if not link.startswith(("http://", "https://")) and not (path.parent / link).exists())


def audit(root: Path) -> dict:
    english = (root / "README.md").read_text(encoding="utf-8")
    chinese = (root / "README.zh-CN.md").read_text(encoding="utf-8")
    narrative_files = [root / "README.md", root / "README.zh-CN.md", *sorted((root / "docs").glob("*.md")), *sorted((root / "figures").glob("*.svg"))]
    gate_count = sum(len(re.findall(r"Gate(?:20|21|22)\b", path.read_text(encoding="utf-8"))) for path in narrative_files)
    en_figures, zh_figures = _figures(english), _figures(chinese)
    markdown_files = [root / "README.md", root / "README.zh-CN.md", *root.glob("*.md"), *root.rglob("*.md")]
    broken = sorted({link for path in markdown_files if path.is_file() for link in _broken_relative_links(path, path.read_text(encoding="utf-8"))})
    return {
        "readme_en": "PASS" if all(section in english for section in EN_SECTIONS) else "FAIL",
        "readme_zh_cn": "PASS" if all(section in chinese for section in ZH_SECTIONS) else "FAIL",
        "bilingual_structure_parity": "PASS" if all(section in english for section in EN_SECTIONS) and all(section in chinese for section in ZH_SECTIONS) else "FAIL",
        "language_switch_en_to_zh": "PASS" if "[简体中文](README.zh-CN.md)" in english else "FAIL",
        "language_switch_zh_to_en": "PASS" if "[English](README.md)" in chinese else "FAIL",
        "shared_figure_set": "PASS" if en_figures == zh_figures == EXPECTED_FIGURES else "FAIL",
        "broken_link_scan": "PASS" if not broken else "FAIL",
        "broken_links": broken,
        "public_narrative_gate_number_count": gate_count,
    }


if __name__ == "__main__":
    print(json.dumps(audit(Path(__file__).resolve().parents[1]), indent=2, sort_keys=True))
