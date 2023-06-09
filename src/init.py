from fastcrc import crc64 as crc
from utils import *
import downloader, updater

def init():
    updater.checkForUpdate()
    downloader.downloadAll()
    clean("WorkingFiles")
    version = getVersion()
    verify(version)
    unzip("SourceFiles/Win" + version + "/Source.zip", "WorkingFiles/Win" + version + "/Source", True)
    unzip("SourceFiles/Win" + version + "/Checksums.zip", "WorkingFiles/Win" + version + "/Checksums", True)

def getVersion():
    print("What version of Windows are you trying to repair? (10/11)")
    temp = input()
    if temp == "10" or temp == "11":
        return(temp)
    else:
        getVersion()