import json

class Windows10():

    def __init__():
        global fileList
        fileList = json.load("src/WorkingFiles/Win10/fileList.json")

    def loadFileChecksum(file):
        if file not in fileList:
            raise FileNotFoundError
        pathPart1 = str(file).split("src/WorkingFiles/Win10/")[2]
        pathPart2 = pathPart1.split("Source")[2]
        path = pathPart1 + "Checksums" + pathPart2
        return(open(path))
    
    
class Windows11():

    def __init__():
        global fileList
        fileList = json.load("src/WorkingFiles/Win11/fileList.json")
    
    def loadFileChecksum(file):
        if file not in fileList:
            raise FileNotFoundError
        pathPart1 = str(file).split("src/WorkingFiles/Win11/")[2]
        pathPart2 = pathPart1.split("Source")[2]
        path = pathPart1 + "Checksums" + pathPart2
        return(path)
    
class Explorer():
    
    def getFileList():
        return(fileList)
    
    def loadFile(path):
        if path not in fileList:
            raise FileNotFoundError
        return(path)