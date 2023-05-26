import requests, os
from zipfile import ZipFile

def checkForUpdate():
    print("Checking for updates...")
    v = requests.get("https://raw.githubusercontent.com/electricboy6/WinRepairTool/main/program.version", allow_redirects=True, timeout=5)
    v = v.text
    currentV = open("program.version").read()
    if not v == currentV:
        print("Found update - Downloading...")
        r = requests.get("https://api.github.com/repos/electricboy6/WinRepairTool/releases/latest", allow_redirects=True, timeout=5)
        version = r.json()["tag_name"]
        r = requests.get("https://github.com/electricboy6/WinRepairTool/archive/refs/tags/" + version + ".zip", allow_redirects=True, timeout=5)
        try:
            os.mkdir("src/newVersion")
            f = open("src/newVersion/source.zip", "x")
            f.close()
        except FileExistsError:
            pass
        open("src/newVersion/source.zip", "wb").write(r.content)
        print("Extracting...")
        with ZipFile("src/newVersion/source.zip", "r") as zip:
            zip.extractall("src/newVersion/")
            zip.close()
        os.remove("src/newVersion/source.zip")
        raise Exception("Please use the latest version. Hint: it's located at src/newVersion.")
    else:
        print("You're on the latest version!")
