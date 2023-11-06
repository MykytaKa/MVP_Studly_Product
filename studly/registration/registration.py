from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from registration.ui_registration import Ui_MainWindow as UIregistration
from registration.ui_stud_registration import Ui_MainWindow as UIstud_registration
from registration.ui_teach_registration import Ui_MainWindow as UIteach_registration


import re
from DB.connect_to_db import connect_to_database


class RegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registration")
        self.ui = UIregistration()
        self.ui.setupUi(self)


        self.ui.nextButton.clicked.connect(self.validate_all_data)

        self.defaultStyle = 'border-style: solid; border-width: 2px; border-color: rgb(69, 119, 108); background-color: rgba(69, 119, 108, 125); border-radius: 10px;'
        self.redStyle = 'border-style: solid; border-width: 2px; border-color: rgb(255, 0, 0); background-color: rgba(69, 119, 108, 125); border-radius: 10px;'


        self.ui.nameEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.nameEdit))
        self.ui.surnameEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.surnameEdit))
        self.ui.patronymicEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.patronymicEdit))
        self.ui.emailEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.emailEdit))
        self.ui.phoneEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.phoneEdit))
        self.ui.passwordEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.passwordEdit))


    ###################################################################################
    ### Validations
    ###################################################################################

    @connect_to_database
    def is_user_already_exists(cursor, self, email, phone):
        cursor.execute('SELECT email, phone_number FROM users WHERE email = ? OR phone_number = ?', (email, phone))
        existing_user = cursor.fetchone()
        if existing_user:
            self.ui.emailEdit.setStyleSheet(self.redStyle)
            self.ui.phoneEdit.setStyleSheet(self.redStyle)
            return ['User with this email or phone number already exists']
        else:
            return []

    def validate_required_fields(self):
        required_fields = ['first_name', 'last_name', 'patronymic', 'email', 'phone_number', 'password', 'status']

        error_messages = []

        for field in required_fields:
            if not self.user.get(field):
                if 'Заповніть усі поля!' not in error_messages:
                    error_messages.append('Заповніть усі поля!')
                    self.ui.nameEdit.setStyleSheet(self.redStyle)
                    self.ui.surnameEdit.setStyleSheet(self.redStyle)
                    self.ui.patronymicEdit.setStyleSheet(self.redStyle)

        return error_messages


    def validate_input_data(self):
        error_messages = []

        email = self.user['email']
        if not email or not re.match(r'^\S+@\S+\.\S+$', email):
            error_messages.append('Invalid email format')
            self.ui.emailEdit.setStyleSheet(self.redStyle)

        phone_number = self.user['phone_number']
        if not re.match(r'^\+\d{1,3}\d{9}$', phone_number):
            error_messages.append('Invalid phone number format')
            self.ui.phoneEdit.setStyleSheet(self.redStyle)

        password = self.user['password']
        if len(password) < 8:
            error_messages.append('Password must be at least 8 characters long')
            self.ui.passwordEdit.setStyleSheet(self.redStyle)

        status = self.user['status']
        if status not in ('student', 'teacher'):
            error_messages.append('Status must be "student" or "teacher"')

        return error_messages


    def validate_all_data(self):
        self.user = {
            'first_name': self.ui.nameEdit.text(),
            'last_name': self.ui.surnameEdit.text(),
            'patronymic': self.ui.patronymicEdit.text(),
            'phone_number': self.ui.phoneEdit.text(),
            'email': self.ui.emailEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'status': 'student' if self.ui.studentButton.isChecked() else ('teacher' if self.ui.teacherButton.isChecked() else None)
        }

        errors = []
        errors += self.is_user_already_exists(self.user['email'], self.user['phone_number'])
        errors += self.validate_required_fields()
        errors += self.validate_input_data()




        if errors:
            self.ui.errorLabel.setText(errors[0])
            self.timer = QTimer()
            self.timer.setInterval(3000)
            self.timer.timeout.connect(lambda: self.hideErrorLabel(self.ui.errorLabel))
            self.timer.start()


        for i in errors:
            print(i)

        if not errors:
            self.hide()
            if self.user['status'] == 'student':
                self.window = StudentRegistrationWindow()
                self.window.ui.groupBox.activated.connect(lambda: self.change_widget_style(self.window.ui.groupBox))


            if self.user['status'] == 'teacher':
                self.window = TeacherRegistrationWindow()
                self.window.ui.departmentBox.activated.connect(lambda: self.change_widget_style(self.window.ui.departmentBox))
                self.window.ui.lineEdit.textChanged.connect(lambda: self.change_widget_style(self.window.ui.lineEdit))

            self.window.show()
            self.window.ui.returnButton.clicked.connect(self.return_to_registration)
            self.get_institute_data()
            self.window.ui.registerButton.clicked.connect(self.registrate_user)
            self.ui.passwordEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.passwordEdit))

    def return_to_registration(self):
        self.window.close()
        self.show()

    def hideErrorLabel(self, label):
        label.setText('')
        self.timer.stop()

    #########################################################################################################
    ### Inserts ###
    #########################################################################################################
    @connect_to_database
    def insert_user_info(cursor, self):
        cursor.execute('INSERT INTO users (first_name, last_name, patronymic,'
                       'phone_number, email, password, status) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (self.user['first_name'], self.user['last_name'], self.user['patronymic'], self.user['phone_number'], self.user['email'],
                        self.user['password'], self.user['status']))

        self.user_id = cursor.lastrowid

    @connect_to_database
    def insert_student_info(cursor, self):
        class_id = self.window.ui.groupBox.currentIndex() + 1
        cursor.execute('INSERT INTO students (user_id, class_id) VALUES (?, ?)', (self.user_id, class_id))

    @connect_to_database
    def insert_teacher_info(cursor, self):
        position = self.window.ui.lineEdit.text()
        department_id = self.window.ui.departmentBox.currentIndex() + 1
        cursor.execute('INSERT INTO teachers (user_id, position, department_id) VALUES (?, ?, ?)', (self.user_id, position, department_id))

    ##########################################################################################################

    def change_widget_style(self, widget):
        widget.setStyleSheet(self.defaultStyle)

    @connect_to_database
    def get_institute_data(cursor, self):
        cursor.execute("SELECT name FROM institutes")
        institute_names = cursor.fetchall()

        for name in institute_names:
            self.window.ui.instituteBox.addItem(name[0])


    def registrate_user(self):
        if self.window.ui.instituteBox.currentText() != "":
            if self.user['status'] == 'student' and self.window.ui.groupBox.currentText() != "":
                self.insert_user_info()
                self.insert_student_info()
            elif self.user['status'] == 'student':
                self.window.ui.groupBox.setStyleSheet(self.redStyle)
                return

            if self.user['status'] == 'teacher' and self.window.ui.departmentBox.currentText() != "" and self.window.ui.lineEdit.text().strip():
                self.insert_user_info()
                self.insert_teacher_info()

            elif self.user['status'] == 'teacher':
                self.window.ui.departmentBox.setStyleSheet(self.redStyle)
                return

            self.window.close()


