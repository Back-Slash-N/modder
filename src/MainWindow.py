from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import Qt


from Views.Ui_MainWindow import Ui_MainWindow
import Scripts.GlobalVariables as GVars
import Scripts.BasicLogger as Logger
#----------------------------------------------------------------


class MainUI(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        
        self.setupUi(self)
        
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
    app.exec_()