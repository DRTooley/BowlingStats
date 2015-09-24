__author__ = 'david'
import sys

from PyQt5.QtWidgets import *

from statviewer import statViewer


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWindow = statViewer()
    mainWindow.show()

    sys.exit(app.exec_())