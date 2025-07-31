import json
import re
from openai.error import OpenAIError

CONTROL_CHARS = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F]")

def sanitize_json_string(data: str) -> str:
    """
    Removes non-printable control characters that break JSON parsing.
    Preserves \n, \t, and \r.
    """
    return CONTROL_CHARS.sub("", data)

def parse_response(response_text: str):
    try:
        clean_text = sanitize_json_string(response_text)
        return json.loads(clean_text)
    except json.JSONDecodeError as e:
        raise OpenAIError(f"Failed to parse API response: {e}")

from typing import Any
from typing_extensions import Iterator, AsyncIterator


def consume_sync_iterator(iterator: Iterator[Any]) -> None:
    for _ in iterator:
        ...


async def consume_async_iterator(iterator: AsyncIterator[Any]) -> None:
    async for _ in iterator:
        ...
