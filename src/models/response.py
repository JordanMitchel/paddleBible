from typing import Any
from pydantic import BaseModel


class ResponseModel(BaseModel):
    success: bool
    data: Any | None = None
    warnings: str | None = None
