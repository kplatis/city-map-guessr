from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.core import get_total_items_of_model
from api.crud.games import list_games
from api.domain.games import Game
from api.domain.core import ListingResult, PaginationParams
from api.models.games import Game as GameModel


async def retrieve_games(pagination_params: PaginationParams, db: AsyncSession) -> list[Game]:
    """
    Retrieve all games from the database.
    """
    games = await list_games(page=pagination_params.page, page_size=pagination_params.page_size, db=db)
    total_items, total_pages = await get_total_items_of_model(GameModel, pagination_params.page_size, db)
    return ListingResult(items=games, total_items=total_items, total_pages=total_pages)
