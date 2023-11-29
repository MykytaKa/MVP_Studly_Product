from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QPushButton, QGroupBox
from PySide6.QtCore import Qt, QTime
from PySide6.QtGui import QFont, QIcon


class MeetWidget(QWidget):
    def __init__(self, meet_id=None, meet_title=None, meet_time=None, meet_duration=None, teacher_id=None, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))

        self.meet_id = meet_id

        # Label для відображення назви зустрічі
        font = QFont()
        font.setBold(True)

        self.title = QLabel(self.wrap_title(meet_title))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(font)
        self.title.setStyleSheet('padding: 5px;\n border-style: none')

        # Label для відображення тривалості зустрічі
        self.durationLalel = QLabel()
        self.setStyleSheet('padding-left: 5px;\npadding-right:5px;')
        self.durationLalel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.durationLalel.setText(self.set_duration(meet_time.toString("dd.MM.yyyy.hh.mm"), meet_duration))

        # Створення Layout для GroupBox
        self.boxContainer = QVBoxLayout()
        self.boxContainer.setContentsMargins(5, 5, 5, 5)

        self.boxContainer.addWidget(self.title)
        self.boxContainer.addWidget(self.durationLalel, 1, Qt.AlignmentFlag.AlignCenter)

        if teacher_id is not None:
            # Кнопка для видалення зустрічі
            self.deleteButton = QPushButton('Видалити')
            self.deleteButton.setCursor(Qt.PointingHandCursor)
            self.deleteButton.setIcon(QIcon(':/icons/delete.png'))
            self.deleteButton.setStyleSheet('''background-color: rgb(69, 119, 108);\n
                                               color: rgb(255, 255, 255); font: 7pt "Segoe UI";''')

            self.boxContainer.addWidget(self.deleteButton, 1, Qt.AlignmentFlag.AlignCenter)

        # Створення GroupBox для більш коректної роботи CSS коду
        self.box = QGroupBox()
        self.box.setStyleSheet('''background-color: rgb(255, 255, 255);\n
                                  border-radius: 10px;\n
                                  border-style: solid;\n
                                  border-color: rgb(69, 119, 108);\n
                                  border-width: 2px;''')
        self.box.setLayout(self.boxContainer)

        # Створення основного Layout для віджетів
        self.mainContainer = QVBoxLayout()
        self.mainContainer.setContentsMargins(0, 0, 0, 0)
        self.mainContainer.addWidget(self.box)

        self.setLayout(self.mainContainer)

    def set_duration(self, start_datetime, duration):
        _, _, _, hour, minute = start_datetime.split('.')
        duration_hours = int(duration) // 60
        duration_minutes = (int(duration) % 60) if duration_hours > 0 else int(duration)
        end_time = QTime(int(hour), int(minute))
        end_time = end_time.addSecs(duration_hours * 3600 + duration_minutes * 60)
        end_time_string = end_time.toString("hh:mm")
        start_time_string = f'{hour}:{minute}'
        return f'{start_time_string} - {end_time_string}'

    def wrap_title(self, input_title):
        max_length = 25
        words = input_title.split()
        new_title = ''
        current_length = 0

        for word in words:
            word_length = len(word)
            if current_length + word_length <= max_length:
                new_title += word + ' '
                current_length += word_length + 1
            else:
                new_title = new_title.rstrip() + '\n' + word + ' '
                current_length = word_length + 1

        return new_title.rstrip()
