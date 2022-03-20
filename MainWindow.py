
import PyQt6.QtWidgets as qtw
import PyQt6.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        # windows title
        self.setWindowTitle("Portal 2: 32 Players Mod")
        self.setWindowIcon(qtg.QIcon('Resources\Images\icon.png'))
        
        # layout type
        self.setLayout(qtw.QVBoxLayout())
        
        # Elements
        testLabel = qtw.QLabel("please work :)")
        testButton = qtw.QPushButton("mount")
        
        # Elements' customizations
        testLabel.setFont(qtg.QFont('Arial', 20))
        
        # Drawing elements on the window
        self.layout().addWidget(testLabel)
        self.layout().addWidget(testButton)
        
        # showing the window
        self.show()
        
        
        
app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec()