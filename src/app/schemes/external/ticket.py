from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from app.schemes.internal import InternalRequestTicket


class RequestTicket(BaseModel):
    buyer_mobile_phone: str = Field(example='9881882838', max_length=10, min_length=10)
    visitor_mobile_phone: str = Field(example='9779669594', max_length=10, min_length=10)
    visitor_full_name: str = Field(example='John Milton Doe')
    event_name: str = Field(example='Exposition')
    event_date: datetime = Field(example=datetime.now())
    sector_number: int = Field(example=1)
    row_number: int = Field(example=16)
    place_number: int = Field(example=9)
    ticket_price: float = Field(example=350.00)
    status: str = Field(example='active')

    def to_internal(self) -> InternalRequestTicket:
        return InternalRequestTicket(**self.model_dump())


class ResponseBriefTicket(BaseModel):
    ticket_id: UUID4
    event_name: str


class ResponseTicket(RequestTicket):
    ticket_id: UUID4
    created_at: datetime
    updated_at: datetime
