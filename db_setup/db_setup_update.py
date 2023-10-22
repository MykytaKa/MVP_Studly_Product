import sqlite3


def create_tables():
    conn = sqlite3.connect('studly.db')

    # Table "Transactions"
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    way_to_photo TEXT,
                    account_description TEXT,
                    phone_number TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    status TEXT NOT NULL
                )''')

    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    user_id INTEGER PRIMARY KEY,
                    position TEXT NOT NULL,
                    department TEXT NOT NULL,
                    institute TEXT NOT NULL
                )''')

    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    group TEXT NOT NULL
                )''')

    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                    user_id INTEGER PRIMARY KEY,
                    group TEXT NOT NULL,
                    institute TEXT NOT NULL
                )''')

    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS meets (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    group TEXT NOT NULL,
                    teacher_id INTEGER PRIMARY KEY,
                    state_date TEXT NOT NULL,
                    duration TEXT NOT NULL
                )''')

    conn.commit()

    conn.execute('''CREATE TABLE IF NOT EXISTS files (
                    subject_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    destination_folder TEXT NOT NULL
                )''')

    conn.commit()

    conn.close()


if __name__ == '__main__':
    create_tables()