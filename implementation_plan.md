# kolaw Implementation Plan

A comprehensive Python library for the Korean National Law Information Center (국가법령정보센터) Open API.

## Proposed Changes

### Project Structure [NEW]

- `pyproject.toml`: Modern packaging configuration (pdm/hatch/poetry style).
- `src/kolaw/`: Main package directory.
    - `__init__.py`: Package entry point.
    - `client.py`: Core `KoLawClient` class.
    - `models/`: Pydantic models for API responses.
    - `parser.py`: Structured XML to Python tree parser.
    - `exceptions.py`: Custom exception classes.
- `tests/`: Unit and integration tests.
- `examples/`: Sample usage scripts.

### Core Client

The client will:
1.  Handle authentication via `OC` (User ID / API Key).
2.  Provide methods for common API endpoints:
    - `search_laws()`: Search for laws with various filters.
    - `get_law_text()`: Fetch the full text of a law.
    - `search_prec()`: Search for precedents.
    - `get_prec_text()`: Fetch the full text of a precedent.
3.  Support both synchronous (requests) and potentially asynchronous (httpx) requests. I'll start with synchronous `requests` for simplicity.

## Key Features

The `kolaw` library will provide:
- **Unified Name**: `pip install kolaw` and `import kolaw` for consistency.
- **Pythonic Data Models**: Comprehensive Pydantic models for all major API responses.
- **Structured Parsing**: Specialized logic to handle the complex nesting of law 조/항/호/목.
- **Scalable Architecture**: A base client that can eventually support all 172+ APIs provided by the National Law Information Center.
- **Export Support**: Methods to export law text to Markdown/JSON/Plain Text.

## Verification Plan

### Automated Tests
- Mock the API responses using `responses` or `pytest-mock`.
- Test parameter encoding and URL construction.
- Test error handling (404, 500, invalid API key).

### Manual Verification
- Create a `demo.py` script that the user can run with their API key.
