# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import json
from typing import Any, Dict, Generator, List, Union, AsyncGenerator

def safe_json_parse(chunk: str) -> Dict[str, Any]:
    """Parses JSON safely by stripping leading whitespace/newlines."""
    return json.loads(chunk.lstrip())

def parse_stream(chunks: List[str]) -> Generator[Dict[str, Any], None, None]:
    """Parses a list of JSON string chunks into Python dicts."""
    for chunk in chunks:
        if not chunk:
            continue
        try:
            yield safe_json_parse(chunk)
        except json.JSONDecodeError:
            continue

async def parse_stream_async(chunks: AsyncGenerator[str, None]) -> AsyncGenerator[Dict[str, Any], None]:
    """Async version for parsing streamed JSON chunks into Python dicts."""
    async for chunk in chunks:
        if not chunk:
            continue
        try:
            yield safe_json_parse(chunk)
        except json.JSONDecodeError:
            continue

from typing import Any
from typing_extensions import Iterator, AsyncIterator


def consume_sync_iterator(iterator: Iterator[Any]) -> None:
    for _ in iterator:
        ...


async def consume_async_iterator(iterator: AsyncIterator[Any]) -> None:
    async for _ in iterator:
        ...
