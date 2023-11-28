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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import rc_img

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(875, 580)
        Form.setStyleSheet(u"background-color: rgb(69, 119, 108);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.insideWidget = QWidget(Form)
        self.insideWidget.setObjectName(u"insideWidget")
        self.insideLayout = QGridLayout(self.insideWidget)
        self.insideLayout.setObjectName(u"insideLayout")
        self.descriptionEdit = QTextEdit(self.insideWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.descriptionEdit.setFont(font)
        self.descriptionEdit.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);")

        self.insideLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)

        self.EditingBox = QGroupBox(self.insideWidget)
        self.EditingBox.setObjectName(u"EditingBox")
        self.EditingBox.setMinimumSize(QSize(168, 0))
        self.EditingBox.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);")
        self.gridLayout_2 = QGridLayout(self.EditingBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.EditingBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setStyleSheet(u"border-style: none;")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 180, 495))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameTexAlignment = QFrame(self.scrollAreaWidgetContents)
        self.frameTexAlignment.setObjectName(u"frameTexAlignment")
        self.frameTexAlignment.setStyleSheet(u"")
        self.frameTexAlignment.setFrameShape(QFrame.StyledPanel)
        self.frameTexAlignment.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frameTexAlignment)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.leftAlignmentButton = QPushButton(self.frameTexAlignment)
        self.leftAlignmentButton.setObjectName(u"leftAlignmentButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftAlignmentButton.sizePolicy().hasHeightForWidth())
        self.leftAlignmentButton.setSizePolicy(sizePolicy2)
        self.leftAlignmentButton.setMinimumSize(QSize(125, 45))
        self.leftAlignmentButton.setMaximumSize(QSize(125, 45))
        font1 = QFont()
        font1.setPointSize(16)
        self.leftAlignmentButton.setFont(font1)
        self.leftAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.leftAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 5px;\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 15px;")
        icon = QIcon()
        icon.addFile(u":/icons/left_alignment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.leftAlignmentButton.setIcon(icon)

        self.gridLayout_6.addWidget(self.leftAlignmentButton, 1, 0, 1, 1)

        self.centerAlignmentButton = QPushButton(self.frameTexAlignment)
        self.centerAlignmentButton.setObjectName(u"centerAlignmentButton")
        sizePolicy2.setHeightForWidth(self.centerAlignmentButton.sizePolicy().hasHeightForWidth())
        self.centerAlignmentButton.setSizePolicy(sizePolicy2)
        self.centerAlignmentButton.setMinimumSize(QSize(125, 45))
        self.centerAlignmentButton.setMaximumSize(QSize(125, 45))
        self.centerAlignmentButton.setFont(font1)
        self.centerAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.centerAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 5px;\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 15px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/center_alignment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.centerAlignmentButton.setIcon(icon1)

        self.gridLayout_6.addWidget(self.centerAlignmentButton, 2, 0, 1, 1)

        self.rightAlignmentButton = QPushButton(self.frameTexAlignment)
        self.rightAlignmentButton.setObjectName(u"rightAlignmentButton")
        self.rightAlignmentButton.setMinimumSize(QSize(125, 45))
        self.rightAlignmentButton.setMaximumSize(QSize(125, 45))
        self.rightAlignmentButton.setFont(font1)
        self.rightAlignmentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.rightAlignmentButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"margin-bottom: 5px;\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 15px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/right_alignment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rightAlignmentButton.setIcon(icon2)

        self.gridLayout_6.addWidget(self.rightAlignmentButton, 3, 0, 1, 1)

        self.label = QLabel(self.frameTexAlignment)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-style: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frameTexAlignment, 9, 0, 1, 1)

        self.frameTextSize = QFrame(self.scrollAreaWidgetContents)
        self.frameTextSize.setObjectName(u"frameTextSize")
        self.frameTextSize.setMinimumSize(QSize(180, 0))
        self.frameTextSize.setMaximumSize(QSize(180, 16777215))
        self.frameTextSize.setStyleSheet(u"border-bottom-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 0px;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;")
        self.frameTextSize.setFrameShape(QFrame.StyledPanel)
        self.frameTextSize.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frameTextSize)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.frameTextSize)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-style: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 2)

        self.increaseFontButton = QPushButton(self.frameTextSize)
        self.increaseFontButton.setObjectName(u"increaseFontButton")
        sizePolicy2.setHeightForWidth(self.increaseFontButton.sizePolicy().hasHeightForWidth())
        self.increaseFontButton.setSizePolicy(sizePolicy2)
        self.increaseFontButton.setMinimumSize(QSize(50, 50))
        self.increaseFontButton.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setPointSize(18)
        self.increaseFontButton.setFont(font3)
        self.increaseFontButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.increaseFontButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 15px;")

        self.gridLayout_4.addWidget(self.increaseFontButton, 1, 0, 1, 1)

        self.reduceFontButton = QPushButton(self.frameTextSize)
        self.reduceFontButton.setObjectName(u"reduceFontButton")
        sizePolicy2.setHeightForWidth(self.reduceFontButton.sizePolicy().hasHeightForWidth())
        self.reduceFontButton.setSizePolicy(sizePolicy2)
        self.reduceFontButton.setMinimumSize(QSize(50, 50))
        self.reduceFontButton.setMaximumSize(QSize(50, 50))
        self.reduceFontButton.setFont(font3)
        self.reduceFontButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reduceFontButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 15px;")

        self.gridLayout_4.addWidget(self.reduceFontButton, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frameTextSize, 2, 0, 1, 1)

        self.frameTextFormat = QFrame(self.scrollAreaWidgetContents)
        self.frameTextFormat.setObjectName(u"frameTextFormat")
        self.frameTextFormat.setStyleSheet(u"border-bottom-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 0px;\n"
"")
        self.frameTextFormat.setFrameShape(QFrame.StyledPanel)
        self.frameTextFormat.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frameTextFormat)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(0)
        self.italicButton = QPushButton(self.frameTextFormat)
        self.italicButton.setObjectName(u"italicButton")
        sizePolicy2.setHeightForWidth(self.italicButton.sizePolicy().hasHeightForWidth())
        self.italicButton.setSizePolicy(sizePolicy2)
        self.italicButton.setMinimumSize(QSize(50, 50))
        self.italicButton.setMaximumSize(QSize(50, 50))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setItalic(True)
        self.italicButton.setFont(font4)
        self.italicButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.italicButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"padding-bottom: 5px;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.italicButton, 2, 2, 1, 1)

        self.underlineButton = QPushButton(self.frameTextFormat)
        self.underlineButton.setObjectName(u"underlineButton")
        sizePolicy2.setHeightForWidth(self.underlineButton.sizePolicy().hasHeightForWidth())
        self.underlineButton.setSizePolicy(sizePolicy2)
        self.underlineButton.setMinimumSize(QSize(50, 50))
        self.underlineButton.setMaximumSize(QSize(50, 50))
        font5 = QFont()
        font5.setPointSize(24)
        font5.setUnderline(True)
        self.underlineButton.setFont(font5)
        self.underlineButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.underlineButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"padding-bottom: 5px;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.underlineButton, 1, 3, 1, 1)

        self.strikeoutButton = QPushButton(self.frameTextFormat)
        self.strikeoutButton.setObjectName(u"strikeoutButton")
        self.strikeoutButton.setMinimumSize(QSize(50, 50))
        self.strikeoutButton.setMaximumSize(QSize(50, 50))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setStrikeOut(True)
        self.strikeoutButton.setFont(font6)
        self.strikeoutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.strikeoutButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"padding-bottom: 5px;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.strikeoutButton, 2, 3, 1, 1)

        self.boldButton = QPushButton(self.frameTextFormat)
        self.boldButton.setObjectName(u"boldButton")
        sizePolicy2.setHeightForWidth(self.boldButton.sizePolicy().hasHeightForWidth())
        self.boldButton.setSizePolicy(sizePolicy2)
        self.boldButton.setMinimumSize(QSize(50, 50))
        self.boldButton.setMaximumSize(QSize(50, 50))
        font7 = QFont()
        font7.setPointSize(24)
        font7.setBold(True)
        self.boldButton.setFont(font7)
        self.boldButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.boldButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"padding-bottom: 5px;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.boldButton, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frameTextFormat)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-style: none;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 2)


        self.gridLayout_3.addWidget(self.frameTextFormat, 7, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 1, 4, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 13, 1, 1, 4)


        self.insideLayout.addWidget(self.EditingBox, 1, 3, 1, 1)

        self.UpperLayout = QHBoxLayout()
        self.UpperLayout.setSpacing(6)
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.UpperLayout.setContentsMargins(-1, -1, -1, 6)
        self.returnButton = QPushButton(self.insideWidget)
        self.returnButton.setObjectName(u"returnButton")
        sizePolicy2.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy2)
        self.returnButton.setMinimumSize(QSize(55, 50))
        self.returnButton.setMaximumSize(QSize(55, 50))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setStyleSheet(u"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 10px;")

        self.UpperLayout.addWidget(self.returnButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.UpperLayout.addItem(self.horizontalSpacer_3)

        self.titleEdit = QLineEdit(self.insideWidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setMinimumSize(QSize(0, 50))
        self.titleEdit.setMaximumSize(QSize(16777215, 50))
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        self.titleEdit.setFont(font8)
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
        self.submitButton.setMinimumSize(QSize(92, 50))
        self.submitButton.setMaximumSize(QSize(92, 50))
        self.submitButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.submitButton.setStyleSheet(u"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 10px;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.submitButton.setIcon(icon3)

        self.UpperLayout.addWidget(self.submitButton)

        self.horizontalSpacer_5 = QSpacerItem(1, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.UpperLayout.addItem(self.horizontalSpacer_5)

        self.cancelButton = QPushButton(self.insideWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(92, 50))
        self.cancelButton.setMaximumSize(QSize(92, 50))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon4)

        self.UpperLayout.addWidget(self.cancelButton)


        self.insideLayout.addLayout(self.UpperLayout, 0, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(6, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.insideLayout.addItem(self.verticalSpacer_5, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.insideWidget, 0, 0, 2, 2)

        self.mainWidget = QWidget(Form)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainLayout = QGridLayout(self.mainWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.widget = QWidget(self.mainWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(1000, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.findEdit = QLineEdit(self.widget)
        self.findEdit.setObjectName(u"findEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.findEdit.sizePolicy().hasHeightForWidth())
        self.findEdit.setSizePolicy(sizePolicy4)
        self.findEdit.setMinimumSize(QSize(0, 40))
        self.findEdit.setMaximumSize(QSize(900, 40))
        font9 = QFont()
        font9.setPointSize(11)
        self.findEdit.setFont(font9)
        self.findEdit.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"")
        self.findEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.findEdit)


        self.mainLayout.addWidget(self.widget, 0, 3, 1, 1)

        self.createNoteButton = QPushButton(self.mainWidget)
        self.createNoteButton.setObjectName(u"createNoteButton")
        self.createNoteButton.setMinimumSize(QSize(50, 50))
        self.createNoteButton.setMaximumSize(QSize(50, 50))
        font10 = QFont()
        font10.setPointSize(30)
        self.createNoteButton.setFont(font10)
        self.createNoteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createNoteButton.setStyleSheet(u"background-color: rgb(69, 119, 108);\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"border-radius: 10px;\n"
"padding-bottom: 10px;")

        self.mainLayout.addWidget(self.createNoteButton, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(40, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer, 2, 6, 4, 1)

        self.scrollArea = QScrollArea(self.mainWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"border-style: hidden;")
        self.scrollArea.setWidgetResizable(True)
        self.notesScrollArea = QWidget()
        self.notesScrollArea.setObjectName(u"notesScrollArea")
        self.notesScrollArea.setGeometry(QRect(0, 0, 272, 462))
        self.notesContainer = QVBoxLayout(self.notesScrollArea)
        self.notesContainer.setObjectName(u"notesContainer")
        self.notesContainer.setContentsMargins(0, -1, 0, -1)
        self.verticalSP = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.notesContainer.addItem(self.verticalSP)

        self.scrollArea.setWidget(self.notesScrollArea)

        self.mainLayout.addWidget(self.scrollArea, 2, 1, 4, 5)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.mainLayout.addItem(self.horizontalSpacer_6, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.mainWidget, 0, 9, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(1, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 10, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.descriptionEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.EditingBox.setTitle("")
        self.centerAlignmentButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0438\u0440\u0456\u0432\u043d\u044e\u0432\u0430\u043d\u043d\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0437\u043c\u0456\u0440 \u0442\u0435\u043a\u0441\u0442\u0443", None))
        self.increaseFontButton.setText(QCoreApplication.translate("Form", u"A+", None))
        self.reduceFontButton.setText(QCoreApplication.translate("Form", u"A-", None))
        self.italicButton.setText(QCoreApplication.translate("Form", u"\u041a", None))
        self.underlineButton.setText(QCoreApplication.translate("Form", u"\u041f", None))
        self.strikeoutButton.setText(QCoreApplication.translate("Form", u"\u0410\u0411\u0412", None))
        self.boldButton.setText(QCoreApplication.translate("Form", u"\u0416", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0440\u043c\u0430\u0442\u0443\u0432\u0430\u043d\u043d\u044f\n"
"\u0442\u0435\u043a\u0441\u0442\u0443", None))
        self.returnButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.titleEdit.setText("")
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430 \u043d\u043e\u0442\u0430\u0442\u043a\u0430", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"\u0412\u0456\u0434\u043c\u0438\u043d\u0438\u0442\u0438", None))
        self.findEdit.setText("")
        self.findEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043d\u043e\u0442\u0430\u0442\u043a\u0443 \u0434\u043b\u044f \u043f\u043e\u0448\u0443\u043a\u0443", None))
        self.createNoteButton.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

