"""API routes for card (問題) management."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud import create_card, get_card, get_cards_by_deck, get_deck
from database import get_db
from schemas import CardCreate, CardResponse

router = APIRouter(prefix="/decks", tags=["cards"])


@router.post(
    "/{deck_id}/cards",
    response_model=CardResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_card_endpoint(
    deck_id: int,
    card: CardCreate,
    db: Session = Depends(get_db),
) -> CardResponse:
    """Create a new card for a deck."""
    # Verify deck exists
    deck = get_deck(db=db, deck_id=deck_id)
    if deck is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deck with id {deck_id} not found",
        )
    # Override deck_id from path parameter
    card.deck_id = deck_id
    return create_card(db=db, card=card)


@router.get("/{deck_id}/cards", response_model=list[CardResponse])
async def get_cards_by_deck_endpoint(
    deck_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[CardResponse]:
    """Get all cards for a specific deck with pagination."""
    # Verify deck exists
    deck = get_deck(db=db, deck_id=deck_id)
    if deck is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deck with id {deck_id} not found",
        )
    cards = get_cards_by_deck(db=db, deck_id=deck_id, skip=skip, limit=limit)
    return cards


@router.get("/cards/{card_id}", response_model=CardResponse)
async def get_card_endpoint(
    card_id: int,
    db: Session = Depends(get_db),
) -> CardResponse:
    """Get a card by ID."""
    card = get_card(db=db, card_id=card_id)
    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card with id {card_id} not found",
        )
    return card
