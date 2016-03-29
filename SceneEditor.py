import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SceneEditor(QMainWindow):
    def __init__(self, filepath=None):
        super().__init__()

        self.filepath = filepath

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Scene Editor")

        self.initFormatbar()

        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

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

        # Create/Add Tooblar
        self.formatbar = self.addToolBar("Format")

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
        if self.text.fontWeight() == QFont.Bold:
            self.text.setFontWeight(QFont.Normal)
        else:
            self.text.setFontWeight(QFont.Bold)

    def italic(self):
        state = self.text.fontItalic()
        self.text.setFontItalic(not state)

    def underline(self):
        state = self.text.fontUnderline()
        self.text.setFontUnderline(not state)

    def strike(self):
        # Get current format
        fmt = self.text.currentCharFormat()
        # Invert strike state
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        # Set the format of text
        self.text.setCurrentCharFormat(fmt)

    # Alignment Functions
    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    # Indent/Dedent Functions
    def indent(self, dedent=False):
        # Get the cursor
        cursor = self.text.textCursor()

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