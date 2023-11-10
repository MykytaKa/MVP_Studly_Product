# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QSizePolicy, QGroupBox, QPushButton, QSpacerItem
from PySide6.QtGui import QFont, QTextBlockFormat, QTextDocumentFragment
from notes.ui_notesClass import Ui_Form

# Віджет для відображення тільки назви та частини опиcу нотатка
class NotesWidget(QWidget):
    # Сигнал, задля подальшої роботи із кліком на вікно
    clicked = Signal()
    closed = Signal()

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
        titleFont = QFont()
        titleFont.setBold(True)

        self.titleLabel = QLabel(title)
        self.titleLabel.setFont(titleFont)

        self.descriptionLabel = QLabel()
        self.deleteButton = QPushButton('Delete')
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
    def setFormatedDescriptionTextAndTitleText(self, descriptionText, labelText):
        if self.isOpened:
            self.formatedDescriptionText = descriptionText
            self.setVisibleText()
            self.titleLabel.setText(labelText)
            self.isOpened = False

    # Перевизначення методу, задля створення можливості надсилати сигнал при клікі на нотаток
    def mousePressEvent(self, event):
        self.clicked.emit()

    # Встановлення тексту опису, який може побачити користувач, не заходячи у саму нотатку
    def setVisibleText(self, event=None):
        if event is None:
            newWidth = self.size().width()
        else:
            newWidth = event.size().width()
        unformatedDescriptionText = QTextDocumentFragment.fromHtml(self.formatedDescriptionText).toPlainText()
        if unformatedDescriptionText[:newWidth-1].find('\n') < newWidth-1 and unformatedDescriptionText[:newWidth-1].find('\n') != -1:
            visibleDescription = unformatedDescriptionText[:unformatedDescriptionText.find('\n')]
        else:
            visibleDescription = f'{unformatedDescriptionText[:int(newWidth/6)-3]}...' if len(unformatedDescriptionText)*6 > newWidth else unformatedDescriptionText
        self.descriptionLabel.setText(visibleDescription)

    # Перевизначення методу, задля більш коректного відображення нотатків з довгим описом та символом '/n' на початку
    def resizeEvent(self, event):
        self.setVisibleText(event)

    def closeEvent(self, event):
        self.closed.emit()

