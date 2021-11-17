from typing import Optional

from pydantic import BaseModel, Field


# defines the  schema to be used
class ErrorResponse(BaseModel):
    code: str
    reason: str
    message: str


class WeatherObject(BaseModel):
    maximum: int
    minimum: int
    average: int
    median: int


class WeatherRequestParams(BaseModel):
    days: int = Field(1)
    city: str
