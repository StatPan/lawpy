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
            api_key: API key from National Law Information Center (email ID).
                     If not provided, reads from LAWPY_API_KEY environment variable.
            timeout: Request timeout in seconds

        Raises:
            ValueError: If api_key is not provided and LAWPY_API_KEY env var is not set
        """
        if api_key is None:
            api_key = os.environ.get("LAWPY_API_KEY")
            if api_key is None:
                msg = "api_key must be provided or set LAWPY_API_KEY environment variable"
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
