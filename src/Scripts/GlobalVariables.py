# this is a file to store all the global variables needed
# it's initiated only once when the mainwindow is created

import datetime
import os
#import Configs as cfg

# AppStartDate is the dateTime when the app was started so the logging won't break if we enter a new day
    # if only kids learned to never use the computer after 10pm i wouldn't have needed to do this
    
    
AppStartDate = ""
configdata = ""

# iow = is on windows
# yes i'll default to windows, cry about it
iow = True
nf = "\\"


def init():
    AppStartDate = datetime.date.today().strftime('%Y-%m-%d %H-%M-%S')
    # configdata = cfg.ImportConfig()
    if os.name != "nt":
        iow = False
        nf = "/"


