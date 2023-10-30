# This Python file uses the following encoding: utf-8
#from PySide6 import QtCore
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QPushButton
from ui_mainwindowteacher import Ui_MainWindow
from scheduleClassTeacher import scheduleClassTeacher
from PySide6.QtCore import Qt

class MainWindowTeacher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.currentWidget = scheduleClassTeacher(mainWindow=self)
        self.ui.widgetContainer.addWidget(self.currentWidget)
        self.ui.scheduleButton.clicked.connect(self.loadSchedule)
        self.currentWidget.ui.createMeetButton.clicked.connect(self.setWindowDisabled)
        self.ui.scheduleButton.setStyleSheet('''border-style: solid;
                                                border-width: 0px;
                                                color: rgb(239, 241, 237);''')

        self.ui.lecturesButton.setStyleSheet('''border-style: solid;
                                                border-width: 0px;
                                                color: rgb(239, 241, 237);''')

        self.ui.teachersButton.setStyleSheet('''border-style: solid;
                                                border-width: 0px;
                                                color: rgb(239, 241, 237);''')

        self.ui.notesButton.setStyleSheet('''border-style: solid;
                                             border-width: 0px;
                                             color: rgb(239, 241, 237);''')

        self.unLightButtons()
        font = QFont()
        font.setUnderline(True)
        self.ui.scheduleButton.setFont(font)

        self.ui.scheduleButton.setCursor(Qt.PointingHandCursor)
        self.ui.lecturesButton.setCursor(Qt.PointingHandCursor)
        self.ui.teachersButton.setCursor(Qt.PointingHandCursor)
        self.ui.notesButton.setCursor(Qt.PointingHandCursor)

        self.ui.scheduleButton.clicked.connect(lambda: self.lightChosenButton(self.ui.scheduleButton))
        self.ui.lecturesButton.clicked.connect(lambda: self.lightChosenButton(self.ui.lecturesButton))
        self.ui.teachersButton.clicked.connect(lambda: self.lightChosenButton(self.ui.teachersButton))
        self.ui.notesButton.clicked.connect(lambda: self.lightChosenButton(self.ui.notesButton))

    def setWindowDisabled(self):
        self.setDisabled(True)

    def lightChosenButton(self, button):
        self.unLightButtons()
        font = QFont()
        font.setUnderline(True)
        button.setFont(font)

    def unLightButtons(self):
        font = QFont()
        font.setUnderline(False)

        self.ui.scheduleButton.setFont(font)
        self.ui.lecturesButton.setFont(font)
        self.ui.teachersButton.setFont(font)
        self.ui.notesButton.setFont(font)

    def loadSchedule(self):
        self.newWidget = scheduleClassTeacher(mainWindow=self)
        self.ui.widgetContainer.replaceWidget(self.currentWidget, self.newWidget)
        self.currentWidget = self.newWidget
        self.currentWidget.ui.createMeetButton.clicked.connect(self.setWindowDisabled)
