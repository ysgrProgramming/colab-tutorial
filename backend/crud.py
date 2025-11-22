"""CRUD operations for database models."""

from sqlalchemy.orm import Session

from models import Deck
from schemas import DeckCreate


def create_deck(db: Session, deck: DeckCreate) -> Deck:
    """Create a new deck."""
    db_deck = Deck(title=deck.title)
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck


def get_deck(db: Session, deck_id: int) -> Deck | None:
    """Get a deck by ID."""
    return db.query(Deck).filter(Deck.id == deck_id).first()


def get_decks(db: Session, skip: int = 0, limit: int = 100) -> list[Deck]:
    """Get all decks with pagination."""
    return db.query(Deck).offset(skip).limit(limit).all()
