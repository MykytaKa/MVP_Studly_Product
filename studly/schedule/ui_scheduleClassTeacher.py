# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleClassTeacher.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(702, 435)
        Form.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(239, 241, 237);")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 10px;")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.dateBack = QPushButton(self.groupBox)
        self.dateBack.setObjectName(u"dateBack")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBack.sizePolicy().hasHeightForWidth())
        self.dateBack.setSizePolicy(sizePolicy)
        self.dateBack.setMinimumSize(QSize(30, 30))
        self.dateBack.setMaximumSize(QSize(30, 30))
        self.dateBack.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateBack.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.dateBack, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.dateForward = QPushButton(self.groupBox)
        self.dateForward.setObjectName(u"dateForward")
        sizePolicy.setHeightForWidth(self.dateForward.sizePolicy().hasHeightForWidth())
        self.dateForward.setSizePolicy(sizePolicy)
        self.dateForward.setMinimumSize(QSize(30, 30))
        self.dateForward.setMaximumSize(QSize(30, 30))
        self.dateForward.setCursor(QCursor(Qt.PointingHandCursor))
        self.dateForward.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.dateForward, 1, 4, 1, 1)

        self.createMeetButton = QPushButton(self.groupBox)
        self.createMeetButton.setObjectName(u"createMeetButton")
        sizePolicy.setHeightForWidth(self.createMeetButton.sizePolicy().hasHeightForWidth())
        self.createMeetButton.setSizePolicy(sizePolicy)
        self.createMeetButton.setMinimumSize(QSize(120, 30))
        self.createMeetButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createMeetButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"background-color: rgba(69, 119, 108, 25);\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")

        self.gridLayout_2.addWidget(self.createMeetButton, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 6, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.daysContainer = QGridLayout()
        self.daysContainer.setObjectName(u"daysContainer")
        self.daysContainer.setHorizontalSpacing(3)
        self.daysContainer.setContentsMargins(-1, -1, 9, -1)
        self.day2Label = QLabel(self.groupBox)
        self.day2Label.setObjectName(u"day2Label")
        font = QFont()
        font.setPointSize(12)
        self.day2Label.setFont(font)
        self.day2Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day2Label, 0, 2, 1, 1)

        self.day5Label = QLabel(self.groupBox)
        self.day5Label.setObjectName(u"day5Label")
        self.day5Label.setFont(font)
        self.day5Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day5Label, 0, 5, 1, 1)

        self.day7Label = QLabel(self.groupBox)
        self.day7Label.setObjectName(u"day7Label")
        self.day7Label.setFont(font)
        self.day7Label.setStyleSheet(u"border-top-right-radius: 10px;")
        self.day7Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day7Label, 0, 7, 1, 1)

        self.day4Label = QLabel(self.groupBox)
        self.day4Label.setObjectName(u"day4Label")
        self.day4Label.setFont(font)
        self.day4Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day4Label, 0, 4, 1, 1)

        self.day3Label = QLabel(self.groupBox)
        self.day3Label.setObjectName(u"day3Label")
        self.day3Label.setFont(font)
        self.day3Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day3Label, 0, 3, 1, 1)

        self.day1Label = QLabel(self.groupBox)
        self.day1Label.setObjectName(u"day1Label")
        self.day1Label.setFont(font)
        self.day1Label.setStyleSheet(u"border-top-left-radius: 10px;")
        self.day1Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day1Label, 0, 1, 1, 1)

        self.day6Label = QLabel(self.groupBox)
        self.day6Label.setObjectName(u"day6Label")
        self.day6Label.setFont(font)
        self.day6Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day6Label, 0, 6, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.daysContainer.addItem(self.verticalSpacer_4, 2, 1, 1, 7)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.VLine)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 657, 293))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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
        self.dayColumn1Layout = QVBoxLayout(self.dayColumn1)
        self.dayColumn1Layout.setSpacing(0)
        self.dayColumn1Layout.setObjectName(u"dayColumn1Layout")
        self.dayColumn1Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn1Layout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.dayColumn1)

        self.dayColumn2 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn2.setObjectName(u"dayColumn2")
        sizePolicy1.setHeightForWidth(self.dayColumn2.sizePolicy().hasHeightForWidth())
        self.dayColumn2.setSizePolicy(sizePolicy1)
        self.dayColumn2.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.dayColumn2Layout = QVBoxLayout(self.dayColumn2)
        self.dayColumn2Layout.setObjectName(u"dayColumn2Layout")
        self.dayColumn2Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn2Layout.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addWidget(self.dayColumn2)

        self.dayColumn3 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn3.setObjectName(u"dayColumn3")
        sizePolicy1.setHeightForWidth(self.dayColumn3.sizePolicy().hasHeightForWidth())
        self.dayColumn3.setSizePolicy(sizePolicy1)
        self.dayColumn3.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.dayColumn3Layout = QVBoxLayout(self.dayColumn3)
        self.dayColumn3Layout.setObjectName(u"dayColumn3Layout")
        self.dayColumn3Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn3Layout.addItem(self.verticalSpacer_6)


        self.horizontalLayout_3.addWidget(self.dayColumn3)

        self.dayColumn4 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn4.setObjectName(u"dayColumn4")
        sizePolicy1.setHeightForWidth(self.dayColumn4.sizePolicy().hasHeightForWidth())
        self.dayColumn4.setSizePolicy(sizePolicy1)
        self.dayColumn4.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.dayColumn4Layout = QVBoxLayout(self.dayColumn4)
        self.dayColumn4Layout.setObjectName(u"dayColumn4Layout")
        self.dayColumn4Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn4Layout.addItem(self.verticalSpacer_7)


        self.horizontalLayout_3.addWidget(self.dayColumn4)

        self.dayColumn5 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn5.setObjectName(u"dayColumn5")
        sizePolicy1.setHeightForWidth(self.dayColumn5.sizePolicy().hasHeightForWidth())
        self.dayColumn5.setSizePolicy(sizePolicy1)
        self.dayColumn5.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.dayColumn5Layout = QVBoxLayout(self.dayColumn5)
        self.dayColumn5Layout.setObjectName(u"dayColumn5Layout")
        self.dayColumn5Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn5Layout.addItem(self.verticalSpacer_8)


        self.horizontalLayout_3.addWidget(self.dayColumn5)

        self.dayColumn6 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn6.setObjectName(u"dayColumn6")
        sizePolicy1.setHeightForWidth(self.dayColumn6.sizePolicy().hasHeightForWidth())
        self.dayColumn6.setSizePolicy(sizePolicy1)
        self.dayColumn6.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-color: rgb(120, 180, 167);\n"
