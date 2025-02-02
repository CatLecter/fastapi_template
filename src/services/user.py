from http import HTTPStatus
from typing import Optional
from uuid import UUID

from fastapi import HTTPException

from src.database import Transaction
from src.repositories import UserRepository
from src.schemes.external import ResponseBriefUser, ResponseUser
from src.schemes.internal import InternalRequestUser


class UserService:
    def __init__(self, transaction: Transaction, user_repository: UserRepository):
        self.transaction = transaction
        self.user_repository = user_repository

    async def add(self, user: InternalRequestUser) -> ResponseUser:
        async with self.transaction:
            is_exist: bool = await self.user_repository.check_by_mobile_phone(user.mobile_phone)
            if is_exist:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail=f'User with phone number {user.mobile_phone} has already been created',
                )
            result: Optional[ResponseUser] = await self.user_repository.add(user)
            await self.transaction.commit()
            if not result:
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST,
                    detail='Failed to create user',
                )
            return result

    async def get_by_id(self, user_id: UUID) -> ResponseUser:
        async with self.transaction:
            user: Optional[ResponseUser] = await self.user_repository.get_by_id(user_id)
            if not user:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND,
                    detail=f'User with ID {user_id} not found',
                )
            return user

    async def get_all(self) -> list[ResponseBriefUser]:
        async with self.transaction:
            users: Optional[list[ResponseBriefUser]] = await self.user_repository.get_all()
            if not users:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Users not found')
            return users
