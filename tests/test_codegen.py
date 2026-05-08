"""Tests for code generation policy."""

import importlib.util
from pathlib import Path


def _load_codegen_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "codegen.py"
    spec = importlib.util.spec_from_file_location("lawpy_codegen", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_decc_prefers_non_mobile_spec_over_mobile_duplicate() -> None:
    codegen = _load_codegen_module()
    mobile = {
        "html_name": "mobDeccInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=decc&mobileYn=Y",
        "response": [{"요청변수": "mobileYn"}],
    }
    non_mobile = {
        "html_name": "deccInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=decc",
        "response": [{"필드": "사건명"}],
    }

    assert codegen.should_replace_spec("decc", mobile, non_mobile)
    assert not codegen.should_replace_spec("decc", non_mobile, mobile)


def test_non_decc_duplicate_policy_keeps_existing_last_write_behavior() -> None:
    codegen = _load_codegen_module()
    current = {
        "html_name": "lawInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law",
    }
    candidate = {
        "html_name": "mobLawInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law&mobileYn=Y",
    }

    assert codegen.should_replace_spec("law", current, candidate)
