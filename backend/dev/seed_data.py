import asyncio
import json
import os
from datetime import datetime
from sqlalchemy import insert

from api.database import SessionLocal
from api.models.games import City, Game

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(CURRENT_DIR, "data")


async def seed_data():
    """
    Function to seed initial data into the database.
    """

    # Start an async session
    async with SessionLocal() as session:
        try:
            print("⬆️ Importing cities...")
            with open(f"{DATA_FILE_PATH}/cities.json", "r") as file:
                cities = json.load(file)
                await session.execute(insert(City).values(cities))
            await session.commit()

            print("⬆️ Importing games...")
            with open(f"{DATA_FILE_PATH}/games.json", "r") as file:
                games = json.load(file)
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
            print(f"❌ An error occurred: {e}")
            raise

        finally:
            await session.close()


if __name__ == "__main__":
    asyncio.run(seed_data())
