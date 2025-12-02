from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.games import Game


async def list_games(page: int, page_size: int, db: AsyncSession) -> list[Game]:
    """
    Retrieve all games from the database.
    """
    offset = (page - 1) * page_size
    result = await db.execute(select(Game).offset(offset).limit(page_size))
    return result.scalars().all()
