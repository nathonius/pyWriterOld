from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TextPane(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.initFormatbar()
        self.initUI()

    def initUI(self):
        text = TextField()
        self.addWidget(text, 10)

    def initFormatbar(self):
        bar = QToolBar("Format")
        
        self.addWidget(bar)


class TextField(QTextEdit):
    def __init__(self):
        super().__init__()