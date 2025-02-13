import glob
import shutil
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
    # Catch exception and log error if unable to create output path
    parpath = Path(parentpath)
    if Path(parentpath).exists():
        outdirpath = parpath.joinpath(dirname)

        result = None
        try:
            outdirpath.mkdir()
        except FileExistsError:
            result = outdirpath
        else:
            result = outdirpath
    return result

# Initialize the las metadata project
def initproject(lasdir, initemplatepath):
    projectini = getproject(lasdir)

    # Need to copy ini template file to the las directory
    if projectini is None:
        lasinipath = lasdir.joinpath('las.ini')

        # Copy las.ini file to metadata folder
        shutil.copy(initemplatepath,lasinipath)
        
# Get the current las.ini config file
def getproject(lasdir):
    laspath = Path(lasdir)
    lasinipath = laspath.joinpath('las.ini')

    if not lasinipath.exists():
        lasinipath = None

    return lasinipath

def getfilename(laspath):
    fpath = Path(laspath)
    fname = fpath.name
    return fname

