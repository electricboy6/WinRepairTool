import zlib, init, os, utils
from fastcrc import crc64 as crc
import fileXplorer as fxplorer

def compareFileChecksum(filePath, checksumPath, sourcePath):
    with open(versionExplorer.loadFile(filePath), "rb") as f:
        fileCheck = crc.ecma_182(f.read())
        f.close()
    with open(checksumPath, "rb") as f:
        checksum = f.read()
        f.close()
    if fileCheck != checksum:
        print(filePath + " did not match source files. Replacing with known good file...")
        with open(sourcePath, "rb") as goodFile:
            with open(filePath, "wb") as badFile:
                badFile.write(goodFile.read())
                badFile.close()
            goodFile.close()

def run():
    global explorer, versionExplorer
    init.init()
    if init.version == "10":
        versionExplorer = fxplorer.Windows10()
    else:
        versionExplorer = fxplorer.Windows11()
    explorer = fxplorer.Explorer()
    fileList = explorer.getFileList()
    for file in fileList:
        compareFileChecksum("file", versionExplorer.loadFileChecksum(file), explorer.loadFile(file))

if __name__ == "__main__":
    run()