import asyncio
import json
import os
from sqlalchemy import insert

from api.database import SessionLocal

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(CURRENT_DIR, "data")


async def seed_data():
    """
    Function to seed initial data into the database.
    """

    # Start an async session
    async with SessionLocal() as session:
        try:

            print("⬆️ Importing data...")

        except Exception as e:
            await session.rollback()
            print(f"❌ An error occurred: {e}")
            raise  # Re-raise the exception to see the full traceback

        finally:
            await session.close()


if __name__ == "__main__":
    asyncio.run(seed_data())
