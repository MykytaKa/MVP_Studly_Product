# This Python file uses the following encoding: utf-8
#from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QPushButton
from ui_mainwindowteacher import Ui_MainWindow
from scheduleClassTeacher import scheduleClassTeacher


class MainWindowTeacher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widgetContainer.addWidget(scheduleClassTeacher())
