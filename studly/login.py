import re
from connect_to_db import connect_to_database


@connect_to_database
def authenticate_user(cursor, identifier, password):
    # If identifier = email
    if re.match(r'^\S+@\S+\.\S+$', identifier):
        cursor.execute('SELECT * FROM users WHERE email = ?', (identifier,))
    # If identifier = phone
    elif re.match(r'^\d{10}$', identifier):
        cursor.execute('SELECT * FROM users WHERE phone_number = ?', (identifier,))
    else:
        return 'Incorrect email/phone format'

    user = cursor.fetchone()

    if user is not None:
        # Successful authentication
        if user[7] == password:  # user[7] - password from DB
            user_data = {
                'user_id': user[0],
                'first_name': user[1],
                'last_name': user[2],
                'way_to_photo': user[3],
                'account_description': user[4],
                'phone_number': user[5],
                'email': user[6],
                'status': user[8]
            }
            return user_data
        # Incorrect password
        else:
            return 'Incorrect password'
    # Unknown user
    else:
        return 'User with that email/phone cannot be found.'


if __name__ == '__main__':
    email_phone = input('Email/phone: ')
    pswrd = input('Password: ')

    authentication_result = authenticate_user(email_phone, pswrd)

    if isinstance(authentication_result, dict):
        print(f'Successful authentication, welcome {authentication_result["first_name"]}!')
    else:
        print(f'{authentication_result}')
