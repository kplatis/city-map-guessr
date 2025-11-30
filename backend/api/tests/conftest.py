from typing import AsyncGenerator
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import SessionLocal, create_tables


@pytest_asyncio.fixture(name="main_db")
async def db() -> AsyncGenerator[AsyncSession, None]:
    """
    Defines the main database which is empty
    """
    async with SessionLocal() as session:
        await create_tables(clear_before_create=True)
        yield session
