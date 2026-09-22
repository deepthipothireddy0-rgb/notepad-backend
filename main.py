from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Notepad backend is running!"

    }
notes = []


@app.post("/notes")
def create_note(note: str):
    notes.append(note)

    return {
        "message": "Note created successfully",
        "note": note
    }


@app.get("/notes")
def get_notes():
    return {
        "notes": notes
    }
@app.delete("/notes/{index}")
def delete_note(index: int):
    if index < 0 or index >= len(notes):
        return {"message": "Note not found"}

    deleted_note = notes.pop(index)

    return {
        "message": "Note deleted successfully",
        "note": deleted_note
    }
@app.put("/notes/{index}")
def update_note(index: int, note: str):
    if index < 0 or index >= len(notes):
        return {"message": "Note not found"}

    notes[index] = note

    return {
        "message": "Note updated successfully",
        "note": note
    }
@app.delete("/notes/{index}")
def delete_note(index: int):
    if index < 0 or index >= len(notes):
        return {"message": "Note not found"}

    deleted_note = notes.pop(index)

    return {
        "message": "Note deleted successfully",
        "note": deleted_note
    }