from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class DataRequest(BaseModel):
    a: int | None = Field(example=1)
    b: int | None = Field(example=2)
    c: int | None = Field(example=3)
    d: int | None = Field(example=7)
    e: int | None = Field(example=8)
    f: int | None = Field(example=9)
    ts: int = Field(example=int(datetime.now().timestamp()))

    @model_validator(mode='before')  # noqa
    @classmethod
    def check_card_number_omitted(cls, data: dict) -> dict:
        return {k.lower(): v for k, v in data.items()}
