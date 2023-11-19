# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QGridLayout, QSizePolicy,
                               QGroupBox, QPushButton, QSpacerItem)
from PySide6.QtGui import QFont, QTextBlockFormat, QTextDocumentFragment, QTextDocument, QIcon
from notes.ui_notesClass import Ui_Form
import pickle
import os


# Віджет для відображення тільки назви та частини опиcу нотатка
class NotesWidget(QWidget):
    # Сигнал, задля подальшої роботи із кліком на вікно
    clicked = Signal()

    def __init__(self, title, description='', parent=None):
        super().__init__(parent)

        # Атрибут задля збереження форматованого тексту
        self.formatedDescriptionText = description

        # Атрибут, котрий показує, чи відкритий зараз саме цей нотаток
        self.isOpened = False

        # Налаштування розмірів вікна, курсора та CSS коду
        self.setFixedHeight(80)
        self.setCursor(Qt.PointingHandCursor)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.setStyleSheet('''background-color: rgb(239, 241, 237);
                              border-radius: 10px;
                              color: rgb(0, 0, 0);''')

        # Створення лейблів та кнопки для видалення нататка та відображення назви нотатка та його опису
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(12)

        self.titleLabel = QLabel(title)
        self.titleLabel.setFont(title_font)

        self.descriptionLabel = QLabel()
        self.deleteButton = QPushButton()
        self.deleteButton.setIcon(QIcon(':/icons/delete.png'))
        self.deleteButton.setFixedSize(40, 72)
        self.deleteButton.setStyleSheet('''background-color: rgb(32, 69, 71);
                                           border-radius: 10px;
                                           border-top-left-radius: 0px;
                                           border-bottom-left-radius: 0px;
                                           color: rgb(239, 241, 237);
                                           margin-bottom: 10px;
                                           ''')

        # Створення контейнера та розміщення усіх відджетів у ньому
        self.boxContainer = QGridLayout()
        self.boxContainer.addWidget(self.titleLabel, 0, 0)
        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.boxContainer.addItem(spacer, 0, 1)
        self.boxContainer.addWidget(self.deleteButton, 0, 2, 2, 1)
        self.boxContainer.addWidget(self.descriptionLabel, 1, 0, 1, 2)
        self.boxContainer.setContentsMargins(9, 0, 0, 0)

        # Створення коробки для групування лейблів та більш короктрої роботи CSS коду
        self.box = QGroupBox()
        self.box.setStyleSheet('''background-color: rgb(239, 241, 237);
                                  border-radius: 10px;
                                  color: rgb(0, 0, 0);''')
        self.box.setLayout(self.boxContainer)

        # Створення леяута для відображення коробки з лейблами
        self.container = QVBoxLayout()
        self.container.addWidget(self.box)

        # Відображення основного леяута
        self.setLayout(self.container)

    # Відкриття нотатка на запис тексту
    def open(self):
        self.isOpened = True

    # Збереження зміненого тексту у нотаток та закриття на запис тексту
    def set_formated_text(self, description_text, label_text):
        if self.isOpened:
            self.formatedDescriptionText = description_text
            self.set_visible_text()
            self.titleLabel.setText(label_text)
            self.isOpened = False

    # Перевизначення методу, задля створення можливості надсилати сигнал при клікі на нотаток
    def mousePressEvent(self, event):
        self.clicked.emit()

    # Встановлення тексту опису, який може побачити користувач, не заходячи у саму нотатку
    def set_visible_text(self, event=None):
        if event is None:
            new_width = self.size().width()
        else:
            new_width = event.size().width()

        unformated_description_text = QTextDocumentFragment.fromHtml(self.formatedDescriptionText).toPlainText()

        if (unformated_description_text[:new_width - 1].find('\n') < new_width - 1
                and unformated_description_text[:new_width - 1].find('\n') != -1):
            visible_description = unformated_description_text[:unformated_description_text.find('\n')]
        else:
            visible_description = f'{unformated_description_text[:int(new_width / 6) - 3]}...' \
                if len(unformated_description_text) * 6 > new_width else unformated_description_text

        self.descriptionLabel.setText(visible_description)

    # Перевизначення методу, задля більш коректного відображення нотатків з довгим описом та символом '/n' на початку
    def resizeEvent(self, event):
        self.set_visible_text(event)


class Note:
    def __init__(self, title, content):
        self.content = QTextDocument()
        self.content.setHtml(content)  # Здесь мы используем HTML-форматированный текст
        self.title = title


