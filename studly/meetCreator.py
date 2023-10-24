# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets
from ui_meetCreator import Ui_Form

class meetCreator(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.groupEdit.addItem("ІКМ-222а")
        self.ui.groupEdit.addItem("ІКМ-222б")
        self.ui.groupEdit.addItem("ІКМ-222в")

#        self.ui.createButton.clicked.connect()

    def getValues(self):
        return self.ui.nameEdit.text,
