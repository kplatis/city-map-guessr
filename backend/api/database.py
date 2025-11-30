"""
Database declaration module
"""

from typing import AsyncGenerator
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from api.settings import Settings

SQLALCHEMY_DATABASE_URL = Settings().database_url


class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy models
    """

    pass


engine = create_async_engine(Settings().database_url, poolclass=NullPool)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Function that injects the database session in requests
    """
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


async def create_tables(clear_before_create: bool = False):
    """
    Creates the tables in the database.

    If clear_before_create = True, the tables will be cleared before being created
    """
    async with engine.begin() as conn:
        if clear_before_create:
            await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
