"""Tests for the E-group root-key probe helper."""

import importlib.util
from pathlib import Path


def _load_probe_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "probe_e_group.py"
    spec = importlib.util.spec_from_file_location("probe_e_group", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_root_item_shape_detects_special_decc_item_key() -> None:
    probe = _load_probe_module()

    result = probe._root_item_shape(
        {"Decc": {"decc": {"사건명": "영업정지처분취소청구"}}},
        "acrSpecialDecc",
    )

    assert result == {
        "target": "acrSpecialDecc",
        "root_key": "Decc",
        "item_key": "decc",
        "item_type": "dict",
        "status": "ok",
    }


def test_root_item_shape_ignores_metadata_keys_for_cgm_expc() -> None:
    probe = _load_probe_module()

    result = probe._root_item_shape(
        {
            "CgmExpc": {
                "target": "dapaCgmExpc",
                "totalCnt": "1",
                "cgmExpc": [{"안건명": "민원"}],
            }
        },
        "dapaCgmExpc",
    )

    assert result["root_key"] == "CgmExpc"
    assert result["item_key"] == "cgmExpc"
    assert result["item_type"] == "list"


def test_root_item_shape_rejects_top_level_error_payload() -> None:
    probe = _load_probe_module()

    result = probe._root_item_shape(
        {"resultCode": "99", "resultMsg": "invalid api key"},
        "dapaCgmExpc",
    )

    assert result == {
        "target": "dapaCgmExpc",
        "status": "error",
        "error": "invalid api key",
    }


def test_root_item_shape_rejects_nested_error_payload() -> None:
    probe = _load_probe_module()

    result = probe._root_item_shape(
        {"CgmExpc": {"resultCode": "99", "resultMsg": "no result"}},
        "dapaCgmExpc",
    )

    assert result == {
        "target": "dapaCgmExpc",
        "status": "error",
        "error": "no result",
    }
