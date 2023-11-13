import re
from DB.connect_to_db import connect_to_database
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from registration.ui_registration import Ui_MainWindow as UIregistration
from registration.ui_stud_registration import Ui_MainWindow as UIstud_registration
from registration.ui_teach_registration import Ui_MainWindow as UIteach_registration


class RegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registration")
        self.ui = UIregistration()
        self.ui.setupUi(self)

        self.user = {}
        self.success = False
        self.timer = None

        self.ui.nextButton.clicked.connect(self.validate_all_data)

        # Styles
        self.defaultStyle = ('border-style: solid; border-width: 2px; border-color: rgb(69, 119, 108); '
                             'background-color: rgba(69, 119, 108, 125); border-radius: 10px;')
        self.redStyle = ('border-style: solid; border-width: 2px; border-color: rgb(255, 0, 0); '
                         'background-color: rgba(69, 119, 108, 125); border-radius: 10px;')

        # Return lineEdits to normal style
        widgets = [self.ui.nameEdit, self.ui.surnameEdit, self.ui.patronymicEdit,
                   self.ui.emailEdit, self.ui.phoneEdit, self.ui.passwordEdit]
        for widget in widgets:
            widget.textChanged.connect(lambda _, w=widget: self.change_widget_style(w))

    # User data from lineEdits
    def get_user_data(self):
        self.user = {
            'first_name': self.ui.nameEdit.text(),
            'last_name': self.ui.surnameEdit.text(),
            'patronymic': self.ui.patronymicEdit.text(),
            'phone_number': self.ui.phoneEdit.text(),
            'email': self.ui.emailEdit.text(),
            'password': self.ui.passwordEdit.text(),
            'status': 'student' if self.ui.studentButton.isChecked() else (
                'teacher' if self.ui.teacherButton.isChecked() else None)
        }

    # Validations
    # Check the string for text and in the DB
    @connect_to_database
    def validate_required_fields(cursor, self, email, phone):
        error_messages = []

        required_fields = {
            'first_name': self.ui.nameEdit,
            'last_name': self.ui.surnameEdit,
            'patronymic': self.ui.patronymicEdit,
            'email': self.ui.emailEdit,
            'phone_number': self.ui.phoneEdit,
            'password': self.ui.passwordEdit
        }

        for field, widget in required_fields.items():
            if not self.user.get(field):
                widget.setStyleSheet(self.redStyle)
                error_messages.append('Заповніть усі поля!')
                return error_messages

        cursor.execute('SELECT email, phone_number FROM users WHERE email = ? OR phone_number = ?', (email, phone))
        existing_user = cursor.fetchone()

        if existing_user:
            if existing_user[0] == email:
                self.ui.emailEdit.setStyleSheet(self.redStyle)
                error_messages.append('Користувач з цією поштою вже існує!')
            if existing_user[1] == phone:
                self.ui.phoneEdit.setStyleSheet(self.redStyle)
                error_messages.append('Користувач з цим номером телефону вже існує!')

        return error_messages

    # Correctness check of input data
    def validate_input_data(self):
        error_messages = []

        fields = {
            'email': {
                'value': self.user['email'],
                'regex': r'^\S+@\S+\.\S+$',
                'error_message': 'Некоректний формат пошти!',
                'widget': self.ui.emailEdit
            },
            'phone_number': {
                'value': self.user['phone_number'],
                'regex': r'^\+\d{1,3}\d{9}$',
                'error_message': 'Некоректний формат телефону!',
                'widget': self.ui.phoneEdit
            },
            'password': {
                'value': self.user['password'],
                'regex': r'^.{8,}$',
                'error_message': 'Пароль має містити щонайменше 8 символів!',
                'widget': self.ui.passwordEdit
            }
        }

        for field, data in fields.items():
            if not data['value'] or not re.match(data['regex'], data['value']):
                error_messages.append(data['error_message'])
                data['widget'].setStyleSheet(self.redStyle)
                return error_messages

        valid_statuses = ['student', 'teacher']
        status = self.user['status']
        if status not in valid_statuses:
            error_messages.append('Оберіть свій статус!')

        return error_messages

    def validate_all_data(self):
        self.get_user_data()
        errors = self.validate_required_fields(self.user['email'], self.user['phone_number'])

        if not errors:
            errors += self.validate_input_data()

        if errors:
            self.ui.errorLabel.setText(errors[0])
            self.setup_timer(self.ui.errorLabel)

            # To logging
            for i in errors:
                print(i)

            return

        self.setup_next_registrarion_window()

        self.hide()
        self.window.show()
        self.success = True

    # Setting up a new window to continue registration
    def setup_next_registrarion_window(self):
        if self.user['status'] == 'student':
            self.window = StudentRegistrationWindow()
            self.window.ui.groupBox.activated.connect(lambda: self.change_widget_style(self.window.ui.groupBox))

        if self.user['status'] == 'teacher':
            self.window = TeacherRegistrationWindow()
            self.window.ui.departmentBox.activated.connect(
                lambda: self.change_widget_style(self.window.ui.departmentBox))
            self.window.ui.lineEdit.textChanged.connect(lambda: self.change_widget_style(self.window.ui.lineEdit))

        # Buttons
        self.window.ui.registerButton.clicked.connect(self.registrate_user)
        self.window.ui.returnButton.clicked.connect(self.return_to_registration)

        # Institute ComboBox
        self.window.ui.instituteBox.activated.connect(lambda: self.change_widget_style(self.window.ui.instituteBox))
        self.get_institute_data()
        self.window.on_institute_select(0)

    def setup_timer(self, error_label):
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(lambda: self.hide_error_label(error_label))
        self.timer.start()

    def return_to_registration(self):
        self.window.close()
        self.show()

    def change_widget_style(self, widget):
        widget.setStyleSheet(self.defaultStyle)

    def hide_error_label(self, error_label):
        error_label.setText('')
        self.timer.stop()

    # Inserts
    @connect_to_database
    def insert_user_info(cursor, self):
        data = (self.user['first_name'], self.user['last_name'], self.user['patronymic'], self.user['phone_number'],
                self.user['email'], self.user['password'], self.user['status'])
        cursor.execute('INSERT INTO users (first_name, last_name, patronymic, phone_number, email, password, status) '
                       'VALUES (?, ?, ?, ?, ?, ?, ?)', data)

        self.user_id = cursor.lastrowid

    @connect_to_database
    def insert_student_info(cursor, self):
        data = (self.user_id, self.window.ui.groupBox.currentIndex() + 1)
        cursor.execute('INSERT INTO students (user_id, class_id) VALUES (?, ?)', data)

    @connect_to_database
    def insert_teacher_info(cursor, self):
        data = (self.user_id, self.window.ui.lineEdit.text(), self.window.ui.departmentBox.currentIndex() + 1)
        cursor.execute('INSERT INTO teachers (user_id, position, department_id) VALUES (?, ?, ?)', data)

    @connect_to_database
    def get_institute_data(cursor, self):
        cursor.execute("SELECT name FROM institutes")
        institute_names = cursor.fetchall()

        for name in institute_names:
            self.window.ui.instituteBox.addItem(name[0])

    def registrate_user(self):
        if self.user['status'] == 'student' and self.window.ui.groupBox.currentText() == "":
            self.insert_user_info()
            self.insert_student_info()

        elif self.user['status'] == 'teacher':
            if self.window.ui.departmentBox.currentText() == "" or not self.window.ui.lineEdit.text().strip():
                self.window.ui.lineEdit.setStyleSheet(self.redStyle)
                self.window.ui.messageLabel.setText("Введіть свою посаду!")
                self.setup_timer(self.window.ui.messageLabel)
                return

            self.insert_user_info()
            self.insert_teacher_info()

        self.success = True
        self.window.close()


def update_combo_box(combo_box, items):
    combo_box.clear()
    for item in items:
        combo_box.addItem(item[0])


# Student window registration
class StudentRegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UIstud_registration()
        self.ui.setupUi(self)
        self.ui.instituteBox.activated.connect(self.on_institute_select)

    @connect_to_database
    def on_institute_select(cursor, self, index):
        cursor.execute("SELECT name FROM classes WHERE institute_id = ?", (index + 1,))
        class_names = cursor.fetchall()
        update_combo_box(self.ui.groupBox, class_names)


# Teacher window registration
class TeacherRegistrationWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UIteach_registration()
        self.ui.setupUi(self)
        self.ui.instituteBox.activated.connect(self.on_institute_select)

    @connect_to_database
    def on_institute_select(cursor, self, index):
        cursor.execute("SELECT name FROM departments WHERE institute_id = ?", (index + 1,))
        departments_names = cursor.fetchall()
        update_combo_box(self.ui.departmentBox, departments_names)
