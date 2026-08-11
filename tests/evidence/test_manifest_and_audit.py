import hashlib
import json
from pathlib import Path

from tools.public_audit import audit


ROOT = Path(__file__).resolve().parents[2]


def test_gate22_evidence_manifest_hashes_and_safety_flags():
    manifest = json.loads((ROOT / "evidence/gate22/public-evidence-manifest.json").read_text())
    for item in manifest["artifacts"]:
        actual = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
        assert actual == item["public_sha256"]
    assert manifest["contains_private_path"] is False
    assert manifest["contains_hidden_oracle"] is False
    assert manifest["contains_private_cot"] is False
    assert manifest["contains_raw_provider_body"] is False


def test_release_boundary_audit_passes():
    result = audit(ROOT)
    assert result["secret_scan_status"] == "PASS"
    assert result["privacy_scan_status"] == "PASS"
    assert result["private_symlink_count"] == 0
    assert result["large_or_binary_count"] == 0

