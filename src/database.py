import backoff
from asyncpg.exceptions import TooManyConnectionsError
from sqlalchemy import Result
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.settings import settings


class Engine:
    def __init__(self) -> None:
        self.engine = create_async_engine(
            url=settings.STORAGE_URI,
            echo=False,
            echo_pool=False,
            pool_size=settings.POOL_SIZE,
            max_overflow=settings.MAX_OVERFLOW,
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )


class Transaction:
    def __init__(self, engine: Engine):
        self._engine = engine
        self._session: AsyncSession | None = None

    async def __aenter__(self):
        self._session = self._engine.async_session()

    async def __aexit__(self, exc_type, *args):
        if self._session:
            await self.rollback()
            await self._session.close()
            self._session = None

    async def commit(self):
        if self._session:
            await self._session.commit()

    async def rollback(self):
        if self._session:
            await self._session.rollback()

    @backoff.on_exception(
        backoff.expo,
        TooManyConnectionsError,
        max_time=settings.MAX_TIME,
        max_tries=settings.MAX_TRIES,
    )
    async def execute(self, *args, **kwargs) -> Result:
        if self._session:
            return await self._session.execute(*args, **kwargs)
