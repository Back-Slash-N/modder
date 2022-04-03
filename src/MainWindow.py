import webbrowser
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import sys


from Views.Ui_MainWindow import Ui_MainWindow
import Scripts.GlobalVariables as GVars
from Scripts.BasicLogger import Log
import Scripts.RunGame as RG
from requests import get
#----------------------------------------------------------------


class MainUI(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Binding click events
        self.ui.actionGuide.triggered.connect(lambda: self.OpenGuide())
        self.ui.Button_Guide.clicked.connect(lambda: self.OpenGuide())
        self.ui.Button_Play.clicked.connect(lambda: self.MountMod())
        self.ui.Button_Discord.clicked.connect(lambda: self.DiscordInvite())
        self.ui.button_CopyIP.clicked.connect(lambda: self.CopyIp())
        # this should be the custom toggle button but i didn't get it to work so i'm giving up for now 
        # self.toggle = qtw.QCheckBox()
        # self.ui.layout = qtw.QHBoxLayout(self)
        # self.ui.layout.addWidget(self.toggle, qtg.Qt.AlignCenter, qtg.Qt.AlignCenter)
        
    def OpenGuide(self):
        guideURL = "https://steamcommunity.com/sharedfiles/filedetails/?id=2458260280"
        webbrowser.open(guideURL)
        Log("Opened the steam guide")

    def MountMod(self):
        RG.Mount()
    
    def DiscordInvite(self):
        discordUrl = "https://discord.com/invite/kW3nG6GKpF"
        webbrowser.open(discordUrl)
        Log("Opened the discord invite")
        
    def GetIp(self):
        ip = get('https://api.ipify.org').text
        self.ui.button_CopyIP.setText(ip)
        Log("Got the ip: " + ip)
    
    def CopyIp(self):
        qtw.QApplication.clipboard().setText(self.ui.button_CopyIP.text())
        Log("coppied the ip: " + self.ui.button_CopyIP.text())
    
def OnStart():

    # populate the global variables
    GVars.init()
    x = GVars.AppStartDate

    # logging
    Log("______________________LAUNCH LOG " + x + "______________________")
    if (GVars.iow):
        Log("")
        Log("Windows OS detected!")
    else:
        Log("")
        Log("Linux OS detected!")

if __name__ =='__main__':
    app = qtw.QApplication([])
    window = MainUI()
    OnStart()
    window.GetIp()
    window.show()
    sys.exit(app.exec())