#            self.return_to_login()



#    def return_to_login(self, user):
#        self.window.close()

#        self.login.show()
#        self.login.ui.loginEdit.setText(user['email'])
#        self.login.ui.passwordEdit.setText(user['password'])


class StudentRegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("StudRegistration")
        self.ui = UIstud_registration()
        self.ui.setupUi(self)
        self.ui.instituteBox.activated.connect(self.on_institute_select)


    @connect_to_database
    def on_institute_select(cursor, self, index):
        self.ui.groupBox.clear()

        # Получаем данные для второго ComboBox на основе выбранного университета
        cursor.execute("SELECT name FROM classes WHERE institute_id = ?", (index + 1,))
        class_names = cursor.fetchall()
        for name in class_names:
            self.ui.groupBox.addItem(name[0])


class TeacherRegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TeachRegistration")
        self.ui = UIteach_registration()
        self.ui.setupUi(self)
        self.ui.instituteBox.activated.connect(self.on_institute_select)



    @connect_to_database
    def on_institute_select(cursor, self, index):
        self.ui.departmentBox.clear()

        # Получаем данные для второго ComboBox на основе выбранного университета
        cursor.execute("SELECT name FROM departments WHERE institute_id = ?", (index + 1,))
        departments_names = cursor.fetchall()
        for name in departments_names:
            self.ui.departmentBox.addItem(name[0])




