# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import
from PySide6.QtWidgets import QWidget, QFrame, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from DB.connect_to_db import connect_to_database
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Signal, Qt

class GroupLabel(QWidget):
    clicked = Signal()
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)
        self.setCursor(Qt.PointingHandCursor)
        self.status = 1
        self.infoLabel = QLabel()

        self.iconLabel = QLabel()
        self.iconLabel.setFixedSize(20, 20)

        icon = QPixmap(':/icons/hideList.png')

        self.iconLabel.setPixmap(icon.scaled(self.iconLabel.size()))
        self.container = QHBoxLayout()
        self.container.setContentsMargins(0, 0, 0, 0)
        self.container.addWidget(self.infoLabel)
        self.container.addWidget(self.iconLabel)
        self.container.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.setLayout(self.container)

    def setFont(self, new_font):
        self.infoLabel.setFont(new_font)

    def setText(self, text):
        self.infoLabel.setText(text)

    def mousePressEvent(self, ev):
        if self.status == 1:
            self.status = 0
        else:
            self.status = 1

        file_path = ':/icons/showList.png' if self.status == 0 else ':/icons/hideList.png'
        icon = QPixmap(file_path)
        self.iconLabel.setPixmap(icon.scaled(self.iconLabel.size()))

        self.clicked.emit()

class GroupUser(QFrame):
    def __init__(self, identifier=-1, userType=None, parent=None):
        super().__init__(parent)
        self.setFixedSize(700, 100)
        self.setStyleSheet('''border-style: solid;
                              border-width: 2px;
                              border-color: rgb(32, 69, 71);
                              border-radius: 20px;
                              background-color: rgb(239, 241, 237);
                              ''')

        self.userType = userType
        self.identifier = identifier

        fullname_font = QFont()
        fullname_font.setPointSize(14)

        self.avatarLabel = QLabel()
        self.avatarLabel.setFixedSize(80, 80)
        self.avatarLabel.setStyleSheet('''border-style: solid;
                                          border-width: 3px;
                                          border-color: rgb(32, 69, 71);
                                          border-radius: 40px;
                                          ''')

        self.fullNameLabel = QLabel()
        self.fullNameLabel.setFont(fullname_font)
        self.fullNameLabel.setStyleSheet('border-style: none;')

        self.positionLabel = QLabel()
        self.positionLabel.setStyleSheet('border-style: none;')

        if self.userType == 'student':
           self.positionLabel.hide()

        self.infoLabel = QLabel()
        self.infoLabel.setStyleSheet('border-style: none;')

        self.mainContainer = QGridLayout()
        self.mainContainer.addWidget(self.avatarLabel, 0, 0, 3, 1)
        self.mainContainer.addWidget(self.fullNameLabel, 0, 1,)
        self.mainContainer.addWidget(self.positionLabel, 1, 1)
        self.mainContainer.addWidget(self.infoLabel, 2, 1)

        self.setLayout(self.mainContainer)

        self.initialize()

    @connect_to_database
    def initialize(cursor, self):
        cursor.execute('SELECT first_name, last_name, patronymic, phone_number, email FROM users WHERE id = ?', (self.identifier, ))

        first_name, last_name, patronymic, phone_number, email = cursor.fetchone()
        self.fullNameLabel.setText(f'{last_name} {first_name} {patronymic}')
        self.infoLabel.setText(f'{phone_number}   |   {email}')

        if self.userType == 'teacher':
            cursor.execute('SELECT position FROM teachers WHERE user_id = ?', (self.identifier,))
            position = cursor.fetchone()[0]
            self.positionLabel.setText(position)


class GroupViewer(QWidget):
    def __init__(self, identifier=-1, userType=None, parent=None):
        super().__init__(parent)
        self.identifier = identifier

        group_name_font = QFont()
        group_name_font.setPointSize(16)
        group_name_font.setBold(True)

        self.nameLabel = GroupLabel()
        self.nameLabel.setFont(group_name_font)
        self.nameLabel.clicked.connect(self.hideInfo)

        self.groupLayout = QVBoxLayout()
        self.groupLayout.setContentsMargins(0, 0, 0, 0)

        self.groupWidget = QWidget()
        self.groupWidget.setLayout(self.groupLayout)

        self.mainContainer = QVBoxLayout()
        self.mainContainer.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainContainer.setContentsMargins(0, 0, 0, 0)
        self.mainContainer.addWidget(self.nameLabel)
        self.mainContainer.addWidget(self.groupWidget)

        self.setLayout(self.mainContainer)

        self.initialize(userType)

    @connect_to_database
    def initialize(cursor, self, userType):
        if userType == 'teacher':
            cursor.execute('SELECT name FROM departments WHERE id = ?', (self.identifier, ))
        else:
            cursor.execute('SELECT name FROM classes WHERE id = ?', (self.identifier, ))
        name = cursor.fetchone()[0]

        self.nameLabel.setText(name)

        if userType == 'teacher':
            cursor.execute('SELECT user_id FROM teachers WHERE department_id = ?', (self.identifier, ))
        else:
            cursor.execute('SELECT user_id FROM students WHERE class_id = ?', (self.identifier, ))

        for user_id in cursor.fetchall():
            self.groupLayout.addWidget(GroupUser(user_id[0], userType))

    def hideInfo(self):
        if self.groupWidget.isHidden():
            self.groupWidget.show()
        else:
            self.groupWidget.hide()


class InstituteViewer(QWidget):
    def __init__(self, identifier=-1, userType=None, parent=None):
        super().__init__(parent)
        self.setStyleSheet('color: rgb(32, 69, 71);')

        self.identifier = identifier

        institute_name_font = QFont()
        institute_name_font.setPointSize(20)
        institute_name_font.setBold(True)

        self.nameLabel = GroupLabel()
        self.nameLabel.setFont(institute_name_font)
        self.nameLabel.clicked.connect(self.hideInfo)

        self.instituteContainer = QVBoxLayout()
        self.instituteContainer.setContentsMargins(0, 0, 0, 0)

        self.instituteWidget = QWidget()
        self.instituteWidget.setLayout(self.instituteContainer)

        self.mainContainer = QVBoxLayout()
        self.mainContainer.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainContainer.setContentsMargins(0, 0, 0, 0)
        self.mainContainer.addWidget(self.nameLabel)
        self.mainContainer.addWidget(self.instituteWidget)

        self.setLayout(self.mainContainer)

        self.initialize(userType)

    def hideInfo(self):
        if self.instituteWidget.isHidden():
            self.instituteWidget.show()
        else:
            self.instituteWidget.hide()

    @connect_to_database
    def initialize(cursor, self, userType):
        cursor.execute('SELECT name FROM institutes WHERE id = ?', (self.identifier, ))

        name = cursor.fetchone()[0]
        self.nameLabel.setText(name)

        if userType == 'teacher':
            cursor.execute('SELECT id FROM departments WHERE institute_id = ? ORDER BY name', (self.identifier, ))
        else:
            cursor.execute('SELECT id FROM classes WHERE institute_id = ? ORDER BY name', (self.identifier, ))

        for group_id in cursor.fetchall():
            self.instituteContainer.addWidget(GroupViewer(group_id[0], userType))
