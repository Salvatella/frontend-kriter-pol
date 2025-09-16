from fastapi import FastAPI
from typing import List
from models.models import  Note, fake_db, fake_db_tasks, fake_db_labels
from starlette.middleware.cors import CORSMiddleware


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
    return [note for note in fake_db["notes"] if note["reminder"]]

@app.post("/notes/check-task/{taskId}")
def check_task(taskId: int):
  
    for task in fake_db_tasks:
        if task["id"] == taskId:
            task["completed"] = not task["completed"]
            return {"message": "Task checkbox toggled successfully", "task": task}
    return {"error": "Task not found"}, 404


@app.post("/notes/add-note/{reminder}", response_model=Note)
def add_note(reminder: bool):

    if reminder==True:
        note = Note(
        id=len(fake_db["notes"]) + 1,
        title="New Note",
        content="This is a new note.",
        link="https://example.com",
        tasks=[fake_db_tasks[18]],
        img=None,
        labels=fake_db_labels,  
        last_modified="Just now",
        notebook_number=1,
        reminder=True
    )
    else:
        note = Note(
        id=len(fake_db["notes"]) + 1,
        title="New Note",
        content="This is a new note.",
        link="https://example.com",
        tasks=[fake_db_tasks[18]],
        img=None,
        labels=fake_db_labels,  
        last_modified="Just now",
        notebook_number=1,
        reminder=False
    )

    fake_db["notes"].append(note.model_dump())
    return note

@app.post("/notes/{note_id}/last-edited/{time}")
def update_last_edited(note_id: int, time: str):  
    for note in fake_db["notes"]:
        if note["id"] == note_id:
            note["last_modified"] = time
            return {"message": "Last edited time updated", "note": note}
    return {"error": "Note not found"}, 404

##parameter
@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    for n in fake_db["notes"]:
        if n["id"] == note_id:
            return n
    return {"error": "Note not kriter"}

@app.get("/notes", response_model=List[Note])
def get_notes():
    return fake_db["notes"]



