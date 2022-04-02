import webbrowser
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import sys


from Views.Ui_MainWindow import Ui_MainWindow
import Scripts.GlobalVariables as GVars
import Scripts.BasicLogger as Logger
import Scripts.RunGame as RG
#----------------------------------------------------------------


class MainUI(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Binding click events
        self.ui.actionGuide.triggered.connect(lambda: self.OpenGuide())
        self.ui.Button_MountMod.clicked.connect(lambda: self.MountMod())
        
        icon = qtg.QIcon()
        icon.addFile("Resources.Images.MainWindowIcon.png",
                     qtc.QSize(), qtg.QIcon.Normal, qtg.QIcon.Off)
        self.setWindowIcon
        # this should be the custom toggle button but i didn't get it to work so i'm giving up for now 
        # self.toggle = qtw.QCheckBox()
        # self.ui.layout = qtw.QHBoxLayout(self)
        # self.ui.layout.addWidget(self.toggle, qtg.Qt.AlignCenter, qtg.Qt.AlignCenter)
        
    def OpenGuide(self):
        guideURL = "https://steamcommunity.com/sharedfiles/filedetails/?id=2458260280"
        webbrowser.open(guideURL)

    def MountMod(self):
        RG.Mount()
    
def OnStart():

    # populate the global variables
    GVars.init()
    x = GVars.AppStartDate

    # logging
    Logger.Log("______________________LAUNCH LOG " + x + "______________________")
    if (GVars.iow):
        Logger.Log("")
        Logger.Log("Windows OS detected!")
    else:
        Logger.Log("")
        Logger.Log("Linux OS detected!")

if __name__ =='__main__':
    app = qtw.QApplication([])
    
    window = MainUI()
    window.show()
    OnStart()
    sys.exit(app.exec())