from dataclasses import asdict
from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import Result, exists, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import load_only

from app.database import Transaction
from app.models import User
from app.schemes.external import ResponseBriefUser, ResponseUser
from app.schemes.internal import InternalRequestUser


class UserRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add(self, user: InternalRequestUser) -> ResponseUser:
        stmt = insert(User).values(**asdict(user)).returning(User)
        cursor: Result = await self.transaction.execute(stmt)
        result: User = cursor.scalar_one()
        return ResponseUser(**result.to_dict())

    async def get_by_id(self, user_id: UUID) -> Optional[ResponseUser]:
        stmt = select(User).where(User.user_id == user_id)
        cursor: Result = await self.transaction.execute(stmt)
        result: Optional[User] = cursor.scalar_one_or_none()
        return ResponseUser(**result.to_dict()) if result else None

    async def get_all(self) -> Optional[list[ResponseBriefUser]]:
        stmt = select(User).options(load_only(User.user_id, User.full_name))
        cursor: Result = await self.transaction.execute(stmt)
        result: Sequence[User] = cursor.scalars().all()
        return [ResponseBriefUser(**_.to_dict()) for _ in result] if result else None

    async def check_by_mobile_phone(self, mobile_phone: str) -> bool:
        stmt = select(exists(User.user_id).where(User.mobile_phone == mobile_phone))
        cursor: Result = await self.transaction.execute(stmt)
        return cursor.scalar()
