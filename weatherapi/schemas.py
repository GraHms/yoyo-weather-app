from pydantic import BaseModel, Field


class WeatherRequestParams(BaseModel):
    # the default value for days is 1
    days: int = Field(1)
    city: str
