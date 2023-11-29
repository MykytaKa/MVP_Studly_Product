# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meetCreator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import rc_img

class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        if not MyDialog.objectName():
            MyDialog.setObjectName(u"MyDialog")
        MyDialog.resize(600, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MyDialog.sizePolicy().hasHeightForWidth())
        MyDialog.setSizePolicy(sizePolicy)
        MyDialog.setMinimumSize(QSize(600, 350))
        MyDialog.setMaximumSize(QSize(600, 350))
        font = QFont()
        font.setPointSize(19)
        MyDialog.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/newMeet.png", QSize(), QIcon.Normal, QIcon.Off)
        MyDialog.setWindowIcon(icon)
        MyDialog.setStyleSheet(u"background-color: rgb(239, 241, 237);")
        self.nameEdit = QLineEdit(MyDialog)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(40, 70, 230, 40))
        font1 = QFont()
        font1.setPointSize(15)
        self.nameEdit.setFont(font1)
        self.nameEdit.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")
        self.nameEdit.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit = QDateTimeEdit(MyDialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(40, 180, 230, 41))
        self.dateTimeEdit.setFont(font1)
        self.dateTimeEdit.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.groupEdit = QComboBox(MyDialog)
        self.groupEdit.setObjectName(u"groupEdit")
        self.groupEdit.setGeometry(QRect(330, 70, 230, 40))
        self.groupEdit.setFont(font1)
        self.groupEdit.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupEdit.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"align: center;\n"
"align-items: center;\n"
"justify-content: center;\n"
"justify-items: center;\n"
"text-align: center;\n"
"display: flex;")
        self.groupEdit.setEditable(False)
        self.groupEdit.setMaxVisibleItems(2)
        self.createButton = QPushButton(MyDialog)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(180, 270, 230, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(False)
        self.createButton.setFont(font2)
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"background-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);")
        self.label = QLabel(MyDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 230, 30))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(MyDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 30, 230, 30))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(MyDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 130, 230, 30))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(MyDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 120, 230, 51))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.duration = QSpinBox(MyDialog)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(330, 180, 230, 41))
        self.duration.setStyleSheet(u"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;")
        self.duration.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.duration.setMinimum(1)
        self.duration.setMaximum(1440)
        self.duration.setSingleStep(10)
        self.duration.setValue(1)
        self.errorLabel = QLabel(MyDialog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(160, 225, 271, 41))
        font3 = QFont()
        font3.setPointSize(9)
        self.errorLabel.setFont(font3)
        self.errorLabel.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(MyDialog)

        QMetaObject.connectSlotsByName(MyDialog)
    # setupUi

    def retranslateUi(self, MyDialog):
        MyDialog.setWindowTitle(QCoreApplication.translate("MyDialog", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0437\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.nameEdit.setText(QCoreApplication.translate("MyDialog", u"\u041d\u043e\u0432\u0430 \u0437\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.nameEdit.setPlaceholderText("")
        self.createButton.setText(QCoreApplication.translate("MyDialog", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MyDialog", u"\u041d\u0430\u0437\u0432\u0430 \u0437\u0443\u0441\u0442\u0440\u0456\u0447\u0456", None))
        self.label_2.setText(QCoreApplication.translate("MyDialog", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MyDialog", u"\u0414\u0430\u0442\u0430 \u0442\u0430 \u0447\u0430\u0441", None))
        self.label_4.setText(QCoreApplication.translate("MyDialog", u"\u0422\u0440\u0438\u0432\u0430\u043b\u0456\u0441\u0442\u044c \u0437\u0443\u0441\u0442\u0440\u0456\u0447\u0456\n"
"(\u0443 \u0445\u0432\u0438\u043b\u0438\u043d\u0430\u0445)", None))
        self.duration.setSuffix("")
        self.duration.setPrefix("")
        self.errorLabel.setText("")
    # retranslateUi

