import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.games import create_game, list_games, read_cities
from api.models.games import City


class TestGamesCRUD:
    """Test suite for game CRUD operations"""

    @pytest.mark.asyncio
    async def test_list_games_populated_db(self, populated_db_session: AsyncSession) -> None:
        """Test listing games from a populated database"""

        games = await list_games(page=1, page_size=5, db=populated_db_session)
        assert len(games) == 2

    @pytest.mark.asyncio
    async def test_list_games_empty_db(self, empty_db_session: AsyncSession) -> None:
        """Test listing games from an empty database"""

        games = await list_games(page=1, page_size=5, db=empty_db_session)
        assert len(games) == 0

    @pytest.mark.asyncio
    async def test_read_cities_populated_db(self, populated_db_session: AsyncSession) -> None:
        """Test reading cities from a populated database"""

        cities = await read_cities(db=populated_db_session)
        assert len(cities) == 2

    @pytest.mark.asyncio
    async def test_read_cities_empty_db(self, empty_db_session: AsyncSession) -> None:
        """Test reading cities from an empty database"""

        cities = await read_cities(db=empty_db_session)
        assert len(cities) == 0

    @pytest.mark.asyncio
    async def test_create_game_with_cities(self, mock_cities: list[City], populated_db_session: AsyncSession) -> None:
        """Test creating a game with a list of cities"""
        game = await create_game(correct_city=mock_cities[0], db=populated_db_session)
        assert game.id is not None
        assert game.correct_city in mock_cities
        assert game.correct_city is not None

    @pytest.mark.asyncio
    async def test_create_game_with_empty_cities(
        self,
        populated_db_session: AsyncSession,
    ) -> None:
        """Test creating a game with an empty list of cities"""
        game = await create_game(correct_city=None, db=populated_db_session)
        assert game.id is not None
        assert game.correct_city is None
