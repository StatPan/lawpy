"""Data models for lawpy."""

from pydantic import BaseModel, Field


class Law(BaseModel):
    """Law information."""

    law_id: str = Field(description="The unique ID of the law")
    law_name: str = Field(description="Korean name of the law")
    law_no: str = Field(description="Promulgation number")
    promulgation_date: str | None = Field(default=None, description="Date of promulgation (YYYYMMDD)")
    enforcement_date: str | None = Field(default=None, description="Date of enforcement (YYYYMMDD)")


class SubItem(BaseModel):
    """목 (sub-item) information."""

    number: str = Field(description="Sub-item number or identifier")
    content: str = Field(description="Content of the sub-item")


class Item(BaseModel):
    """호 (item) information."""

    number: int = Field(description="Item number")
    content: str = Field(description="Content of the item")
    sub_items: list[SubItem] = Field(default_factory=list, description="List of sub-items (목)")


class Paragraph(BaseModel):
    """항 (paragraph) information."""

    number: str = Field(description="Paragraph number")
    content: str = Field(description="Content of the paragraph")
    items: list[Item] = Field(default_factory=list, description="List of items (호)")


class Article(BaseModel):
    """조문 (article) information."""

    number: int = Field(description="Article number")
    title: str = Field(description="Article title")
    content: str = Field(description="Full content of the article")
    paragraphs: list[Paragraph] = Field(default_factory=list, description="List of paragraphs (항)")
    changed: bool = Field(default=False, description="Whether the article was modified")
    effective_date: str | None = Field(default=None, description="Effective date of this article")


class LawDetail(BaseModel):
    """Detailed law information with full text."""

    law_id: str = Field(description="The unique ID of the law")
    law_name_korean: str = Field(description="Korean name of the law")
    law_name_chinese: str | None = Field(default=None, description="Chinese name of the law")
    law_name_abbr: str | None = Field(default=None, description="Abbreviated name of the law")
    promulgation_date: str | None = Field(default=None, description="Date of promulgation (YYYYMMDD)")
    promulgation_number: int | None = Field(default=None, description="Promulgation number")
    enforcement_date: str | None = Field(default=None, description="Date of enforcement (YYYYMMDD)")
    law_type: str | None = Field(default=None, description="Type of law (e.g., '법률')")
    ministry: str | None = Field(default=None, description="Responsible ministry")
    articles: list[Article] = Field(default_factory=list, description="List of articles (조문)")
    language: str = Field(default="KO", description="Language code (KO or ORI)")


# Deprecated but kept for backward compatibility if needed internally
class LawText(BaseModel):
    """Full text of a law."""

    law_id: str
    law_name: str
    articles: list[dict]
