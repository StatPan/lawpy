"""Data models for lawpy."""

from typing import Any


class BaseModel:
    """Base model for all lawpy data models."""

    def to_dict(self) -> dict[str, Any]:
        """Convert model to dictionary."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class Law(BaseModel):
    """Law information."""

    def __init__(
        self,
        law_id: str,
        law_name: str,
        law_no: str,
        promulgation_date: str | None = None,
        enforcement_date: str | None = None,
    ) -> None:
        self.law_id = law_id
        self.law_name = law_name
        self.law_no = law_no
        self.promulgation_date = promulgation_date
        self.enforcement_date = enforcement_date


class LawText(BaseModel):
    """Full text of a law."""

    def __init__(
        self,
        law_id: str,
        law_name: str,
        articles: list[dict[str, Any]],
    ) -> None:
        self.law_id = law_id
        self.law_name = law_name
        self.articles = articles
