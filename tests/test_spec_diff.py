"""Tests for scraped API spec diffing."""

import importlib.util
import json
import sys
from pathlib import Path


def _load_spec_diff_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "spec_diff.py"
    spec = importlib.util.spec_from_file_location("lawpy_spec_diff", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_field_set_ignores_sample_urls_and_numbered_examples() -> None:
    spec_diff = _load_spec_diff_module()

    rows = [
        {"필드": "사건명"},
        {"필드": "샘플 URL"},
        {"필드": "1. 판례 HTML 조회"},
        {"필드": "http://www.law.go.kr/DRF/lawService.do?target=prec"},
    ]

    assert spec_diff._field_set(rows, "필드") == {"사건명"}


def test_diff_specs_compares_field_response_headers(tmp_path: Path) -> None:
    spec_diff = _load_spec_diff_module()
    old_dir = tmp_path / "old"
    new_dir = tmp_path / "new"
    old_dir.mkdir()
    new_dir.mkdir()

    index = [{"html_name": "precInfoGuide", "label": "판례 본문 조회"}]
    (old_dir / "_index.json").write_text(json.dumps(index), encoding="utf-8")
    (new_dir / "_index.json").write_text(json.dumps(index), encoding="utf-8")
    (old_dir / "precInfoGuide.json").write_text(
        json.dumps({"params": [], "response": [{"필드": "사건명"}]}, ensure_ascii=False),
        encoding="utf-8",
    )
    (new_dir / "precInfoGuide.json").write_text(
        json.dumps({"params": [], "response": [{"필드": "사건명"}, {"필드": "판례내용"}]}, ensure_ascii=False),
        encoding="utf-8",
    )

    diff = spec_diff.diff_specs(old_dir, new_dir)

    assert diff.changed_guides == [
        {
            "html_name": "precInfoGuide",
            "label": "판례 본문 조회",
            "added_params": [],
            "removed_params": [],
            "added_response": ["판례내용"],
            "removed_response": [],
        }
    ]


def test_diff_specs_compares_mixed_response_headers(tmp_path: Path) -> None:
    spec_diff = _load_spec_diff_module()
    old_dir = tmp_path / "old"
    new_dir = tmp_path / "new"
    old_dir.mkdir()
    new_dir.mkdir()

    index = [{"html_name": "lawInfoGuide", "label": "법령 본문 조회"}]
    (old_dir / "_index.json").write_text(json.dumps(index), encoding="utf-8")
    (new_dir / "_index.json").write_text(json.dumps(index), encoding="utf-8")
    (old_dir / "lawInfoGuide.json").write_text(
        json.dumps({"params": [], "response": [{"필드": "법령ID"}]}, ensure_ascii=False),
        encoding="utf-8",
    )
    (new_dir / "lawInfoGuide.json").write_text(
        json.dumps({"params": [], "response": [{"요청변수": "법령ID"}]}, ensure_ascii=False),
        encoding="utf-8",
    )

    diff = spec_diff.diff_specs(old_dir, new_dir)

    assert diff.changed_guides == []
