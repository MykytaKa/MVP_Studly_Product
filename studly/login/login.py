import re
from DB.connect_to_db import connect_to_database
from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtCore import QTimer, QSettings
from login.ui_login import Ui_MainWindow
from mainwindowstudent import MainWindowStudent
from mainwindowteacher import MainWindowTeacher

#from mainwindow import MainWindow

from registration.registration import RegistrationWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic user_acc.ui -o ui_user_acc.py, or
#     pyside2-uic form.ui -o ui_form.py

class Login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_settings()

        self.ui.loginButton.clicked.connect(self.loginUser)
        self.ui.show.stateChanged.connect(self.show_hide_password)
        self.ui.loginEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.loginEdit))
        self.ui.passwordEdit.textChanged.connect(lambda: self.change_widget_style(self.ui.passwordEdit))

        self.ui.registrationlLabel.mousePressEvent = self.open_registration

        self.defaultStyle = "border-style: solid; border-width: 2px; border-color: rgb(69, 119, 108); background-color: rgba(69, 119, 108, 125); border-radius: 5px;"
        self.redStyle = "border: 2px solid red; border-style: solid; background-color: rgba(69, 119, 108, 125); border-radius: 5px;"

    def load_settings(self):
        settings = QSettings('studly', 'studly')

        email = settings.value('user/email')
        password = settings.value('user/password')

        self.ui.loginEdit.setText(email)
        self.ui.passwordEdit.setText(password)

        if self.ui.loginEdit.text() != '' and  self.ui.passwordEdit.text() != '':
            self.ui.rememberUser.setChecked(True)


    def change_widget_style(self, widget):
        widget.setStyleSheet(self.defaultStyle)

    def show_hide_password(self, state):
        if state == 2:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.Password)

    @connect_to_database
    def authenticate_user(cursor, self, identifier, password):
        # If identifier = email
        if re.match(r'^\S+@\S+\.\S+$', identifier):
            cursor.execute('SELECT * FROM users WHERE email = ?', (identifier,))
        # If identifier = phone
        elif re.match(r'^\+\d{1,3}\d{9}$', identifier):
            cursor.execute('SELECT * FROM users WHERE phone_number = ?', (identifier,))
        else:
            self.ui.loginEdit.setStyleSheet(self.redStyle)
            return 'Некоректний формат пошти/телефону.'

        user = cursor.fetchone()

        if user is not None:
            # Successful authentication
            print(user[8])
            if user[8] == password:  # user[7] - password from DB
                user_data = {
                    'user_id': user[0],
                    'first_name': user[1],
                    'last_name': user[2],
                    'patronymic': user[3],
                    'way_to_photo': user[4],
                    'account_description': user[5],
                    'phone_number': user[6],
                    'email': user[7],
                    'status': user[9]
                }
                return user_data
            # Incorrect password
            else:
                return 'Неправильний пароль! Спробуйте знову.'
        # Unknown user
        else:
            return 'Користувач з цією поштою/телефоном не знайдений!'


    def loginUser(self):
        email_phone = self.ui.loginEdit.text()  # Получить содержимое QLineEdit loginEdit
        pswrd = self.ui.passwordEdit.text()  # Получить содержимое QLineEdit passwordEdit
        authentication_result = self.authenticate_user(email_phone, pswrd)

        if isinstance(authentication_result, dict):
            if self.ui.rememberUser.isChecked():
                settings = QSettings('studly', 'studly')
                settings.setValue('user/email', email_phone)
                settings.setValue('user/password', pswrd)
            else:
                settings = QSettings('studly', 'studly')
                settings.setValue('user/email', '')
                settings.setValue('user/password', '')

            ###################################################################################
            print(f'Successful authentication, welcome {authentication_result["first_name"]}!')
            ###################################################################################
            print(f'{authentication_result}')
            self.close()

            if authentication_result["status"] == 'teacher':
                self.appWindow = MainWindowTeacher()

            elif authentication_result["status"] == 'student':
                self.appWindow = MainWindowStudent()

            else:
                print('error')
                return

            self.appWindow.show()

        else:
            self.ui.passwordEdit.setStyleSheet(self.redStyle)
            self.ui.errorLabel.setText(f'{authentication_result}')
            self.timer = QTimer()
            self.timer.setInterval(3000)
            self.timer.timeout.connect(self.hideErrorLabel)
            self.timer.start()

    def hideErrorLabel(self):
        self.ui.errorLabel.setText('')
        self.timer.stop()

    def open_registration(self, event):
        self.registration = RegistrationWindow()
        self.registration.show()
        self.hide()
        self.registration.ui.returnButton.clicked.connect(self.return_to_login)
#        self.registration.window.ui.registerButton.clicked.connect(self.registration)


    def return_to_login(self):
        self.registration.close()
        self.show()



    def open_login_window(self):
        # Используйте QTimer для асинхронного открытия окна Login
        QTimer.singleShot(0, self.login_window.show)



