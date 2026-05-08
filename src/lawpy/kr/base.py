"""Base class for Korean law API clients."""

import os
import re
import xml.etree.ElementTree as ET
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import httpx

from lawpy.client import LawClient
from lawpy.exceptions import APIError, ApiResponseTypeError, ApiSubscriptionError, ParseError

_SUBSCRIPTION_MARKERS = ("미신청된 목록/본문",)

_HTML_DOCTYPE = "<!DOCTYPE"
_PREVIEW_CHARS = 500


class KoreanBaseClient(LawClient):
    """Base class for Korean law API clients."""

    BASE_URL = "https://www.law.go.kr/DRF/lawSearch.do"
    SERVICE_URL = "http://www.law.go.kr/DRF/lawService.do"

    def __init__(self, api_key: str | None = None, timeout: int = 30) -> None:
        """Initialize Korean law client.

        Args:
            api_key: API key for the National Law Information Center (법제처 OpenAPI).

                     **What is the API key?**
                     It is the **email username** (the part before ``@``) of the email
                     address you registered at https://open.law.go.kr.

                     Example: if you registered with ``user@example.com``,
                     set ``api_key="user"``.

                     If not provided, reads from the ``LAWPY_KR_API_KEY`` environment
                     variable (falls back to ``LAWPY_API_KEY`` for backwards compatibility).
            timeout: Request timeout in seconds.

        Raises:
            ValueError: If api_key is not provided and no env var is set.
        """
        if api_key is None:
            api_key = (
                os.environ.get("LAWPY_KR_API_KEY")
                or os.environ.get("LAWPY_API_KEY")  # backwards compat
            )
            if not api_key:
                msg = (
                    "api_key must be provided or set the LAWPY_KR_API_KEY "
                    "environment variable (your law.go.kr email username, "
                    "e.g. 'user' for 'user@example.com')."
                )
                raise ValueError(msg)

        super().__init__(api_key=api_key, base_url=self.BASE_URL, timeout=timeout)

    def _make_request(
        self,
        url: str,
        params: dict[str, str | int],
        raise_404: bool = False,
    ) -> httpx.Response:
        """Make HTTP request to the API.

        Args:
            url: Request URL
            params: Request parameters
            raise_404: If True, raise NotFoundError for 404 status

        Returns:
            HTTP response

        Raises:
            APIError: If the request fails
        """
        try:
            full_params = {"OC": str(self.api_key), **params}
            response = self._client.get(url, params=full_params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            from lawpy.exceptions import NotFoundError

            if raise_404 and e.response.status_code == 404:
                raise NotFoundError("Resource not found", status_code=404) from e
            raise APIError(
                f"HTTP error: {e.response.status_code}", status_code=e.response.status_code
            ) from e
        except httpx.RequestError as e:
            raise APIError(f"Request error: {e}") from e

        self._check_response(response, str(params.get("target", "")))
        return response

    def _check_response(self, response: httpx.Response, target: str) -> None:
        """Check response for known API error patterns.

        Args:
            response: HTTP response to check
            target: API target name for error messages

        Raises:
            ApiSubscriptionError: If the target is not subscribed
            ApiResponseTypeError: If the API returns HTML instead of expected format
        """
        body = getattr(response, "text", "")
        if not isinstance(body, str):
            content = getattr(response, "content", b"")
            if isinstance(content, bytes):
                encoding = getattr(response, "encoding", None)
                if not isinstance(encoding, str):
                    encoding = "utf-8"
                body = content.decode(encoding, errors="replace")
            elif isinstance(content, str):
                body = content
            else:
                body = ""

        for marker in _SUBSCRIPTION_MARKERS:
            if marker in body:
                msg = (
                    f"Target '{target}' is not activated in your API subscription. "
                    f"Log in to https://open.law.go.kr and enable it under "
                    f"[OPEN API] -> [OPEN API 신청]."
                )
                raise ApiSubscriptionError(msg, status_code=response.status_code, response=body)

        response_type = self._response_request_type(response)
        if response_type in {"json", "xml"} and (
            self._is_html_content_type(response) or self._looks_like_html(body)
        ):
            content_type = self._response_content_type(response)
            url = self._response_url(response)
            preview = self._content_preview(body)
            msg = (
                f"Target '{target}' returned HTML instead of {response_type.upper()}"
                f" (content-type: {content_type}, url: {url}); "
                f"response preview: {preview}"
            )
            raise ApiResponseTypeError(msg, status_code=response.status_code, response=body)

    def _parse_json_response(self, response: httpx.Response, target: str) -> Any:
        """Parse a JSON API response with actionable diagnostics on failure."""
        try:
            return response.json()
        except ValueError as e:
            content_type = self._response_content_type(response)
            url = self._response_url(response)
            preview = self._response_preview(response)
            msg = (
                f"Failed to parse JSON response for target '{target}'"
                f" (content-type: {content_type}, url: {url}): {e}; "
                f"response preview: {preview}"
            )
            raise ParseError(msg) from e

    @classmethod
    def _response_content_type(cls, response: httpx.Response) -> str:
        headers = getattr(response, "headers", {}) or {}
        if hasattr(headers, "get"):
            value = headers.get("content-type") or headers.get("Content-Type")
            if value:
                return str(value)
        return "unknown"

    @classmethod
    def _response_url(cls, response: httpx.Response) -> str:
        request = getattr(response, "request", None)
        url = getattr(request, "url", None)
        if url is None:
            url = getattr(response, "url", None)
        return cls._redact_url(str(url)) if url is not None else "unknown"

    @classmethod
    def _response_request_type(cls, response: httpx.Response) -> str:
        request = getattr(response, "request", None)
        request_params = getattr(request, "params", {}) or {}
        if hasattr(request_params, "get"):
            value = request_params.get("type")
            if isinstance(value, str | int):
                return str(value).lower()

        url = getattr(request, "url", None)
        if url is None:
            url = getattr(response, "url", None)
        if url is None:
            return ""

        try:
            query = parse_qsl(urlsplit(str(url)).query, keep_blank_values=True)
        except ValueError:
            return ""
        for key, value in query:
            if key.lower() == "type":
                return value.lower()
        return ""

    @classmethod
    def _is_html_content_type(cls, response: httpx.Response) -> bool:
        content_type = cls._response_content_type(response).lower()
        return "html" in content_type or "xhtml" in content_type

    @classmethod
    def _looks_like_html(cls, content: str | bytes) -> bool:
        if isinstance(content, bytes):
            content = content.decode("utf-8", errors="replace")
        sample = content.lstrip()[:200].lower()
        return (
            sample.startswith("<!doctype html")
            or sample.startswith("<html")
            or "<html" in sample
            or "xhtml" in sample
        )

    @classmethod
    def _redact_url(cls, url: str) -> str:
        try:
            parts = urlsplit(url)
        except ValueError:
            return url
        if not parts.query:
            return url
        query = [
            (key, "***" if key.lower() == "oc" else value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
        ]
        return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))

    @classmethod
    def _response_preview(cls, response: httpx.Response) -> str:
        body = getattr(response, "text", "")
        if not isinstance(body, str):
            content = getattr(response, "content", b"")
            if isinstance(content, bytes):
                encoding = getattr(response, "encoding", None)
                if not isinstance(encoding, str):
                    encoding = "utf-8"
                body = content.decode(encoding, errors="replace")
            elif isinstance(content, str):
                body = content
            else:
                body = ""
        return cls._content_preview(body)

    @classmethod
    def _content_preview(cls, content: str | bytes) -> str:
        if isinstance(content, bytes):
            content = content.decode("utf-8", errors="replace")
        content = cls._redact_sensitive_text(content)
        normalized = " ".join(content.split())
        if len(normalized) > _PREVIEW_CHARS:
            return normalized[:_PREVIEW_CHARS] + "..."
        return normalized or "<empty>"

    @classmethod
    def _redact_sensitive_text(cls, text: str) -> str:
        text = re.sub(r"(?i)(\bOC=)[^&\s<>\"']+", r"\1***", text)
        text = re.sub(r'(?i)("OC"\s*:\s*")[^"]+(")', r"\1***\2", text)
        return text

    @staticmethod
    def _xml_to_dict(element: ET.Element) -> dict[str, Any]:
        """Convert an XML element to a dict.

        Text content becomes a string value. Child elements with the same tag
        are collected into a list. Attributes are ignored (the API uses id attrs
        only as positional markers).
        """
        result: dict[str, Any] = {}
        for child in element:
            tag = child.tag
            value: Any = child.text.strip() if child.text else None
            if len(child) > 0:
                value = KoreanBaseClient._xml_to_dict(child)
            if tag in result:
                existing = result[tag]
                if isinstance(existing, list):
                    existing.append(value)
                else:
                    result[tag] = [existing, value]
            else:
                result[tag] = value
        return result

    def _make_xml_request(
        self,
        url: str,
        params: dict[str, str | int],
    ) -> dict[str, Any]:
        """Make HTTP request expecting XML response, return parsed dict.

        Args:
            url: Request URL
            params: Request parameters (type=XML will be added automatically)

        Returns:
            Parsed dict from XML response
        """
        full_params = {**params, "type": "XML"}
        response = self._make_request(url, params=full_params)
        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as e:
            target = str(params.get("target", ""))
            content_type = self._response_content_type(response)
            url = self._response_url(response)
            preview = self._response_preview(response)
            msg = (
                f"Failed to parse XML response for target '{target}'"
                f" (content-type: {content_type}, url: {url}): {e}; "
                f"response preview: {preview}"
            )
            raise ParseError(msg) from e
        return self._xml_to_dict(root)
