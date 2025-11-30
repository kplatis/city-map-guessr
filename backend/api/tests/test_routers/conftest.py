from httpx import ASGITransport, AsyncClient
import pytest_asyncio
from api.main import app as main_app


@pytest_asyncio.fixture(name="test_app")
async def app():
    """
    Application override with loggedin
    """
    yield main_app
    main_app.dependency_overrides = {}


@pytest_asyncio.fixture
async def test_client(test_app):
    """
    Test client fixture
    """
    async with AsyncClient(transport=ASGITransport(app=test_app), base_url="http://test/api") as client:
        yield client
