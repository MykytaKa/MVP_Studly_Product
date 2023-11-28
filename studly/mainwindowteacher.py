from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QMainWindow
from ui_mainwindowteacher import Ui_MainWindow
from schedule.scheduleClassTeacher import ScheduleClassTeacher
from notes.NotesClass import NotesWindow
from about.about import About
from PySide6.QtCore import Qt


class MainWindowTeacher(QMainWindow):
    def __init__(self, user_data = None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentWidget = ScheduleClassTeacher(user_data['user_id'])
        self.ui.widgetContainer.addWidget(self.currentWidget)

        self.ui.scheduleButton.clicked.connect(lambda: self.loadSection(ScheduleClassTeacher(user_data['user_id'])))
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

        self.ui.logoLabel.mousePressEvent = self.open_about_window

    def open_about_window(self, event):
        self.about = About()
        self.about.setModal(True)
        self.about.show()


    def resizeEvent(self, event):
        self.ui.logoLabel.setPixmap(QPixmap(":/icons/icon.png").scaled(self.ui.logoLabel.size(), Qt.KeepAspectRatio))


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


