from fastcrc import crc64 as crc
from utils import *

def init():
    clean("WorkingFiles")
    version = getVersion()
    verify(version)
    unzip(version, "WorkingFiles/Source", True)

def getVersion():
    print("What version of Windows are you trying to repair? (10/11)")
    temp = input()
    if temp == "10" or temp == "11":
        return(temp)
    else:
        getVersion()