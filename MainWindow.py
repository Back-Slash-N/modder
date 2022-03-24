from selectors import SelectorKey
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # app dimensions
        windowWidth = 400
        windowHeight = 400
        # this is to start the app in the center of the screen
        primaryScreenInfo = app.primaryScreen()
        startPositionX = int(primaryScreenInfo.size().width() / 2) - int(windowWidth / 2)
        startPositionY = int(primaryScreenInfo.size().height() / 2) - int(windowHeight / 2)
        self.setGeometry(startPositionX, startPositionY, windowWidth, windowHeight)

        self.setWindowTitle("portal 2 | 32 Players mod")
        self.initUI()
    
    # defining elements
    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("please work :)")
        self.label1.move(100,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("mount")
        self.b1.clicked.connect(self.MountClicked)

    def MountClicked(self):
        self.label1.setText("mounting... ok i guess the mount finished")
        self.update()

    def update(self):
        self.label1.adjustSize()

def window():
    global app
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
window()