from dataclasses import asdict
from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import Result, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import load_only

from src.database import Transaction
from src.models import Ticket
from src.schemes.external import ResponseBriefTicket, ResponseTicket
from src.schemes.internal import InternalRequestTicket


class TicketRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add(self, item: InternalRequestTicket) -> ResponseTicket:
        stmt = insert(Ticket).values(**asdict(item)).returning(Ticket)
        cursor: Result = await self.transaction.execute(stmt)
        result: Ticket = cursor.scalar_one()
        return ResponseTicket(**result.to_dict())

    async def get_by_id(self, ticket_id: UUID) -> Optional[ResponseTicket]:
        stmt = select(Ticket).where(Ticket.ticket_id == ticket_id)
        cursor: Result = await self.transaction.execute(stmt)
        result: Optional[Ticket] = cursor.scalar_one_or_none()
        return ResponseTicket(**result.to_dict()) if result else None

    async def get_by_user_mobile_phone(self, mobile_phone: str) -> Optional[list[ResponseBriefTicket]]:
        stmt = (
            select(Ticket)
            .where(Ticket.visitor_mobile_phone == mobile_phone)
            .options(load_only(Ticket.ticket_id, Ticket.event_name))
        )
        cursor: Result = await self.transaction.execute(stmt)
        result: Sequence[Ticket] = cursor.scalars().all()
        return [ResponseBriefTicket(**_.to_dict()) for _ in result] if result else None
