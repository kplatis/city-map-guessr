"""Database declaration module"""

from collections.abc import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from api.settings import Settings

SQLALCHEMY_DATABASE_URL = Settings().database_url


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models"""

    pass  # noqa: PIE790


engine = create_async_engine(Settings().database_url, poolclass=NullPool)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Inject the database session in requests"""
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_tables() -> None:
    """Create the tables in the database.

    If clear_before_create = True, the tables will be cleared before being created
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
