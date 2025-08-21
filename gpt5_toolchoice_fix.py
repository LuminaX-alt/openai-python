"""
responses_gpt5_fix.py

Fix for Issue #2537:
"GPT5 Models | Tool choices other than 'auto' are not supported with model"

This patch adds client-side validation so the SDK raises a clear ValueError
instead of sending invalid payloads to the API, which currently causes
400 BadRequestError responses.
"""

from openai import AsyncOpenAI


class GPT5SafeClient(AsyncOpenAI):
    """
    A subclass of AsyncOpenAI that validates GPT-5 tool_choice usage.
    """

    async def create_response(self, model: str, input_text: str, tools=None, tool_choice="auto", stream=False):
        """
        Wraps client.responses.create with GPT-5 validation.

        :param model: model name (e.g., "gpt-5" or "gpt-5-mini")
        :param input_text: text input for the model
        :param tools: list of tools (optional)
        :param tool_choice: must be "auto" for GPT-5 models
        :param stream: whether to stream responses
        """
        # ✅ Validation for GPT-5 models
        if model.startswith("gpt-5") and tool_choice != "auto":
            raise ValueError(
                f"Invalid tool_choice for {model}. "
                f"GPT-5 models only support tool_choice='auto'. "
                f"You provided: {tool_choice}"
            )

        # Call original API
        return await self.responses.create(
            model=model,
            input=input_text,
            tools=tools,
            tool_choice=tool_choice,
            stream=stream,
        )


# ---------------------------
# Example Usage (Demo)
# ---------------------------
async def main():
    client = GPT5SafeClient()

    # ✅ Valid request
    stream = await client.create_response(
        model="gpt-5",
        input_text="Calculate 8*9183*7663",
        tools=[{"type": "code_interpreter"}],
        tool_choice="auto",  # ✅ Allowed
        stream=True,
    )
    async for event in stream:
        print(event.model_dump_json(indent=2))

    # ❌ This will raise ValueError (instead of hitting API with 400)
    # await client.create_response(
    #     model="gpt-5",
    #     input_text="test",
    #     tools=[{"type": "code_interpreter"}],
    #     tool_choice={"type": "allowed_tools"},  # ❌ Not allowed
    #     stream=True,
    # )