# Основний віджет вікна "Нотатки"
class NotesWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Атрибут для зберігання відкритого нотатку
        self.currentNote = None
        self.currentNoteText = ''

        # Таймер задля уникнення проблем зі швидкими кліками на кнопки
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.create_new)

        # Масив для зберігання нотатків
        self.notesList = []
        self.notes = []

        # self.cart = Cart()  # добавляем корзину
        self.filename = 'notes/notes.pkl'
        self.load_notes()
        self.get_notes()

        # Створення курсору задля форматування виділеного тексту
        self.cursor = self.ui.descriptionEdit.textCursor()

        # Приховування допоміжного віджету за замовчуванням
        self.ui.insideWidget.hide()

        # Connect задля роботи кнопок "повернутися на головне меню" та "відкривання" нотатка
        self.ui.returnButton.clicked.connect(self.return_to_main)
        self.ui.createNoteButton.clicked.connect(self.startTimer)

        # Connect задля роботи кнопок, які форматують виділений текст
        self.ui.boldButton.clicked.connect(self.set_bold_text)
        self.ui.underlineButton.clicked.connect(self.set_underline_text)
        self.ui.italicButton.clicked.connect(self.set_italic_text)
        self.ui.increaseFontButton.clicked.connect(lambda: self.change_font_size(1))
        self.ui.reduceFontButton.clicked.connect(lambda: self.change_font_size(-1))
        self.ui.leftAlignmentButton.clicked.connect(lambda: self.set_alignment(Qt.AlignmentFlag.AlignLeft))
        self.ui.centerAlignmentButton.clicked.connect(lambda: self.set_alignment(Qt.AlignmentFlag.AlignCenter))
        self.ui.rightAlignmentButton.clicked.connect(lambda: self.set_alignment(Qt.AlignmentFlag.AlignRight))
        self.ui.strikeoutButton.clicked.connect(self.set_strikeout_text)

        # Connect задля того, аби шукати по назві необхідні нотатки
        self.ui.findEdit.textChanged.connect(self.viev_found_notes)

    def startTimer(self):
        self.timer.start()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                notes_data = pickle.load(file)
                self.notes = [Note(title, html) for title, html in notes_data]

    def get_notes(self):
        while self.ui.notesContainer.count() > 0:
            item = self.ui.notesContainer.takeAt(0)
            if item is not None:
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)

        self.ui.notesContainer.addItem(self.ui.verticalSP)
        self.display_notes()

    def display_notes(self):
        self.notesList = []
        for i, note in enumerate(self.notes, 0):
            j = NotesWidget(note.title, note.content.toHtml())
            j.clicked.connect(lambda j=j: self.open_note(j))
            j.deleteButton.clicked.connect(lambda checked=False, j=j: self.delete_note(j))
            self.notesList.append(j)
            self.ui.notesContainer.insertWidget(i, j)

    def save_changes(self):
        with open(self.filename, 'wb') as file:
            pickle.dump([(i.title, i.content.toHtml()) for i in self.notes], file)

    def delete_note(self, note_widget):
        index = self.ui.notesContainer.indexOf(note_widget)
        if index >= 0:
            item = self.ui.notesContainer.takeAt(index)
            if item is not None:
                widget_to_remove = item.widget()
                if widget_to_remove is not None:
                    widget_to_remove.setParent(None)
                    self.notes.pop(index)
                    self.save_changes()

        self.get_notes()
        self.update_searchline_status()

    def create_new(self, title='', description=''):
        note_number = self.ui.notesContainer.count()
        if not title.strip():
            title = f'Нова нотатка {note_number}'

        new_note = Note(title, '')
        self.notes.append(new_note)  # Добавляем заметку в конец списка
        self.save_changes()

        self.get_notes()
        self.update_searchline_status()
        self.timer.stop()

    def save_text(self, note_widget):
        index = self.ui.notesContainer.indexOf(note_widget)
        if index >= 0:
            # Получаем текущую заметку
            current_note = self.notes[index]
            # Обновляем заголовок и содержание заметки
            current_note.title = self.ui.titleEdit.text()
            current_note.content.setHtml(self.ui.descriptionEdit.toHtml())
            # Сохраняем изменения
            self.save_changes()
            self.get_notes()

    # Метод задля відміни усіх змін та повернення до тексу, який останій збережено
    def cancel_saving(self):
        self.ui.descriptionEdit.clear()
        self.ui.descriptionEdit.insertHtml(self.currentNoteText)

    def update_searchline_status(self):
        self.ui.findEdit.setDisabled(True if len(self.notes) == 0 else False)

    # Метод задля відкриття нотатку на іншій панелі
    def open_note(self, note):
        self.currentNote = note
        self.currentNoteText = self.ui.descriptionEdit.toHtml()
        note.open()
        self.ui.mainWidget.hide()
        self.ui.titleEdit.setText(note.titleLabel.text())
        self.ui.descriptionEdit.clear()
        self.ui.descriptionEdit.insertHtml(note.formatedDescriptionText)
        # Встановлення зв'язку задля збереження зміненої інформації у нотаток по натисканню на кнопку "Зберегти"
        self.ui.cancelButton.clicked.connect(self.cancel_saving)
        self.ui.submitButton.clicked.connect(lambda: self.save_text(note))
        self.ui.submitButton.clicked.connect(
            lambda: note.set_formated_text(self.ui.descriptionEdit.toHtml(),
                                           self.ui.titleEdit.text()))
        self.ui.insideWidget.show()

    # Метод задля повернення на головну сторінку з нотаткими
    def return_to_main(self):
        self.ui.insideWidget.hide()
        self.ui.mainWidget.show()

    # Метод для приховування усіх нотатків
    def hide_all_notes(self):
        for note in self.notesList:
            note.hide()

    # Метод для відображення усіх нотатків
    def show_all_notes(self):
        for note in self.notesList:
            note.show()

    # Метод задля відображення лише необхідних нотатків
    def viev_found_notes(self):
        # Відображаємо усі нотатки, якщо поле для запитів пусте
        if self.ui.findEdit.text() == '':
            self.show_all_notes()
        else:
            self.hide_all_notes()
            for note in self.notesList:
                if note.titleLabel.text().find(self.ui.findEdit.text()) != -1:
                    note.show()

    # Встановити жирним виділений тест
    def set_bold_text(self):
        self.cursor = self.ui.descriptionEdit.textCursor()
        char_format = self.cursor.charFormat()
        # Перевірка, чи виділений текст жирний
        if char_format.fontWeight() == 400:
            # Якщо не жирний, робимо жирним
            char_format.setFontWeight(1000)
        else:
            # Якщо жирний, робимо не жирним
            char_format.setFontWeight(400)

        # Застосування нового формату до виділеного тексту
        self.cursor.mergeCharFormat(char_format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)

    # Встановити підкресленним виділений тест
    def set_underline_text(self):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        # Перевірка, чи виділений текст підкреслений
        if format.fontUnderline():
            # Якщо підкреслений, робимо не підкресленим
            format.setFontUnderline(False)
        else:
            # Якщо не підкреслений, робимо підкресленим
            format.setFontUnderline(True)

        # Застосування нового формату до виділеного тексту
        self.cursor.mergeCharFormat(format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)

    # Встановити курсивним виділений тест
    def set_italic_text(self):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        # Перевірка, чи виділений текст курсивний
        if format.fontItalic():
            # Якщо курсивний, робимо не курсивним
            format.setFontItalic(False)
        else:
            # Якщо не курсивний, робимо курсивним
            format.setFontItalic(True)

        # Застосування нового формату до виділеного тексту
        self.cursor.mergeCharFormat(format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)

    # Встановити розмір виділеного тесту
    def change_font_size(self, value):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        font = format.font()
        fontSize = font.pointSize()
        newFontSize = fontSize + value

        font.setPointSize(newFontSize)
        format.setFont(font)

        if (self.cursor.selectedText() == ''):
            self.ui.descriptionEdit.setFont(font)
        else:
            self.cursor.setCharFormat(format)
            self.ui.descriptionEdit.setTextCursor(self.cursor)

    # Встановити вирівнювання виділеного тесту
    def set_alignment(self, alignment):
        self.cursor = self.ui.descriptionEdit.textCursor()
        #        char_format = self.cursor.charFormat()

        # Отримання формату блока (для вирівнювання тексту)
        block_format = QTextBlockFormat()
        block_format.setAlignment(alignment)

        # Встановлення вирівнювання для виділеного тексту
        self.cursor.mergeBlockFormat(block_format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)

    def set_strikeout_text(self):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        # Перевірка, чи виділений текст закреслений
        if format.fontStrikeOut():
            # Якщо закреслений, робимо не закресленим
            format.setFontStrikeOut(False)
        else:
            # Якщо не закреслений, робимо закресленим
            format.setFontStrikeOut(True)

        # Застосування нового формату до виділеного тексту
        self.cursor.mergeCharFormat(format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)
