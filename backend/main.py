"""FlashLearn Backend - FastAPI Application Entry Point."""

from fastapi import FastAPI

from database import Base, engine
from routers import decks

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FlashLearn API", version="0.1.0")

# Include routers
app.include_router(decks.router)


@app.get("/")
async def root():
    """Hello World endpoint."""
    return {"message": "Hello World"}