# Основний віджет вікна "Нотатки"
class NotesWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Атрибут для зберігання відкритого нотатку
        self.currentNote = None
        self.currentNoteText = ''

        # Масив для зберігання нотатків
        self.notesList = []

        # Створення курсору задля форматування виділеного тексту
        self.cursor = self.ui.descriptionEdit.textCursor()

        # Приховування допоміжного віджету за замовчуванням
        self.ui.insideWidget.hide()

        # Connect задля роботи кнопок "повернутися на головне меню" та "відкривання" нотатка
        self.ui.returnButton.clicked.connect(self.returnToMain)
        self.ui.createNoteButton.clicked.connect(self.createNew)

        # Connect задля роботи кнопок, які форматують виділений текст
        self.ui.boldButton.clicked.connect(self.setSelectedTextBold)
        self.ui.underlineButton.clicked.connect(self.setSelectedTextUnderline)
        self.ui.italicButton.clicked.connect(self.setSelectedTextItalic)
        self.ui.increaseFontButton.clicked.connect(lambda: self.changeFontSize(1))
        self.ui.reduceFontButton.clicked.connect(lambda: self.changeFontSize(-1))
        self.ui.leftAlignmentButton.clicked.connect(lambda: self.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.ui.centerAlignmentButton.clicked.connect(lambda: self.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.ui.rightAlignmentButton.clicked.connect(lambda: self.setAlignment(Qt.AlignmentFlag.AlignRight))

        # Connect задля того, аби при шукати по назві необхідні нотатки
        self.ui.findEdit.textChanged.connect(self.vievFoundNotes)

    def hideAllNotes(self):
        for note in self.notesList:
            note.hide()

    def showAllNotes(self):
        for note in self.notesList:
            note.show()

    def vievFoundNotes(self):
        if self.ui.findEdit.text() == '':
            self.showAllNotes()
        else:
            self.hideAllNotes()
            for note in self.notesList:
                if note.titleLabel.text().find(self.ui.findEdit.text()) != -1:
                    note.show()

    # Метод задля створення нового нотатка та розміщення його у самий початок(вверх) списку усіх нотатків
    def createNew(self, title='', description=''):
        noteNumber = self.ui.notesContainer.count()
        if not title.strip():
            title = f'Нова нотатка {noteNumber}'
        note = NotesWidget(title, description)
        note.clicked.connect(lambda: self.openNote(note))
        note.deleteButton.clicked.connect(lambda: self.deleteNote(note))
        self.notesList.insert(0, note)
        self.ui.notesContainer.insertWidget(0, note)

    # Метод задля видалення нотатка
    def deleteNote(self, note):
        if note in self.notesList:
            index = self.notesList.index(note)
            self.ui.notesContainer.itemAt(index).widget().close()
            self.ui.notesContainer.removeWidget(note)
            del self.notesList[index]

    def saveText(self):
        self.currentNoteText = self.ui.descriptionEdit.toHtml()

    def cancelSaving(self):
        self.ui.descriptionEdit.clear()
        self.ui.descriptionEdit.insertHtml(self.currentNoteText)

    # Метод задля відкриття нотатку на іншій панелі
    def openNote(self, note):
        self.currentNote = note
        self.currentNoteText = self.ui.descriptionEdit.toHtml()
        note.open()
        self.ui.mainWidget.hide()
        self.ui.titleEdit.setText(note.titleLabel.text())
        self.ui.descriptionEdit.clear()
        self.ui.descriptionEdit.insertHtml(note.formatedDescriptionText)
        # Встановлення зв'язку задля збереження зміненої інформації у нотаток по натисканню на кнопку "Зберегти"
        self.ui.cancelButton.clicked.connect(self.cancelSaving)
        self.ui.submitButton.clicked.connect(self.saveText)
        self.ui.submitButton.clicked.connect(lambda: note.setFormatedDescriptionTextAndTitleText(self.ui.descriptionEdit.toHtml(), self.ui.titleEdit.text()))
        self.ui.insideWidget.show()

    # Метод задля повернення на головну сторінку з нотаткими
    def returnToMain(self):
        self.ui.insideWidget.hide()
        self.ui.mainWidget.show()

    def setSelectedTextBold(self):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        # Перевірка, чи виділений текст жирний
        if format.fontWeight() == 400:
            # Якщо не жирний, робимо жирним
            format.setFontWeight(1000)
        else:
            # Якщо жирний, робимо не жирним
            format.setFontWeight(400)

        # Застосування нового формату до виділеного тексту
        self.cursor.mergeCharFormat(format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)

    def setSelectedTextUnderline(self):
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

    def setSelectedTextItalic(self):
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

    def changeFontSize(self, value):
        self.cursor = self.ui.descriptionEdit.textCursor()
        format = self.cursor.charFormat()
        font = format.font()
        fontSize = font.pointSize()
        newFontSize = fontSize + value

        font.setPointSize(newFontSize)
        format.setFont(font)

        if(self.cursor.selectedText() == ''):
            self.ui.descriptionEdit.setFont(font)
        else:
            self.cursor.setCharFormat(format)
            self.ui.descriptionEdit.setTextCursor(self.cursor)

    def setAlignment(self, alignment):
        self.cursor = self.ui.descriptionEdit.textCursor()
#        char_format = self.cursor.charFormat()

        # Отримання формату блока (для вирівнювання тексту)
        block_format = QTextBlockFormat()
        block_format.setAlignment(alignment)

        # Встановлення вирівнювання для виділеного тексту
        self.cursor.mergeBlockFormat(block_format)
        self.ui.descriptionEdit.setTextCursor(self.cursor)
