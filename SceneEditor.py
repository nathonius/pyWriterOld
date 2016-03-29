import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from SceneEditorTabs import Tabs


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
        self.tabs = Tabs()

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

    def initChapterSelect(self):
        pass