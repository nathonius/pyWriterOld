import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SceneEditor(QWidget):
    def __init__(self, filepath=None):
        super().__init__()

        self.filepath = filepath

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1030, 800)

        # Set window title to scene name
        self.setWindowTitle("Scene Editor")

        # Set up the menubar
        self.menubar = QMenuBar(self)
        self.initMenubar()

        # Create the main tab pane
        self.tabs = QTabWidget(self)
        self.initTabs()

        # Create the chapter select and save pane
        self.chapterSelect = QWidget(self)
        self.initChapterSelect()

        # Add all widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.menubar)
        layout.addWidget(self.tabs)
        layout.addWidget(self.chapterSelect)
        self.setLayout(layout)

    def initMenubar(self):
        # Add menus
        self.menubar.addMenu("File")
        self.menubar.addMenu("Scene")
        self.menubar.addMenu("Edit")
        self.menubar.addMenu("Spelling")
        self.menubar.addMenu("Settings")
        self.menubar.addMenu("Help")

    def initTabs(self):
        # Create each tab
        contentTab = QWidget(self.tabs)
        detailsTab = QWidget(self.tabs)
        charactersTab = QWidget(self.tabs)
        locationsTab = QWidget(self.tabs)
        itemsTab = QWidget(self.tabs)
        notesTab = QWidget(self.tabs)
        pictureTab = QWidget(self.tabs)
        goalsTab = QWidget(self.tabs)
        exportingTab = QWidget(self.tabs)
        timeTab = QWidget(self.tabs)
        ratingsTab = QWidget(self.tabs)

        # Set up content tab
        contentLayout = QVBoxLayout(contentTab)
        self.formatbar = QToolBar("Format")
        self.initFormatbar()
        self.sceneText = QTextEdit(contentTab)
        contentLayout.addWidget(self.formatbar)
        contentLayout.addWidget(self.sceneText)
        contentTab.setLayout(contentLayout)

        # Set up details tab
        detailsLayout = QVBoxLayout(detailsTab)
        detailsText = QTextEdit(detailsTab)
        detailsLayout.addWidget(detailsText)
        detailsTab.setLayout(detailsLayout)

        # Set up ...

        # Add tabs
        self.tabs.addTab(contentTab, "Content")
        self.tabs.addTab(detailsTab, "Details")
        self.tabs.addTab(charactersTab, "Characters")
        self.tabs.addTab(locationsTab, "Locations")
        self.tabs.addTab(itemsTab, "Items")
        self.tabs.addTab(notesTab, "Notes")
        self.tabs.addTab(pictureTab, "Picture")
        self.tabs.addTab(goalsTab, "Goals")
        self.tabs.addTab(exportingTab, "Exporting")
        self.tabs.addTab(timeTab, "Time")
        self.tabs.addTab(ratingsTab, "Ratings")

    def initChapterSelect(self):
        pass

    def initFormatbar(self):
        # Create Format Actions
        boldAction = QAction("Bold", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QAction("Italic", self)
        italicAction.triggered.connect(self.italic)

        underlineAction = QAction("Underline", self)
        underlineAction.triggered.connect(self.underline)

        strikeAction = QAction("Strike-Through", self)
        strikeAction.triggered.connect(self.strike)

        # Create Alignment Actions
        alignLeftAction = QAction("Align Left", self)
        alignLeftAction.triggered.connect(self.alignLeft)

        alignCenterAction = QAction("Align Center", self)
        alignCenterAction.triggered.connect(self.alignCenter)

        alignRightAction = QAction("Align Right", self)
        alignRightAction.triggered.connect(self.alignRight)

        alignJustifyAction = QAction("Align Justify", self)
        alignJustifyAction.triggered.connect(self.alignJustify)

        # Create Indent/Dedent Actions
        indentAction = QAction("Indent", self)
        indentAction.triggered.connect(self.indent)

        dedentAction = QAction("Dedent", self)
        dedentAction.triggered.connect(self.dedent)

        # Add Format Actions
        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlineAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addSeparator()

        # Add Alignment Actions
        self.formatbar.addAction(alignLeftAction)
        self.formatbar.addAction(alignCenterAction)
        self.formatbar.addAction(alignRightAction)
        self.formatbar.addAction(alignJustifyAction)
        self.formatbar.addSeparator()

        # Add Indent/Dedent Actions
        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)
        self.formatbar.addSeparator()

    # Formatting Functions
    def bold(self):
        if self.sceneText.fontWeight() == QFont.Bold:
            self.sceneText.setFontWeight(QFont.Normal)
        else:
            self.sceneText.setFontWeight(QFont.Bold)

    def italic(self):
        state = self.sceneText.fontItalic()
        self.sceneText.setFontItalic(not state)

    def underline(self):
        state = self.sceneText.fontUnderline()
        self.sceneText.setFontUnderline(not state)

    def strike(self):
        # Get current format
        fmt = self.sceneText.currentCharFormat()
        # Invert strike state
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        # Set the format of text
        self.sceneText.setCurrentCharFormat(fmt)

    # Alignment Functions
    def alignLeft(self):
        self.sceneText.setAlignment(Qt.AlignLeft)

    def alignCenter(self):
        self.sceneText.setAlignment(Qt.AlignCenter)

    def alignRight(self):
        self.sceneText.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.sceneText.setAlignment(Qt.AlignJustify)

    # Indent/Dedent Functions
    def indent(self, dedent=False):
        # Get the cursor
        cursor = self.sceneText.textCursor()

        if cursor.hasSelection():
            # Get current line/block number
            block = cursor.blockNumber()
            # Figure out how many lines are in selection
            cursor.setPosition(cursor.selectionEnd())
            lines = cursor.blockNumber() - block

            # Indent/Dedent each line
            for i in range(lines+1):
                # Move to start of line
                cursor.movePosition(QTextCursor.StartOfLine)

                # Indent/Dedent
                if dedent:
                    # Get the current line
                    line = cursor.block().text()
                    # If the line starts with a tab, remove it.
                    if line.startswith("\t"):
                        cursor.deleteChar()
                    # Otherwise delete spaces up to first non-space char
                    else:
                        for char in line[:8]:
                            if char != " ":
                                break
                            cursor.deleteChar()
                else:
                    cursor.insertText("\t")

                # Move to next line
                cursor.movePosition(QTextCursor.Up)

        else:
            if dedent:
                cursor.movePosition(QTextCursor.StartOfLine)
                # Get the current line
                line = cursor.block().text()
                # If the line starts with a tab, remove it.
                if line.startswith("\t"):
                    cursor.deleteChar()
                # Otherwise delete spaces up to first non-space char
                else:
                    for char in line[:8]:
                        if char != " ":
                            break
                        cursor.deleteChar()
            else:
                cursor.insertText("\t")


    def dedent(self):
        self.indent(True)