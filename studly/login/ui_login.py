# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import rc_img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(32, 69, 71);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(150, 150, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 350))
        self.widget.setMaximumSize(QSize(300, 350))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setStyleSheet(u"background-color: rgb(127, 180, 175);\n"
"border-radius: 20px;")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.studlyLabel = QLabel(self.widget)
        self.studlyLabel.setObjectName(u"studlyLabel")
        self.studlyLabel.setMinimumSize(QSize(0, 84))
        font = QFont()
        font.setFamilies([u"Ink Free"])
        font.setPointSize(35)
        font.setBold(False)
        self.studlyLabel.setFont(font)
        self.studlyLabel.setStyleSheet(u"color: rgb(32, 69, 71);")
        self.studlyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.studlyLabel)

        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLabel)

        self.loginLabel = QLabel(self.widget)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.loginLabel.setLineWidth(5)
        self.loginLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.loginLabel.setMargin(5)

        self.verticalLayout.addWidget(self.loginLabel)

        self.loginEdit = QLineEdit(self.widget)
        self.loginEdit.setObjectName(u"loginEdit")
        self.loginEdit.setMinimumSize(QSize(0, 30))
        self.loginEdit.setMaximumSize(QSize(16777215, 16777214))
        self.loginEdit.setMouseTracking(True)
        self.loginEdit.setTabletTracking(False)
        self.loginEdit.setAutoFillBackground(False)
        self.loginEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.loginEdit)

        self.passworrdLabel = QLabel(self.widget)
        self.passworrdLabel.setObjectName(u"passworrdLabel")
        self.passworrdLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.passworrdLabel.setFrameShape(QFrame.NoFrame)
        self.passworrdLabel.setFrameShadow(QFrame.Plain)
        self.passworrdLabel.setLineWidth(5)
        self.passworrdLabel.setMidLineWidth(0)
        self.passworrdLabel.setTextFormat(Qt.AutoText)
        self.passworrdLabel.setScaledContents(False)
        self.passworrdLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.passworrdLabel.setMargin(5)
        self.passworrdLabel.setIndent(-1)
        self.passworrdLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.passworrdLabel)

        self.passwordEdit = QLineEdit(self.widget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setMinimumSize(QSize(0, 30))
        self.passwordEdit.setMaximumSize(QSize(16777215, 16777214))
        self.passwordEdit.setMouseTracking(True)
        self.passwordEdit.setTabletTracking(False)
        self.passwordEdit.setAutoFillBackground(False)
        self.passwordEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 5px;")
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setDragEnabled(False)
        self.passwordEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.verticalLayout.addWidget(self.passwordEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.show = QCheckBox(self.widget)
        self.show.setObjectName(u"show")
        self.show.setCursor(QCursor(Qt.PointingHandCursor))
        self.show.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.show)

        self.rememberUser = QCheckBox(self.widget)
        self.rememberUser.setObjectName(u"rememberUser")
        self.rememberUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.rememberUser.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.rememberUser)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy1)
        self.loginButton.setMinimumSize(QSize(0, 50))
        self.loginButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.loginButton.setFont(font1)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"border-radius: 9px;\n"
"background-color: rgba(69, 119, 108, 125);")
        self.loginButton.setIconSize(QSize(16, 16))

        self.verticalLayout_2.addWidget(self.loginButton)

        self.registrationlLabel = QLabel(self.widget)
        self.registrationlLabel.setObjectName(u"registrationlLabel")
        font2 = QFont()
        font2.setUnderline(True)
        self.registrationlLabel.setFont(font2)
        self.registrationlLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.registrationlLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.registrationlLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.registrationlLabel)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(150, 150, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u0456\u0434", None))
        self.studlyLabel.setText(QCoreApplication.translate("MainWindow", u"Studly", None))
        self.errorLabel.setText("")
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d/Email", None))
        self.loginEdit.setInputMask("")
        self.passworrdLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.passwordEdit.setInputMask("")
        self.show.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u0438", None))
        self.rememberUser.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0430\u043c'\u044f\u0442\u0430\u0442\u0438 \u043c\u0435\u043d\u0435", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0456\u0439\u0442\u0438", None))
        self.registrationlLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043c\u0430\u0454\u0442\u0435 \u0430\u043a\u0430\u0443\u043d\u0442\u0443? \u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0439\u0442\u0435\u0441\u044c.", None))
    # retranslateUi

