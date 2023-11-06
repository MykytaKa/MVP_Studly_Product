# This Python file uses the following encoding: utf-8
#from PySide6.QtCore import
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy


class meetWidget(QWidget):
    def __init__(self, subjectName = None, meetTime = None, teacherName = None, parent = None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.text = QLabel(subjectName)
        self.widgetLayout = QVBoxLayout()
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetLayout.addWidget(self.text)

        self.setLayout(self.widgetLayout)

        self.setStyleSheet('background-color: rgb(255, 255, 255); border-radius: 0px;')
