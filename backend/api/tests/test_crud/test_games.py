import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.games import list_games, read_cities, create_game


class TestGamesCRUD:
    """Test suite for game CRUD operations"""

    @pytest.mark.asyncio
    async def test_list_games_populated_db(self, populated_db_session: AsyncSession) -> None:
        """Test listing games from a populated database"""

        games = await list_games(page=1, page_size=5, db=populated_db_session)
        assert len(games) == 5

    @pytest.mark.asyncio
    async def test_list_games_empty_db(self, empty_db_session: AsyncSession) -> None:
        """Test listing games from an empty database"""

        games = await list_games(page=1, page_size=5, db=empty_db_session)
        assert len(games) == 0

    @pytest.mark.asyncio
    async def test_read_cities_populated_db(self, populated_db_session: AsyncSession) -> None:
        """Test reading cities from a populated database"""

        cities = await read_cities(db=populated_db_session)
        assert len(cities) == 3

    @pytest.mark.asyncio
    async def test_read_cities_empty_db(self, empty_db_session: AsyncSession) -> None:
        """Test reading cities from an empty database"""

        cities = await read_cities(db=empty_db_session)
        assert len(cities) == 0

    @pytest.mark.asyncio
    async def test_create_game_with_cities(self, populated_db_session: AsyncSession) -> None:
        """Test creating a game with a list of cities"""
        cities = await read_cities(db=populated_db_session)
        game = await create_game(cities=cities, db=populated_db_session)
        assert game.id is not None
        assert len(game.cities) == len(cities)
        assert game.correct_city in cities
        assert game.correct_city is not None

    @pytest.mark.asyncio
    async def test_create_game_with_empty_cities(self, populated_db_session: AsyncSession) -> None:
        """Test creating a game with an empty list of cities"""
        game = await create_game(cities=[], db=populated_db_session)
        assert game.id is not None
        assert len(game.cities) == 0
