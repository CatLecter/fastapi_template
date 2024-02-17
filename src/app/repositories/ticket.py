from dataclasses import asdict

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncResult

from app.database import Transaction
from app.models import Ticket
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
