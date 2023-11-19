# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleClass.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 449)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(239, 241, 237);")
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.todayButton = QPushButton(self.groupBox)
        self.todayButton.setObjectName(u"todayButton")
        self.todayButton.setMinimumSize(QSize(80, 30))
        self.todayButton.setMaximumSize(QSize(80, 30))
        font = QFont()
        font.setPointSize(10)
        self.todayButton.setFont(font)
        self.todayButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.todayButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.todayButton, 1, 7, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 3, 1, 1)

        self.groupLabel = QLabel(self.groupBox)
        self.groupLabel.setObjectName(u"groupLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupLabel.sizePolicy().hasHeightForWidth())
        self.groupLabel.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.groupLabel.setFont(font1)
        self.groupLabel.setLayoutDirection(Qt.LeftToRight)
        self.groupLabel.setAutoFillBackground(False)
        self.groupLabel.setStyleSheet(u"padding-right: 5px;\n"
"padding-bottom: 10px;\n"
"padding-left: 95px;")
        self.groupLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.groupLabel, 1, 0, 1, 5)

        self.chooseDateButton = QPushButton(self.groupBox)
        self.chooseDateButton.setObjectName(u"chooseDateButton")
        self.chooseDateButton.setMinimumSize(QSize(100, 30))
        self.chooseDateButton.setMaximumSize(QSize(100, 30))
        self.chooseDateButton.setFont(font)
        self.chooseDateButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.chooseDateButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.chooseDateButton, 1, 5, 1, 1)

        self.dateForward = QPushButton(self.groupBox)
        self.dateForward.setObjectName(u"dateForward")
        self.dateForward.setMinimumSize(QSize(30, 30))
        self.dateForward.setMaximumSize(QSize(30, 30))
        self.dateForward.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateForward.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.dateForward, 1, 8, 1, 1)

        self.dateBack = QPushButton(self.groupBox)
        self.dateBack.setObjectName(u"dateBack")
        self.dateBack.setMinimumSize(QSize(30, 30))
        self.dateBack.setMaximumSize(QSize(30, 30))
        self.dateBack.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateBack.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.dateBack, 1, 6, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 9)

        self.horizontalSpacer = QSpacerItem(20, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 9, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.daysContainer = QGridLayout()
        self.daysContainer.setObjectName(u"daysContainer")
        self.daysContainer.setContentsMargins(-1, -1, 9, 0)
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 725, 313))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dayColumn1 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn1.setObjectName(u"dayColumn1")
        sizePolicy1.setHeightForWidth(self.dayColumn1.sizePolicy().hasHeightForWidth())
        self.dayColumn1.setSizePolicy(sizePolicy1)
        self.dayColumn1.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;")
        self.verticalLayout = QVBoxLayout(self.dayColumn1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.dayColumn1)

        self.dayColumn2 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn2.setObjectName(u"dayColumn2")
        sizePolicy1.setHeightForWidth(self.dayColumn2.sizePolicy().hasHeightForWidth())
        self.dayColumn2.setSizePolicy(sizePolicy1)
        self.dayColumn2.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.verticalLayout_2 = QVBoxLayout(self.dayColumn2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addWidget(self.dayColumn2)

        self.dayColumn3 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn3.setObjectName(u"dayColumn3")
        sizePolicy1.setHeightForWidth(self.dayColumn3.sizePolicy().hasHeightForWidth())
        self.dayColumn3.setSizePolicy(sizePolicy1)
        self.dayColumn3.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.verticalLayout_3 = QVBoxLayout(self.dayColumn3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addWidget(self.dayColumn3)

        self.dayColumn4 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn4.setObjectName(u"dayColumn4")
        sizePolicy1.setHeightForWidth(self.dayColumn4.sizePolicy().hasHeightForWidth())
        self.dayColumn4.setSizePolicy(sizePolicy1)
        self.dayColumn4.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.verticalLayout_4 = QVBoxLayout(self.dayColumn4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addWidget(self.dayColumn4)

        self.dayColumn5 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn5.setObjectName(u"dayColumn5")
        sizePolicy1.setHeightForWidth(self.dayColumn5.sizePolicy().hasHeightForWidth())
        self.dayColumn5.setSizePolicy(sizePolicy1)
        self.dayColumn5.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.verticalLayout_5 = QVBoxLayout(self.dayColumn5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)


        self.horizontalLayout_2.addWidget(self.dayColumn5)

        self.dayColumn6 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn6.setObjectName(u"dayColumn6")
        sizePolicy1.setHeightForWidth(self.dayColumn6.sizePolicy().hasHeightForWidth())
        self.dayColumn6.setSizePolicy(sizePolicy1)
        self.dayColumn6.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.verticalLayout_6 = QVBoxLayout(self.dayColumn6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)


        self.horizontalLayout_2.addWidget(self.dayColumn6)

        self.dayColumn7 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn7.setObjectName(u"dayColumn7")
        sizePolicy1.setHeightForWidth(self.dayColumn7.sizePolicy().hasHeightForWidth())
        self.dayColumn7.setSizePolicy(sizePolicy1)
        self.dayColumn7.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-radius: 0px;\n"
"border-color: rgb(120, 180, 167);\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.verticalLayout_7 = QVBoxLayout(self.dayColumn7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)


        self.horizontalLayout_2.addWidget(self.dayColumn7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.daysContainer.addWidget(self.scrollArea, 2, 1, 1, 7)

        self.day1Label = QLabel(self.groupBox)
        self.day1Label.setObjectName(u"day1Label")
        font2 = QFont()
        font2.setPointSize(12)
        self.day1Label.setFont(font2)
        self.day1Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day1Label, 1, 1, 1, 1)

        self.day2Label = QLabel(self.groupBox)
        self.day2Label.setObjectName(u"day2Label")
        self.day2Label.setFont(font2)
        self.day2Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day2Label, 1, 2, 1, 1)

        self.day3Label = QLabel(self.groupBox)
        self.day3Label.setObjectName(u"day3Label")
        self.day3Label.setFont(font2)
        self.day3Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day3Label, 1, 3, 1, 1)

        self.day4Label = QLabel(self.groupBox)
        self.day4Label.setObjectName(u"day4Label")
        self.day4Label.setFont(font2)
        self.day4Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day4Label, 1, 4, 1, 1)

        self.day5Label = QLabel(self.groupBox)
        self.day5Label.setObjectName(u"day5Label")
        self.day5Label.setFont(font2)
        self.day5Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day5Label, 1, 5, 1, 1)

        self.day6Label = QLabel(self.groupBox)
        self.day6Label.setObjectName(u"day6Label")
        self.day6Label.setFont(font2)
        self.day6Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day6Label, 1, 6, 1, 1)

        self.day7Label = QLabel(self.groupBox)
        self.day7Label.setObjectName(u"day7Label")
        self.day7Label.setFont(font2)
        self.day7Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day7Label, 1, 7, 1, 1)


        self.horizontalLayout.addLayout(self.daysContainer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 10)


        self.verticalLayout_8.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"scheduleWindow", None))
        self.groupBox.setTitle("")
        self.todayButton.setText(QCoreApplication.translate("Form", u"\u0421\u044c\u043e\u0433\u043e\u0434\u043d\u0456", None))
        self.groupLabel.setText(QCoreApplication.translate("Form", u"\u0406\u041a\u041c-222\u0430", None))
        self.chooseDateButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.dateForward.setText(QCoreApplication.translate("Form", u">", None))
        self.dateBack.setText(QCoreApplication.translate("Form", u"<", None))
        self.day1Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day2Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day3Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day4Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day5Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day6Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day7Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

