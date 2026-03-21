"""Custom exceptions for lawpy."""

from typing import Any


class LawpyError(Exception):
    """Base exception for all lawpy errors."""

    pass


class AuthenticationError(LawpyError):
    """Raised when authentication fails."""

    pass


class InvalidAPIKeyError(AuthenticationError):
    """Raised when the API key is invalid."""

    pass


class RateLimitError(LawpyError):
    """Raised when rate limit is exceeded."""

    pass


class APIError(LawpyError):
    """Raised when the API returns an error."""

    def __init__(self, message: str, status_code: int | None = None, response: Any = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class NotFoundError(APIError):
    """Raised when a resource is not found."""

    pass


class ParseError(LawpyError):
    """Raised when parsing API response fails."""

    pass
