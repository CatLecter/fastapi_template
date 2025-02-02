from uuid import UUID

from fastapi import APIRouter, Depends

from src.dependencies import get_ticket_service
from src.schemes.external import (
    RequestTicket,
    ResponseBriefTicket,
    ResponseTicket,
)
from src.services import TicketService

router = APIRouter(prefix='/ticket', tags=['Tickets'])


@router.post(path='/', response_model=ResponseTicket)  # noqa
async def add_ticket(
    item: RequestTicket,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> ResponseTicket:
    return await ticket_service.add(item.to_internal())


@router.get('/', response_model=ResponseTicket)
async def get_ticket_by_id(
    ticket_id: UUID,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> ResponseTicket:
    return await ticket_service.get_by_id(ticket_id)


@router.get('/by_mobile_phone/', response_model=list[ResponseBriefTicket])
async def get_tickets_by_user_mobile_phone(
    mobile_phone: str,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> list[ResponseBriefTicket]:
    return await ticket_service.get_by_user_mobile_phone(mobile_phone)
