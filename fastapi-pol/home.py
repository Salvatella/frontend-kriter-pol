

from fastapi import FastAPI
from git import List
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