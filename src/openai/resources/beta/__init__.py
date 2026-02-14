# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from . import vector_stores

from .beta import (
    Beta,
    AsyncBeta,
    BetaWithRawResponse,
    AsyncBetaWithRawResponse,
    BetaWithStreamingResponse,
    AsyncBetaWithStreamingResponse,
)
from .threads import (
    Threads,
    AsyncThreads,
    ThreadsWithRawResponse,
    AsyncThreadsWithRawResponse,
    ThreadsWithStreamingResponse,
    AsyncThreadsWithStreamingResponse,
)
from .assistants import (
    Assistants,
    AsyncAssistants,
    AssistantsWithRawResponse,
    AsyncAssistantsWithRawResponse,
    AssistantsWithStreamingResponse,
    AsyncAssistantsWithStreamingResponse,
)
class Beta(APIResourceGroup):
    ...
    vector_stores: vector_stores.VectorStores
def __init__(self, client):
    super().__init__(client)
    self.vector_stores = vector_stores.VectorStores(client)


__all__ = [
    "Assistants",
    "AsyncAssistants",
    "AssistantsWithRawResponse",
    "AsyncAssistantsWithRawResponse",
    "AssistantsWithStreamingResponse",
    "AsyncAssistantsWithStreamingResponse",
    "Threads",
    "AsyncThreads",
    "ThreadsWithRawResponse",
    "AsyncThreadsWithRawResponse",
    "ThreadsWithStreamingResponse",
    "AsyncThreadsWithStreamingResponse",
    "Beta",
    "AsyncBeta",
    "BetaWithRawResponse",
    "AsyncBetaWithRawResponse",
    "BetaWithStreamingResponse",
    "AsyncBetaWithStreamingResponse",
]
