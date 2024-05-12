from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class InternalRequestTicket:
    __slots__ = [
        'buyer_mobile_phone',
        'visitor_mobile_phone',
        'visitor_full_name',
        'event_name',
        'event_date',
        'sector_number',
        'row_number',
        'place_number',
        'ticket_price',
        'status',
    ]
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
