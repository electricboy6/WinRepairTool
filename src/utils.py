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


def unzip(version, unzipDir, doClean):
    if doClean:
        clean(unzipDir)
    with ZipFile("SourceFiles/Win" + version + ".zip", 'r') as zip:
        zip.extractall(unzipDir)
        zip.close()

def verify(version):
    print("Generating checksum of source file...")
    with open("SourceFiles/Win" + version + ".zip", "rb") as f:
        currentCheck = crc.ecma_182(f.read())
        f.close()
    print("Reading original checksum...")
    with open("SourceFiles/Win" + version + ".checksum", "r") as f:
        originalCheck = f.read()
        f.close()
    if int(currentCheck) == int(originalCheck):
        print("Checksums match - moving on...")
    else:
        raise Exception("Source checksums do not match!")
    
if __name__ == "__main__":
    print("Generating checksum...")
    with open("SourceFiles/Win10.zip", "rb") as f:
        checksum = crc.ecma_182(f.read())
        f.close()
    print("Writing checksum to file...")
    with open("SourceFiles/Win10.checksum", "w") as f:
        f.write(str(checksum))
        f.close()
