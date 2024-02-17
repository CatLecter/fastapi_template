from dataclasses import asdict

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncResult

from app.database import Transaction
from app.models import User
from app.schemes.internal import InternalUserRequest, InternalUserResponse
from app.utils import to_dict


class UserRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add_user(self, user: InternalUserRequest) -> InternalUserResponse | None:
        stmt = insert(User).values(**asdict(user)).returning(User)
        try:
            cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        except IntegrityError:
            return None
        result: User | None = cursor.scalar_one_or_none()  # noqa
        return InternalUserResponse(**to_dict(result))
