import logging
import pickle
import os

logging.basicConfig(filename='file.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Note:
    def __init__(self, title, content):
        logging.info("making note")
        self.content = content
        self.title = title

class NoteBook:
    def __init__(self):
        self.notes = []
        self.filename = 'notes.pkl'
        self.load_notes(self.filename)

    def add_note(self, note):
        self.notes.append(note)

    def save_notes(self):
        logging.info("saving notes === sereilize")
        with open(self.filename, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes(self, filename):
        logging.info("loading them before the start == desereilize")
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                self.notes = pickle.load(file)

    def display_notes(self):
        logging.info("just check all notes")
        for i, note in enumerate(self.notes, 1):
            print(f"Note {i}:")
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
            print("")


if __name__ == "__main__":
    """
    test main
    """
    note_manager = NoteBook()

    while True:
        print("Note Manager")
        print("1. Add a new note")
        print("2. Display notes")
        print("3. Save notes and exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the note title: ")
            content = input("Enter the note content: ")
            new_note = Note(title, content)
            note_manager.add_note(new_note)
        elif choice == '2':
            note_manager.display_notes()
        elif choice == '3':
            note_manager.save_notes()
            break
        else:
            print("Invalid choice. Please try again.")


