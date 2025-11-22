"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from models import CardStatus


# ==================== Deck Schemas ====================


class DeckBase(BaseModel):
    """Base schema for Deck with common fields."""

    title: str


class DeckCreate(DeckBase):
    """Schema for creating a new deck."""

    pass


class DeckResponse(DeckBase):
    """Schema for deck API response."""

    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==================== Card Schemas ====================


class CardBase(BaseModel):
    """Base schema for Card with common fields."""

    question: str
    answer: str
    explanation: str
    status: CardStatus = CardStatus.NOT_STUDIED


class CardCreate(CardBase):
    """Schema for creating a new card."""

    deck_id: int


class CardResponse(CardBase):
    """Schema for card API response."""

    id: int
    deck_id: int

    model_config = ConfigDict(from_attributes=True)


# ==================== Extended Response Schemas ====================


class DeckWithCardsResponse(DeckResponse):
    """Schema for deck response with nested cards."""

    cards: list[CardResponse] = []


class CardWithDeckResponse(CardResponse):
    """Schema for card response with nested deck info."""

    deck: Optional[DeckResponse] = None
