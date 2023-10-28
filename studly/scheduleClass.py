# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_scheduleClass import Ui_Form
from datetime import datetime, timedelta
from consts import translatedMonth, weekDayCoefficient

class scheduleClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.meetColumns = [self.ui.dayColumn1, self.ui.dayColumn2, self.ui.dayColumn3, self.ui.dayColumn4, self.ui.dayColumn5, self.ui.dayColumn6, self.ui.dayColumn7]
        self.setDates()

    def setDates(self):
        day = int(datetime.now().strftime('%w'))
        koeff = weekDayCoefficient[day]
        dayDate = datetime.now() + timedelta(days=koeff)
        for col in range(7):
            if(dayDate == datetime.now()):
                self.meetColumns[col].setStyleSheet(f'''{self.meetColumns[col].styleSheet()}
                                                        border-style: solid;
                                                        border-color: rgb(32, 69, 71);
                                                        border-width: 5px;''')
            label = self.ui.daysContainer.itemAtPosition(0, col+1).widget()
            dayDate = self.convertDate(dayDate.strftime('%d %b'))
            label.setText(dayDate)
            dayDate = datetime.now() + timedelta(days=col+1+koeff)


    def convertDate(self, englishDate):
        day, englishMonth = englishDate.split(' ')
        return f'{day} {translatedMonth[englishMonth]}'
