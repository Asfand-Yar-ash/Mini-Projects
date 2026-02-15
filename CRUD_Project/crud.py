from schemas import NoteCreate
from datetime import datetime
from fastapi import HTTPException
note_list = []
note_counter = 1
def create_note(note_data: NoteCreate):
    global note_counter
    now = datetime.now()
    note = {
        "id": note_counter,
        "title": note_data.title,
        "content": note_data.content,
        "created_at": now,
        "updated_at": now,
    }
    note_list.append(note)
    note_counter+=1
    return note


def delete(note_id: int):
    if note_id >= len(note_list) or note_id < 0:
        raise HTTPException(status_code=404, detail="Not Found")
    del note_list[note_id]

def get_note(note_id: int):
    if note_id >= len(note_list) or note_id < 0:
        raise HTTPException(status_code=404, detail="Not Found")
    return note_list[note_id]

def update(note_id: int):
    if note_id >= len(note_list) or note_id < 0:
        raise HTTPException(status_code=404, detail="Not Found")
    return note_list[note_id] 
