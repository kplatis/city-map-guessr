from http import HTTPStatus
from unittest.mock import patch

import pytest
from httpx import AsyncClient

from api.domain.core import ListingResult
from api.domain.games import Game


class TestGamesRouter:
    """Tests for the Games router."""

    @pytest.mark.asyncio
    async def test_retrieve_games(self, test_client: AsyncClient, mock_games: list[Game]) -> None:
        """Tests retrieval of the games."""
        with patch(
            "api.routers.games.retrieve_games",
            return_value=ListingResult(
                items=[
                    Game(id=game.id, started_at=game.started_at, ended_at=game.ended_at, map_image="test_image")
                    for game in mock_games
                ],
                total_items=10,
                total_pages=1,
            ),
        ):
            response = await test_client.get("/games")

            assert response.status_code == HTTPStatus.OK
            data = response.json()
            assert data["pagination"]["total_items"] == len(mock_games)
            assert len(data["items"]) == len(mock_games)
