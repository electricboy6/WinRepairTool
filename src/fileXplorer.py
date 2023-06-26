import utils, os, pickle

class Windows10Dir():
    def __init__():
        global fileList
        fileList = pickle.load("src/WorkingFiles/Win10/fileList.pickle")
    def loadFile(file):
        if file not in fileList:
            raise FileNotFoundError
        return(open(file))
    def loadFileChecksum(file):
        if file not in fileList:
            raise FileNotFoundError
        pathPart1 = str(file).split("src/WorkingFiles/Win10/")[2]
        pathPart2 = pathPart1.split("Source")[2]
        path = pathPart1 + "Checksums" + pathPart2
        return(open(path))