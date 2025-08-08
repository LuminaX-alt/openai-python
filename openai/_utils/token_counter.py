import openai
openai.count_tokens("Hello world", model="gpt-4o")
# openai/_utils/token_counter.py

import tiktoken
from typing import Union, List

def count_tokens(
    text: Union[str, List[str]],
    model: str = "gpt-4o"
) -> int:
    """
    Count the number of tokens a given string or list of strings will use for a specific model.

    Args:
        text: A single string or a list of strings to tokenize.
        model: The name of the OpenAI model to match encoding.

    Returns:
        int: The number of tokens.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # Fallback if model not recognized
        encoding = tiktoken.get_encoding("cl100k_base")

    if isinstance(text, str):
        return len(encoding.encode(text))
    elif isinstance(text, list):
        return sum(len(encoding.encode(t)) for t in text)
    else:
        raise TypeError("`text` must be a string or list of strings.")
openai/__init__.py
from ._utils.token_counter import count_tokens

__all__ = [
    # ... existing items ...
    "count_tokens",
]
pip install tiktoken
import openai

tokens = openai.count_tokens("This is a test message", model="gpt-4o")
print("Token count:", tokens)

