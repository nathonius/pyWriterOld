import sys
from MainPane import *

def main():
    app = QApplication(sys.argv)
    main = MainPane()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
