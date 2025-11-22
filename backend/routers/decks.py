"""API routes for deck (問題集) management."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud import create_deck, get_deck, get_decks
from database import get_db
from schemas import DeckCreate, DeckResponse

router = APIRouter(prefix="/decks", tags=["decks"])


@router.post("", response_model=DeckResponse, status_code=status.HTTP_201_CREATED)
async def create_deck_endpoint(
    deck: DeckCreate,
    db: Session = Depends(get_db),
) -> DeckResponse:
    """Create a new deck."""
    return create_deck(db=db, deck=deck)


@router.get("", response_model=list[DeckResponse])
async def get_decks_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[DeckResponse]:
    """Get all decks with pagination."""
    decks = get_decks(db=db, skip=skip, limit=limit)
    return decks


@router.get("/{deck_id}", response_model=DeckResponse)
async def get_deck_endpoint(
    deck_id: int,
    db: Session = Depends(get_db),
) -> DeckResponse:
    """Get a deck by ID."""
    deck = get_deck(db=db, deck_id=deck_id)
    if deck is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Deck with id {deck_id} not found",
        )
    return deck
