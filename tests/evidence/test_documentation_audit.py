from pathlib import Path

from tools.documentation_audit import audit


ROOT = Path(__file__).resolve().parents[2]


def test_public_bilingual_documentation_has_parity_and_no_gate_narrative():
    result = audit(ROOT)
    assert result["readme_en"] == "PASS"
    assert result["readme_zh_cn"] == "PASS"
    assert result["bilingual_structure_parity"] == "PASS"
    assert result["language_switch_en_to_zh"] == "PASS"
    assert result["language_switch_zh_to_en"] == "PASS"
    assert result["shared_figure_set"] == "PASS"
    assert result["broken_link_scan"] == "PASS"
    assert result["public_narrative_gate_number_count"] == 0
