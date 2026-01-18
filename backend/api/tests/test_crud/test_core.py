import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.core import get_total_items_of_model
from api.models.games import Game as GameModel


class TestCoreCRUD:
    """Test suite for core CRUD operations"""

    @pytest.mark.asyncio
    async def test_get_total_items_of_model_populated_db(self, populated_db_session: AsyncSession) -> None:
        """Test total items and pages for a populated database"""
        total_items, total_pages = await get_total_items_of_model(GameModel, page_size=2, db=populated_db_session)
        assert total_items == 2
        assert total_pages == 1

    @pytest.mark.asyncio
    async def test_get_total_items_of_model_empty_db(self, empty_db_session: AsyncSession) -> None:
        """Test total items and pages for an empty database"""
        total_items, total_pages = await get_total_items_of_model(GameModel, page_size=2, db=empty_db_session)
        assert total_items == 0
        assert total_pages == 0
