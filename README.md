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

# Get law text
law_text = client.get_law_text("000001")
print(law_text.law_name)
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
