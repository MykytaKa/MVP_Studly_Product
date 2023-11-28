# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MembersClass.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 559)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setStyleSheet(u"background-color: rgb(69, 119, 108);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(Form)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy1)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameLayout = QGridLayout(self.mainFrame)
        self.mainFrameLayout.setSpacing(0)
        self.mainFrameLayout.setObjectName(u"mainFrameLayout")
        self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.mainFrameLayout.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.teachersButton = QPushButton(self.mainFrame)
        self.teachersButton.setObjectName(u"teachersButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.teachersButton.sizePolicy().hasHeightForWidth())
        self.teachersButton.setSizePolicy(sizePolicy2)
        self.teachersButton.setMinimumSize(QSize(200, 200))
        self.teachersButton.setMaximumSize(QSize(450, 450))
        self.teachersButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.teachersButton.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 50px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);")

        self.buttonsLayout.addWidget(self.teachersButton)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.studentsButton = QPushButton(self.mainFrame)
        self.studentsButton.setObjectName(u"studentsButton")
        sizePolicy2.setHeightForWidth(self.studentsButton.sizePolicy().hasHeightForWidth())
        self.studentsButton.setSizePolicy(sizePolicy2)
        self.studentsButton.setMinimumSize(QSize(200, 200))
        self.studentsButton.setMaximumSize(QSize(450, 450))
        self.studentsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.studentsButton.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 50px;\n"
"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);")

        self.buttonsLayout.addWidget(self.studentsButton)


        self.mainLayout.addLayout(self.buttonsLayout, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)


        self.mainFrameLayout.addLayout(self.mainLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.mainFrame, 0, 1, 1, 1)

        self.searchFrame = QFrame(Form)
        self.searchFrame.setObjectName(u"searchFrame")
        sizePolicy.setHeightForWidth(self.searchFrame.sizePolicy().hasHeightForWidth())
        self.searchFrame.setSizePolicy(sizePolicy)
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.searchFrame.setLineWidth(0)
        self.loadLayout = QGridLayout(self.searchFrame)
        self.loadLayout.setSpacing(0)
        self.loadLayout.setObjectName(u"loadLayout")
        self.loadLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(1, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.loadLayout.addItem(self.verticalSpacer_2, 2, 0, 2, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.loadLayout.addItem(self.horizontalSpacer_4, 4, 0, 1, 2)

        self.horizontalSpacer_10 = QSpacerItem(1, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.loadLayout.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)

        self.findLoadWidget = QWidget(self.searchFrame)
        self.findLoadWidget.setObjectName(u"findLoadWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.findLoadWidget.sizePolicy().hasHeightForWidth())
        self.findLoadWidget.setSizePolicy(sizePolicy3)
        self.findLoadWidget.setMinimumSize(QSize(0, 40))
        self.findLoadWidget.setMaximumSize(QSize(700, 40))
        self.findLoadLayout = QHBoxLayout(self.findLoadWidget)
        self.findLoadLayout.setSpacing(0)
        self.findLoadLayout.setObjectName(u"findLoadLayout")
        self.findLoadLayout.setContentsMargins(0, 0, 0, 0)
        self.returnButton = QPushButton(self.findLoadWidget)
        self.returnButton.setObjectName(u"returnButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.returnButton.sizePolicy().hasHeightForWidth())
        self.returnButton.setSizePolicy(sizePolicy4)
        self.returnButton.setMinimumSize(QSize(130, 40))
        self.returnButton.setMaximumSize(QSize(130, 40))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")

        self.findLoadLayout.addWidget(self.returnButton)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.findLoadLayout.addItem(self.horizontalSpacer_8)

        self.findLoadEdit = QLineEdit(self.findLoadWidget)
        self.findLoadEdit.setObjectName(u"findLoadEdit")
        sizePolicy3.setHeightForWidth(self.findLoadEdit.sizePolicy().hasHeightForWidth())
        self.findLoadEdit.setSizePolicy(sizePolicy3)
        self.findLoadEdit.setMinimumSize(QSize(0, 40))
        self.findLoadEdit.setMaximumSize(QSize(600, 40))
        font = QFont()
        font.setPointSize(12)
        self.findLoadEdit.setFont(font)
        self.findLoadEdit.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"color: rgb(32, 69, 71);\n"
"padding-left: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"")

        self.findLoadLayout.addWidget(self.findLoadEdit)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.findLoadLayout.addItem(self.horizontalSpacer_2)

        self.findLoadButton = QPushButton(self.findLoadWidget)
        self.findLoadButton.setObjectName(u"findLoadButton")
        self.findLoadButton.setMinimumSize(QSize(60, 40))
        self.findLoadButton.setMaximumSize(QSize(60, 40))
        self.findLoadButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.findLoadButton.setStyleSheet(u"color: rgb(239, 241, 237);\n"
"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 2px;\n"
"border-radius: 10px;")

        self.findLoadLayout.addWidget(self.findLoadButton)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.findLoadLayout.addItem(self.horizontalSpacer_7)

        self.clearButton = QPushButton(self.findLoadWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMinimumSize(QSize(60, 40))
        self.clearButton.setMaximumSize(QSize(60, 40))
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearButton.setStyleSheet(u"color: rgb(239, 241, 237);\n"
"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 2px;\n"
"border-radius: 10px;")

        self.findLoadLayout.addWidget(self.clearButton)


        self.loadLayout.addWidget(self.findLoadWidget, 0, 2, 1, 1)

        self.scrollArea = QScrollArea(self.searchFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(720, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"border-style: none;")
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.usersWidget = QWidget()
        self.usersWidget.setObjectName(u"usersWidget")
        self.usersWidget.setGeometry(QRect(0, 0, 720, 497))
        sizePolicy.setHeightForWidth(self.usersWidget.sizePolicy().hasHeightForWidth())
        self.usersWidget.setSizePolicy(sizePolicy)
        self.usersWidget.setMinimumSize(QSize(0, 0))
        self.usersWidget.setMaximumSize(QSize(16777215, 16777215))
        self.usersLayout = QVBoxLayout(self.usersWidget)
        self.usersLayout.setSpacing(0)
        self.usersLayout.setObjectName(u"usersLayout")
        self.usersLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.usersLayout.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.usersWidget)

        self.loadLayout.addWidget(self.scrollArea, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.loadLayout.addItem(self.horizontalSpacer_5, 4, 3, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.loadLayout.addItem(self.horizontalSpacer_9, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.searchFrame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.teachersButton.setText("")
        self.studentsButton.setText("")
        self.returnButton.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u043b\u043e\u0432\u043d\u0430 \u0441\u0442\u043e\u0440\u0456\u043d\u043a\u0430", None))
        self.findLoadEdit.setText("")
        self.findLoadEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u041f\u0406\u0411 \u043a\u043e\u0440\u0438\u0441\u0442\u0443\u0432\u0430\u0447\u0430", None))
        self.findLoadButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u0438", None))
    # retranslateUi

