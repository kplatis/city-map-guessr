from typing import AsyncGenerator
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import SessionLocal, create_tables
from api.models.games import Game, City
from datetime import datetime
import uuid


@pytest_asyncio.fixture(name="empty_db_session")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Defines the main database which is empty
    """
    async with SessionLocal() as session:
        await create_tables(clear_before_create=True)
        yield session


@pytest_asyncio.fixture
async def mock_games() -> list[Game]:
    return [
        Game(id=uuid.uuid4(), started_at=datetime(2025, 11, 30, 10, 0, 0), ended_at=None, map_image=f"map{i}.png")
        for i in range(10)
    ]


@pytest_asyncio.fixture
async def populated_db_session(
    mock_games: list[Game], empty_db_session: AsyncSession
) -> AsyncGenerator[AsyncSession, None]:
    """
    Defines the main database which is pre-populated with seed data
    """
    # Create mock cities
    city1 = City(
        id=uuid.uuid4(), name="Tirana", country="ALBANIA", continent="EUROPE", latitude="41.3275", longitude="19.8187"
    )
    city2 = City(
        id=uuid.uuid4(), name="Athens", country="GREECE", continent="EUROPE", latitude="37.9838", longitude="23.7275"
    )
    # Add cities
    empty_db_session.add_all([city1, city2])
    await empty_db_session.commit()

    # Add games
    empty_db_session.add_all(mock_games)
    await empty_db_session.commit()

    yield empty_db_session
