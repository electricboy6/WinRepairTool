from utils import *
import downloader, updater

def init():
    global version
    updater.checkForUpdate()
    downloader.downloadAll()
    clean("WorkingFiles")
    version = getVersion()
    verify(version)
    unzipLarge("src/SourceFiles/Win" + version + "/Source.zip", "src/WorkingFiles/Win" + version + "/Source", True)
    unzipLarge("src/SourceFiles/Win" + version + "/Checksums.zip", "src/WorkingFiles/Win" + version + "/Checksums", True)

def getVersion():
    print("What version of Windows are you trying to repair? (10/11)")
    temp = input()
    if temp == "10" or temp == "11":
        return(temp)
    else:
        getVersion()