import requests
from utils import *

def downloadVirusRemovalTools():
    print("Downloading Norton Power Eraser...")
    r = requests.get("https://buy-download.norton.com/downloads/premium_services/NPE/x64/prod/NPE.exe", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/NPE.exe", "wb").write(r.content)
    print("Downloading Kaspersky Virus Removal Tool...")
    r = requests.get("https://usa.kaspersky.com/downloads/free-virus-removal-tool", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/KVRT.exe", "wb").write(r.content)
    print("Downloading Malwarebytes AdwCleaner...")
    r = requests.get("https://adwcleaner.malwarebytes.com/adwcleaner?channel=release", allow_redirects=True, timeout=5)
    open("VirusRemovalTools/adwcleaner.exe", "wb").write(r.content)

def downloadSourceFiles():
    print("Downloading Win10 source file...")
    downloadLargeFile("https://db.MYSITENAME.com/Win10.zip", "src/SourceFiles/Win10/Source.zip")
    print("Downloading Win11 source file...")
    downloadLargeFile("https://db.MYSITENAME.com/Win11.zip", "src/SourceFiles/Win11/Source.zip")
    print("Downloading Win10 source file checksum...")
    downloadFile("https://db.MYSITENAME.com/Win10.checksum", "src/SourceFiles/Win10/Source.checksum")
    print("Downloading Win11 source file checksum...")
    downloadFile("https://db.MYSITENAME.com/Win11.checksum", "src/SourceFiles/Win11/Source.checksum")
    print("Verifying Win10 source download...")
    verify("10")
    print("Verifying Win11 source download...")
    verify("11")

def downloadLargeFile(url, path):
    with requests.get(url, stream=True, allow_redirects=True, timeout=5) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def downloadFile(url, path):
    r = requests.get(url, allow_redirects=True, timeout=5)
    open(path, "wb").write(r.content)

def downloadAll():
    with open("src/SourceFiles/downloadedSources.txt", "r") as f:
        downloaded = f.read()
        f.close()
    if downloaded == "false":
        downloadVirusRemovalTools()
        #downloadSourceFiles()
        with open("src/SourceFiles/downloadedSources.txt", "w") as f:
            f.write("true")
            f.close()
    elif input("Source files are already downloaded, do you want to download them again? (y/n) ") == "y":
        downloadVirusRemovalTools()
        #downloadSourceFiles()
        with open("src/SourceFiles/downloadedSources.txt", "w") as f:
            f.write("true")
            f.close()
    else:
        pass
