import pytest
import tempfile
import os

from notebook import Note,  NoteBook

@pytest.fixture
def notes_manager():
    return NoteBook()

@pytest.fixture
def temp_notes_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    yield temp_file.name
    temp_file.close()
    os.remove(temp_file.name)

def test_add_and_display_notes(notes_manager):
    note1 = Note("Title 1", "Content 1")
    note2 = Note("Title 2", "Content 2")

    notes_manager.add_note(note1)
    notes_manager.add_note(note2)

    assert len(notes_manager.notes) == 2
    assert notes_manager.notes[0].title == "Title 1"
    assert notes_manager.notes[1].content == "Content 2"

def test_save_and_load_notes(notes_manager):
    note1 = Note("Title 1", "Content 1")
    note2 = Note("Title 2", "Content 2")

    notes_manager.add_note(note1)
    notes_manager.add_note(note2)

    notes_manager.save_notes()

    loaded_manager = NoteBook()
    loaded_manager.load_notes(loaded_manager.filename)

    assert len(loaded_manager.notes) == 2
    assert loaded_manager.notes[0].content == "Content 1"
    assert loaded_manager.notes[1].title == "Title 2"