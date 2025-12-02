from datetime import datetime
from pydantic import UUID4, BaseModel, ConfigDict


class GameOut(BaseModel):
    """
    Pydantic model representing a game output
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID4
    started_at: datetime
    ended_at: datetime | None
    map_image: str
