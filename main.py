import sys
from MainWindow import *
from SceneEditor import *

def main():
    app = QApplication(sys.argv)
    """
    main = MainPane()
    main.show()
    """
    # Testing Scene Editor
    scene = SceneEditor()
    scene.show()
    # End Testing Scene Editor

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
