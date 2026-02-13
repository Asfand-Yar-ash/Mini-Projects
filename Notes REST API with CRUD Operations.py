from typing import Annotated
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()
note_counter = 1
class Note(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

notes = []
@app.post("/notes/", response_model=Note)
def create_note(note: Note):
    global note_counter
    note.id = note_counter
    note.created_at = datetime.now()
    note.updated_at = datetime.now()
    notes.append(note)
    note_counter += 1
    return note

@app.get("/notes/",response_model=Note)
def get_notes():
    return notes

@app.get("/notes/{id}",response_model=Note)
def get_note(id: int):
    if id != notes[id]:
        raise HTTPException(status_code=404, detail="Not Found")
    return notes[id]

@app.put("/notes/{id}")
async def update(id: int):
    if id == notes[id]:
        
