# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NotesClass.ui'
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
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(875, 580)
        Form.setStyleSheet(u"background-color: rgb(69, 119, 108);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(1, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 10, 1, 1)

        self.mainWidget = QWidget(Form)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QGridLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.verticalSpacer = QSpacerItem(1, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer, 3, 5, 4, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.mainWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"border-style: hidden;")
        self.scrollArea.setWidgetResizable(True)
        self.notesScrollArea = QWidget()
        self.notesScrollArea.setObjectName(u"notesScrollArea")
        self.notesScrollArea.setGeometry(QRect(0, 0, 351, 462))
        self.notesContainer = QVBoxLayout(self.notesScrollArea)
        self.notesContainer.setObjectName(u"notesContainer")
        self.notesContainer.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.notesContainer.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.notesScrollArea)

        self.mainLayout.addWidget(self.scrollArea, 3, 0, 4, 5)

        self.createNoteButton = QPushButton(self.mainWidget)
        self.createNoteButton.setObjectName(u"createNoteButton")
        self.createNoteButton.setMinimumSize(QSize(50, 50))
        self.createNoteButton.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setPointSize(30)
        self.createNoteButton.setFont(font)
        self.createNoteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createNoteButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 10px;\n"
"padding-bottom: 10px;")

        self.mainLayout.addWidget(self.createNoteButton, 1, 4, 1, 1)

        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(856, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.findEdit = QLineEdit(self.widget)
        self.findEdit.setObjectName(u"findEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.findEdit.sizePolicy().hasHeightForWidth())
        self.findEdit.setSizePolicy(sizePolicy2)
        self.findEdit.setMinimumSize(QSize(0, 40))
        self.findEdit.setMaximumSize(QSize(800, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.findEdit.setFont(font1)
        self.findEdit.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"")
        self.findEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.findEdit)


        self.mainLayout.addWidget(self.widget, 1, 2, 1, 1)

        self.menuButtonOutside = QPushButton(self.mainWidget)
        self.menuButtonOutside.setObjectName(u"menuButtonOutside")
        self.menuButtonOutside.setMinimumSize(QSize(50, 50))
        self.menuButtonOutside.setMaximumSize(QSize(50, 50))
        self.menuButtonOutside.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuButtonOutside.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 10px;")

        self.mainLayout.addWidget(self.menuButtonOutside, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 5)


        self.gridLayout.addWidget(self.mainWidget, 0, 9, 2, 1)

        self.insideWidget = QWidget(Form)
        self.insideWidget.setObjectName(u"insideWidget")
        self.insideLayout = QGridLayout(self.insideWidget)
        self.insideLayout.setObjectName(u"insideLayout")
        self.EditingBox = QGroupBox(self.insideWidget)
        self.EditingBox.setObjectName(u"EditingBox")
        self.EditingBox.setMinimumSize(QSize(168, 0))
        self.EditingBox.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 15px;")
        self.gridLayout_2 = QGridLayout(self.EditingBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 13, 2, 1, 3)

        self.scrollArea_2 = QScrollArea(self.EditingBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 152, 530))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 2)

        self.increaseFontButton = QPushButton(self.scrollAreaWidgetContents)
        self.increaseFontButton.setObjectName(u"increaseFontButton")
        self.increaseFontButton.setMinimumSize(QSize(60, 60))
        self.increaseFontButton.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setPointSize(18)
        self.increaseFontButton.setFont(font3)
        self.increaseFontButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.increaseFontButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.increaseFontButton, 1, 0, 1, 1)

        self.reduceFontButton = QPushButton(self.scrollAreaWidgetContents)
        self.reduceFontButton.setObjectName(u"reduceFontButton")
        self.reduceFontButton.setMinimumSize(QSize(60, 60))
        self.reduceFontButton.setMaximumSize(QSize(60, 60))
        self.reduceFontButton.setFont(font3)
        self.reduceFontButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reduceFontButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.reduceFontButton, 1, 1, 1, 1)

        self.leftAlignmentButton = QPushButton(self.scrollAreaWidgetContents)
        self.leftAlignmentButton.setObjectName(u"leftAlignmentButton")
        self.leftAlignmentButton.setMinimumSize(QSize(125, 60))
        self.leftAlignmentButton.setMaximumSize(QSize(125, 60))
        font4 = QFont()
        font4.setPointSize(16)
        self.leftAlignmentButton.setFont(font4)
        self.leftAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.leftAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 10px;\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.leftAlignmentButton, 10, 0, 1, 2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 3)

        self.rightAlignmentButton = QPushButton(self.scrollAreaWidgetContents)
        self.rightAlignmentButton.setObjectName(u"rightAlignmentButton")
        self.rightAlignmentButton.setMinimumSize(QSize(125, 60))
        self.rightAlignmentButton.setMaximumSize(QSize(125, 60))
        self.rightAlignmentButton.setFont(font4)
        self.rightAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rightAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 10px;\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.rightAlignmentButton, 12, 0, 1, 2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 2)

        self.boldButton = QPushButton(self.scrollAreaWidgetContents)
        self.boldButton.setObjectName(u"boldButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy3)
        self.boldButton.setMinimumSize(QSize(60, 60))
        self.boldButton.setMaximumSize(QSize(60, 60))
        font5 = QFont()
        font5.setPointSize(28)
        font5.setBold(True)
        self.boldButton.setFont(font5)
        self.boldButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.boldButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.boldButton, 6, 0, 1, 1)

        self.centerAlignmentButton = QPushButton(self.scrollAreaWidgetContents)
        self.centerAlignmentButton.setObjectName(u"centerAlignmentButton")
        self.centerAlignmentButton.setMinimumSize(QSize(125, 60))
        self.centerAlignmentButton.setMaximumSize(QSize(125, 60))
        self.centerAlignmentButton.setFont(font4)
        self.centerAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.centerAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 10px;\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.centerAlignmentButton, 11, 0, 1, 2)

        self.underlineButton = QPushButton(self.scrollAreaWidgetContents)
        self.underlineButton.setObjectName(u"underlineButton")
        sizePolicy3.setHeightForWidth(self.underlineButton.sizePolicy().hasHeightForWidth())
        self.underlineButton.setSizePolicy(sizePolicy3)
        self.underlineButton.setMinimumSize(QSize(60, 60))
        self.underlineButton.setMaximumSize(QSize(60, 60))
        font6 = QFont()
        font6.setPointSize(28)
        font6.setUnderline(True)
        self.underlineButton.setFont(font6)
        self.underlineButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.underlineButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.underlineButton, 6, 1, 1, 1)

        self.italicButton = QPushButton(self.scrollAreaWidgetContents)
        self.italicButton.setObjectName(u"italicButton")
        sizePolicy3.setHeightForWidth(self.italicButton.sizePolicy().hasHeightForWidth())
        self.italicButton.setSizePolicy(sizePolicy3)
        self.italicButton.setMinimumSize(QSize(60, 60))
        self.italicButton.setMaximumSize(QSize(60, 60))
        font7 = QFont()
        font7.setPointSize(28)
        font7.setItalic(True)
        self.italicButton.setFont(font7)
        self.italicButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.italicButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.gridLayout_3.addWidget(self.italicButton, 7, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 1, 4, 4)


        self.insideLayout.addWidget(self.EditingBox, 1, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(6, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.insideLayout.addItem(self.verticalSpacer_5, 1, 2, 1, 1)

        self.UpperLayout = QHBoxLayout()
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.UpperLayout.setContentsMargins(-1, -1, -1, 6)
        self.returnButton = QPushButton(self.insideWidget)
        self.returnButton.setObjectName(u"returnButton")
        sizePolicy3.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy3)
        self.returnButton.setMinimumSize(QSize(55, 0))
        self.returnButton.setMaximumSize(QSize(55, 40))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 10px;")

        self.UpperLayout.addWidget(self.returnButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.UpperLayout.addItem(self.horizontalSpacer_3)

        self.titleEdit = QLineEdit(self.insideWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setFont(font2)
        self.titleEdit.setAutoFillBackground(False)
        self.titleEdit.setStyleSheet(u"alternate-background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(69, 119, 108);\n"
"color: rgb(239, 241, 237);")
        self.titleEdit.setAlignment(Qt.AlignCenter)

        self.UpperLayout.addWidget(self.titleEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.UpperLayout.addItem(self.horizontalSpacer_4)

        self.submitButton = QPushButton(self.insideWidget)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setMinimumSize(QSize(65, 40))
        self.submitButton.setMaximumSize(QSize(65, 40))
        self.submitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 10px;")

        self.UpperLayout.addWidget(self.submitButton)

        self.cancelButton = QPushButton(self.insideWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(75, 40))
        self.cancelButton.setMaximumSize(QSize(75, 40))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237); \n"
"border-radius: 10px;")

        self.UpperLayout.addWidget(self.cancelButton)


        self.insideLayout.addLayout(self.UpperLayout, 0, 0, 1, 4)

        self.descriptionEdit = QTextEdit(self.insideWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        font8 = QFont()
        font8.setPointSize(10)
        self.descriptionEdit.setFont(font8)
        self.descriptionEdit.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 15px;")

        self.insideLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.insideWidget, 0, 0, 2, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.createNoteButton.setText(QCoreApplication.translate("Form", u"+", None))
        self.findEdit.setText("")
        self.findEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043d\u043e\u0442\u0430\u0442\u043a\u0443", None))
        self.menuButtonOutside.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u043d\u044e", None))
        self.EditingBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0440\u0456\u0432\u043d\u044e\u0432\u0430\u043d\u043d\u044f", None))
        self.increaseFontButton.setText(QCoreApplication.translate("Form", u"A+", None))
        self.reduceFontButton.setText(QCoreApplication.translate("Form", u"A-", None))
        self.leftAlignmentButton.setText(QCoreApplication.translate("Form", u"\u041b\u0456\u0432\u043e\u0440\u0443\u0447", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0437\u043c\u0456\u0440 \u0442\u0435\u043a\u0441\u0442\u0443", None))
        self.rightAlignmentButton.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e\u0440\u0443\u0447", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0443\u0432\u0430\u043d\u043d\u044f\n"
"\u0442\u0435\u043a\u0441\u0442\u0443", None))
        self.boldButton.setText(QCoreApplication.translate("Form", u"B", None))
        self.centerAlignmentButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443", None))
        self.underlineButton.setText(QCoreApplication.translate("Form", u"U", None))
        self.italicButton.setText(QCoreApplication.translate("Form", u"I", None))
        self.returnButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430 \u043d\u043e\u0442\u0430\u0442\u043a\u0430", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"\u0412\u0456\u0434\u043c\u0438\u043d\u0438\u0442\u0438", None))
        self.descriptionEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

