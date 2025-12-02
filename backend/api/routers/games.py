from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_db
from api.schemas.core import PaginatedResponse, PaginationInfoOut, PaginationParamsIn
from api.schemas.games import GameOut
from api.services.games import retrieve_games

games_router = APIRouter()


@games_router.get("", operation_id="retrieveGames")
async def retrieve_games_endpoint(
    pagination_parameters: PaginationParamsIn = Depends(),  # noqa: B008
    db: AsyncSession = Depends(get_db),  # noqa: B008
) -> PaginatedResponse[GameOut]:
    """Retrieve all games with pagination"""

    games = await retrieve_games(pagination_params=pagination_parameters.to_domain(), db=db)
    return PaginatedResponse[GameOut](
        items=[GameOut.model_validate(game) for game in games.items],
        pagination=PaginationInfoOut(
            page=pagination_parameters.page,
            page_size=pagination_parameters.page_size,
            total_items=games.total_items,
            total_pages=games.total_pages,
        ),
    )
