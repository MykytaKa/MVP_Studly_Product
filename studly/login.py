import re
from connect_to_db import connect_to_database
from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtCore import QTimer, QSettings
from ui_login import Ui_MainWindow
from mainwindow import MainWindow


class Login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(600, 600)
        self.load_settings()

        self.ui.loginButton.clicked.connect(self.loginUser)
        self.ui.show.stateChanged.connect(self.show_hide_password)
        self.ui.loginEdit.textChanged.connect(self.change_loginEdit_style)
        self.ui.passwordEdit.textChanged.connect(self.change_passwordEdit_style)

        self.redStyle = "border-style: solid; border-width: 2px; border-color: rgb(69, 119, 108); background-color: rgba(69, 119, 108, 125);"

    def load_settings(self):
        settings = QSettings('studly', 'studly')

        email = settings.value('user/email')
        password = settings.value('user/password')

        self.ui.loginEdit.setText(email)
        self.ui.passwordEdit.setText(password)

        if self.ui.loginEdit.text() != '' and  self.ui.passwordEdit.text() != '':
            self.ui.rememberUser.setChecked(True)



    def change_loginEdit_style(self):
        self.ui.loginEdit.setStyleSheet(self.redStyle)

    def change_passwordEdit_style(self):
        self.ui.passwordEdit.setStyleSheet(self.redStyle)


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
            self.ui.loginEdit.setStyleSheet("border: 2px solid red; border-style: solid; background-color: rgba(69, 119, 108, 125);")
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
            self.close()
            self.wind = MainWindow()
            self.wind.show()

        else:
            print(f'{authentication_result}')
            self.ui.passwordEdit.setStyleSheet("border: 2px solid red; border-style: solid; background-color: rgba(69, 119, 108, 125);")
            self.ui.errorLabel.setText(f'{authentication_result}')
            self.timer = QTimer()
            self.timer.setInterval(3000)
            self.timer.timeout.connect(self.hideErrorLabel)
            self.timer.start()

    def hideErrorLabel(self):
        self.ui.errorLabel.setText('')
        self.timer.stop()


