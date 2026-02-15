from fastapi import FastAPI
from crud import create_note, delete, note_list, get_note, update
from schemas import NoteResponse, CreateNote

app = FastAPI()

@app.post("/notes/", response_model=NoteResponse, status_code=201)
async def create_note_Endpoint(note: CreateNote):
    return create_note(note)

@app.get("/notes/",response_model=list[NoteResponse])
def get_notes():
    return note_list

@app.get("/notes/{note_id}",response_model=NoteResponse)
def get_note_endpoint(note_id: int):
    return get_note(note_id)

@app.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note_endpoint(note_id: int):
    return update(note_id)
    

@app.delete("/notes/{note_id}", status_code=204)
async def delete_endpoint(note_id: int):
    delete(note_id)

