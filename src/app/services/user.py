from http import HTTPStatus
from uuid import UUID

from fastapi import HTTPException

from app.database import Transaction
from app.repositories import UserRepository
from app.schemes.internal import InternalBriefUserResponse
from app.schemes.internal import InternalUserRequest, InternalUserResponse


class UserService:
    def __init__(self, transaction: Transaction, user_repository: UserRepository):
        self.transaction = transaction
        self.user_repository = user_repository

    async def add_user(self, user: InternalUserRequest) -> InternalUserResponse:
        async with self.transaction:
            result: InternalUserResponse | None = await self.user_repository.add_user(user)
            await self.transaction.commit()
            if not result:
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail='Failed to create user')
            return result

    async def get_users(self) -> list[InternalBriefUserResponse]:
        async with self.transaction:
            users: list[InternalBriefUserResponse] | None = await self.user_repository.get_users()
            if not users:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Users not found')
            return users

    async def get_user(self, user_id: UUID) -> InternalUserResponse:
        async with self.transaction:
            user: InternalUserResponse | None = await self.user_repository.get_user(user_id)
            if not user:
                raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'User with id={user_id} not found')
            return user
