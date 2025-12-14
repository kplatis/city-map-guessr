"""General conftest definitions"""

import datetime
import uuid
from collections.abc import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import SessionLocal, create_tables
from api.enums import Continent, Country
from api.models.games import City, Game


@pytest_asyncio.fixture(name="empty_db_session")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Defines the main database which is empty"""
    async with SessionLocal() as session:
        await create_tables()
        yield session


@pytest_asyncio.fixture(name="mock_cities")
async def mock_cities_list() -> list[City]:
    """Provides a list of mock cities"""
    return [
        City(
            id=uuid.uuid4(),
            name=f"City {i}",
            country=Country.GREECE,
            continent=Continent.EUROPE,
            latitude="0.0",
            longitude="0.0",
            map_image="https://example.com/city_map.png",
        )
        for i in range(10)
    ]


@pytest_asyncio.fixture(name="mock_games")
async def mock_games_list(mock_cities: list[City]) -> list[Game]:
    """Provides a list of mock games"""
    return [
        Game(
            id=uuid.uuid4(),
            started_at=datetime.datetime(2025, 11, 30, 10, 0, 0, tzinfo=datetime.UTC),
            ended_at=None,
            correct_city=mock_cities[0],
        )
        for _ in range(10)
    ]


@pytest_asyncio.fixture
async def populated_db_session(
    mock_games: list[Game],
    empty_db_session: AsyncSession,
) -> AsyncGenerator[AsyncSession, None]:
    """Defines the main database which is pre-populated with seed data"""
    # Create mock cities
    city1 = City(
        id=uuid.uuid4(),
        name="Tirana",
        country="ALBANIA",
        continent="EUROPE",
        latitude="41.3275",
        longitude="19.8187",
        map_image="https://example.com/tirana_map.png",
    )
    city2 = City(
        id=uuid.uuid4(),
        name="Athens",
        country="GREECE",
        continent="EUROPE",
        latitude="37.9838",
        longitude="23.7275",
        map_image="https://example.com/athens_map.png",
    )
    # Add cities
    empty_db_session.add_all([city1, city2])
    await empty_db_session.commit()

    # Assign correct_city_id for each game to a random city
    for game in mock_games:
        game.correct_city_id = city1.id

    # Add games
    empty_db_session.add_all(mock_games)
    await empty_db_session.commit()

    yield empty_db_session
