from connect_to_db.py import connect_to_database
import re


@connect_to_database
def is_user_already_exists(cursor, email, phone):
    cursor.execute('SELECT email, phone_number FROM users WHERE email = ? OR phone_number = ?', (email, phone))
    existing_user = cursor.fetchone()
    return ['User with this email or phone number already exists'] if existing_user else []


def validate_required_fields(user_data):
    required_fields = {
        'first_name': 'First name be entered!',
        'last_name': 'Last name must be entered!',
        'email': 'Email must be entered!',
        'phone_number': 'Phone must be entered!',
        'password': 'Password must be entered!',
        'status': 'Status must be entered!'
    }

    error_messages = []

    for field, message in required_fields.items():
        if not user_data.get(field):
            error_messages.append(message)

    return error_messages


def validate_input_data(user_data):
    error_messages = []

    email = user_data['email']
    if not email or not re.match(r'^\S+@\S+\.\S+$', email):
        error_messages.append('Invalid email format')

    phone_number = user_data['phone_number']
    if not re.match(r'^\+\d{1,3}\d{9}$', phone_number):
        error_messages.append('Invalid phone number format')

    password = user_data['password']
    if len(password) < 8:
        error_messages.append('Password must be at least 8 characters long')

    status = user_data['status']
    if status not in ('student', 'teacher'):
        error_messages.append('Status must be "student" or "teacher"')

    return error_messages


def validate_all_data(user_data):
    errors = []
    errors += is_user_already_exists(user_data['email'], user_data['phone_number'])
    errors += validate_required_fields(user_data)
    errors += validate_input_data(user_data)

    return errors


@connect_to_database
def insert_user_info(cursor, user_data):
    cursor.execute('INSERT INTO users (first_name, last_name, way_to_photo, account_description, '
                   'phone_number, email, password, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                   (user_data['first_name'], user_data['last_name'], user_data['way_to_photo'],
                    user_data['account_description'], user_data['phone_number'], user_data['email'],
                    user_data['password'], user_data['status']))


if __name__ == '__main__':
    user1 = {
        'first_name': input("First name: "),
        'last_name': input("Last name: "),
        'way_to_photo': input("Way to photo: "),
        'account_description': input("Description: "),
        'phone_number': input("Phone number: "),
        'email': input("Email: "),
        'password': input("Password: "),
        'status': input("Who are you: ")
    }

    mistakes = validate_all_data(user1)

    for i in mistakes:
        print(i)

    if not mistakes:
        insert_user_info(user1)
