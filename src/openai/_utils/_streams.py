import json
from openai.error import OpenAIError

class IncompleteResponseError(OpenAIError):
    """Raised when the API returns an incomplete or truncated response."""
    pass

def parse_response(response_text: str):
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        # Detect truncated JSON (common with structured output streaming)
        if response_text and not response_text.strip().endswith("}"):
            raise IncompleteResponseError(
                "The API returned an incomplete or truncated response. "
                "Consider retrying or using non-structured output mode."
            )
        raise OpenAIError(f"Failed to parse API response: {e}")

from typing import Any
from typing_extensions import Iterator, AsyncIterator


def consume_sync_iterator(iterator: Iterator[Any]) -> None:
    for _ in iterator:
        ...


async def consume_async_iterator(iterator: AsyncIterator[Any]) -> None:
    async for _ in iterator:
        ...
