"""Seed initial data into the database"""

import asyncio
import json
from datetime import datetime
from pathlib import Path

import anyio
from sqlalchemy import insert

from api.database import SessionLocal
from api.models.games import City, Game

CURRENT_DIR = Path(Path(__file__).resolve()).parent
DATA_FILE_PATH = Path(CURRENT_DIR) / "data"


async def seed_data() -> None:
    """Seed initial data into the database."""

    # Start an async session
    async with SessionLocal() as session:
        try:
            print("⬆️ Importing cities...")  # noqa: T201
            async with await anyio.open_file(f"{DATA_FILE_PATH}/cities.json") as file:
                cities_content = await file.read()
                cities = json.loads(cities_content)
                await session.execute(insert(City).values(cities))
            await session.commit()

            print("⬆️ Importing games...")  # noqa: T201
            async with await anyio.open_file(f"{DATA_FILE_PATH}/games.json") as file:
                games_content = await file.read()
                games = json.loads(games_content)
                # Convert started_at and ended_at to datetime objects
                for game in games:
                    game["started_at"] = datetime.fromisoformat(game["started_at"].replace("Z", "+00:00"))
                    game["ended_at"] = (
                        datetime.fromisoformat(game["ended_at"].replace("Z", "+00:00")) if game["ended_at"] else None
                    )
                await session.execute(insert(Game).values(games))
            await session.commit()

        except Exception as e:
            await session.rollback()
            print(f"❌ An error occurred: {e}")  # noqa: T201
            raise

        finally:
            await session.close()


if __name__ == "__main__":
    asyncio.run(seed_data())
