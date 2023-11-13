from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow
from ui_mainwindowteacher import Ui_MainWindow
from schedule.scheduleClassTeacher import ScheduleClassTeacher
from notes.NotesClass import NotesWindow
from PySide6.QtCore import Qt


class MainWindowTeacher(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentWidget = ScheduleClassTeacher(main_window=self)
        self.ui.widgetContainer.addWidget(self.currentWidget)

        self.ui.scheduleButton.clicked.connect(lambda: self.loadSection(ScheduleClassTeacher()))
        self.ui.notesButton.clicked.connect(lambda: self.loadSection(NotesWindow()))

        self.unlight_buttons()
        font = QFont()
        font.setUnderline(True)
        self.ui.scheduleButton.setFont(font)

        self.ui.scheduleButton.setCursor(Qt.PointingHandCursor)
        self.ui.lecturesButton.setCursor(Qt.PointingHandCursor)
        self.ui.teachersButton.setCursor(Qt.PointingHandCursor)
        self.ui.notesButton.setCursor(Qt.PointingHandCursor)

        self.ui.scheduleButton.clicked.connect(lambda: self.light_chosen_button(self.ui.scheduleButton))
        self.ui.lecturesButton.clicked.connect(lambda: self.light_chosen_button(self.ui.lecturesButton))
        self.ui.teachersButton.clicked.connect(lambda: self.light_chosen_button(self.ui.teachersButton))
        self.ui.notesButton.clicked.connect(lambda: self.light_chosen_button(self.ui.notesButton))

    def light_chosen_button(self, button):
        self.unlight_buttons()
        font = QFont()
        font.setUnderline(True)
        button.setFont(font)

    def unlight_buttons(self):
        font = QFont()
        font.setUnderline(False)

        self.ui.scheduleButton.setFont(font)
        self.ui.lecturesButton.setFont(font)
        self.ui.teachersButton.setFont(font)
        self.ui.notesButton.setFont(font)

    def loadSection(self, section):
        self.currentWidget.close()
        self.newWidget = section
        self.ui.widgetContainer.replaceWidget(self.currentWidget, self.newWidget)
        self.currentWidget = self.newWidget
