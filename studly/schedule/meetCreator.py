from PySide6 import QtWidgets
from schedule.ui_meetCreator import Ui_MyDialog


class MeetCreator(QtWidgets.QDialog):
    def __init__(self, main_window=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)
        self.mainWindow = main_window
        self.ui.groupEdit.addItem("ІКМ-222а")
        self.ui.groupEdit.addItem("ІКМ-222б")
        self.ui.groupEdit.addItem("ІКМ-222в")

        self.ui.createButton.clicked.connect(self.send_values)

    def send_values(self):
        self.accept()
