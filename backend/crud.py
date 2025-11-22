"""CRUD operations for database models."""

from sqlalchemy.orm import Session

from models import Card, Deck
from schemas import CardCreate, DeckCreate


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


def create_card(db: Session, card: CardCreate) -> Card:
    """Create a new card."""
    db_card = Card(
        deck_id=card.deck_id,
        question=card.question,
        answer=card.answer,
        explanation=card.explanation,
        status=card.status,
    )
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_card(db: Session, card_id: int) -> Card | None:
    """Get a card by ID."""
    return db.query(Card).filter(Card.id == card_id).first()


def get_cards_by_deck(
    db: Session, deck_id: int, skip: int = 0, limit: int = 100
) -> list[Card]:
    """Get all cards for a specific deck with pagination."""
    return (
        db.query(Card).filter(Card.deck_id == deck_id).offset(skip).limit(limit).all()
    )
