import glob
from pathlib import Path

# Get LAS/LAZ file path list from directory
def readlasdir(lasdir):
    laspath = Path(lasdir)
    return list(laspath.glob('**/*.la[z,s]'))

def getlaspath():
    path = input("Enter path to LAS/LAZ files: ")
    laspath = Path(path)

    while not laspath.exists():
        path = input("Enter path to LAS/LAZ files: ")
        laspath = Path(path)
    else:
        return laspath

# TODO: Create metadata folder
# TODO: Copy header_field_properties.py file to metadata folder

