import zlib, init, os, utils
from fastcrc import crc64 as crc

def compareFileChecksum(filePath, checksumPath, sourcePath):
    with open(filePath, "rb") as f:
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
    init.init()

if __name__ == "__main__":
    run()