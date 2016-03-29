import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from FormatBar import FormatBar


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
        self.sceneText = QTextEdit(contentTab)
        self.formatbar = FormatBar(self.sceneText)
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