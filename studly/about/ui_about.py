# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import rc_img

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QSize(600, 400))
        Dialog.setMaximumSize(QSize(600, 400))
        Dialog.setStyleSheet(u"background-color: rgb(239, 241, 237);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 200, 200))
        self.label.setPixmap(QPixmap(u":/icons/exe_icon.png"))
        self.label.setScaledContents(True)
        self.closeButton = QPushButton(Dialog)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(225, 340, 150, 40))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"background-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 20, 150, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 286, 211, 20))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 20, 250, 130))
        self.label_4.setPixmap(QPixmap(u":/icons/team_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 130, 350, 150))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)
        self.label_4.raise_()
        self.label.raise_()
        self.closeButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.closeButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u0438\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Developed by:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Built in November 2023", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u043a\u0438\u0442\u0430 \u041a\u0430\u043b\u044e\u0436\u043d\u0438\u0439 - Team lead, Front-end\n"
"\u041e\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u0430 \u0410\u0442\u0430\u043c\u0430\u043d\u0435\u043d\u043a\u043e - UI/UX Designer, Front-end\n"
"\u0410\u043d\u0434\u0440\u0456\u0439 \u0428\u0442\u0435\u043f\u0443\u0440\u0430 - Back-end\n"
"\u0410\u043d\u0434\u0440\u0456\u0439 \u0416\u0435\u043c\u0435\u0440\u0435\u043d\u043a\u043e - Back-end\n"
"\u0425\u0430\u0440\u0447\u0435\u043d\u043a\u043e \u041e\u0440\u0438\u043d\u0430 - Data Engineer\n"
"\u0413\u0443\u0440\u0442\u043e\u0432\u0430 \u0421\u0432\u0456\u0442\u043b\u0430\u043d\u0430 - Data Engineer", None))
    # retranslateUi

