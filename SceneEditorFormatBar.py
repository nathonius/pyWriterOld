import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FormatBar(QToolBar):
    def __init__(self, text):
        super().__init__()
        self.sceneText = text
        self.initFormatbar()

    def initFormatbar(self):
        # Create Format Actions
        boldAction = QAction(QIcon("icons/bold.png"), "Bold", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QAction(QIcon("icons/italic.png"), "Italic", self)
        italicAction.triggered.connect(self.italic)

        underlineAction = QAction(QIcon("icons/underline.png"), "Underline", self)
        underlineAction.triggered.connect(self.underline)

        strikeAction = QAction(QIcon("icons/strike.png"), "Strike-Through", self)
        strikeAction.triggered.connect(self.strike)

        # Create Alignment Actions
        alignLeftAction = QAction(QIcon("icons/alignLeft.png"), "Align Left", self)
        alignLeftAction.triggered.connect(self.alignLeft)

        alignCenterAction = QAction(QIcon("icons/alignCenter.png"), "Align Center", self)
        alignCenterAction.triggered.connect(self.alignCenter)

        alignRightAction = QAction(QIcon("icons/alignRight.png"), "Align Right", self)
        alignRightAction.triggered.connect(self.alignRight)

        alignJustifyAction = QAction(QIcon("icons/alignJustify.png"), "Align Justify", self)
        alignJustifyAction.triggered.connect(self.alignJustify)

        # Create Indent/Dedent Actions
        indentAction = QAction(QIcon("icons/indent.png"), "Indent", self)
        indentAction.triggered.connect(self.indent)

        dedentAction = QAction(QIcon("icons/dedent.png"), "Dedent", self)
        dedentAction.triggered.connect(self.dedent)

        # Add Format Actions
        self.addAction(boldAction)
        self.addAction(italicAction)
        self.addAction(underlineAction)
        self.addAction(strikeAction)
        self.addSeparator()

        # Add Alignment Actions
        self.addAction(alignLeftAction)
        self.addAction(alignCenterAction)
        self.addAction(alignRightAction)
        self.addAction(alignJustifyAction)
        self.addSeparator()

        # Add Indent/Dedent Actions
        self.addAction(indentAction)
        self.addAction(dedentAction)
        self.addSeparator()

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
            atStart = True
            if cursor.position() is cursor.selectionEnd():
                atStart = False
            # Get first line/block number
            block = cursor.blockNumber()
            # Figure out how many lines are in selection
            if atStart:
                cursor.setPosition(cursor.selectionEnd())
                lines = cursor.blockNumber() - block
            else:
                cursor.setPosition(cursor.selectionStart())
                lines = block - cursor.blockNumber()

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
                if atStart:
                    cursor.movePosition(QTextCursor.Up)
                else:
                    cursor.movePosition(QTextCursor.Down)

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