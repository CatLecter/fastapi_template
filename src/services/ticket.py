from http import HTTPStatus
from typing import Optional
from uuid import UUID

from fastapi import HTTPException

from src.database import Transaction
from src.repositories import TicketRepository, UserRepository
from src.schemes.external import ResponseBriefTicket, ResponseTicket
from src.schemes.internal import InternalRequestTicket


class TicketService:
    def __init__(
        self,
        transaction: Transaction,
        user_repository: UserRepository,
        ticket_repository: TicketRepository,
    ):
        self.transaction = transaction
        self.user_repository = user_repository
        self.ticket_repository = ticket_repository

    async def add(self, ticket: InternalRequestTicket) -> ResponseTicket:
        async with self.transaction:
            is_user_exist = await self.user_repository.check_by_mobile_phone(ticket.visitor_mobile_phone)
            if not is_user_exist:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Visitor with mobile phone {ticket.visitor_mobile_phone} not found',
                )
            result: Optional[ResponseTicket] = await self.ticket_repository.add(ticket)
            await self.transaction.commit()
            if not result:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Failed to create ticket',
                )
            return result

    async def get_by_id(self, ticket_id: UUID) -> ResponseTicket:
        async with self.transaction:
            ticket: Optional[ResponseTicket] = await self.ticket_repository.get_by_id(ticket_id)
            if not ticket:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Ticket with ID {ticket_id} not found',
                )
            return ticket

    async def get_by_user_mobile_phone(self, mobile_phone: str) -> list[ResponseBriefTicket]:
        async with self.transaction:
            is_user_exist = await self.user_repository.check_by_mobile_phone(mobile_phone)
            if not is_user_exist:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'User with mobile phone {mobile_phone} not found',
                )
            tickets: Optional[list[ResponseBriefTicket]] = await self.ticket_repository.get_by_user_mobile_phone(
                mobile_phone
            )
            if not tickets:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'Tickets with mobile phone {mobile_phone} not found',
                )
            return tickets
