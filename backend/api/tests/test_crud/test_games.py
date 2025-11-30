import pytest

from api.crud.games import list_games


class TestGamesCRUD:
    """
    Test suite for game CRUD operations
    """

    @pytest.mark.asyncio
    async def test_list_games_populated_db(self, populated_db_session):
        """
        Test listing games from a populated database
        """

        games = await list_games(page=1, page_size=5, db=populated_db_session)
        assert len(games) == 5

    @pytest.mark.asyncio
    async def test_list_games_empty_db(self, empty_db_session):
        """
        Test listing games from an empty database
        """

        games = await list_games(page=1, page_size=5, db=empty_db_session)
        assert len(games) == 0
