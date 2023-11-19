from schedule.scheduleClass import ScheduleClass
from notes.NotesClass import NotesWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_mainwindowstudent import Ui_MainWindow


class MainWindowStudent(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentWidget = ScheduleClass()
        self.ui.widgetContainer.addWidget(self.currentWidget)

        self.ui.scheduleButton.clicked.connect(lambda: self.loadSection(ScheduleClass()))
        self.ui.notesButton.clicked.connect(lambda: self.loadSection(NotesWindow()))

        self.unlight_buttons()

        buttonFont = QFont()
        buttonFont.setPointSize(11)

        self.ui.scheduleButton.setFont(buttonFont)
        self.ui.lecturesButton.setFont(buttonFont)
        self.ui.teachersButton.setFont(buttonFont)
        self.ui.notesButton.setFont(buttonFont)

        buttonFont.setPointSize(11)
        buttonFont.setBold(True)
        self.ui.scheduleButton.setFont(buttonFont)

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
        font.setPointSize(11)
        font.setBold(True)
        button.setFont(font)

    def unlight_buttons(self):
        buttonFont = QFont()
        buttonFont.setPointSize(11)

        self.ui.scheduleButton.setFont(buttonFont)
        self.ui.lecturesButton.setFont(buttonFont)
        self.ui.teachersButton.setFont(buttonFont)
        self.ui.notesButton.setFont(buttonFont)

    def loadSection(self, section):
        self.currentWidget.close()
        self.newWidget = section
        self.ui.widgetContainer.replaceWidget(self.currentWidget, self.newWidget)
        self.currentWidget = self.newWidget
