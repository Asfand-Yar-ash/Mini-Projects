from pydantic import BaseModel
from datetime import datetime


class CreateNote(BaseModel):
    title: str
    content: str


class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
