# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
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
"border-radius: 20px;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(26)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(32, 69, 71);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLabel)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.nameEdit = QLineEdit(self.widget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setMinimumSize(QSize(0, 30))
        self.nameEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")
        self.nameEdit.setMaxLength(25)

        self.verticalLayout.addWidget(self.nameEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.surnameEdit = QLineEdit(self.widget)
        self.surnameEdit.setObjectName(u"surnameEdit")
        self.surnameEdit.setMinimumSize(QSize(0, 30))
        self.surnameEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")
        self.surnameEdit.setMaxLength(25)

        self.verticalLayout.addWidget(self.surnameEdit)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.patronymicEdit = QLineEdit(self.widget)
        self.patronymicEdit.setObjectName(u"patronymicEdit")
        self.patronymicEdit.setMinimumSize(QSize(0, 30))
        self.patronymicEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.patronymicEdit)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.emailEdit = QLineEdit(self.widget)
        self.emailEdit.setObjectName(u"emailEdit")
        self.emailEdit.setMinimumSize(QSize(0, 30))
        self.emailEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")
        self.emailEdit.setMaxLength(255)

        self.verticalLayout.addWidget(self.emailEdit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.phoneEdit = QLineEdit(self.widget)
        self.phoneEdit.setObjectName(u"phoneEdit")
        self.phoneEdit.setMinimumSize(QSize(0, 30))
        self.phoneEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")
        self.phoneEdit.setMaxLength(13)

        self.verticalLayout.addWidget(self.phoneEdit)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.passwordEdit = QLineEdit(self.widget)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setMinimumSize(QSize(0, 30))
        self.passwordEdit.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")
        self.passwordEdit.setMaxLength(25)
        self.passwordEdit.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.passwordEdit)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(70)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(133, 10, 0, -1)
        self.studentButton = QRadioButton(self.widget)
        self.studentButton.setObjectName(u"studentButton")
        self.studentButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.studentButton)

        self.teacherButton = QRadioButton(self.widget)
        self.teacherButton.setObjectName(u"teacherButton")
        self.teacherButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.teacherButton)


        self.verticalLayout.addLayout(self.formLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.formLayout_2.setContentsMargins(-1, 5, 6, -1)
        self.nextButton = QPushButton(self.widget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(100, 30))
        self.nextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextButton.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nextButton)

        self.returnButton = QPushButton(self.widget)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setMinimumSize(QSize(100, 30))
        self.returnButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnButton.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"background-color: rgba(69, 119, 108, 125);\n"
"border-radius: 10px;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.returnButton)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0454\u0441\u0442\u0440\u0430\u0446\u0456\u044f", None))
        self.errorLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0406\u043c'\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435", None))
        self.surnameEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.studentButton.setText(QCoreApplication.translate("MainWindow", u"\u042f \u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))
        self.teacherButton.setText(QCoreApplication.translate("MainWindow", u"\u042f \u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0456", None))
        self.returnButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

