from .. import models, schemas
from ..database import database


async def get_note(id: str):
    query = models.notes.select().where(models.notes.c.id == id)
    return await database.fetch_one(query)


async def get_note_by_text(text: str):
    query = models.notes.select().where(models.notes.c.text == text)
    return await database.fetch_one(query)


async def get_notes(skip: int = 0, limit: int = 100):
    query = models.notes.select().offset(skip).limit(limit)
    return await database.fetch_all(query)


async def create_note(note: schemas.NoteOut):
    query = models.notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}

async def delete_note(id: str):
    query= models.notes.delete().where(models.notes.c.id == id)
    return await database.execute(query)