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
        vbox = QVBoxLayout(self.chapterSelect)
        selectHbox = QHBoxLayout(self.chapterSelect)
        acceptHbox = QHBoxLayout(self.chapterSelect)


        chapterLbl = QLabel(self.chapterSelect)
        chapterLbl.setText("Chapter:")
        chapterBox = self.initChapterBox()

        sceneLbl = QLabel(self.chapterSelect)
        sceneLbl.setText("Scene:")
        sceneBox = self.initSceneBox()

        # Create the buttons
        prevButton = QPushButton("Prev", self.chapterSelect)
        nextButton = QPushButton("Next", self.chapterSelect)
        saveButton = QPushButton("Save", self.chapterSelect)
        saveExitButton = QPushButton("Save and Exit", self.chapterSelect)
        # Connect the buttons. They call the same functions,
        # but the source parameter makes the functions act differently
        prevButton.clicked[bool].connect(self.selectChapter)
        nextButton.clicked[bool].connect(self.selectChapter)
        saveButton.clicked[bool].connect(self.save)
        saveExitButton.clicked[bool].connect(self.save)

        selectHbox.addWidget(chapterLbl)
        selectHbox.addWidget(chapterBox)
        selectHbox.addWidget(sceneLbl)
        selectHbox.addWidget(sceneBox)
        acceptHbox.addWidget(prevButton)
        acceptHbox.addWidget(nextButton)
        acceptHbox.addWidget(saveButton)
        acceptHbox.addWidget(saveExitButton)

        vbox.addLayout(selectHbox)
        vbox.addLayout(acceptHbox)
        self.chapterSelect.setLayout(vbox)

    def initChapterBox(self):
        box = QComboBox(self.chapterSelect)
        pass
        return box

    def initSceneBox(self):
        box = QComboBox(self.chapterSelect)
        pass
        return box

    def selectChapter(self):
        pass

    def save(self):
        pass