"border-radius: 0px;")
        self.dayColumn6Layout = QVBoxLayout(self.dayColumn6)
        self.dayColumn6Layout.setObjectName(u"dayColumn6Layout")
        self.dayColumn6Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn6Layout.addItem(self.verticalSpacer_9)


        self.horizontalLayout_3.addWidget(self.dayColumn6)

        self.dayColumn7 = QWidget(self.scrollAreaWidgetContents)
        self.dayColumn7.setObjectName(u"dayColumn7")
        sizePolicy1.setHeightForWidth(self.dayColumn7.sizePolicy().hasHeightForWidth())
        self.dayColumn7.setSizePolicy(sizePolicy1)
        self.dayColumn7.setStyleSheet(u"background-color: rgb(120, 180, 167);\n"
"alternate-background-color: rgb(120, 180, 167);\n"
"border-radius: 0px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.dayColumn7Layout = QVBoxLayout(self.dayColumn7)
        self.dayColumn7Layout.setObjectName(u"dayColumn7Layout")
        self.dayColumn7Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.dayColumn7Layout.addItem(self.verticalSpacer_10)


        self.horizontalLayout_3.addWidget(self.dayColumn7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.daysContainer.addWidget(self.scrollArea, 1, 1, 1, 7)


        self.gridLayout_2.addLayout(self.daysContainer, 3, 0, 1, 6)


        self.horizontalLayout.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.dateBack.setText(QCoreApplication.translate("Form", u"<", None))
        self.dateForward.setText(QCoreApplication.translate("Form", u">", None))
        self.createMeetButton.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0437\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.day2Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day5Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day7Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day4Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day3Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day1Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day6Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

