# This Python file uses the following encoding: utf-8
from members.GroupViewer import InstituteViewer, GroupUser
from DB.connect_to_db import connect_to_database
from PySide6.QtWidgets import QWidget, QLabel
from members.ui_MembersClass import Ui_Form
from PySide6.QtGui import QFont,QIcon
from PySide6.QtCore import Qt

class MembersClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.searchFrame.hide()
#        self.ui.returnLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui.teachersButton.setIcon(QIcon(':/icons/teacher.png'))
        self.ui.teachersButton.setIconSize(self.ui.teachersButton.size())
        self.ui.studentsButton.setIcon(QIcon(':/icons/student.png'))
        self.ui.studentsButton.setIconSize(self.ui.studentsButton.size())

        self.userType = ''

        self.ui.teachersButton.clicked.connect(lambda: self.loadUsers('teacher'))
        self.ui.studentsButton.clicked.connect(lambda: self.loadUsers('student'))
        self.ui.returnButton.clicked.connect(self.gotoMain)
        self.ui.findLoadButton.clicked.connect(self.findUsers)
        self.ui.clearButton.clicked.connect(self.loadCurrentUsers)

    @connect_to_database
    def loadUsers(cursor, self, userType):
        self.userType = userType

        cursor.execute('SELECT id FROM institutes ORDER BY name DESC')
        for institute_id in cursor.fetchall():
            self.ui.usersLayout.insertWidget(0, InstituteViewer(institute_id[0], self.userType))

        self.ui.mainFrame.hide()
        self.ui.searchFrame.show()


    @connect_to_database
    def findUsers(cursor, self):
        # Очищення контейнера
        self.clearLayout()
        self.ui.usersLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Розділення пошукового рядка на слова
        user_requests = self.ui.findLoadEdit.text().split(' ')
        user_requests = [i for i in user_requests if i != '']

        # Список з id користувачів, які мають хоча б одне з пошукових слів у своїх ініалах
        users_id = []

        # Занесення id користувачів, які мають співпадіння
        for request in user_requests:
            cursor.execute(f"SELECT id FROM users \
                             WHERE (first_name LIKE '%{request}%' OR last_name LIKE '%{request}%' OR patronymic LIKE '%{request}%') AND status = '{self.userType}'")
            ids = [i[0] for i in cursor.fetchall()]
            users_id.extend(ids)

        # Унікальний неповторювальний список id користувачів, які мають співпадіння
        users_id_set = set(users_id)

        # Список id користувачів, котрі мають кожне шукане слово у своїх ініціалах
        found_users_id = []

        # Відбір id користувачів, які мають збіги з усіма пошуковими словами
        for id in users_id_set:
            if users_id.count(id) == len(user_requests):
                found_users_id.append(id)

        if found_users_id == []:
            not_found_font = QFont()
            not_found_font.setPointSize(16)

            not_found_label = QLabel('Користувач не знайдений')
            not_found_label.setFont(not_found_font)
            not_found_label.setStyleSheet('color: rgb(239, 241, 237)')

            self.ui.usersLayout.insertWidget(0, not_found_label)
        else:
            for id in found_users_id:
                self.ui.usersLayout.insertWidget(0, GroupUser(id, self.userType))
                self.ui.usersLayout.insertSpacing(1, 20)

    @connect_to_database
    def clearLayout(cursor, self):
        self.ui.usersLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        while self.ui.usersLayout.count() - 1:
            instituteWidget = self.ui.usersLayout.takeAt(0).widget()
            if instituteWidget:
                instituteWidget.setParent(None)

    @connect_to_database
    def loadCurrentUsers(cursor, self):
        self.clearLayout()
        self.ui.findLoadEdit.clear()
        cursor.execute('SELECT id FROM institutes ORDER BY name DESC')
        for institute_id in cursor.fetchall():
            self.ui.usersLayout.insertWidget(0, InstituteViewer(institute_id[0], self.userType))

    def gotoMain(self):
        self.userType = ''
        self.clearLayout()
        self.ui.searchFrame.hide()
        self.ui.mainFrame.show()
        self.ui.findLoadEdit.clear()

