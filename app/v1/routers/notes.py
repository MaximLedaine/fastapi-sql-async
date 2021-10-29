from fastapi import APIRouter
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from .. import models, schemas
from ..controllers import notes as db

router = APIRouter(
    tags=["notes"]
)

@router.get("/notes/{note_id}", response_model=schemas.NoteOut)
async def get_note(note_id: str):
    note = await db.get_note(id= note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="NoteOut not found")
    return note

@router.get("/notes/", response_model=List[schemas.NoteOut])
async def read_notes(skip: int = 0, limit: int = 100):
    notes = await db.get_notes(skip=skip, limit=limit)
    return notes

@router.post("/notes/", response_model=schemas.NoteOut)
async def create_note(note: schemas.NoteIn):
    note = await db.create_note(note= note)
    return note

@router.delete("/notes/{note_id}", response_model=schemas.NoteOut)
async def delete_note(note_id: str):
    note = await db.get_note(id= note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="NoteOut not found")
    await db.delete_note(id= note_id)
    return note