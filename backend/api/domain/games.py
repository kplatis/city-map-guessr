from dataclasses import dataclass
from datetime import datetime


@dataclass
class Game:
    """Domain model for Game"""

    id: str
    started_at: datetime
    ended_at: datetime | None
    map_image: str
