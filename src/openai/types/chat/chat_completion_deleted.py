# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletionDeleted"]


class ChatCompletionDeleted(BaseModel):
    id: str
    """The ID of the chat completion that was deleted."""

    deleted: bool
    """Whether the chat completion was deleted."""

    object: Literal["chat.completion.deleted"]
    """The type of object being deleted."""
class ChatModel(str, Enum):
    GPT4 = "gpt-4"
    GPT4O = "gpt-4o"
    GPT45 = "gpt-4.5"
    export type ChatModel =
  | "gpt-4"
  | "gpt-4o"
  ...
  | "gpt-4.5"; // <-- add this back


