# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog
from schedule.ui_scheduleClass import Ui_Form
from datetime import datetime, timedelta
from consts import translatedMonth, weekDayCoefficient
from schedule.DateDialog import DateDialog
from consts import translatedDay, weekDayCoefficient, translatedFullMonth, weekDayPosition

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
        self.ui.todayButton.clicked.connect(self.set_today_date)
        self.ui.chooseDateButton.clicked.connect(self.set_chosen_date)
        self.set_dates()

    def set_chosen_date(self):
        date_dialog = DateDialog()
        result = date_dialog.exec()
        if result == QDialog.Accepted:
            selected_date = date_dialog.selected_date
            if datetime.strptime(selected_date, '%d.%m.%Y') > datetime.now():
                passed_days = 0
                while True:
                    if (datetime.now() + timedelta(days=passed_days)).strftime('%d.%m.%Y') == selected_date:
                        break
                    passed_days += 1
                days_lambda = passed_days - weekDayPosition[(datetime.now() + timedelta(days=passed_days)).strftime('%A')] + weekDayPosition[(datetime.now()).strftime('%A')]
                self.dateMovement = days_lambda
            else:
                passed_days = 0
                while True:
                    if (datetime.now() - timedelta(days=passed_days)).strftime('%d.%m.%Y') == selected_date:
                        break
                    passed_days += 1
                days_lambda = - (passed_days) - weekDayPosition[(datetime.now() - timedelta(days=passed_days)).strftime('%A')] + weekDayPosition[(datetime.now()).strftime('%A')]
                self.dateMovement = days_lambda
            self.set_dates()

    def set_today_date(self):
        self.dateMovement = 0
        self.set_dates()

    def set_dates(self):
        months = []
        day = int(datetime.now().strftime('%w'))
        coeff = weekDayCoefficient[day]
        day_date = datetime.now() + timedelta(days=coeff+self.dateMovement)
        for col in range(7):
            if col == 0 or col == 6:
                months.append(f'{day_date.strftime("%B %Y")} р.')
            label = self.labelsDate[col]
            # Встановлення рамки для сьогоднішньої дати
            if day_date.strftime('%d.%m.%Y') == datetime.now().strftime('%d.%m.%Y'):
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
            # Встановлення рамки для усіх інших дат дат
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

            day_date = self.convert_date(day_date.strftime('%d %A'))
            label.setText(day_date)
            day_date = datetime.now() + timedelta(days=col+1+coeff+self.dateMovement)


        if months[0] != months[1]:
            self.ui.chooseDateButton.setFixedWidth(230)
            translated_month1 = translatedFullMonth[months[0].split(" ")[0]]
            new_year1 = f'{months[0].split(" ")[-2:-1][0]} р.'
            translated_month2 = translatedFullMonth[months[1].split(" ")[0]]
            new_year2 = f'{months[1].split(" ")[-2:-1][0]} р.'
            new_text = f'{translated_month1} {new_year1} - {translated_month2} {new_year2}'
            self.ui.chooseDateButton.setText(new_text)
        else:
            self.ui.chooseDateButton.setFixedWidth(120)
            translated_month = translatedFullMonth[months[0].split(" ")[0]]
            new_year = f'{months[0].split(" ")[-2:-1][0]} р.'
            new_text = f'{translated_month} {new_year}'
            self.ui.chooseDateButton.setText(new_text)

    def convert_date(self, english_date):
        day, english_day = english_date.split(' ')
        return f'{day} {translatedDay[english_day]}'

    # Переміщення дати на попередній тиждень
    def move_date_back(self):
        self.dateMovement -= 7
        self.set_dates()

    # Переміщення дати на наступний тиждень
    def move_date_forward(self):
        self.dateMovement += 7
        self.set_dates()

