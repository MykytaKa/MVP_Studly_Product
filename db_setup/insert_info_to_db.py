from connect_to_db import connect_to_database


@connect_to_database
def insert_user_info(cursor, user_data):
    cursor.execute('INSERT INTO users (first_name, last_name, patronymic, way_to_photo, account_description, '
                   'phone_number, email, password, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (user_data['first_name'], user_data['last_name'], user_data['patronymic'], user_data['way_to_photo'],
                    user_data['account_description'], user_data['phone_number'], user_data['email'],
                    user_data['password'], user_data['status']))


if __name__ == '__main__':
    users = []

    user1 = {
        'first_name': 'Alice',
        'last_name': 'Smith',
        'patronymic': 'Smitovna',
        'way_to_photo': 'path/to/alice.jpg',
        'account_description': 'Another description',
        'phone_number': '9876543210',
        'email': 'alice@example.com',
        'password': 'securepass',
        'status': 'student'
    }

    user2 = {
        'first_name': 'Bob',
        'last_name': 'Johnson',
        'patronymic': 'Jonsovich',
        'way_to_photo': 'path/to/bob.jpg',
        'account_description': 'Yet another description',
        'phone_number': '5555555555',
        'email': 'bob@example.com',
        'password': 'bobs-password',
        'status': 'student'
    }

    user3 = {
        'first_name': 'John',
        'last_name': 'Doe',
        'patronymic': 'Doevich',
        'way_to_photo': 'path/to/photo.jpg',
        'account_description': 'Some description',
        'phone_number': '1234567890',
        'email': 'john@example.com',
        'password': 'password123',
        'status': 'teacher'
    }

    users.append(user1)
    users.append(user2)
    users.append(user3)

    for user in users:
        insert_user_info(user)


@connect_to_database
def insert_teacher_info(cursor, teacher_data):
    cursor.execute('INSERT INTO teachers (position, department_id) VALUES (?, ?)',
                   (teacher_data['position'], teacher_data['department_id']))


if __name__ == '__main__':
    teachers = []

    teacher1 = {
        'position': 'teacher assistant',
        'department_id': '001'
    }

    teacher2 = {
        'position': 'junior lecturer',
        'department_id': '002'
    }

    teacher3 = {
        'position': 'senior lecturer',
        'department_id': '003'
    }

    teachers.append(teacher1)
    teachers.append(teacher2)
    teachers.append(teacher3)

    for teacher in teachers:
        insert_teacher_info(teacher)


@connect_to_database
def insert_subject_info(cursor, subject_data):
    cursor.execute('INSERT INTO subjects (name) VALUES (?)',
                   (subject_data['name'],))


if __name__ == '__main__':
    subjects = []

    subject1 = {
        'name': 'mathematical logic'
    }

    subject2 = {
        'name': 'programming GUI'
    }

    subject3 = {
        'name': 'programming technology'
    }

    subjects.append(subject1)
    subjects.append(subject2)
    subjects.append(subject3)

    for subject in subjects:
        insert_subject_info(subject)


@connect_to_database
def insert_student_info(cursor, student_data):
    cursor.execute('INSERT INTO students (class_id) VALUES (?)',
                   (student_data['class_id']),)


if __name__ == '__main__':
    students = []

    student1 = {
        'class_id': '1'
    }

    student2 = {
        'class_id': '2'
    }

    student3 = {
        'class_id': '3'
    }

    students.append(student1)
    students.append(student2)
    students.append(student3)

    for student in students:
        insert_student_info(student)


@connect_to_database
def insert_meet_info(cursor, meet_data):
    cursor.execute('INSERT INTO meets (name, class_id, teacher_id, state_date, duration) VALUES (?, ?, ?, ?, ?)',
                   (meet_data['name'], meet_data['class_id'], meet_data['teacher_id'],
                    meet_data['state_date'], meet_data['duration']))


if __name__ == '__main__':
    meets = []

    meet1 = {
        'name': 'Meeting 1',
        'class_id': 1,
        'teacher_id': '666',
        'state_date': '2023-10-21 09:00',
        'duration': '60'
    }

    meet2 = {
        'name': 'Meeting 2',
        'class_id': 2,
        'teacher_id': '777',
        'state_date': '2023-10-22 10:00',
        'duration': '45'
    }

    meet3 = {
        'name': 'Meeting 3',
        'class_id': 3,
        'teacher_id': '888',
        'state_date': '2023-10-23 11:00',
        'duration': '90'
    }

    meets.append(meet1)
    meets.append(meet2)
    meets.append(meet3)

    for meet in meets:
        insert_meet_info(meet)


@connect_to_database
def insert_file_info(cursor, file_data):
    cursor.execute('INSERT INTO files (name, description, destination_folder) VALUES (?, ?, ?)',
                   (file_data['name'], file_data['description'], file_data['destination_folder']))


if __name__ == '__main__':
    files = []

    file1 = {
        'name': 'File1.txt',
        'description': 'Description_of_File1 ',
        'destination_folder': 'Documents'
    }

    file2 = {
        'name': 'Image1.jpg ',
        'description': 'Description_of_Image1',
        'destination_folder': 'Pictures'
    }

    file3 = {
        'name': 'Presentation1',
        'description': 'Description_of_Presentation1',
        'destination_folder': 'Presentations'
    }

    files.append(file1)
    files.append(file2)
    files.append(file3)

    for file in files:
        insert_file_info(file)


@connect_to_database
def insert_institute_info(cursor, institute_data):
    cursor.execute('INSERT INTO institutes (name) VALUES (?)',
                   (institute_data['name'],))


if __name__ == '__main__':
    institutes = []

    institute1 = {
        'name': 'Institute A'
    }

    institute2 = {
        'name': 'Institute B'
    }

    institute3 = {
        'name': 'Institute C'
    }

    institutes.append(institute1)
    institutes.append(institute2)
    institutes.append(institute3)

    for institute in institutes:
        insert_institute_info(institute)


@connect_to_database
def insert_group_info(cursor, class_data):
    cursor.execute('INSERT INTO classes (name, institute_id) VALUES (?, ?)',
                   (class_data['name'], class_data['institute_id']))


if __name__ == '__main__':
    classes = []

    class1 = {
        'name': 'Group A',
        'institute_id': 1
    }

    class2 = {
        'name': 'Group B',
        'institute_id': 2
    }

    class3 = {
        'name': 'Group C',
        'institute_id': 3
    }

    classes.append(class1)
    classes.append(class2)
    classes.append(class3)

    for group in classes:
        insert_group_info(group)


@connect_to_database
def insert_department_info(cursor, department_data):
    cursor.execute('INSERT INTO departments (name, institute_id) VALUES (?, ?)',
                   (department_data['name'], department_data['institute_id']))


if __name__ == '__main__':
    departments = []

    department1 = {
        'name': 'Mathematics',
        'institute_id': 1
    }

    department2 = {
        'name': 'Computer Science',
        'institute_id': 2
    }

    department3 = {
        'name': 'Mechanical Engineering',
        'institute_id': 3
    }

    departments.append(department1)
    departments.append(department2)
    departments.append(department3)

    for department in departments:
        insert_department_info(department)
