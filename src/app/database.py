from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.settings import settings


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
            bind=self.engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False
        )


class Transaction:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session: AsyncSession | None = None

    async def __aenter__(self):
        self.session: AsyncSession = self.engine.async_session()

    async def __aexit__(self, exc_type, *args):
        if self.session:
            await self.rollback()
            await self.session.close()
            self.session = None

    async def commit(self):
        if self.session:
            await self.session.commit()

    async def rollback(self):
        if self.session:
            await self.session.rollback()
