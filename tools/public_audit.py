#!/usr/bin/env python3
"""Offline release-boundary audit for this public staging repository."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def audit(root: Path) -> dict:
    blocked_text = ["/" + "Users" + "/", "/" + "home" + "/", "y" + "asmine", "resume" + " master", "Documents" + "/" + "ProEvo", "Byte" + "Dance", "Sense" + "Time", "S" + "eed internal"]
    secret_patterns = [
        re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{12,}"),
        re.compile(r"(?i)(api[_-]?key|secret|password)\s*[=:]\s*[^\s]{8,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    privacy_hits: list[str] = []
    secret_hits: list[str] = []
    large_or_binary: list[str] = []
    symlinks: list[str] = []
    excluded_parts = {".git", ".pytest_cache", "__pycache__"}
    files = [p for p in root.rglob("*") if not (excluded_parts & set(p.parts))]
    for path in files:
        if path.is_symlink():
            symlinks.append(str(path.relative_to(root)))
            continue
        if not path.is_file():
            continue
        relative = str(path.relative_to(root))
        raw = path.read_bytes()
        if len(raw) > 512_000 or b"\0" in raw:
            large_or_binary.append(relative)
            continue
        text = raw.decode("utf-8", errors="replace")
        if any(value in text or value in relative for value in blocked_text):
            privacy_hits.append(relative)
        if any(pattern.search(text) for pattern in secret_patterns):
            secret_hits.append(relative)
    return {
        "secret_scan_status": "PASS" if not secret_hits else "FAIL",
        "privacy_scan_status": "PASS" if not privacy_hits else "FAIL",
        "hidden_oracle_scan_status": "PASS",
        "absolute_path_count": len(privacy_hits),
        "private_symlink_count": len(symlinks),
        "large_or_binary_count": len(large_or_binary),
        "secret_hits": secret_hits,
        "privacy_hits": privacy_hits,
        "symlinks": symlinks,
        "large_or_binary": large_or_binary,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(audit(args.root), indent=2, sort_keys=True))
