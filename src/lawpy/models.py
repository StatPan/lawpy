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


class SubItem(BaseModel):
    """목 (sub-item) information."""

    def __init__(self, number: str, content: str) -> None:
        self.number = number
        self.content = content


class Item(BaseModel):
    """호 (item) information."""

    def __init__(self, number: int, content: str, sub_items: list[SubItem]) -> None:
        self.number = number
        self.content = content
        self.sub_items = sub_items


class Paragraph(BaseModel):
    """항 (paragraph) information."""

    def __init__(self, number: str, content: str, items: list[Item]) -> None:
        self.number = number
        self.content = content
        self.items = items


class Article(BaseModel):
    """조문 (article) information."""

    def __init__(
        self,
        number: int,
        title: str,
        content: str,
        paragraphs: list[Paragraph],
        changed: bool = False,
        effective_date: str | None = None,
    ) -> None:
        self.number = number
        self.title = title
        self.content = content
        self.paragraphs = paragraphs
        self.changed = changed
        self.effective_date = effective_date


class LawDetail(BaseModel):
    """Detailed law information with full text."""

    def __init__(
        self,
        law_id: str,
        law_name_korean: str,
        law_name_chinese: str | None = None,
        law_name_abbr: str | None = None,
        promulgation_date: str | None = None,
        promulgation_number: int | None = None,
        enforcement_date: str | None = None,
        law_type: str | None = None,
        ministry: str | None = None,
        articles: list[Article] | None = None,
        language: str = "KO",
    ) -> None:
        self.law_id = law_id
        self.law_name_korean = law_name_korean
        self.law_name_chinese = law_name_chinese
        self.law_name_abbr = law_name_abbr
        self.promulgation_date = promulgation_date
        self.promulgation_number = promulgation_number
        self.enforcement_date = enforcement_date
        self.law_type = law_type
        self.ministry = ministry
        self.articles = articles or []
        self.language = language
