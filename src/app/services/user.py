from http import HTTPStatus

from fastapi import HTTPException

from app.database import Transaction
from app.repositories import UserRepository
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
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=f'Failed to create user')
            return result
