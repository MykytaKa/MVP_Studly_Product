# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from schedule.ui_meetCreator import Ui_Form

class meetCreator(QtWidgets.QWidget):
    def __init__(self, mainWindow=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow
        self.ui.groupEdit.addItem("ІКМ-222а")
        self.ui.groupEdit.addItem("ІКМ-222б")
        self.ui.groupEdit.addItem("ІКМ-222в")
        self.setStyleSheet('background-color: rgb(239, 241, 237);')
        self.ui.nameEdit.setStyleSheet('''border-radius: 10px;
                                          border-style: solid;
                                          border-color: rgb(69, 119, 108);
                                          border-width: 2px;''')
        self.ui.groupEdit.setStyleSheet('''border-top-left-radius: 10px;
                                           border-bottom-left-radius: 10px;
                                           border-style: solid;
                                           border-color: rgb(69, 119, 108);
                                           border-width: 2px;''')
        self.ui.dateTimeEdit.setStyleSheet('''border-top-left-radius: 10px;
                                              border-bottom-left-radius: 10px;
                                              border-style: solid;
                                              border-color: rgb(69, 119, 108);
                                              border-width: 2px;''')
        self.ui.frequency.setStyleSheet('''border-top-left-radius: 10px;
                                           border-bottom-left-radius: 10px;
                                           border-style: solid;
                                           border-color: rgb(69, 119, 108);
                                           border-width: 2px;''')
        self.ui.duration.setStyleSheet('''border-radius: 10px;
                                          border-style: solid;
                                          border-color: rgb(69, 119, 108);
                                          border-width: 2px;''')
        self.ui.createButton.setStyleSheet('''border-radius: 10px;
                                              border-style: solid;
                                              border-color: rgb(69, 119, 108);
                                              border-width: 2px;''')
        self.ui.createButton.setCursor(Qt.PointingHandCursor)

        self.ui.createButton.clicked.connect(self.sendValues)

    def sendValues(self):
        self.close()

    def closeEvent(self, event):
        self.mainWindow.setDisabled(False)
        print('Close')
        event.accept()



