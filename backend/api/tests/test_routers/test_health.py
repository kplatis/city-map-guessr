import pytest


class TestHealthRouter:
    """
    Tests for the Health router.
    """

    @pytest.mark.asyncio
    async def test_get_health_status(self, test_client):
        """
        Tests retrieval of the health status.
        """
        response = await test_client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
