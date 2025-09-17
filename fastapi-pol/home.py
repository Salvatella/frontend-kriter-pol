from datetime import datetime
from fastapi import FastAPI
from typing import List
from models.models import Note, fake_db, fake_db_tasks, fake_db_labels
from starlette.middleware.cors import CORSMiddleware
import pytz


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "hello"


@app.get("/notes/reminder", response_model=List[Note])
def get_notes_with_reminder():
    return [note for note in fake_db if note["reminder"]]


@app.post("/notes/{note_id}/check-task/{taskId}")
def check_task(note_id: int, taskId: int):
    ##cambiar la hora a la hora actual
    #fake_db[note_id]["last_modified"] = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M")
    
    for note in fake_db:
        if note["id"] == note_id:
            note["last_modified"] = datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M")
            note["tasks"][0]["completed"] = not note["tasks"][0]["completed"]



    return {"message": "Task status toggled successfully hour saved was " + datetime.now(tz=pytz.timezone("Europe/Madrid")).strftime("%H:%M")}


@app.post("/notes/add-note/{reminder}", response_model=Note)
def add_note(reminder: bool):

    note = Note(
                id=len(fake_db) + 1,
                title="New Note",
                content="This is a new note.",
                link="https://example.com",
                tasks=[fake_db_tasks[18]],
                img=None,
                labels=fake_db_labels,
                last_modified="Just now",
                notebook_number=1,
                reminder=reminder
            )

    fake_db.append(note.model_dump())
    return note


# parameter

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for n in fake_db:
        if n["id"] == note_id:
            return n
    return {"error": "Note not kriter"}


@app.get("/notes", response_model=List[Note])
def get_notes():
    return fake_db
