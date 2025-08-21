# fix_dict_schema.py
"""
Fix for bug: Dict fields in Pydantic models are incorrectly mapped
to {"additionalProperties": false} in strict JSON schema generation.

This patch updates the logic so that Dict[str, Any] is correctly represented
as {"additionalProperties": true} (or unrestricted schema), allowing
arbitrary key-value pairs.
"""

from typing import Any, Dict, get_origin, get_args
import pydantic
from openai.lib._pydantic import to_strict_json_schema as original_to_strict_json_schema


def fixed_to_strict_json_schema(model: type[pydantic.BaseModel]) -> dict[str, Any]:
    """
    Wrapper around the original to_strict_json_schema that corrects handling of Dict fields.
    """
    schema = original_to_strict_json_schema(model)

    def _fix_dicts(node: Any):
        if isinstance(node, dict):
            # Check if this node looks like a schema with "type": "object"
            if node.get("type") == "object":
                # If explicitly disabled, re-enable dictionary properties
                if node.get("additionalProperties") is False:
                    # Allow arbitrary properties instead of forcing empty dict
                    node["additionalProperties"] = True
            # Recurse into children
            for v in node.values():
                _fix_dicts(v)
        elif isinstance(node, list):
            for v in node:
                _fix_dicts(v)

    _fix_dicts(schema)
    return schema


# --- Example usage / test ---
if __name__ == "__main__":
    class GenerateToolCallArguments(pydantic.BaseModel):
        arguments: Dict[str, Any] = pydantic.Field(description="The arguments to pass to the tool")

    import json
    print(json.dumps(fixed_to_strict_json_schema(GenerateToolCallArguments), indent=4))
