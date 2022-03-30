import webbrowser
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import Qt
import sys

from Views.Ui_MainWindow import Ui_MainWindow
import Scripts.GlobalVariables as GVars
import Scripts.BasicLogger as Logger
import Scripts.RunGame as RG
#----------------------------------------------------------------


class MainUI(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        
        # Binding click events
        self.actionGuide.triggered.connect(lambda: self.OpenGuide())
        self.Button_MountMod.clicked.connect(lambda: self.MountMod())
        
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
    
    widget = MainUI()
    widget.show()
    OnStart()
    sys.exit(app.exec_())