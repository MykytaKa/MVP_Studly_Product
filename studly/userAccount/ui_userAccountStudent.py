# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userAccountStudent.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import rc_img

class Ui_UserAccountStudent(object):
    def setupUi(self, UserAccountStudent):
        if not UserAccountStudent.objectName():
            UserAccountStudent.setObjectName(u"UserAccountStudent")
        UserAccountStudent.resize(737, 454)
        UserAccountStudent.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 10px;")
        self.verticalLayout_4 = QVBoxLayout(UserAccountStudent)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(UserAccountStudent)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(239, 241, 237);\n"
"border-radius: 10px;")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.lastName = QLabel(self.widget)
        self.lastName.setObjectName(u"lastName")
        font = QFont()
        font.setPointSize(15)
        self.lastName.setFont(font)
        self.lastName.setAlignment(Qt.AlignCenter)
        self.lastName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.lastName)

        self.firstName = QLabel(self.widget)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setFont(font)
        self.firstName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.firstName)

        self.patronymic = QLabel(self.widget)
        self.patronymic.setObjectName(u"patronymic")
        self.patronymic.setFont(font)
        self.patronymic.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.patronymic)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.group = QLabel(self.widget)
        self.group.setObjectName(u"group")
        self.group.setAlignment(Qt.AlignCenter)
        self.group.setMargin(5)
        self.group.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_11.addWidget(self.group, 1, 1, 1, 1)

        self.institute = QLabel(self.widget)
        self.institute.setObjectName(u"institute")
        self.institute.setAlignment(Qt.AlignCenter)
        self.institute.setMargin(5)
        self.institute.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_11.addWidget(self.institute, 1, 0, 1, 1)

        self.instituteImg = QLabel(self.widget)
        self.instituteImg.setObjectName(u"instituteImg")
        self.instituteImg.setMinimumSize(QSize(0, 80))
        self.instituteImg.setMaximumSize(QSize(16777215, 80))
        self.instituteImg.setStyleSheet(u"image: url(:/icons/univeristy.png);")
        self.instituteImg.setScaledContents(False)
        self.instituteImg.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.instituteImg, 0, 0, 1, 1)

        self.groupImg = QLabel(self.widget)
        self.groupImg.setObjectName(u"groupImg")
        self.groupImg.setMinimumSize(QSize(0, 80))
        self.groupImg.setMaximumSize(QSize(16777215, 80))
        self.groupImg.setAutoFillBackground(False)
        self.groupImg.setStyleSheet(u"image: url(:/icons/group.png);")
        self.groupImg.setScaledContents(False)

        self.gridLayout_11.addWidget(self.groupImg, 0, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 393, 130))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.description = QLabel(self.scrollAreaWidgetContents)
        self.description.setObjectName(u"description")
        self.description.setAlignment(Qt.AlignCenter)
        self.description.setWordWrap(True)
        self.description.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_7.addWidget(self.description)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.email = QLabel(self.widget)
        self.email.setObjectName(u"email")
        font1 = QFont()
        font1.setPointSize(8)
        self.email.setFont(font1)
        self.email.setAlignment(Qt.AlignCenter)
        self.email.setMargin(5)
        self.email.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.email, 1, 1, 1, 1)

        self.emailLabel = QLabel(self.widget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setMinimumSize(QSize(0, 50))
        self.emailLabel.setMaximumSize(QSize(16777215, 50))
        self.emailLabel.setStyleSheet(u"image: url(:/icons/mail.png);")
        self.emailLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.emailLabel, 0, 1, 1, 1)

        self.phone = QLabel(self.widget)
        self.phone.setObjectName(u"phone")
        self.phone.setFont(font1)
        self.phone.setAlignment(Qt.AlignCenter)
        self.phone.setMargin(5)
        self.phone.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_5.addWidget(self.phone, 1, 0, 1, 1)

        self.phoneLabel = QLabel(self.widget)
        self.phoneLabel.setObjectName(u"phoneLabel")
        self.phoneLabel.setMinimumSize(QSize(0, 50))
        self.phoneLabel.setMaximumSize(QSize(16777215, 50))
        self.phoneLabel.setStyleSheet(u"image: url(:/icons/telephone.png);")
        self.phoneLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.phoneLabel, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_6.addLayout(self.gridLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.photoLabel = QLabel(self.widget)
        self.photoLabel.setObjectName(u"photoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoLabel.sizePolicy().hasHeightForWidth())
        self.photoLabel.setSizePolicy(sizePolicy)
        self.photoLabel.setMinimumSize(QSize(200, 200))
        self.photoLabel.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(69, 119, 108);\n"
"border-radius: 100%;\n"
"background-color: rgb(127, 180, 175);")
        self.photoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.photoLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.choosePhoto = QPushButton(self.widget)
        self.choosePhoto.setObjectName(u"choosePhoto")
        sizePolicy.setHeightForWidth(self.choosePhoto.sizePolicy().hasHeightForWidth())
        self.choosePhoto.setSizePolicy(sizePolicy)
        self.choosePhoto.setMinimumSize(QSize(200, 30))
        self.choosePhoto.setCursor(QCursor(Qt.PointingHandCursor))
        self.choosePhoto.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"background-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"text-align: left; padding-left: 10px;")
        icon = QIcon()
        icon.addFile(u":/icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.choosePhoto.setIcon(icon)

        self.verticalLayout.addWidget(self.choosePhoto)

        self.editAcc = QPushButton(self.widget)
        self.editAcc.setObjectName(u"editAcc")
        sizePolicy.setHeightForWidth(self.editAcc.sizePolicy().hasHeightForWidth())
        self.editAcc.setSizePolicy(sizePolicy)
        self.editAcc.setMinimumSize(QSize(200, 30))
        self.editAcc.setCursor(QCursor(Qt.PointingHandCursor))
        self.editAcc.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"background-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"text-align: left; padding-left: 10px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editAcc.setIcon(icon1)

        self.verticalLayout.addWidget(self.editAcc)

        self.logout = QPushButton(self.widget)
        self.logout.setObjectName(u"logout")
        sizePolicy.setHeightForWidth(self.logout.sizePolicy().hasHeightForWidth())
        self.logout.setSizePolicy(sizePolicy)
        self.logout.setMinimumSize(QSize(200, 30))
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout.setStyleSheet(u"border-radius: 10px;\n"
"border-style: solid;\n"
"border-color: rgb(69, 119, 108);\n"
"border-width: 2px;\n"
"background-color: rgb(32, 69, 71);\n"
"color: rgb(239, 241, 237);\n"
"text-align: left; padding-left: 10px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout.setIcon(icon2)

        self.verticalLayout.addWidget(self.logout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.retranslateUi(UserAccountStudent)

        QMetaObject.connectSlotsByName(UserAccountStudent)
    # setupUi

    def retranslateUi(self, UserAccountStudent):
        UserAccountStudent.setWindowTitle(QCoreApplication.translate("UserAccountStudent", u"MainWindow", None))
        self.lastName.setText(QCoreApplication.translate("UserAccountStudent", u"\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435", None))
        self.firstName.setText(QCoreApplication.translate("UserAccountStudent", u"\u0406\u043c'\u044f", None))
        self.patronymic.setText(QCoreApplication.translate("UserAccountStudent", u"\u041f\u043e \u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456", None))
        self.group.setText(QCoreApplication.translate("UserAccountStudent", u"\u0413\u0440\u0443\u043f\u0430", None))
        self.institute.setText(QCoreApplication.translate("UserAccountStudent", u"\u0406\u043d\u0441\u0442\u0438\u0442\u0443\u0442", None))
        self.instituteImg.setText("")
        self.groupImg.setText("")
        self.description.setText(QCoreApplication.translate("UserAccountStudent", u"\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"", None))
        self.email.setText(QCoreApplication.translate("UserAccountStudent", u"teach@gmail.com", None))
        self.emailLabel.setText("")
        self.phone.setText(QCoreApplication.translate("UserAccountStudent", u"+380971111111", None))
        self.phoneLabel.setText("")
        self.photoLabel.setText(QCoreApplication.translate("UserAccountStudent", u"\u0424\u043e\u0442\u043e \u043f\u0440\u043e\u0444\u0456\u043b\u044e", None))
        self.choosePhoto.setText(QCoreApplication.translate("UserAccountStudent", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438 \u0444\u043e\u0442\u043e", None))
        self.editAcc.setText(QCoreApplication.translate("UserAccountStudent", u"\u0420\u0435\u0434\u0430\u0433\u0443\u0432\u0430\u0442\u0438 \u043f\u0440\u043e\u0444\u0456\u043b\u044c", None))
        self.logout.setText(QCoreApplication.translate("UserAccountStudent", u"\u0412\u0438\u0439\u0442\u0438 \u0437 \u0430\u043a\u0430\u0443\u043d\u0442\u0443", None))
    # retranslateUi

