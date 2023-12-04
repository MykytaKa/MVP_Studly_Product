from PySide6.QtWidgets import QLabel, QPushButton, QDialog, QVBoxLayout, QLineEdit, QMessageBox, QWidget
from PySide6.QtGui import QPixmap, QPainter, QColor, Qt, QImage, QPainterPath, QIcon
from PySide6.QtCore import QTimer
from userAccount.ui_userAccountTeacher import Ui_UserAccountTeacher
from DB.connect_to_db import connect_to_database


class UserAccountTeacher(QWidget):
    def __init__(self, user_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserAccountTeacher()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.isLogout = False

        # Подключение события кнопки
        self.ui.editAcc.clicked.connect(self.edit_labels)
        self.ui.logout.clicked.connect(self.logout)
        self.set_user_data()

    @connect_to_database
    def set_user_data(cursor, self):
        cursor.execute('SELECT * FROM users WHERE id = ?', (self.user_id,))
        user = cursor.fetchone()

        user_data = {
            'user_id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'patronymic': user[3],
            'way_to_photo': user[4],
            'account_description': user[5],
            'phone_number': user[6],
            'email': user[7],
            'status': user[9]
        }

        # User name
        self.ui.firstName.setText(user_data['first_name'])
        self.ui.lastName.setText(user_data['last_name'])
        self.ui.patronymic.setText(user_data['patronymic'])

        # Contacts
        self.ui.phone.setText(user_data['phone_number'])
        self.ui.email.setText(user_data['email'])

        # Photo and description
        self.ui.description.setText(user_data['account_description'])

        if user_data['way_to_photo'] is not None:
            self.set_photo(user_data['way_to_photo'])
        else:
            self.ui.photoLabel.setText(''.join([user_data['first_name'][0].upper(), user_data['last_name'][0].upper()]))

        # University info
        cursor.execute("""
        SELECT teachers.position, departments.name as department_name, institutes.name as institute_name
        FROM teachers
        JOIN departments ON teachers.department_id = departments.id
        JOIN users ON teachers.user_id = users.id
        JOIN institutes ON departments.institute_id = institutes.id
        WHERE teachers.user_id = ?
        """, (self.user_id,))

        position, department_name, institute_name = cursor.fetchone()

        self.ui.position.setText(position)
        self.ui.department.setText(department_name)
        self.ui.institute.setText(institute_name)

    def logout(self):
        if QMessageBox.question(None, "Вийти", "Ви впевнені, що бажаєте вийти з акаунту?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.isLogout = True

    def set_photo(self, file_path):
        if file_path:
            self.ui.photoLabel.setText('')
            # Загружаем изображение
            original_pixmap = QPixmap(file_path)

            # Создаем маску в форме круга
            mask = QImage(original_pixmap.size(), QImage.Format_ARGB32)
            mask.fill(QColor(0, 0, 0, 0))

            painter = QPainter(mask)
            painter.setRenderHint(QPainter.Antialiasing)

            center = mask.rect().center()
            radius = min(center.x(), center.y())  # Минимум из половины ширины и высоты
            print(f'Radius: {radius}')
            print(f'Center: {center.x()}.{center.y()}')

            # Создаем QPainterPath в форме круга с динамическим размером
            path = QPainterPath()
            path.addEllipse(original_pixmap.rect())  # Тут змінив на розміри самого лейбла

            # Создаем QPixmap для отображения обрезанного изображения
            cropped_pixmap = QPixmap(original_pixmap.size())
            cropped_pixmap.fill(Qt.transparent)

            # Рисуем обрезанное изображение на QPixmap
            painter = QPainter(cropped_pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, original_pixmap)
            painter.end()

            # Масштабируем обрезанное изображение под размер лейбла
            scaled_cropped_pixmap = self.scale_pixmap_to_label(cropped_pixmap)

            # Устанавливаем масштабированное изображение в лейбл
            self.ui.photoLabel.setPixmap(scaled_cropped_pixmap)

    def scale_pixmap_to_label(self, pixmap):
        # Получаем размеры лейбла
        label_width = self.ui.photoLabel.width()
        label_height = self.ui.photoLabel.height()

        # Масштабируем изображение под размер лейбла
        scaled_pixmap = pixmap.scaled(label_width - 5, label_height - 5, Qt.IgnoreAspectRatio)

        return scaled_pixmap

    @connect_to_database
    def edit_labels(cursor, self):
        dialog = EditLabelsDialog(self.ui.firstName.text(), self.ui.lastName.text(), self.ui.patronymic.text(),
                                  self.ui.position.text(), self.ui.description.text(), self.ui.phone.text(),
                                  self.ui.email.text())
        result = dialog.exec_()

        # Применяем изменения, если пользователь подтвердил
        if result == QDialog.Accepted:
            cursor.execute("UPDATE users "
                           "SET first_name = ?, last_name = ?, patronymic = ?, account_description = ?, "
                           "phone_number = ?, email = ? "
                           "WHERE id = ?",
                           (dialog.labelFirstName_edit.text(), dialog.labelLastName_edit.text(),
                            dialog.labelPatronymic_edit.text(),
                            dialog.labelDescription_edit.text(), dialog.labelPhoneEdit_edit.text(),
                            dialog.labelEmailEdit_edit.text(), self.user_id))
            cursor.execute("UPDATE teachers "
                           "SET position = ? "
                           "WHERE user_id = ?", (dialog.labelPositionEdit_edit.text(), self.user_id))

            QTimer.singleShot(100, self.set_user_data)


class EditLabelsDialog(QDialog):
    def __init__(self, first_name, last_name, patronymic, position, description, phone, email, parent=None):
        super(EditLabelsDialog, self).__init__(parent)
        self.setWindowTitle("Редагувати профіль")
        self.setWindowIcon(QIcon(':/icons/edit_dark.png'))

        self.setFixedSize(500, 550)

        self.setStyleSheet('background-color: rgb(239, 241, 237);')

        self.labelFN = QLabel("Ім'я", self)
        self.labelSN = QLabel('Прізвище', self)
        self.labelPat = QLabel('По батькові', self)
        self.labelPos = QLabel('Посада', self)
        self.labelD = QLabel('Опис', self)
        self.labelPhone = QLabel('Телефон', self)
        self.labelEmail = QLabel('Пошта', self)

        # Создаем поля ввода для редактирования лейблов
        self.labelFirstName_edit = QLineEdit(self)
        self.labelLastName_edit = QLineEdit(self)
        self.labelPatronymic_edit = QLineEdit(self)
        self.labelPositionEdit_edit = QLineEdit(self)
        self.labelDescription_edit = QLineEdit(self)
        self.labelPhoneEdit_edit = QLineEdit(self)
        self.labelEmailEdit_edit = QLineEdit(self)
        self.labelFirstName_edit.setStyleSheet('''  border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelLastName_edit.setStyleSheet('''   border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelPatronymic_edit.setStyleSheet(''' border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelPositionEdit_edit.setStyleSheet('''    border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelDescription_edit.setStyleSheet('''border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelPhoneEdit_edit.setStyleSheet('''  border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')
        self.labelEmailEdit_edit.setStyleSheet('''  border-style: solid;
                                                    border-width: 2px;
                                                    border-color: rgb(69, 119, 108);
                                                    background-color: rgba(69, 119, 108, 125);
                                                    border-radius: 10px;
                                                    width: 500px;
                                                    height: 30px;
                                                    word-wrap: break-word;''')

        # Устанавливаем текст из начальных лейблов в соответствующие QLineEdit
        self.labelFirstName_edit.setText(first_name)
        self.labelLastName_edit.setText(last_name)
        self.labelPatronymic_edit.setText(patronymic)
        self.labelPositionEdit_edit.setText(position)
        self.labelDescription_edit.setText(description)
        self.labelPhoneEdit_edit.setText(phone)
        self.labelEmailEdit_edit.setText(email)

        # Устанавливаем максимальную длину для каждого QLineEdit
        self.labelFirstName_edit.setMaxLength(100)
        self.labelLastName_edit.setMaxLength(100)
        self.labelPatronymic_edit.setMaxLength(100)
        self.labelPositionEdit_edit.setMaxLength(50)
        self.labelDescription_edit.setMaxLength(500)
        self.labelPhoneEdit_edit.setMaxLength(14)
        self.labelEmailEdit_edit.setMaxLength(100)

        # Создаем кнопку подтверждения редактирования
        self.confirm_button = QPushButton("Зберегти", self)
        self.confirm_button.clicked.connect(self.accept)

        self.confirm_button.setStyleSheet('''   border-style: solid;
                                                border-width: 2px;
                                                border-color: rgb(69, 119, 108);
                                                background-color: rgba(69, 119, 108, 125);
                                                border-radius: 10px;
                                                min-width: 150px;
                                                max-width: 150px;
                                                height: 30px;
                                                margin-top: 20px;''')

        # Размещаем виджеты на макете
        layout = QVBoxLayout(self)

        layout.addWidget(self.labelSN)
        layout.addWidget(self.labelLastName_edit)

        layout.addWidget(self.labelFN)
        layout.addWidget(self.labelFirstName_edit)

        layout.addWidget(self.labelPat)
        layout.addWidget(self.labelPatronymic_edit)

        layout.addWidget(self.labelPos)
        layout.addWidget(self.labelPositionEdit_edit)

        layout.addWidget(self.labelD)
        layout.addWidget(self.labelDescription_edit)

        layout.addWidget(self.labelPhone)
        layout.addWidget(self.labelPhoneEdit_edit)

        layout.addWidget(self.labelEmail)
        layout.addWidget(self.labelEmailEdit_edit)

        layout.addWidget(self.confirm_button)

        self.labelFirstName_edit.setCursor(Qt.IBeamCursor)
        self.labelLastName_edit.setCursor(Qt.IBeamCursor)
        self.labelPatronymic_edit.setCursor(Qt.IBeamCursor)
        self.labelPositionEdit_edit.setCursor(Qt.IBeamCursor)
        self.labelDescription_edit.setCursor(Qt.IBeamCursor)
        self.labelPhoneEdit_edit.setCursor(Qt.IBeamCursor)
        self.labelEmailEdit_edit.setCursor(Qt.IBeamCursor)
        self.confirm_button.setCursor(Qt.PointingHandCursor)
