from typing import Any
from pydantic import BaseModel


class ResponseModel(BaseModel):
    success: bool
    data: Any
    warnings: str | None = None