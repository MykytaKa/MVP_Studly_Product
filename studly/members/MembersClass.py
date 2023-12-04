from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from members.GroupViewer import InstituteViewer, GroupUser
from members.ui_MembersClass import Ui_Form
from DB.connect_to_db import connect_to_database


class MembersClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.searchFrame.hide()

        self.ui.teachersButton.setIcon(QIcon(':/icons/teacher.png'))
        self.ui.teachersButton.setIconSize(self.ui.teachersButton.size())
        self.ui.studentsButton.setIcon(QIcon(':/icons/student.png'))
        self.ui.studentsButton.setIconSize(self.ui.studentsButton.size())

        self.userType = ''

        self.ui.teachersButton.clicked.connect(lambda: self.load_users('teacher'))
        self.ui.studentsButton.clicked.connect(lambda: self.load_users('student'))
        self.ui.returnButton.clicked.connect(self.goto_main)
        self.ui.findLoadButton.clicked.connect(self.find_users)
        self.ui.clearButton.clicked.connect(self.load_current_users)

    @connect_to_database
    def load_users(cursor, self, user_type):
        self.userType = user_type

        cursor.execute('SELECT id FROM institutes ORDER BY name DESC')
        for institute_id in cursor.fetchall():
            self.ui.usersLayout.insertWidget(0, InstituteViewer(institute_id[0], self.userType))

        self.ui.mainFrame.hide()
        self.ui.searchFrame.show()

    @connect_to_database
    def find_users(cursor, self):
        # Очищення контейнера
        self.clear_layout()
        self.ui.usersLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Розділення пошукового рядка на слова
        user_requests = self.ui.findLoadEdit.text().split(' ')
        user_requests = [i for i in user_requests if i != '']

        # Список з id користувачів, які мають хоча б одне з пошукових слів у своїх ініалах
        users_id = []

        # Занесення id користувачів, які мають співпадіння
        for request in user_requests:
            cursor.execute(f"SELECT id FROM users \
                             WHERE (first_name LIKE '%{request}%' OR last_name LIKE '%{request}%' "
                           f"OR patronymic LIKE '%{request}%') AND status = '{self.userType}'")
            ids = [i[0] for i in cursor.fetchall()]
            users_id.extend(ids)

        # Унікальний неповторювальний список id користувачів, які мають співпадіння
        users_id_set = set(users_id)

        # Список id користувачів, котрі мають кожне шукане слово у своїх ініціалах
        found_users_id = []

        # Відбір id користувачів, які мають збіги з усіма пошуковими словами
        for i in users_id_set:
            if users_id.count(i) == len(user_requests):
                found_users_id.append(i)

        if found_users_id == []:
            not_found_font = QFont()
            not_found_font.setPointSize(16)

            not_found_label = QLabel('Користувач не знайдений')
            not_found_label.setFont(not_found_font)
            not_found_label.setStyleSheet('color: rgb(239, 241, 237)')

            self.ui.usersLayout.insertWidget(0, not_found_label)
        else:
            for i in found_users_id:
                self.ui.usersLayout.insertWidget(0, GroupUser(i, self.userType))
                self.ui.usersLayout.insertSpacing(1, 20)

    @connect_to_database
    def clear_layout(cursor, self):
        self.ui.usersLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        while self.ui.usersLayout.count() - 1:
            institute_widget = self.ui.usersLayout.takeAt(0).widget()
            if institute_widget:
                institute_widget.setParent(None)

    @connect_to_database
    def load_current_users(cursor, self):
        self.clear_layout()
        self.ui.findLoadEdit.clear()
        cursor.execute('SELECT id FROM institutes ORDER BY name DESC')
        for institute_id in cursor.fetchall():
            self.ui.usersLayout.insertWidget(0, InstituteViewer(institute_id[0], self.userType))

    def goto_main(self):
        self.userType = ''
        self.clear_layout()
        self.ui.searchFrame.hide()
        self.ui.mainFrame.show()
        self.ui.findLoadEdit.clear()
