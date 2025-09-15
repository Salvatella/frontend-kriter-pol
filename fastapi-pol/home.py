from fastapi import FastAPI
from typing import List
from models.models import  Note, fake_db
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


@app.post("/notes/check-task/{taskId}")
def check_task(taskId: int):
    fake_db_tasks = fake_db.get("tasks", [])
    for task in fake_db_tasks:
        if task["id"] == taskId:
            task["completed"] = not task["completed"]
            return {"message": "Task checkbox toggled successfully", "task": task}
    return {"error": "Task not found"}, 404


@app.get("/notes/reminder", response_model=List[Note])
def get_notes_with_reminder():
    return [note for note in fake_db["notes"] if note["reminder"]]

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



