import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from SceneEditorFormatBar import FormatBar
import os.path


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initTabs()

    def initTabs(self):
        # Create each tab
        contentTab = QWidget(self)
        detailsTab = QWidget(self)
        charactersTab = QWidget(self)
        locationsTab = QWidget(self)
        itemsTab = QWidget(self)
        notesTab = QWidget(self)
        pictureTab = QWidget(self)
        goalsTab = QWidget(self)
        exportingTab = QWidget(self)
        timeTab = QWidget(self)
        ratingsTab = QWidget(self)

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
        self.addTab(contentTab, "Content")
        self.addTab(detailsTab, "Details")
        self.addTab(charactersTab, "Characters")
        self.addTab(locationsTab, "Locations")
        self.addTab(itemsTab, "Items")
        self.addTab(notesTab, "Notes")
        self.addTab(pictureTab, "Picture")
        self.addTab(goalsTab, "Goals")
        self.addTab(exportingTab, "Exporting")
        self.addTab(timeTab, "Time")
        self.addTab(ratingsTab, "Ratings")

    def openFile(self, filepath):
        """Called from SceneEditor every time a new scene is selected in the bottom select pane."""
        if os.path.isfile(filepath):
            with open(filepath, "rt") as fp:
                self.sceneText.setText(fp.read())
        else:
            raise(IOError)