from PySide6 import QtWidgets
from about.ui_about import Ui_Dialog
from PySide6.QtGui import QIcon


class About(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("About")
        self.setWindowIcon(QIcon(':/icons/exe_icon.png'))

        self.ui.closeButton.clicked.connect(self.send_values)

    def send_values(self):
        self.accept()
