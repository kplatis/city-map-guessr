from collections.abc import AsyncGenerator

import pytest_asyncio
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from api.main import app as main_app


@pytest_asyncio.fixture(name="test_app")
async def app() -> AsyncGenerator:
    """Application override"""
    yield main_app
    main_app.dependency_overrides = {}


@pytest_asyncio.fixture
async def test_client(test_app: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    """Test client fixture"""
    async with AsyncClient(transport=ASGITransport(app=test_app), base_url="http://test/api") as client:
        yield client
