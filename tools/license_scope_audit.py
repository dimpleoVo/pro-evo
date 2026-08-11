#!/usr/bin/env python3
"""Deterministic scope check for the repository's path-scoped licenses."""
from __future__ import annotations

import json
from pathlib import Path


APACHE = ("open_core/", "examples/", "tests/", "tools/", "pyproject.toml", ".gitignore")
DOCS = ("docs/", "README.md", "CLAIM_BOUNDARY.md", "PUBLIC_RELEASE_SCOPE.md", "SECURITY_AND_PRIVACY.md")
EVIDENCE = ("evidence/", "figures/", "release/")
NOTICE = ("LICENSE.md", "LICENSES/")


def _scope(path: str) -> str | None:
    for prefix in APACHE:
        if path == prefix or path.startswith(prefix):
            return "APACHE-2.0"
    for prefix in DOCS:
        if path == prefix or path.startswith(prefix):
            return "CC-BY-NC-4.0"
    for prefix in EVIDENCE:
        if path == prefix or path.startswith(prefix):
            return "CC-BY-NC-ND-4.0"
    for prefix in NOTICE:
        if path == prefix or path.startswith(prefix):
            return "LICENSE_NOTICE"
    return None


def audit(root: Path) -> dict:
    excluded_parts = {".git", ".pytest_cache", "__pycache__"}
    tracked = [
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file() and not (excluded_parts & set(path.parts))
    ]
    unscoped = sorted(path for path in tracked if _scope(path) is None)
    license_notice = (root / "LICENSE.md").read_text(encoding="utf-8")
    required_files = {
        "Apache-2.0.txt": "Apache License",
        "CC-BY-NC-4.0.txt": "Attribution-NonCommercial 4.0 International",
        "CC-BY-NC-ND-4.0.txt": "Attribution-NonCommercial-NoDerivatives 4.0 International",
    }
    missing_or_invalid = [name for name, marker in required_files.items() if marker not in (root / "LICENSES" / name).read_text(encoding="utf-8")]
    scope_markers = ["Open Core and Public Evidence Release", "not included", "No license is granted"]
    return {
        "open_core_license": "APACHE-2.0",
        "docs_license": "CC-BY-NC-4.0",
        "evidence_license": "CC-BY-NC-ND-4.0",
        "private_implementation_licensed": False,
        "ambiguous_license_scope": bool(unscoped or missing_or_invalid or any(marker not in license_notice for marker in scope_markers)),
        "unscoped_paths": unscoped,
        "missing_or_invalid_license_files": missing_or_invalid,
        "license_scope_scan": "PASS" if not unscoped and not missing_or_invalid and all(marker in license_notice for marker in scope_markers) else "FAIL",
    }


if __name__ == "__main__":
    print(json.dumps(audit(Path(__file__).resolve().parents[1]), indent=2, sort_keys=True))
