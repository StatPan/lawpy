# lawpy

Universal law information API client library.

## Features

- **Multi-country support**: Access law APIs from multiple countries (currently Korea)
- **Simple interface**: Intuitive API design for easy integration
- **Type-safe**: Full type hints for better IDE support
- **Well-tested**: Comprehensive test coverage

## Installation

```bash
pip install lawpy
```

## Quick Start

### Korean Law API

Set your API key (email ID) as an environment variable:

```bash
export LAWPY_API_KEY="your-email-id"
```

Or pass it directly:

```python
from lawpy import KoreanLawClient

# Using environment variable
client = KoreanLawClient()

# Or pass api_key directly
client = KoreanLawClient(api_key="your-api-key")
```

#### Search for laws

```python
laws = client.search_laws("민법", per_page=5)
for law in laws:
    print(f"{law.law_name} (ID: {law.law_id})")
```

#### Get detailed law information

```python
law_detail = client.get_law_detail(law_id="001706")
print(f"Law: {law_detail.law_name_korean}")
print(f"Ministry: {law_detail.ministry}")
print(f"Promulgation Date: {law_detail.promulgation_date}")
print(f"Enforcement Date: {law_detail.enforcement_date}")

# Access articles
for article in law_detail.articles[:3]:
    print(f"Article {article.number}: {article.title}")
    for paragraph in article.paragraphs:
        print(f"  {paragraph.content}")
```

#### Get specific article

```python
law_detail = client.get_law_detail(law_id="001706", article_number=1)
```

#### Get law by MST (master number)

```python
law_detail = client.get_law_detail(mst=123456)
```

#### Get original text

```python
law_detail = client.get_law_detail(law_id="001706", language="ORI")
```

#### Get current law list

```python
laws = client.get_law_list(per_page=10)
for law in laws:
    print(f"{law.law_name} (Effective: {law.enforcement_date})")
```

#### Get law amendment history

```python
history = client.get_law_history(query="민법", per_page=10)
for h in history:
    print(f"{h.law_name} ({h.promulgation_date})")
```

#### Get detailed law history

```python
history_detail = client.get_law_history_detail(mst=9094)
print(history_detail)  # Returns HTML text
```

## API Key

To use the Korean Law API, you need an API key:

1. Visit [Korean Law Open API](https://open.law.go.kr/)
2. Sign up and get your email ID as API key
3. Set it as environment variable: `LAWPY_API_KEY`

## Development

```bash
# Clone repository
git clone https://github.com/statpan/lawpy.git
cd lawpy

# Install development dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Run linting
uv run ruff check src/lawpy tests
uv run ruff format src/lawpy tests

# Type checking
uv run mypy src/lawpy

# Build package
uv build
```

## Project Structure

```
lawpy/
├── src/lawpy/
│   ├── __init__.py
│   ├── client.py          # Base client class
│   ├── exceptions.py      # Exception definitions
│   ├── models.py         # Data models
│   └── kr/             # Korean API modules
│       ├── __init__.py
│       ├── base.py       # Base class for Korean clients
│       ├── client.py     # Integrated Korean client
│       ├── law.py       # Law (법령) APIs
│       └── README.md     # Korean API documentation
└── tests/
    └── test_kr.py       # Korean API tests
```

## Roadmap

- [ ] Add more countries (Japan, China, etc.)
- [ ] Implement all Korean Law API categories
- [ ] Add async support
- [ ] Add caching layer

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- [GitHub Repository](https://github.com/statpan/lawpy)
- [PyPI Package](https://pypi.org/project/lawpy/)
- [Korean Law Open API Guide](https://open.law.go.kr/LSO/openApi/guideList.do)
