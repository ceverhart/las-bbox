import glob
from pathlib import Path

# Get LAS/LAZ file path list from directory
def readlasdir(lasdir):
    laspath = Path(lasdir)
    return list(laspath.glob('**/*.la[z,s]'))

# Get path to folder with LAS/Z files from the user
def getlaspath():
    while True:
        laspath = Path(input("Enter path to LAS/LAZ files: "))
        if laspath.exists():
            return laspath
        else:
            print("Invalid folder path.")

# TODO: Create metadata folder
# TODO: Copy header_field_properties.py file to metadata folder

