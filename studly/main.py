# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = Login()
    myWidget.show()
    sys.exit(app.exec())
