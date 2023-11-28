# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowteacher.ui'
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
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color: rgb(69, 119, 108);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widgetContainer = QVBoxLayout()
        self.widgetContainer.setObjectName(u"widgetContainer")

        self.gridLayout.addLayout(self.widgetContainer, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.menuWidget = QWidget(self.centralwidget)
        self.menuWidget.setObjectName(u"menuWidget")
        self.verticalLayout = QVBoxLayout(self.menuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonsMenuWidget = QWidget(self.menuWidget)
        self.buttonsMenuWidget.setObjectName(u"buttonsMenuWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsMenuWidget.sizePolicy().hasHeightForWidth())
        self.buttonsMenuWidget.setSizePolicy(sizePolicy)
        self.buttonsMenuWidget.setMinimumSize(QSize(0, 70))
        self.buttonsMenuWidget.setMaximumSize(QSize(16777215, 70))
        self.buttonsMenu = QHBoxLayout(self.buttonsMenuWidget)
        self.buttonsMenu.setObjectName(u"buttonsMenu")
        self.logoLabel = QLabel(self.buttonsMenuWidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.buttonsMenu.addWidget(self.logoLabel)

        self.horizontalSpacer_5 = QSpacerItem(110, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_5)

        self.scheduleButton = QPushButton(self.buttonsMenuWidget)
        self.scheduleButton.setObjectName(u"scheduleButton")
        self.scheduleButton.setMinimumSize(QSize(120, 40))
        self.scheduleButton.setMaximumSize(QSize(500, 40))
        font = QFont()
        font.setPointSize(12)
        self.scheduleButton.setFont(font)
        self.scheduleButton.setStyleSheet(u"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.scheduleButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer)

        self.lecturesButton = QPushButton(self.buttonsMenuWidget)
        self.lecturesButton.setObjectName(u"lecturesButton")
        self.lecturesButton.setMinimumSize(QSize(120, 40))
        self.lecturesButton.setMaximumSize(QSize(500, 40))
        self.lecturesButton.setFont(font)
        self.lecturesButton.setStyleSheet(u"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.lecturesButton)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_2)

        self.membersButton = QPushButton(self.buttonsMenuWidget)
        self.membersButton.setObjectName(u"membersButton")
        self.membersButton.setMinimumSize(QSize(120, 40))
        self.membersButton.setMaximumSize(QSize(500, 40))
        self.membersButton.setFont(font)
        self.membersButton.setStyleSheet(u"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.membersButton)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_3)

        self.notesButton = QPushButton(self.buttonsMenuWidget)
        self.notesButton.setObjectName(u"notesButton")
        self.notesButton.setMinimumSize(QSize(120, 40))
        self.notesButton.setMaximumSize(QSize(500, 40))
        self.notesButton.setFont(font)
        self.notesButton.setStyleSheet(u"border-style: solid;\n"
"border-color: rgb(32, 69, 71);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"background-color: rgb(55, 95, 86);\n"
"color: rgb(239, 241, 237);")

        self.buttonsMenu.addWidget(self.notesButton)

        self.horizontalSpacer_6 = QSpacerItem(110, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.buttonsMenu.addItem(self.horizontalSpacer_6)

        self.profileContainer = QGridLayout()
        self.profileContainer.setObjectName(u"profileContainer")
        self.profileContainer.setHorizontalSpacing(6)
        self.userInfoContainer = QVBoxLayout()
        self.userInfoContainer.setSpacing(0)
        self.userInfoContainer.setObjectName(u"userInfoContainer")
        self.userFullname = QLabel(self.buttonsMenuWidget)
        self.userFullname.setObjectName(u"userFullname")

        self.userInfoContainer.addWidget(self.userFullname)

        self.userInfo = QLabel(self.buttonsMenuWidget)
        self.userInfo.setObjectName(u"userInfo")

        self.userInfoContainer.addWidget(self.userInfo)


        self.profileContainer.addLayout(self.userInfoContainer, 0, 2, 1, 1)

        self.userIcon = QLabel(self.buttonsMenuWidget)
        self.userIcon.setObjectName(u"userIcon")
        self.userIcon.setMinimumSize(QSize(60, 60))
        self.userIcon.setMaximumSize(QSize(60, 60))
        self.userIcon.setStyleSheet(u"border-style: solid;\n"
"border-width: 5px;\n"
"border-color: rgb(32, 69, 71);\n"
"border-radius: 30%;")

        self.profileContainer.addWidget(self.userIcon, 0, 1, 1, 1)


        self.buttonsMenu.addLayout(self.profileContainer)


        self.verticalLayout.addWidget(self.buttonsMenuWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.menuWidget, 1, 0, 1, 1)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"STUDLY", None))
        self.scheduleButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u041e\u0417\u041a\u041b\u0410\u0414", None))
        self.lecturesButton.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0415\u041a\u0426\u0406\u0407", None))
        self.membersButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0427\u0410\u0421\u041d\u0418\u041a\u0418", None))
        self.notesButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u041e\u0422\u0410\u0422\u041a\u0418", None))
        self.userFullname.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435 \u0406.\u041f.", None))
        self.userInfo.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.userIcon.setText("")
    # retranslateUi

