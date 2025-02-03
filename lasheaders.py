import utilities as lasutils
import header as lasheader

# ini template path
inipath = r'C:\Development\geospatialdm\src\las\config\las.ini'

if __name__ == "__main__":

    # Get system path from the user
    lasdir = lasutils.getlaspath()

    # Initialize the project, including get or create output path
    lasutils.initproject(lasdir, inipath)

    # List of LAS/Z file path values
    laspaths = lasutils.readlasdir(lasdir)

    # Iterate LAS/Z path values, get header fields
    alllasdata = []
    for laspath in laspaths:
        lasdata = lasheader.collectheaderdata(laspath)
        lasdata['filename'] = lasutils.getfilename(laspath)
        alllasdata.append(lasdata)
    print(alllasdata)
