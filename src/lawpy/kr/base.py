"""Base class for Korean law API clients."""

import os

import httpx

from lawpy.client import LawClient
from lawpy.exceptions import APIError


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
            response = self._client.get(url, params=params)
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

        return response
