from unittest.mock import patch
import pytest
from api.domain.core import PaginationParams
from api.services.games import retrieve_games


class TestGamesServices:
    """
    Test suite for game services
    """

    @pytest.mark.asyncio
    async def test_retrieve_games(self, mock_games, empty_db_session):
        pagination_params = PaginationParams(page=1, page_size=10)
        with patch("api.services.games.list_games", return_value=mock_games), patch(
            "api.services.games.get_total_items_of_model", return_value=[10, 1]
        ):
            result = await retrieve_games(pagination_params, empty_db_session)
            assert len(result.items) == 10
            assert result.total_items == 10
            assert result.total_pages == 1
