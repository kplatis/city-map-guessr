from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.games import City, Game


async def list_games(page: int, page_size: int, db: AsyncSession) -> list[Game]:
    """Retrieve all games from the database."""
    offset = (page - 1) * page_size
    result = await db.execute(select(Game).offset(offset).limit(page_size))
    return result.scalars().all()


async def read_cities(db: AsyncSession) -> list[City]:
    """Retrieve all cities from the database."""
    result = await db.execute(select(City))
    return result.scalars().all()


async def create_game(correct_city: City, db: AsyncSession) -> Game:
    """Create a new game in the database."""
    new_game = Game(ended_at=None, correct_city=correct_city)
    db.add(new_game)
    await db.commit()
    await db.refresh(new_game)
    return new_game
