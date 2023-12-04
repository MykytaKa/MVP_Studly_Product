# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stud_registration.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import rc_img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/student.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(32, 69, 71);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, 30, 100, 30)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(500, 500))
        self.widget.setMaximumSize(QSize(500, 500))
        self.widget.setStyleSheet(u"background-color: rgb(127, 180, 175);\n"
"border-radius: 20px;\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(32, 69, 71);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.instituteBox = QComboBox(self.widget)
        self.instituteBox.setObjectName(u"instituteBox")
        self.instituteBox.setMinimumSize(QSize(0, 30))
        self.instituteBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.instituteBox.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.instituteBox)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QComboBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 30))
        self.groupBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(220, 210, -1, -1)
        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(100, 30))
        self.registerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.registerButton.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.registerButton)

        self.returnButton = QPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setMinimumSize(QSize(100, 30))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setLayoutDirection(Qt.LeftToRight)
        self.returnButton.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.returnButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0406\u043d\u0441\u0442\u0438\u0442\u0443\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f", None))
        self.returnButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

