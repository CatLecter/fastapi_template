from uuid import UUID

from fastapi import APIRouter, Depends

from app.dependencies import get_ticket_service
from app.schemes.external import TicketRequest
from app.schemes.internal import InternalBriefTicketResponse
from app.schemes.internal import InternalTicketRequest, InternalTicketResponse
from app.services import TicketService

router = APIRouter(prefix='/ticket', tags=['Tickets'])


@router.post(path='/', response_model=InternalTicketResponse)
async def add_ticket(
    item: TicketRequest,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> InternalTicketResponse:
    return await ticket_service.add_ticket(InternalTicketRequest(**item.model_dump()))


@router.get('/', response_model=InternalTicketResponse)
async def get_user(
    ticket_id: UUID,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> InternalTicketResponse:
    return await ticket_service.get_ticket(ticket_id)


@router.get('/by_user_id/', response_model=list[InternalBriefTicketResponse])
async def get_users(
    user_id: UUID,
    ticket_service: TicketService = Depends(get_ticket_service),
) -> list[InternalBriefTicketResponse]:
    return await ticket_service.get_tickets_by_user_id(user_id)
