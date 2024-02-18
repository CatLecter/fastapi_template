from dataclasses import asdict
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.orm import load_only

from app.database import Transaction
from app.models import User
from app.schemes.internal import InternalBriefUserResponse
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

    async def get_users(self) -> list[InternalBriefUserResponse] | None:
        stmt = select(User).options(load_only(User.user_id, User.full_name))
        cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        result: list[User] | None = cursor.scalars().all()  # noqa
        return [InternalBriefUserResponse(**to_dict(_)) for _ in result]

    async def get_user(self, user_id: UUID) -> InternalUserResponse | None:
        stmt = select(User).where(User.user_id == user_id)
        cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        result: User | None = cursor.scalar_one_or_none()  # noqa
        return InternalUserResponse(**to_dict(result)) if result else None
