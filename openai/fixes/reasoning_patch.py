"""
Fix for bug #2561:
Ensures that 'reasoning' items are always followed by a valid message/output item
before sending request payloads to the API.
"""

from openai.types.responses import Response
import logging

logger = logging.getLogger(__name__)

def patched_to_dict(response: Response) -> dict:
    """
    Convert a Response to a dict while ensuring that 'reasoning' items
    are always followed by a valid message/output item.
    
    Args:
        response (Response): OpenAI Response object
    
    Returns:
        dict: Safe response dict suitable for API consumption
    """
    data = response.model_dump()

    # Defensive check: ensure output list exists
    items = data.get("output", [])
    if not isinstance(items, list):
        logger.warning("Expected list for response['output'], got %s", type(items))
        return data

    fixed_items = []
    for i, item in enumerate(items):
        fixed_items.append(item)

        # If we encounter a reasoning item, ensure it's followed correctly
        if item.get("type") == "reasoning":
            # Check if next exists & valid
            needs_patch = (
                i + 1 == len(items) or
                items[i + 1].get("type") not in ("message", "output_text")
            )

            if needs_patch:
                logger.debug("Patching missing follow-up for reasoning item: %s", item)
                fixed_items.append({
                    "type": "message",
                    "role": "assistant",
                    "content": [{"type": "text", "text": ""}],
                })

    # Replace output with fixed sequence
    data["output"] = fixed_items
    return data
#Production Level Code 
from openai import OpenAI
from openai.fixes.reasoning_patch import patched_to_dict

client = OpenAI()

resp = client.responses.create(
    model="gpt-5",
    input=[{"role": "user", "content": [{"type": "text", "text": "2+2"}]}],
    tools=[{"type": "code_interpreter"}],
)

# Safe serialization
safe_response = patched_to_dict(resp)
print(safe_response)
