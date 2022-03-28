import os
import Scripts.GlobalVariables as GVars

def Log(message):
    # get the path of the python file and set the directory to it
    path = os.path.dirname(os.path.realpath(__file__))
    # if there is open it as utf-8 but dont delete the contents
    with open(path + GVars.nf + "Log-"+GVars.AppStartDate+".log", "a", encoding="utf-8") as log:
        # write the message to the log
        log.write(message + "\n")
        log.write(GVars.AppStartDate)
        # close the log
        log.close()
    print("(P2:MM): " + message)
