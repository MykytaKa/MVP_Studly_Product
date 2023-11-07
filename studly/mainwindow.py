from schedule.scheduleClass import scheduleClass
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.currentWidget = scheduleClass()
        self.ui.widgetContainer.addWidget(self.currentWidget)
        self.ui.scheduleButton.clicked.connect(self.loadSchedule)

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


    def loadSchedule(self):
        newWidget = scheduleClass()
        self.ui.widgetContainer.replaceWidget(self.currentWidget, newWidget)
        self.currentWidget = newWidget

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



#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    widget = MainWindow()
#    window2 = MainWindowTeacher()
#    widget.show()
#    window2.show()
#    sys.exit(app.exec())
