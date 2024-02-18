from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class InternalTicketRequest:
    __slots__ = [
        'buyer_mobile_phone',
        'visitor_id',
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
    visitor_id: UUID
    visitor_mobile_phone: str
    visitor_full_name: str
    event_name: str
    event_date: datetime
    sector_number: int
    row_number: int
    place_number: int
    ticket_price: float
    status: str


@dataclass
class InternalTicketResponse(InternalTicketRequest):
    __slots__ = ['ticket_id', 'created_at', 'updated_at']
    ticket_id: UUID
    created_at: datetime
    updated_at: datetime


@dataclass
class InternalBriefTicketResponse:
    __slots__ = ['ticket_id', 'event_name']
    ticket_id: UUID
    event_name: str
