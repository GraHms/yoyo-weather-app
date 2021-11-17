from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    code: str
    reason: str
    message: str
    schemaLocation: Optional[str]
