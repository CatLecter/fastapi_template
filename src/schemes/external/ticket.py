from datetime import datetime

from pydantic import UUID4, BaseModel, Field

from src.schemes.internal import InternalRequestTicket


class RequestTicket(BaseModel):
    buyer_mobile_phone: str = Field(examples=['9881882838'], max_length=10, min_length=10)
    visitor_mobile_phone: str = Field(examples=['9779669594'], max_length=10, min_length=10)
    visitor_full_name: str = Field(examples=['John Milton Doe'])
    event_name: str = Field(examples=['Exposition'])
    event_date: datetime = Field(examples=[datetime.now()])
    sector_number: int = Field(examples=[1])
    row_number: int = Field(examples=[16])
    place_number: int = Field(examples=[9])
    ticket_price: float = Field(examples=[350.00])
    status: str = Field(examples=['active'])

    def to_internal(self) -> InternalRequestTicket:
        return InternalRequestTicket(**self.model_dump())


class ResponseBriefTicket(BaseModel):
    ticket_id: UUID4
    event_name: str


class ResponseTicket(RequestTicket):
    ticket_id: UUID4
    created_at: datetime
    updated_at: datetime
