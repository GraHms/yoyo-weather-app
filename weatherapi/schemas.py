from pydantic import BaseModel, Field


# defines the  schema to be used
class ErrorResponse(BaseModel):
    code: str
    reason: str
    message: str


class WeatherRequestParams(BaseModel):
    days: int = Field(1)
    city: str
