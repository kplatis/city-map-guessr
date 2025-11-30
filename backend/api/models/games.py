"""
Model definition for game
"""

import uuid
from sqlalchemy import Column, UUID, DateTime, Enum, ForeignKey, String, func
from sqlalchemy.orm import relationship

from api.database import Base
from api.enums import Continent, Country


class Game(Base):
    """
    SQLAlchemy model for game
    """

    __tablename__ = "games"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    started_at = Column(DateTime(timezone=True), server_default=func.now())
    ended_at = Column(DateTime(timezone=True), nullable=True)
    map_image = Column(String, nullable=False)

    # relationships
    guesses = relationship("Guess", back_populates="game", lazy="selectin")


class City(Base):
    """
    SQLAlchemy model for city
    """

    __tablename__ = "cities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)
    country = Column(Enum(Country, name="country"), nullable=False, default=Country.ALBANIA)
    continent = Column(Enum(Continent, name="continent"), nullable=False, default=Continent.EUROPE)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)

    # relationships
    guesses = relationship("Guess", back_populates="city", lazy="selectin")


class Guess(Base):
    """
    SQLAlchemy model for guess
    """

    __tablename__ = "guesses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    guessed_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    game_id = Column(UUID, ForeignKey("games.id"))
    game = relationship("Game", back_populates="guesses", lazy="selectin")

    city_id = Column(UUID, ForeignKey("cities.id"))
    city = relationship("City", back_populates="guesses", lazy="selectin")
