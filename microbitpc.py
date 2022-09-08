#Adapted from: Dr. Ron van Schyndel's Tutorial
from datetime import time

import microfs
import serial

def restartMB(com):
    """
    Starts the microbit program 'main.py'
    """
    wr = "import main" + chr(13)
    com.write(wr.encode())

def stopMB(com):
    """
    Stops the running program on the microbit
    """
    wr = chr(3)                   # ctrl-C to stop the running program
    com.write(wr.encode())

def resetMB(com):
    """
    Resets the microbit without losing internal data
    """
    stopMB(com)                      # Reset without losing data or files
    wr = "from microbit import reset"+chr(13)
    wr += "reset()"+chr(13)     # use internal reset function
    com.write(wr.encode())      # to reset+run main.py if it exists

def openMB():
    """
    Gets serial port microbit is connected
    """
    com = microfs.get_serial()       # that micro:bit is connected to.
    return com

def readMB(com, num=99999):
    """
    Reads from given serial port
    """
    ln = com.read(num)            # port until exhausted
    return ln

def writeMB(com, ln=""):
    """
    Writes to currently open serial port
    """
    num = com.write(ln.encode())
    return num

def closeMB(com):
    """
    Closes serial port
    """
    com.close()

def main():
    c = openMB()              # open relevant COM port for MB
    resetMB(c)     # reset MB, then run main.py if on device
    time.sleep(1)
    ln = readMB(c,50)       # read 50 bytes from MB into ln
    print(ln)
    closeMB(c)
    return 0


if __name__ == "__main__":
    main()

