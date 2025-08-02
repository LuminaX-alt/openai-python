from openai import AsyncOpenAI
from safe_async_stream import safe_async_stream

client = AsyncOpenAI()

async def main():
    stream = client.chat.completions.stream(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello"}]
    )
    async for event in safe_async_stream(stream, force_gc=True):
        print(event)

# Run with asyncio.run(main())
import gc
from typing import AsyncIterator, Any

async def safe_async_stream(stream: AsyncIterator[Any], force_gc: bool = False):
    """
    Wraps an async streaming iterator and clears memory after each chunk.
    Usage:
        async for chunk in safe_async_stream(stream):
            ...
    """
    async for chunk in stream:
        yield chunk
        del chunk
        if force_gc:
            gc.collect()

