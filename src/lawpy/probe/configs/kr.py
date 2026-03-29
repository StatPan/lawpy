"""Probe configurations for Korean National Law Information Center API.

Each :class:`ProbeConfig` describes one API endpoint to probe:
- Which URL to call
- Which fixed query parameters to use (representative, minimal call)
- Which dot-path in the parsed response holds the target object

These configs are used by :class:`~lawpy.probe.runner.ProbeRunner` for
both ``capture`` (maintaining snapshots) and ``diff`` (drift detection).

Confirmed from live responses on 2026-03-29 using dlfrnaos19 API key.
"""

from __future__ import annotations

from dataclasses import dataclass


BASE_SEARCH = "https://www.law.go.kr/DRF/lawSearch.do"
BASE_SERVICE = "http://www.law.go.kr/DRF/lawService.do"


@dataclass(frozen=True)
class ProbeConfig:
    """Configuration for a single API probe."""

    name: str
    """Unique identifier, used as snapshot filename (e.g. 'kr.prec.search')."""

    url: str
    """Endpoint URL."""

    fixed_params: dict[str, str]
    """Query params (excluding OC which is injected at runtime). display=1 keeps probes fast."""

    schema_path: str
    """Dot-path into the parsed JSON to the representative object.
    E.g. 'PrecSearch.prec' navigates parsed['PrecSearch']['prec']."""

    description: str = ""
    """Human-readable description shown in `probe list`."""


# ---------------------------------------------------------------------------
# Korean Law (법령) configs
# ---------------------------------------------------------------------------

KR_LAW_SEARCH = ProbeConfig(
    name="kr.law.search",
    url=BASE_SEARCH,
    fixed_params={"target": "law", "type": "JSON", "query": "민법", "display": "1"},
    schema_path="LawSearch.law",
    description="현행법령 목록 조회 (target=law)",
)

KR_LAW_EFLAW_SEARCH = ProbeConfig(
    name="kr.law.eflaw.search",
    url=BASE_SEARCH,
    fixed_params={"target": "eflaw", "type": "JSON", "query": "민법", "display": "1"},
    schema_path="LawSearch.law",
    description="현행법령(시행일) 목록 조회 (target=eflaw)",
)

KR_LAW_DETAIL = ProbeConfig(
    name="kr.law.detail",
    url=BASE_SERVICE,
    fixed_params={"target": "law", "type": "JSON", "MST": "188376"},
    # MST 188376 = 민법 (stable, long-running law)
    schema_path="법령",
    description="법령 본문 조회 (target=law, MST=188376 민법)",
)

# ---------------------------------------------------------------------------
# Korean Precedent (판례) configs
# ---------------------------------------------------------------------------

KR_PREC_SEARCH = ProbeConfig(
    name="kr.prec.search",
    url=BASE_SEARCH,
    fixed_params={"target": "prec", "type": "JSON", "query": "손해배상", "display": "1"},
    schema_path="PrecSearch.prec",
    description="판례 목록 조회 (target=prec)",
)

KR_PREC_DETAIL = ProbeConfig(
    name="kr.prec.detail",
    url=BASE_SERVICE,
    fixed_params={"target": "prec", "type": "JSON", "ID": "616249"},
    # ID 616249 = 2026.01.29 대법원 손해배상(기) — confirmed live 2026-03-29
    schema_path="PrecService",
    description="판례 본문 조회 (target=prec, ID=616249)",
)

# ---------------------------------------------------------------------------
# Registry — all active probes in preferred run order
# ---------------------------------------------------------------------------

ALL_CONFIGS: list[ProbeConfig] = [
    KR_LAW_SEARCH,
    KR_LAW_EFLAW_SEARCH,
    KR_LAW_DETAIL,
    KR_PREC_SEARCH,
    KR_PREC_DETAIL,
]

CONFIGS_BY_NAME: dict[str, ProbeConfig] = {c.name: c for c in ALL_CONFIGS}
