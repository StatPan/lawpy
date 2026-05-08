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


def test_duplicate_policy_prefers_non_mobile_spec_for_all_targets() -> None:
    codegen = _load_codegen_module()
    current = {
        "html_name": "lawInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law",
    }
    candidate = {
        "html_name": "mobLawInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law&mobileYn=Y",
    }

    assert not codegen.should_replace_spec("law", current, candidate)
    assert codegen.should_replace_spec("law", candidate, current)


def test_mobile_policy_does_not_mix_different_guide_families() -> None:
    codegen = _load_codegen_module()
    current = {
        "html_name": "lsNwInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law",
    }
    candidate = {
        "html_name": "mobLsInfoGuide",
        "request_url": "http://www.law.go.kr/DRF/lawService.do?target=law&mobileYn=Y",
    }

    assert codegen.should_replace_spec("law", current, candidate)


def test_detail_models_keep_known_request_echo_compat_fields() -> None:
    codegen = _load_codegen_module()

    rendered = codegen.render_model(
        "detc",
        "Detail",
        "헌재결정례 본문 조회",
        [{"key": "사건명", "pyname": "사건명", "description": ""}],
        "detcInfoGuide",
    )

    assert 'id: str | None = Field(None, alias="ID")' in rendered
    assert 'lm: str | None = Field(None, alias="LM")' in rendered
