from pathlib import Path

from tools.license_scope_audit import audit


ROOT = Path(__file__).resolve().parents[2]


def test_every_public_file_has_a_clear_scope_or_is_a_license_notice():
    actual = audit(ROOT)
    assert actual["license_scope_scan"] == "PASS"
    assert actual["open_core_license"] == "APACHE-2.0"
    assert actual["docs_license"] == "CC-BY-NC-4.0"
    assert actual["evidence_license"] == "CC-BY-NC-ND-4.0"
    assert actual["private_implementation_licensed"] is False
    assert actual["ambiguous_license_scope"] is False

