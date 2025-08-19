"""
Fix: Handle ImportError for ResponseTextConfigParam from openai.types.responses

In newer versions of the OpenAI Python SDK (>=1.0), ResponseTextConfigParam was
removed or renamed. Some agent modules still expect it, which causes:

    ImportError: cannot import name 'ResponseTextConfigParam'

This file ensures forward + backward compatibility by:
- Importing the real class if it exists (older SDKs).
- Providing a placeholder shim if it does not (newer SDKs).
"""

from typing import Any, Dict


# ----------------------------------------------------------------------
# Import OpenAI response types with compatibility shim
# ----------------------------------------------------------------------
try:
    # Older SDKs still have ResponseTextConfigParam
    from openai.types.responses import (
        ResponseTextConfigParam,
        ResponseContentText,
        ResponseContentImage,
        ResponseContentRefusal,
    )
except ImportError:
    # Newer SDKs removed ResponseTextConfigParam
    from openai.types.responses import (
        ResponseContentText,
        ResponseContentImage,
        ResponseContentRefusal,
    )

    class ResponseTextConfigParam:
        """
        Shim class for compatibility with older code expecting ResponseTextConfigParam.
        Removed in openai>=1.0. Safe to leave empty since dependent code typically
        uses it only for typing/config references.
        """
        pass


__all__ = [
    "ResponseTextConfigParam",
    "ResponseContentText",
    "ResponseContentImage",
    "ResponseContentRefusal",
    "Converter",
]


# ----------------------------------------------------------------------
# Converter class (example implementation)
# ----------------------------------------------------------------------
class Converter:
    """
    Converts raw response payloads from OpenAI API into normalized formats
    used by agent models. Updated to handle missing ResponseTextConfigParam.
    """

    @staticmethod
    def convert_response(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert an OpenAI response object into a normalized dictionary format.

        Args:
            response (Dict[str, Any]): The raw response from OpenAI.

        Returns:
            Dict[str, Any]: Normalized response.
        """
        normalized: Dict[str, Any] = {}

        # Example handling for different response content types
        if "content" in response:
            content = response["content"]

            if isinstance(content, dict):
                if "text" in content:
                    normalized["text"] = content["text"]
                if "image_url" in content:
                    normalized["image"] = content["image_url"]
                if "refusal" in content:
                    normalized["refusal"] = content["refusal"]

        # Attach metadata if present
        if "id" in response:
            normalized["id"] = response["id"]
        if "created" in response:
            normalized["created"] = response["created"]

        return normalized
