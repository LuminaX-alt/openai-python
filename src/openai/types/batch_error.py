# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BatchError"]
error_obj = data.get("error")
if error_obj and isinstance(error_obj, dict):
    error_msg = error_obj.get("message", "Unknown error")
else:
    # Responses API places `message` at the top level
    error_msg = data.get("message", "Unknown error")



class BatchError(BaseModel):
    code: Optional[str] = None
    """An error code identifying the error type."""

    line: Optional[int] = None
    """The line number of the input file where the error occurred, if applicable."""

    message: Optional[str] = None
    """A human-readable message providing more details about the error."""

    param: Optional[str] = None
    """The name of the parameter that caused the error, if applicable."""
