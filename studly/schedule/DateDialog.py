# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import
from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QSpacerItem
from PySide6.QtCore import Qt
from datetime import datetime, timedelta
from consts import weekDayCoefficient, translatedFullMonth
from PySide6.QtGui import QIcon

class QDateButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.day = -1
        self.month = -1
        self.year = -1
        self.setFixedSize(30, 30)
        self.setStyleSheet('''background-color: rgb(239, 241, 237);\n
                              color: rgb(32, 69, 71);
                              border-style: none;''')
        self.setCursor(Qt.PointingHandCursor)



    def set_day(self, new_day):
        self.setText(new_day)
        self.day = new_day

    def set_month(self, new_month):
        self.month = new_month

    def set_year(self, new_year):
        self.year = new_year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

#
class DateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(250, 270)
        self.setWindowTitle('Оберіть дату')
        self.setWindowIcon(QIcon(':/icons/calendar.png'))
        self.current_month = int(datetime.now().strftime('%m'))
        self.current_year = int(datetime.now().strftime('%Y'))
        self.selected_date = datetime.now().strftime('%d.%m.%Y')

        # Контейнер для зберігання кнопок з датами
        self.days_container = QGridLayout()

        # Кнопка переміщення дати назад на один місяць
        self.next_month_button = QPushButton()
        self.next_month_button.setText('>')
        self.next_month_button.clicked.connect(lambda: self.move_date(self.next_month_button))
        self.next_month_button.setStyleSheet('''border-radius: 10px;
                                                border-style: solid;
                                                background-color: rgba(69, 119, 108, 25);
                                                border-color: rgb(69, 119, 108);
                                                border-width: 2px;''')
        self.next_month_button.setCursor(Qt.PointingHandCursor)

        # Кнопка переміщення дати вперед на один місяць
        self.prev_month_button = QPushButton()
        self.prev_month_button.setText('<')
        self.prev_month_button.clicked.connect(lambda: self.move_date(self.prev_month_button))
        self.prev_month_button.setStyleSheet('''border-radius: 10px;
                                                border-style: solid;
                                                background-color: rgba(69, 119, 108, 25);
                                                border-color: rgb(69, 119, 108);
                                                border-width: 2px;''')
        self.prev_month_button.setCursor(Qt.PointingHandCursor)

        # Напис для відображення місяця
        self.month_label = QLabel()
        self.month_label.setText(translatedFullMonth[datetime.now().strftime('%B')])

        # Напис для відображення року
        self.year_label = QLabel()
        self.year_label.setText(datetime.now().strftime('%Y'))

        # Контейнер для збереження написів та кнопок верхньої панелі
        self.menu_container = QHBoxLayout()
        self.menu_container.addWidget(self.prev_month_button)
        self.menu_container.addSpacerItem(QSpacerItem(30, 1))
        self.menu_container.addWidget(self.month_label)
        self.menu_container.addWidget(self.year_label)
        self.menu_container.addSpacerItem(QSpacerItem(20, 1))
        self.menu_container.addWidget(self.next_month_button)

        # Кнопка відправленя обраної дати
        self.button_ok = QPushButton('OK')
        self.button_ok.setStyleSheet('border-radius: 10px;\nborder-style: solid;\nborder-color: rgb(69, 119, 108);\nborder-width: 2px;\nbackground-color: rgb(32, 69, 71);\ncolor: rgb(239, 241, 237);')
        self.button_ok.setCursor(Qt.PointingHandCursor)
        self.button_ok.clicked.connect(self.accept)

        self.week_days_container = QHBoxLayout()
        week_days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
        for day in week_days:
            label = QLabel(day)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setFixedSize(30, 24)
            self.week_days_container.addWidget(label)

        self.initialize_buttons()
        self.set_dates()
        self.calendar = QVBoxLayout()
        self.calendar.addLayout(self.menu_container)
        self.calendar.addLayout(self.week_days_container)
        self.calendar.addLayout(self.days_container)
        self.calendar.addSpacing(10)
        self.calendar.addWidget(self.button_ok)

        self.setLayout(self.calendar)

    def initialize_buttons(self):
        for week in range(1, 7):
            for day in range (1, 8):
                date_button = QDateButton()
                date_button.clicked.connect(lambda checked=True, button=date_button: self.light_date(button))
                self.days_container.addWidget(date_button, week-1, day-1)

    def set_dates(self):
        current_month_first_day = datetime.strptime(f'01.{self.current_month}.{self.current_year}', '%d.%m.%Y')
        # Прорахування положення першого числа теперішнього місяця у тижні,
        # Тобто яким днем тижня є перше число теперішнього місяця
        current_day = int(current_month_first_day.strftime('%w'))
        # Прорахування того, яка дата буде стояти у понеділок у той же тиждень, в
        # якому стоїть перше число місяця
        coeff = weekDayCoefficient[current_day]
        first_calendar_day = current_month_first_day + timedelta(days=coeff)
        for week in range(1, 7):
            for day in range (1, 8):
                day_date = first_calendar_day + timedelta(days=day-1, weeks=week-1)
                date_button = self.days_container.itemAtPosition(week-1, day-1).widget()
                date_button.set_day(day_date.strftime('%d'))
                date_button.set_month(day_date.strftime('%m'))
                date_button.set_year(day_date.strftime('%Y'))

                if day_date.strftime('%d.%m.%Y') == datetime.now().strftime('%d.%m.%Y'):
                    date_button.setStyleSheet('''background-color: rgb(32, 69, 71);\n
                                                 color: rgb(239, 241, 237);\n
                                                 border-style: none;''')
                elif day_date.strftime('%m') != current_month_first_day.strftime('%m'):
                    date_button.setStyleSheet('''background-color: rgb(239, 241, 237);\n
                                                 color: rgba(32, 69, 71, 150);
                                                 border-style: none;''')
                else:
                    date_button.setStyleSheet('''background-color: rgb(239, 241, 237);\n
                                                 color: rgb(32, 69, 71);
                                                 border-style: none;''')

    def light_date(self, date_button):
        self.unlight_dates()
        date_button.setStyleSheet('border-style: solid;\nborder-width: 1px;\nborder-color: rgb(32, 69, 71);')
        self.selected_date = f'{date_button.get_day()}.{date_button.get_month()}.{date_button.get_year()}'

    def unlight_dates(self):
        for i in range(6):
            for j in range(7):
                date_button = self.days_container.itemAtPosition(i, j).widget()

                if f'{date_button.get_day()}.{date_button.get_month()}.{date_button.get_year()}' == datetime.now().strftime('%d.%m.%Y'):
                    date_button.setStyleSheet('''background-color: rgb(32, 69, 71);\n
                                                 color: rgb(239, 241, 237);\n
                                                 border-style: none;''')
                elif int(date_button.get_month()) != self.current_month:
                    date_button.setStyleSheet('''background-color: rgb(239, 241, 237);\n
                                                 color: rgba(32, 69, 71, 150);
                                                 border-style: none;''')
                else:
                    date_button.setStyleSheet('background-color: rgb(239, 241, 237);\ncolor: rgb(32, 69, 71);\nborder-style: none;')

    def move_date(self, button):
        if button == self.prev_month_button:
            if self.current_month == 1:
                self.current_month = 12
                self.current_year -= 1
            else:
                self.current_month -= 1
        else:
            if self.current_month == 12:
                self.current_month = 1
                self.current_year += 1
            else:
                self.current_month += 1
        current_date = datetime.strptime(f'{self.current_month}.{self.current_year}', '%m.%Y')
        self.month_label.setText(translatedFullMonth[current_date.strftime('%B')])
        self.year_label.setText(f'{self.current_year}')
        self.set_dates()


