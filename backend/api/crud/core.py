from math import ceil
from typing import Generic, TypeVar
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


async def get_total_items_of_model(model: Generic[T], page_size: int, db: AsyncSession) -> tuple[int, int]:
    """
    Retrieves the total items and pages of the model
    """
    result = await db.execute(select(func.count()).select_from(model))
    total_items = result.scalar()
    total_pages = ceil(total_items / page_size)
    return total_items, total_pages
