import requests
from utils import *

def downloadVirusRemovalTools():
    print("Downloading Norton Power Eraser...")
    r = requests.get("https://www.norton.com/npe_latest", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/NPE.exe", "wb").write(r.content)
    print("Downloading Kaspersky Virus Removal Tool...")
    r = requests.get("https://www.kaspersky.com/downloads/free-virus-removal-tool", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/KVRT.exe", "wb").write(r.content)
    print("Downloading Malwarebytes AdwCleaner...")
    r = requests.get("https://adwcleaner.malwarebytes.com/adwcleaner?channel=release", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/adwcleaner.exe", "wb").write(r.content)

def downloadUtilities():
    print("Downloading Win10 utilites...")
    r = requests.get("https://db.MYSITENAME.com/Win10utils.zip", allow_redirects=True, timeout=5)
    open("SourceFiles/ISOimages/Win10.iso", "wb").write(r.content)
    print("Downloading Win11 utilities...")
    r = requests.get("https://db.MYSITENAME.com/Win11utils.zip", allow_redirects=True, timeout=5)
    open("SourceFiles/ISOimages/Win11utils.zip", "wb").write(r.content)
    print("Downloading Win10 utilities checksum...")
    r = requests.get("https://db.MYSITENAME.com/Win10utils.checksum", allow_redirects=True, timeout=5)
    open("SourceFiles/ISOimages/Win10utils.checksum", "wb").write(r.content)
    print("Downloading Win11 utilities checksum...")
    r = requests.get("https://db.MYSITENAME.com/Win11utils.checksum", allow_redirects=True, timeout=5)
    open("SourceFiles/ISOimages/Win11utils.checksum", "wb").write(r.content)
    print("Verifying Win10 utilities download...")
    verify("10")
    print("Verifying Win11 utilities download...")
    verify("11")

def downloadSourceFiles():
    print("Downloading Win10 source file...")
    r = requests.get("https://db.MYSITENAME.com/Win10.zip", allow_redirects=True, timeout=5)
    open("SourceFiles/Win10/Source.zip", "wb").write(r.content)
    print("Downloading Win11 source file...")
    r = requests.get("https://db.MYSITENAME.com/Win11.zip", allow_redirects=True, timeout=5)
    open("SourceFiles/Win11/Source.zip", "wb").write(r.content)
    print("Downloading Win10 source file checksum...")
    r = requests.get("https://db.MYSITENAME.com/Win10.checksum", allow_redirects=True, timeout=5)
    open("SourceFiles/Win10/Source.checksum", "wb").write(r.content)
    print("Downloading Win11 source file checksum...")
    r = requests.get("https://db.MYSITENAME.com/Win11.checksum", allow_redirects=True, timeout=5)
    open("SourceFiles/Win11/Source.checksum", "wb").write(r.content)
    print("Verifying Win10 download...")
    verify("10")
    print("Verifying Win11 download...")
    verify("11")

def downloadAll():
    with open("SourceFiles/downloadedSources", "r") as f:
        downloaded = f.read()
        f.close()
    if downloaded == "false":
        downloadVirusRemovalTools()
        downloadUtilities()
        downloadSourceFiles()
    elif input("Source files are already downloaded, do you want to download them again? (y/n) ") == "y":
        downloadVirusRemovalTools()
        downloadUtilities()
        downloadSourceFiles()
    else:
        pass
