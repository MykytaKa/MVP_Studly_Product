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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(252, 212)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(252, 212))
        Form.setMaximumSize(QSize(252, 212))
        font = QFont()
        font.setPointSize(19)
        Form.setFont(font)
        self.nameEdit = QLineEdit(Form)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setGeometry(QRect(10, 10, 231, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.nameEdit.setFont(font1)
        self.nameEdit.setAlignment(Qt.AlignCenter)
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 47, 231, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 98, 231, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.dateTimeEdit = QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(10, 115, 231, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.dateTimeEdit.setFont(font2)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        self.groupEdit = QComboBox(Form)
        self.groupEdit.setObjectName(u"groupEdit")
        self.groupEdit.setGeometry(QRect(10, 62, 231, 41))
        font3 = QFont()
        font3.setPointSize(13)
        self.groupEdit.setFont(font3)
        self.createButton = QPushButton(Form)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(80, 170, 91, 31))
        font4 = QFont()
        font4.setPointSize(11)
        self.createButton.setFont(font4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430 \u0437\u0443\u0441\u0442\u0440\u0456\u0447", None))
        self.nameEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438", None))
    # retranslateUi

