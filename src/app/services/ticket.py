from http import HTTPStatus

from fastapi import HTTPException

from app.database import Transaction
from app.repositories import TicketRepository
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
