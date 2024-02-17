from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    full_name: str = Field(example='John Milton Doe')
    mobile_phone: str = Field(example='+79881882838')
