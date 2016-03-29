from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


"""
Main Pane Classes
"""
class MainPane(QWidget):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()
        self.initUI(mainLayout)
        self.setLayout(mainLayout)

    def initUI(self, layout):
        # Instatiate
        top = ScenePane()
        text = TextPane()
        left = ChapterPane()
        menubar = self.initMenubar()
        layout.addWidget(menubar)

        # Create hbox layout for top and bottom panes
        vbox = QVBoxLayout()
        vbox.addWidget(top, 5)
        vbox.addLayout(text, 5)

        # Create vbox layout to hold left pane and right hbox
        hbox = QHBoxLayout()

        hbox.setAlignment(Qt.AlignLeft)
        hbox.addWidget(left, 3)
        hbox.addLayout(vbox, 7)

        layout.addLayout(hbox)

    def initMenubar(self):
        menubar = QMenuBar()

        file = menubar.addMenu("File")
        print = menubar.addMenu("Print")
        search = menubar.addMenu("Search")
        chapter = menubar.addMenu("Chapter")
        scene = menubar.addMenu("Scene")
        characters = menubar.addMenu("Characters")
        locations = menubar.addMenu("Locations")
        items = menubar.addMenu("Items")
        tools = menubar.addMenu("Tools")
        localise = menubar.addMenu("Localise")
        help = menubar.addMenu("Help")

        return menubar


"""
Text Pane Classes
"""
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


"""
Scene Pane Classes
"""
class ScenePane(QListWidget):
    def __init__(self):
        super().__init__()


"""
Chapter Pane Classes
"""
class ChapterPane(QListWidget):
    def __init__(self):
        super().__init__()