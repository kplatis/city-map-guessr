from http import HTTPStatus

import pytest
from httpx import AsyncClient


class TestHealthRouter:
    """Tests for the Health router."""

    @pytest.mark.asyncio
    async def test_get_health_status(self, test_client: AsyncClient) -> None:
        """Tests retrieval of the health status."""
        response = await test_client.get("/health")

        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert data["status"] == "ok"
