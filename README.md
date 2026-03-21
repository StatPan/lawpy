# lawpy

Universal law information API client library.

## Installation

```bash
pip install lawpy
```

## Usage

### Korean Law API

```python
from lawpy import KoreanLawClient

client = KoreanLawClient(api_key="your-api-key")

# Search for laws
laws = client.search_laws("민법")
for law in laws:
    print(f"{law.law_name} (ID: {law.law_id})")

# Get detailed law information with full text
law_detail = client.get_law_detail(law_id="009682")
print(f"법령명: {law_detail.law_name_korean}")
print(f"공포일: {law_detail.promulgation_date}")
print(f"시행일: {law_detail.enforcement_date}")

# Access articles
for article in law_detail.articles:
    print(f"제{article.number}조: {article.title}")
    for paragraph in article.paragraphs:
        print(f"  {paragraph.content}")

# Get specific article
law_detail = client.get_law_detail(law_id="009682", article_number=1)

# Get law by MST (master number)
law_detail = client.get_law_detail(mst=123456)

# Get original text
law_detail = client.get_law_detail(law_id="009682", language="ORI")
```

## Development

```bash
# Install dev dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Run linting
uv run ruff check src/lawpy tests
uv run ruff format src/lawpy tests

# Type checking
uv run mypy src/lawpy
```

## License

MIT
