from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


"""
Main Pane Classes
"""
class MainPane(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout, menubar, main widget
        layout = QVBoxLayout()
        menubar = self.initMenubar()
        layout.addWidget(menubar)
        mainWidget = QWidget()

        # Set up mainWidget
        stretch = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        mainWidget.setSizePolicy(stretch)

        # Instatiate Panes
        top = ScenePane()
        text = TextPane()
        left = ChapterPane()

        # Create vbox layout for top and bottom panes
        vbox = QVBoxLayout()
        vboxSplitter = QSplitter(Qt.Vertical)
        vboxSplitter.addWidget(top)
        vboxSplitter.addWidget(text)
        vbox.addWidget(vboxSplitter)
        right = QWidget()
        right.setLayout(vbox)

        # Create hbox layout to hold left pane and right vbox
        hbox = QHBoxLayout()

        hbox.setAlignment(Qt.AlignLeft)
        hboxSplitter = QSplitter(Qt.Horizontal)
        hboxSplitter.addWidget(left)
        hboxSplitter.addWidget(right)
        hboxSplitter.setStretchFactor(0, 0)
        hboxSplitter.setStretchFactor(1, 1)
        hbox.addWidget(hboxSplitter)

        mainWidget.setLayout(hbox)
        layout.addWidget(mainWidget)
        self.setLayout(layout)

    def initMenubar(self):
        menubar = QMenuBar()

        # Add menus
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

        #Set size policy
        stretch = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        menubar.setSizePolicy(stretch)

        return menubar


"""
Text Pane Classes
"""
class TextPane(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        text = TextField()
        vbox.addWidget(text, 10)
        self.setLayout(vbox)


class TextField(QTextEdit):
    def __init__(self):
        super().__init__()


"""
Scene Pane Classes
"""
class ScenePane(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        sceneList = QListWidget()
        vbox.addWidget(sceneList)
        self.setLayout(vbox)


"""
Chapter Pane Classes
"""
class ChapterPane(QListWidget):
    def __init__(self):
        super().__init__()