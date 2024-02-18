from http import HTTPStatus
from uuid import UUID

from fastapi import HTTPException

from app.database import Transaction
from app.repositories import TicketRepository
from app.schemes.internal import InternalBriefTicketResponse
from app.schemes.internal import InternalTicketRequest, InternalTicketResponse


class TicketService:
    def __init__(self, transaction: Transaction, ticket_repository: TicketRepository):
        self.transaction = transaction
        self.ticket_repository = ticket_repository

    async def add_ticket(self, ticket: InternalTicketRequest) -> InternalTicketResponse:
        async with self.transaction:
            result: InternalTicketResponse | None = await self.ticket_repository.add_ticket(ticket)
            await self.transaction.commit()
            if not result:
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=f'Failed to create ticket')
            return result

    async def get_tickets_by_user_id(self, user_id: UUID) -> list[InternalBriefTicketResponse]:
        async with self.transaction:
            tickets = await self.ticket_repository.get_tickets_by_user_id(user_id)
            if not tickets:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND, detail=f'Tickets with user_id={user_id} not found'
                )
            return tickets

    async def get_ticket(self, ticket_id: UUID) -> InternalTicketResponse:
        async with self.transaction:
            ticket: InternalTicketResponse | None = await self.ticket_repository.get_ticket(ticket_id)
            if not ticket:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'Ticket with id={ticket_id} not found')
            return ticket
