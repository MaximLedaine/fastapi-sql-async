from typing import List, Optional

from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str
    completed: bool


class NoteOut(BaseModel):
    id: int
    text: str
    completed: bool