from unittest.mock import patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.domain.core import PaginationParams
from api.models.games import City, Game
from api.services.games import initialize_game, retrieve_games


class TestGamesServices:
    """Test suite for game services"""

    @pytest.mark.asyncio
    async def test_retrieve_games(self, mock_games: list[Game], empty_db_session: AsyncSession) -> None:
        """Test retrieve_games service"""
        pagination_params = PaginationParams(page=1, page_size=10)
        with patch("api.services.games.list_games", return_value=mock_games), patch(
            "api.services.games.get_total_items_of_model",
            return_value=[10, 1],
        ):
            result = await retrieve_games(pagination_params, empty_db_session)
            assert len(result.items) == len(mock_games)
            assert result.total_items == len(mock_games)
            assert result.total_pages == 1

    @pytest.mark.asyncio
    async def test_initialize_game(
        self,
        mock_game: Game,
        mock_cities: list[City],
        empty_db_session: AsyncSession,
    ) -> None:
        """Test initialize_game service"""

        with patch("api.services.games.read_cities", return_value=mock_cities), patch(
            "api.services.games.create_game",
            return_value=mock_game,
        ):

            result = await initialize_game(empty_db_session)
            assert result.id is not None
            assert result.map_image == "https://example.com/city_map.png"
            assert result.ended_at is None
