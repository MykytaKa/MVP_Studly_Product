from PySide6 import QtWidgets
from schedule.ui_meetCreator import Ui_MyDialog


class MeetCreator(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)

        self.ui.frequency.addItem("Єдиноразово");
        self.ui.frequency.addItem("Кожен день");
        self.ui.frequency.addItem("Кожен тиждень");
        self.ui.frequency.addItem("Кожні два тижня");
        self.ui.frequency.addItem("Кожен місяць");

        self.ui.createButton.clicked.connect(self.send_values)

    def send_values(self):
        self.accept()
