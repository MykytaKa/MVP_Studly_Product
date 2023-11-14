# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowstudent.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(69, 119, 108);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menuWidget = QWidget(self.centralwidget)
        self.menuWidget.setObjectName(u"menuWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuWidget.sizePolicy().hasHeightForWidth())
        self.menuWidget.setSizePolicy(sizePolicy)
        self.menuWidget.setStyleSheet(u"height: 20%;")
        self.verticalLayout = QVBoxLayout(self.menuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonsMenu = QHBoxLayout()
        self.buttonsMenu.setSpacing(5)
        self.buttonsMenu.setObjectName(u"buttonsMenu")
        self.buttonsMenu.setContentsMargins(-1, -1, 0, 0)
        self.logoLabel = QLabel(self.menuWidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.buttonsMenu.addWidget(self.logoLabel)

        self.scheduleButton = QPushButton(self.menuWidget)
        self.scheduleButton.setObjectName(u"scheduleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scheduleButton.sizePolicy().hasHeightForWidth())
        self.scheduleButton.setSizePolicy(sizePolicy1)
        self.scheduleButton.setStyleSheet(u"border-style: solid;\n"
"        border-width: 0px;\n"
"        color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.scheduleButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer)

        self.lecturesButton = QPushButton(self.menuWidget)
        self.lecturesButton.setObjectName(u"lecturesButton")
        sizePolicy1.setHeightForWidth(self.lecturesButton.sizePolicy().hasHeightForWidth())
        self.lecturesButton.setSizePolicy(sizePolicy1)
        self.lecturesButton.setStyleSheet(u"border-style: solid;\n"
"        border-width: 0px;\n"
"        color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.lecturesButton)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_2)

        self.teachersButton = QPushButton(self.menuWidget)
        self.teachersButton.setObjectName(u"teachersButton")
        sizePolicy1.setHeightForWidth(self.teachersButton.sizePolicy().hasHeightForWidth())
        self.teachersButton.setSizePolicy(sizePolicy1)
        self.teachersButton.setStyleSheet(u"border-style: solid;\n"
"        border-width: 0px;\n"
"        color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.teachersButton)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_3)

        self.notesButton = QPushButton(self.menuWidget)
        self.notesButton.setObjectName(u"notesButton")
        sizePolicy1.setHeightForWidth(self.notesButton.sizePolicy().hasHeightForWidth())
        self.notesButton.setSizePolicy(sizePolicy1)
        self.notesButton.setStyleSheet(u"border-style: solid;\n"
"        border-width: 0px;\n"
"        color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.notesButton)

        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_5)

        self.profileContainer = QGridLayout()
        self.profileContainer.setObjectName(u"profileContainer")
        self.profileContainer.setVerticalSpacing(0)
        self.profileContainer.setContentsMargins(-1, 0, -1, 0)
        self.userInfoContainer = QVBoxLayout()
        self.userInfoContainer.setObjectName(u"userInfoContainer")
        self.userFullname = QLabel(self.menuWidget)
        self.userFullname.setObjectName(u"userFullname")
        self.userFullname.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.userInfoContainer.addWidget(self.userFullname)

        self.userInfo = QLabel(self.menuWidget)
        self.userInfo.setObjectName(u"userInfo")
        self.userInfo.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.userInfoContainer.addWidget(self.userInfo)


        self.profileContainer.addLayout(self.userInfoContainer, 0, 2, 1, 1)

        self.userIcon = QLabel(self.menuWidget)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.profileContainer.addWidget(self.userIcon, 0, 1, 1, 1)


        self.buttonsMenu.addLayout(self.profileContainer)


        self.verticalLayout.addLayout(self.buttonsMenu)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.menuWidget, 1, 1, 1, 1)

        self.widgetContainer = QVBoxLayout()
        self.widgetContainer.setObjectName(u"widgetContainer")

        self.gridLayout.addLayout(self.widgetContainer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"STUDLY", None))
        self.scheduleButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u043a\u043b\u0430\u0434", None))
        self.lecturesButton.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u043a\u0446\u0456\u0457", None))
        self.teachersButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447\u0456", None))
        self.notesButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0442\u0430\u0442\u043a\u0438", None))
        self.userFullname.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435 \u0406.\u041f.", None))
        self.userInfo.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.userIcon.setText(QCoreApplication.translate("MainWindow", u"ICONA", None))
    # retranslateUi

