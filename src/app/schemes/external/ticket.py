from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class TicketRequest(BaseModel):
    buyer_mobile_phone: str = Field(example='+79881882838')
    visitor_id: UUID4 = Field(example=uuid4())
    visitor_mobile_phone: str = Field(example='+79779669594')
    visitor_full_name: str = Field(example='John Milton Doe')
    event_name: str = Field(example='Exposition')
    event_date: datetime = Field(example=datetime.now())
    sector_number: int = Field(example=1)
    row_number: int = Field(example=16)
    place_number: int = Field(example=9)
    ticket_price: float = Field(example=350.00)
    status: str = Field(example='active')
