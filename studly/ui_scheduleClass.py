# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scheduleClass.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 449)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupLabel = QLabel(Form)
        self.groupLabel.setObjectName(u"groupLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupLabel.sizePolicy().hasHeightForWidth())
        self.groupLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        self.groupLabel.setFont(font)
        self.groupLabel.setAutoFillBackground(False)
        self.groupLabel.setStyleSheet(u"padding-right: 5px;")
        self.groupLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.groupLabel, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.daysContainer = QGridLayout()
        self.daysContainer.setObjectName(u"daysContainer")
        self.dayColumn6 = QWidget(Form)
        self.dayColumn6.setObjectName(u"dayColumn6")
        self.dayColumn6.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.dayColumn6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn6, 1, 5, 1, 1)

        self.day7Label = QLabel(Form)
        self.day7Label.setObjectName(u"day7Label")
        self.day7Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day7Label, 0, 6, 1, 1)

        self.dayColumn7 = QWidget(Form)
        self.dayColumn7.setObjectName(u"dayColumn7")
        self.dayColumn7.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.dayColumn7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn7, 1, 6, 1, 1)

        self.day3Label = QLabel(Form)
        self.day3Label.setObjectName(u"day3Label")
        self.day3Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day3Label, 0, 2, 1, 1)

        self.day1Label = QLabel(Form)
        self.day1Label.setObjectName(u"day1Label")
        self.day1Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day1Label, 0, 0, 1, 1)

        self.dayColumn3 = QWidget(Form)
        self.dayColumn3.setObjectName(u"dayColumn3")
        self.dayColumn3.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.dayColumn3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn3, 1, 2, 1, 1)

        self.dayColumn5 = QWidget(Form)
        self.dayColumn5.setObjectName(u"dayColumn5")
        self.dayColumn5.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.dayColumn5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn5, 1, 4, 1, 1)

        self.day6Label = QLabel(Form)
        self.day6Label.setObjectName(u"day6Label")
        self.day6Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day6Label, 0, 5, 1, 1)

        self.dayColumn1 = QWidget(Form)
        self.dayColumn1.setObjectName(u"dayColumn1")
        self.verticalLayout = QVBoxLayout(self.dayColumn1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn1, 1, 0, 1, 1)

        self.dayColumn2 = QWidget(Form)
        self.dayColumn2.setObjectName(u"dayColumn2")
        self.dayColumn2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.dayColumn2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn2, 1, 1, 1, 1)

        self.day4Label = QLabel(Form)
        self.day4Label.setObjectName(u"day4Label")
        self.day4Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day4Label, 0, 3, 1, 1)

        self.day5Label = QLabel(Form)
        self.day5Label.setObjectName(u"day5Label")
        self.day5Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day5Label, 0, 4, 1, 1)

        self.day2Label = QLabel(Form)
        self.day2Label.setObjectName(u"day2Label")
        self.day2Label.setAlignment(Qt.AlignCenter)

        self.daysContainer.addWidget(self.day2Label, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(1, 800, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.daysContainer.addItem(self.verticalSpacer, 1, 7, 1, 1)

        self.dayColumn4 = QWidget(Form)
        self.dayColumn4.setObjectName(u"dayColumn4")
        self.dayColumn4.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.dayColumn4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.daysContainer.addWidget(self.dayColumn4, 1, 3, 1, 1)


        self.horizontalLayout.addLayout(self.daysContainer)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"scheduleWindow", None))
        self.groupLabel.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.day7Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day3Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day1Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day6Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day4Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day5Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.day2Label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

