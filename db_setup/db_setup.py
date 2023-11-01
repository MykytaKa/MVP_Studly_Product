import sqlite3


def create_tables():
    conn = sqlite3.connect('studly.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        patronymic TEXT NOT NULL,
        way_to_photo TEXT,
        account_description TEXT,
        phone_number TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        status TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS teachers (
        user_id INTEGER PRIMARY KEY,
        position TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS students (
        user_id INTEGER PRIMARY KEY,
        class_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS meets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class_id INTEGER NOT NULL,
        teacher_id INTEGER,
        state_date TEXT NOT NULL,
        duration TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS files (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        destination_folder TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS institutes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS classes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        institute_id INTEGER NOT NULL,
        FOREIGN KEY (institute_id) REFERENCES institutes(id)
    )''')

    conn.execute('''CREATE TABLE IF NOT EXISTS departments (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        institute_id INTEGER NOT NULL,
        FOREIGN KEY (institute_id) REFERENCES institutes(id)
    )''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()
