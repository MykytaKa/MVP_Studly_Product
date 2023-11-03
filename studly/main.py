# This Python file uses the following encoding: utf-8

#Команды для нормального запуска проекта с Гита:
#python -m venv venv
#venv\Scripts\activate
#pip install -r requirements.txt
#(requirements.txt должен лежать в папке с проектом)
#pip install PySide6

# EXE: pyinstaller -F -w main.py

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
from PySide6.QtWidgets import QApplication
from login.login import Login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()

    login.show()
    sys.exit(app.exec())
