from PySide6.QtGui import QFont, QPixmap, QPainter, QColor, QImage, QPainterPath
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QFileDialog
from PySide6.QtCore import Qt
from ui_mainwindowteacher import Ui_MainWindow
from schedule.scheduleClassTeacher import ScheduleClassTeacher
from members.MembersClass import MembersClass
from notes.NotesClass import NotesWindow
from userAccount.userAccountTeacher import UserAccountTeacher
from about.about import About
from DB.connect_to_db import connect_to_database


class MainWindowTeacher(QMainWindow):
    def __init__(self, user_data=None, login=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stackedWidget = QStackedWidget()
        self.login = login
        self.user_id = user_data['user_id']

        if user_data['way_to_photo'] is not None:
            self.set_photo(user_data['way_to_photo'])
        else:
            self.ui.userIcon.setText(''.join([user_data['first_name'][0].upper(), user_data['last_name'][0].upper()]))

        self.widgets = {
            'schedule': ScheduleClassTeacher(self.user_id),
            'members': MembersClass(),
            'notes': NotesWindow(),
            'userAccount': UserAccountTeacher(self.user_id)
        }

        for widget in self.widgets.values():
            self.stackedWidget.addWidget(widget)

        self.ui.widgetContainer.addWidget(self.stackedWidget)

        self.isLogout = False

        self.ui.scheduleButton.clicked.connect(lambda: self.load_section('schedule'))
        self.ui.membersButton.clicked.connect(lambda: self.load_section('members'))
        self.ui.notesButton.clicked.connect(lambda: self.load_section('notes'))
        self.ui.logoLabel.mousePressEvent = self.open_about_window
        self.ui.userInfo.mousePressEvent = self.open_user_account

        self.unlight_buttons()

        button_font = QFont()
        button_font.setPointSize(11)

        self.ui.scheduleButton.setFont(button_font)
        self.ui.membersButton.setFont(button_font)
        self.ui.notesButton.setFont(button_font)

        button_font.setPointSize(11)
        button_font.setBold(True)
        self.ui.scheduleButton.setFont(button_font)

        self.ui.scheduleButton.setCursor(Qt.PointingHandCursor)
        self.ui.membersButton.setCursor(Qt.PointingHandCursor)
        self.ui.notesButton.setCursor(Qt.PointingHandCursor)

        self.ui.scheduleButton.clicked.connect(lambda: self.light_chosen_button(self.ui.scheduleButton))
        self.ui.membersButton.clicked.connect(lambda: self.light_chosen_button(self.ui.membersButton))
        self.ui.notesButton.clicked.connect(lambda: self.light_chosen_button(self.ui.notesButton))

        self.ui.userInfo.setText(f"{user_data['last_name']} {user_data['first_name'][0]}.{user_data['patronymic'][0]}."
                                 f"\n{self.get_department_name(user_data['user_id'])}")

    @connect_to_database
    def get_department_name(cursor, self, user_id):
        cursor.execute('SELECT departments.name '
                       'FROM teachers '
                       'JOIN departments ON teachers.department_id = departments.id '
                       'WHERE teachers.user_id = ?', (user_id,))
        result = cursor.fetchone()
        return result[0]

    def open_user_account(self, event):
        self.load_section('userAccount')

    def open_about_window(self, event):
        self.about = About()
        self.about.setModal(True)
        self.about.show()

    def resizeEvent(self, event):
        self.ui.logoLabel.setPixmap(QPixmap(":/icons/icon.png").scaled(self.ui.logoLabel.size(), Qt.KeepAspectRatio))

    def light_chosen_button(self, button):
        self.unlight_buttons()
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        button.setFont(font)

    def unlight_buttons(self):
        button_font = QFont()
        button_font.setPointSize(11)

        self.ui.scheduleButton.setFont(button_font)
        self.ui.membersButton.setFont(button_font)
        self.ui.notesButton.setFont(button_font)

    def load_section(self, section):
        widget = self.widgets[section]
        self.stackedWidget.setCurrentWidget(widget)
        if section == 'userAccount':
            self.unlight_buttons()
            widget.ui.logout.clicked.connect(self.logout)
            widget.ui.choosePhoto.clicked.connect(self.choose_photo)

    def logout(self):
        if self.widgets['userAccount'].isLogout:
            self.login.show()
            self.close()
            self.deleteLater()

    @connect_to_database
    def choose_photo(cursor, self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Оберіть зображення", "",
                                                   "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)")
        if file_name:
            self.set_photo(file_name)
            self.widgets['userAccount'].set_photo(file_name)
            cursor.execute('UPDATE users SET way_to_photo = ? WHERE id = ?', (file_name, self.user_id))

    def set_photo(self, file_path):
        if file_path:
            self.ui.userIcon.setText('')
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
            self.ui.userIcon.setPixmap(scaled_cropped_pixmap)

    def scale_pixmap_to_label(self, pixmap):
        # Получаем размеры лейбла
        label_width = self.ui.userIcon.width()
        label_height = self.ui.userIcon.height()

        # Масштабируем изображение под размер лейбла
        scaled_pixmap = pixmap.scaled(label_width - 10, label_height - 10, Qt.IgnoreAspectRatio)

        return scaled_pixmap
