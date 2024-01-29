from http import HTTPStatus

from fastapi import HTTPException

from app.database import Transaction
from app.repositories import DataRepository
from app.schemes.internal import InternalDataRequest, InternalDataResponse


class DataService:
    def __init__(self, transaction: Transaction, data_repository: DataRepository):
        self.transaction = transaction
        self.data_repository = data_repository

    async def add_data(self, item: InternalDataRequest) -> InternalDataResponse:
        async with self.transaction:
            result: InternalDataResponse | None = await self.data_repository.add_data(item)
            await self.transaction.commit()
            if not result:
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=f'Failed to create data')
            return result
