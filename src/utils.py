from zipfile import ZipFile
from fastcrc import crc64 as crc
import os, glob

def clean(dir):
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        try:
            os.remove(f)
        except IsADirectoryError:
            pass


def unzip(file, unzipDir, doClean):
    if doClean:
        clean(unzipDir)
    with ZipFile(file, 'r') as zip:
        zip.extractall(unzipDir)
        zip.close()

def verify(version):
    print("Generating checksum of source file...")
    with open("src/SourceFiles/Win" + version + "/Source.zip", "rb") as f:
        currentCheck = crc.ecma_182(f.read())
        f.close()
    print("Reading original checksum...")
    with open("src/SourceFiles/Win" + version + "/Source.checksum", "r") as f:
        originalCheck = f.read()
        f.close()
    if int(currentCheck) == int(originalCheck):
        print("Checksums match - moving on...")
    else:
        raise Exception("Source checksums do not match!")
    
if __name__ == "__main__":
    print("Generating Win10 checksum...")
    with open("src/SourceFiles/Win10/Source.zip", "rb") as f:
        checksum = crc.ecma_182(f.read())
        f.close()
    print("Writing Win10 checksum to file...")
    with open("src/SourceFiles/Win10/Source.checksum", "w") as f:
        f.write(str(checksum))
        f.close()
    print("Generating Win11 checksum...")
    with open("src/SourceFiles/Win11/Source.zip", "rb") as f:
        checksum = crc.ecma_182(f.read())
        f.close()
    print("Writing Win11 checksum to file...")
    with open("src/SourceFiles/Win11/Source.checksum", "w") as f:
        f.write(str(checksum))
        f.close()