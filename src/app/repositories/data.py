from dataclasses import asdict

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncResult

from app.database import Transaction
from app.models import Data
from app.schemes.internal import InternalDataRequest, InternalDataResponse
from app.utils import to_dict


class DataRepository:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    async def add_data(self, item: InternalDataRequest) -> InternalDataResponse | None:
        stmt = insert(Data).values(**asdict(item)).returning(Data)
        cursor: AsyncResult = await self.transaction.session.execute(stmt)  # noqa
        result: Data | None = cursor.scalar_one_or_none()  # noqa
        return InternalDataResponse(**to_dict(result))
