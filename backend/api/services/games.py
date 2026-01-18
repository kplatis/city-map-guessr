import random

from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.core import get_total_items_of_model
from api.crud.games import create_game, list_games, read_cities
from api.domain.core import ListingResult, PaginationParams
from api.domain.games import Game
from api.models.games import Game as GameModel


async def retrieve_games(pagination_params: PaginationParams, db: AsyncSession) -> list[Game]:
    """Retrieve all games from the database."""
    games = await list_games(page=pagination_params.page, page_size=pagination_params.page_size, db=db)
    total_items, total_pages = await get_total_items_of_model(GameModel, pagination_params.page_size, db)
    return ListingResult(
        items=[
            Game(id=game.id, started_at=game.started_at, ended_at=game.ended_at, map_image=game.correct_city.map_image)
            for game in games
        ],
        total_items=total_items,
        total_pages=total_pages,
    )


async def initialize_game(db: AsyncSession) -> Game:
    """Initialize a new game in the database."""
    all_cities = await read_cities(db)

    correct_city = random.choice(all_cities) if all_cities else None  # noqa: S311
    game = await create_game(correct_city=correct_city, db=db)
    return Game(id=game.id, started_at=game.started_at, ended_at=game.ended_at, map_image=game.correct_city.map_image)
