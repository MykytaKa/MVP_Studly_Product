# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont, QFontDatabase
from ui_scheduleClassTeacher import Ui_Form
from datetime import datetime, timedelta
from meetCreator import meetCreator
from meetWidget import meetWidget
from consts import translatedMonth, weekDayCoefficient

class scheduleClassTeacher(QWidget):
    def __init__(self, mainWindow=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.window = None
        self.mainWindow = mainWindow
        self.ui.createMeetButton.clicked.connect(self.createMeetWindow)

        ## Розібратися з проблемою підключення шрифту
#        font_id = QFontDatabase.addApplicationFont('://Montserrat-VariableFont_wght.ttf');
#        print(font_id)
#        font_families = QFontDatabase.applicationFontFamilies(font_id);
#        family = ""
#        if font_families:
#            family = font_families[0]
#        labelFont = QFont(family, 12)
        ###############################################
        self.labelsDate = [self.ui.day1Label, self.ui.day2Label, self.ui.day3Label, self.ui.day4Label, self.ui.day5Label, self.ui.day6Label, self.ui.day7Label]
        self.meetColumns = [self.ui.dayColumn1, self.ui.dayColumn2, self.ui.dayColumn3, self.ui.dayColumn4, self.ui.dayColumn5, self.ui.dayColumn6, self.ui.dayColumn7]
        self.setDates()

    def setDates(self):
        day = int(datetime.now().strftime('%w'))
        koeff = weekDayCoefficient[day]
        dayDate = datetime.now() + timedelta(days=koeff)
        for col in range(7):
            label =  self.labelsDate[col]
            if(dayDate == datetime.now()):
                self.meetColumns[col].setStyleSheet(f'''{self.meetColumns[col].styleSheet()}
                                                        border-style: solid;
                                                        border-color: rgb(32, 69, 71);
                                                        border-width: 5px;''')
            dayDate = self.convertDate(dayDate.strftime('%d %b'))
#            label.setFont(labelFont)
            label.setText(dayDate)
            dayDate = datetime.now() + timedelta(days=col+1+koeff)

    def convertDate(self, englishDate):
        day, englishMonth = englishDate.split(' ')
        return f'{day} {translatedMonth[englishMonth]}'

    def createMeetWindow(self):
        self.window = meetCreator(mainWindow=self.mainWindow)
        self.window.show()
        self.window.ui.createButton.clicked.connect(self.createMeet)

    def createMeet(self):
        self.ui.dayColumn1Layout.insertWidget(0, meetWidget(subjectName=self.window.ui.nameEdit.text()))

        print(f'{self.window.ui.nameEdit.text()} {self.window.ui.groupEdit.currentText()}') ## Брати інформацію таким способом
