from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from app.schemes.internal import InternalRequestUser


class RequestUser(BaseModel):
    full_name: str = Field(example='John Milton Doe')
    mobile_phone: str = Field(example='9881882838', max_length=10, min_length=10)

    def to_internal(self) -> InternalRequestUser:
        return InternalRequestUser(**self.model_dump())


class ResponseBriefUser(BaseModel):
    user_id: UUID4
    full_name: str


class ResponseUser(ResponseBriefUser):
    mobile_phone: str
    created_at: datetime
    updated_at: datetime
