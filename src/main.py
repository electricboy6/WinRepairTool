import zlib, init, os, utils
from fastcrc import crc64 as crc

def compareFileChecksum(path):
    with open(path, "rb") as f:
        fileCheck = crc.ecma_182(f.read())

init.init()