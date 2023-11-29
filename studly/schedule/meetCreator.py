from PySide6 import QtWidgets
from PySide6.QtCore import QDateTime
from schedule.ui_meetCreator import Ui_MyDialog
from datetime import datetime, timedelta
from DB.connect_to_db import connect_to_database


class MeetCreator(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MyDialog()
        self.ui.setupUi(self)
        self.ui.dateTimeEdit.setDateTime(QDateTime((datetime.now() + timedelta(hours=1)).replace(minute=0, second=0,
                                                                                                 microsecond=0)))

        self.get_groups()

    @connect_to_database
    def get_groups(cursor, self):
        cursor.execute("SELECT name FROM classes")
        class_names = cursor.fetchall()

        self.ui.groupEdit.clear()
        for item in class_names:
            self.ui.groupEdit.addItem(item[0])

    def send_values(self):
        self.accept()
