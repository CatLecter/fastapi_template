from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class InternalRequestTicket:
    buyer_mobile_phone: str
    visitor_mobile_phone: str
    visitor_full_name: str
    event_name: str
    event_date: datetime
    sector_number: int
    row_number: int
    place_number: int
    ticket_price: float
    status: str
