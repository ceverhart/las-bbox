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

# TODO: Create output folder (metadata, product, other)
def createoutputdir(parentpath, dirname='las_',dirype=None):
    # TODO: catch exception and log error if unable to create output path
    parpath = Path(parentpath)
    if Path(parentpath).exists():
        outdirpath = parpath.joinpath(dirname)
        outdirpath.mkdir()
            
# Find output dir. Will have a las.ini file
    

# TODO: Copy las.ini file to metadata folder

