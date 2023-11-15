# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meetCreator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        if not MyDialog.objectName():
            MyDialog.setObjectName(u"MyDialog")
        MyDialog.resize(583, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MyDialog.sizePolicy().hasHeightForWidth())
        MyDialog.setSizePolicy(sizePolicy)
        MyDialog.setMinimumSize(QSize(583, 350))
        MyDialog.setMaximumSize(QSize(583, 350))
        font = QFont()
        font.setPointSize(19)
        MyDialog.setFont(font)
        MyDialog.setStyleSheet(u"background-color: rgb(239, 241, 237);")
        self.nameEdit = QLineEdit(MyDialog)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(40, 60, 231, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.nameEdit.setFont(font1)
        self.nameEdit.setStyleSheet(u"border-radius: 10px;\n"
"                                          border-style: solid;\n"
"                                          border-color: rgb(69, 119, 108);\n"
"                                          border-width: 2px;")
        self.nameEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit = QDateTimeEdit(MyDialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(40, 170, 231, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.dateTimeEdit.setFont(font2)
        self.dateTimeEdit.setStyleSheet(u"border-top-left-radius: 10px;\n"
"                                              border-bottom-left-radius: 10px;\n"
"                                              border-style: solid;\n"
"                                              border-color: rgb(69, 119, 108);\n"
"                                              border-width: 2px;")
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.groupEdit = QComboBox(MyDialog)
        self.groupEdit.setObjectName(u"groupEdit")
        self.groupEdit.setGeometry(QRect(320, 60, 231, 41))
        font3 = QFont()
        font3.setPointSize(13)
        self.groupEdit.setFont(font3)
        self.groupEdit.setStyleSheet(u"border-top-left-radius: 10px;\n"
"                                           border-bottom-left-radius: 10px;\n"
"                                           border-style: solid;\n"
"                                           border-color: rgb(69, 119, 108);\n"
"                                           border-width: 2px;")
        self.createButton = QPushButton(MyDialog)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(360, 260, 151, 61))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setUnderline(False)
        self.createButton.setFont(font4)
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.setStyleSheet(u"border-radius: 10px;\n"
"                                              border-style: solid;\n"
"                                              border-color: rgb(69, 119, 108);\n"
"                                              border-width: 2px;")
        self.frequency = QComboBox(MyDialog)
        self.frequency.setObjectName(u"frequency")
        self.frequency.setGeometry(QRect(320, 170, 231, 41))
        self.frequency.setStyleSheet(u"border-top-left-radius: 10px;\n"
"                                           border-bottom-left-radius: 10px;\n"
"                                           border-style: solid;\n"
"                                           border-color: rgb(69, 119, 108);\n"
"                                           border-width: 2px;")
        self.label = QLabel(MyDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 27, 231, 31))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(MyDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 27, 231, 31))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(MyDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 130, 231, 31))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.duration = QLineEdit(MyDialog)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(40, 280, 231, 41))
        self.duration.setFont(font1)
        self.duration.setStyleSheet(u"border-radius: 10px;\n"
"                                          border-style: solid;\n"
"                                          border-color: rgb(69, 119, 108);\n"
"                                          border-width: 2px;")
        self.duration.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(MyDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 240, 231, 31))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(MyDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 130, 231, 31))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(MyDialog)

        QMetaObject.connectSlotsByName(MyDialog)
    # setupUi

    def retranslateUi(self, MyDialog):
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("MyDialog", u"\u041d\u0430\u0437\u0432\u0430 \u0437\u0443\u0441\u0442\u0440\u0456\u0447\u0456", None))
        self.createButton.setText(QCoreApplication.translate("MyDialog", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MyDialog", u"\u041d\u0430\u0437\u0432\u0430 \u0437\u0443\u0441\u0442\u0440\u0456\u0447\u0456", None))
        self.label_2.setText(QCoreApplication.translate("MyDialog", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MyDialog", u"\u0414\u0430\u0442\u0430 \u0442\u0430 \u0447\u0430\u0441", None))
        self.duration.setPlaceholderText(QCoreApplication.translate("MyDialog", u"\u0427\u0430\u0441 \u0443 \u0445\u0432\u0438\u043b\u0438\u043d\u0430\u0445", None))
        self.label_4.setText(QCoreApplication.translate("MyDialog", u"\u0422\u0440\u0438\u0432\u0430\u043b\u0456\u0441\u0442\u044c \u0437\u0443\u0441\u0442\u0440\u0456\u0447\u0456", None))
        self.label_5.setText(QCoreApplication.translate("MyDialog", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u043d\u044f", None))
        pass
    # retranslateUi

