"""Tests for installed lawpy help guidance."""

import subprocess
import sys

import pytest

import lawpy
from lawpy.help import guide


def test_top_level_help_points_to_main_client() -> None:
    text = lawpy.help()

    assert "KRClient" in text
    assert "KoreanLawClient" in text
    assert "LAWPY_KR_API_KEY" in text


def test_kr_help_explains_public_wrapper_pattern() -> None:
    text = guide("kr")

    assert "search_laws" in text
    assert "search_precedents" in text
    assert "search_administrative_rules" in text
    assert "search_ordinances" in text


def test_generated_help_explains_direct_import_pattern() -> None:
    text = guide("generated")

    assert "lawpy.kr.generated.<target>" in text
    assert "model_dump(by_alias=True)" in text
    assert "89 generated modules" in text


def test_unknown_help_topic_raises() -> None:
    with pytest.raises(ValueError, match="Unknown lawpy help topic"):
        guide("missing")


def test_help_module_cli() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "lawpy.help", "generated"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Generated-only target pattern" in result.stdout
