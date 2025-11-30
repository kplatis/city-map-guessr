from dataclasses import dataclass


@dataclass
class Game:
    """
    Domain model for Game
    """

    id: str
    started_at: str
    ended_at: str | None
    map_image: str
