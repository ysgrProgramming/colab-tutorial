"""FlashLearn Backend - FastAPI Application Entry Point."""

from fastapi import FastAPI

app = FastAPI(title="FlashLearn API", version="0.1.0")


@app.get("/")
async def root():
    """Hello World endpoint."""
    return {"message": "Hello World"}

