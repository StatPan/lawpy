"""Regression tests for spec scraper network retry behavior."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import httpx


def _load_scrape_specs_module():
    module_path = Path(__file__).resolve().parents[1] / "scripts" / "scrape_specs.py"
    spec = importlib.util.spec_from_file_location("lawpy_scrape_specs", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class _Response:
    def __init__(self, text: str, *, status_code: int = 200) -> None:
        self.text = text
        self.status_code = status_code
        self.url = "https://open.law.go.kr/test"
        self.closed = False

    def close(self) -> None:
        self.closed = True

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise httpx.HTTPStatusError(
                "error",
                request=httpx.Request("GET", self.url),
                response=httpx.Response(self.status_code),
            )


def test_get_all_guide_names_retries_transient_dns_failure(monkeypatch) -> None:
    scrape_specs = _load_scrape_specs_module()
    calls = []
    sleeps = []

    def fake_get(url: str, **kwargs):
        calls.append((url, kwargs))
        if len(calls) == 1:
            raise httpx.ConnectError("Temporary failure in name resolution")
        return _Response(
            """
            <html><body>
              <a href="#" onclick="openApiGuide('lawInfoGuide')">법령</a>
            </body></html>
            """
        )

    monkeypatch.setattr(scrape_specs.httpx, "get", fake_get)
    monkeypatch.setattr(scrape_specs.time, "sleep", sleeps.append)

    guides = scrape_specs.get_all_guide_names(retries=2, retry_delay=0.01)

    assert guides == [("lawInfoGuide", "법령")]
    assert len(calls) == 2
    assert sleeps == [0.01]


def test_scrape_guide_retries_transient_post_failure(monkeypatch) -> None:
    scrape_specs = _load_scrape_specs_module()
    sleeps = []

    class Client:
        def __init__(self) -> None:
            self.calls = 0

        def post(self, url: str, **kwargs):
            self.calls += 1
            if self.calls == 1:
                raise httpx.ConnectError("Temporary failure in name resolution")
            return _Response(
                """
                <html><body>
                  <p>요청 URL https://open.law.go.kr/LSO/openApi/lawService.do?target=law</p>
                </body></html>
                """
            )

    client = Client()
    monkeypatch.setattr(scrape_specs.time, "sleep", sleeps.append)

    spec = scrape_specs.scrape_guide("lawInfoGuide", "법령", client, retries=2, retry_delay=0.01)

    assert client.calls == 2
    assert sleeps == [0.01]
    assert spec["html_name"] == "lawInfoGuide"
    assert spec["request_url"].startswith("https://open.law.go.kr/")


def test_request_with_retries_retries_5xx_response(monkeypatch) -> None:
    scrape_specs = _load_scrape_specs_module()
    sleeps = []
    responses = [_Response("server error", status_code=502), _Response("ok")]

    monkeypatch.setattr(scrape_specs.time, "sleep", sleeps.append)

    response = scrape_specs.request_with_retries(
        lambda url: responses.pop(0),
        "https://open.law.go.kr/test",
        attempts=2,
        retry_delay=0.01,
    )

    assert response.text == "ok"
    assert sleeps == [0.01]
