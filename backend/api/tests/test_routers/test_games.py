from unittest.mock import patch
import pytest

from api.domain.core import ListingResult
from api.domain.games import Game


class TestHealthRouter:
    """
    Tests for the Health router.
    """

    @pytest.mark.asyncio
    async def test_retrieve_games(self, test_client, mock_games):
        """
        Tests retrieval of the health status.
        """
        with patch(
            "api.routers.games.retrieve_games",
            return_value=ListingResult(
                items=[
                    Game(id=game.id, started_at=game.started_at, ended_at=game.ended_at, map_image=game.map_image)
                    for game in mock_games
                ],
                total_items=10,
                total_pages=1,
            ),
        ):
            response = await test_client.get("/games")

            assert response.status_code == 200
            data = response.json()
            assert data["pagination"]["total_items"] == 10
            assert len(data["items"]) == 10
