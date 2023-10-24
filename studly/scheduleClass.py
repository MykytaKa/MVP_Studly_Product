# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_scheduleClass import Ui_Form
from datetime import datetime, timedelta

class scheduleClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        dayDate = datetime.now()
        for col in range(7):
            label = self.ui.daysContainer.itemAtPosition(0, col).widget()
            dayDate = dayDate.strftime('%d %b')
            label.setText(dayDate)
            dayDate = datetime.now() + timedelta(days=col+1)

