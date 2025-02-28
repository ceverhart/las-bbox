import tomli
from pathlib import Path
import shutil

templatepath = Path(__file__).parent / "las.toml"

# Initialize the las metadata project
def initproject(lasdir, initemplatepath):
    projectini = getproject(lasdir)

    # Need to copy ini template file to the las directory
    if projectini is None:
        lasinipath = lasdir.joinpath('las.toml')

        # Copy las.ini file to metadata folder
        shutil.copy(initemplatepath,lasinipath)

        return lasinipath
    else:
        return projectini

        
# Get the current las.ini config file
def getproject(lasdir):
    laspath = Path(lasdir)
    lasinipath = laspath.joinpath('las.toml')

    if not lasinipath.exists():
        lasinipath = None

    return lasinipath

def readconfig(configpath):
    with open(configpath,mode='rb') as f:
        config = tomli.load(f)

        return config
