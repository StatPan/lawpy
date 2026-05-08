"""Base class for Korean law API clients."""

import os
import xml.etree.ElementTree as ET
from typing import Any

import httpx

from lawpy.client import LawClient
from lawpy.exceptions import APIError, ApiResponseTypeError, ApiSubscriptionError

_SUBSCRIPTION_MARKERS = ("미신청된 목록/본문",)

_HTML_DOCTYPE = "<!DOCTYPE"


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

        request = getattr(response, "request", None)
        request_params = getattr(request, "params", {}) or {}
        response_type = str(request_params.get("type", "")).lower()
        if "json" in response_type:
            if _HTML_DOCTYPE in body:
                msg = (
                    f"Target '{target}' returned HTML instead of JSON. "
                    f"This target may not support JSON responses."
                )
                raise ApiResponseTypeError(msg, status_code=response.status_code, response=body)

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
        root = ET.fromstring(response.text)
        return self._xml_to_dict(root)
