from dataclasses import asdict
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.orm import load_only

from app.database import Transaction
from app.models import Ticket
from app.schemes.internal import InternalBriefTicketResponse
from app.schemes.internal import InternalTicketRequest, InternalTicketResponse
from app.utils import to_dict


class TicketRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add_ticket(self, item: InternalTicketRequest) -> InternalTicketResponse | None:
        stmt = insert(Ticket).values(**asdict(item)).returning(Ticket)
        try:
            cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        except (ProgrammingError, IntegrityError):
            return None
        result: Ticket | None = cursor.scalar_one_or_none()  # noqa
        return InternalTicketResponse(**to_dict(result))

    async def get_tickets_by_user_id(self, user_id: UUID) -> list[InternalBriefTicketResponse] | None:
        stmt = (
            select(Ticket).where(Ticket.visitor_id == user_id).options(load_only(Ticket.ticket_id, Ticket.event_name))
        )
        cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        result: list[Ticket] | None = cursor.scalars().all()  # noqa
        return [InternalBriefTicketResponse(**to_dict(_)) for _ in result]

    async def get_ticket(self, ticket_id: UUID) -> InternalTicketResponse | None:
        stmt = select(Ticket).where(Ticket.ticket_id == ticket_id)
        cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        result: Ticket | None = cursor.scalar_one_or_none()  # noqa
        return InternalTicketResponse(**to_dict(result)) if result else None
