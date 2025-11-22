"""SQLAlchemy database models for Decks and Cards."""

from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Enum
from sqlalchemy.orm import relationship

from database import Base


class CardStatus(PyEnum):
    """Card status enumeration."""

    NOT_STUDIED = "未学習"
    MASTERED = "覚えた"
    WEAK = "苦手"


class Deck(Base):
    """Deck (問題集) model."""

    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship: One deck has many cards
    cards = relationship("Card", back_populates="deck", cascade="all, delete-orphan")


class Card(Base):
    """Card (問題) model."""

    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    deck_id = Column(Integer, ForeignKey("decks.id"), nullable=False, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    explanation = Column(Text, nullable=False)
    status = Column(
        Enum(CardStatus, native_enum=False, values_callable=lambda x: [e.value for e in x]),
        default=CardStatus.NOT_STUDIED,
        nullable=False,
    )

    # Relationship: Many cards belong to one deck
    deck = relationship("Deck", back_populates="cards")
