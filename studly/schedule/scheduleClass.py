# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from schedule.ui_scheduleClass import Ui_Form
from datetime import datetime, timedelta
from consts import translatedMonth, weekDayCoefficient


class ScheduleClass(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dateMovement = 0
        self.labelsDate = [self.ui.day1Label, self.ui.day2Label, self.ui.day3Label, self.ui.day4Label,
                           self.ui.day5Label, self.ui.day6Label, self.ui.day7Label]
        self.meetColumns = [self.ui.dayColumn1, self.ui.dayColumn2, self.ui.dayColumn3, self.ui.dayColumn4,
                            self.ui.dayColumn5, self.ui.dayColumn6, self.ui.dayColumn7]
        self.ui.dateBack.clicked.connect(self.move_date_back)
        self.ui.dateForward.clicked.connect(self.move_date_forward)
        self.set_dates()

    def set_dates(self):
        day = int(datetime.now().strftime('%w'))
        coeff = weekDayCoefficient[day]
        day_date = datetime.now() + timedelta(days=coeff+self.dateMovement)
        for col in range(7):
            label =  self.labelsDate[col]
            ### Встановлення рамки для сьогоднішньої дати
            if day_date == datetime.now():
                if col == 0:
                    self.meetColumns[col].setStyleSheet('''background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-style: solid;
                                                            border-color: rgb(32, 69, 71);
                                                            border-width: 5px;
                                                            border-radius: 0px;
                                                            border-top-left-radius: 10px;
                                                            border-bottom-left-radius: 10px;}
                                                            ''')
                elif col == 6:
                    self.meetColumns[col].setStyleSheet('''background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-radius: 0px;
                                                            border-top-right-radius: 10px;
                                                            border-bottom-right-radius: 10px;
                                                            border-style: solid;
                                                            border-color: rgb(32, 69, 71);
                                                            border-width: 5px;
                                                            ''')
                else:
                    self.meetColumns[col].setStyleSheet('''background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-radius: 0px;
                                                            border-style: solid;
                                                            border-color: rgb(32, 69, 71);
                                                            border-width: 5px;
                                                            ''')
            ### Встановлення рамки для усіх інших дат дат
            else:
                if col == 0:
                    self.meetColumns[col].setStyleSheet('''border-radius: 0px;
                                                            background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-color: rgb(120, 180, 167);
                                                            border-top-left-radius: 10px;
                                                            border-bottom-left-radius: 10px;''')
                elif col == 6:
                    self.meetColumns[col].setStyleSheet('''border-radius: 0px;
                                                            border-top-right-radius: 10px;
                                                            border-bottom-right-radius: 10px;
                                                            background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-color: rgb(120, 180, 167);''')
                else:
                    self.meetColumns[col].setStyleSheet('''border-radius: 0px;
                                                            background-color: rgb(120, 180, 167);
                                                            alternate-background-color: rgb(120, 180, 167);
                                                            border-color: rgb(120, 180, 167);''')

            day_date = self.convert_date(day_date.strftime('%d %b'))
            label.setText(day_date)
            day_date = datetime.now() + timedelta(days=col+1+coeff+self.dateMovement)

    def convert_date(self, english_date):
        day, english_month = english_date.split(' ')
        return f'{day} {translatedMonth[english_month]}'

    def move_date_back(self):
        self.dateMovement -= 7
        self.set_dates()

    def move_date_forward(self):
        self.dateMovement += 7
        self.set_dates()
