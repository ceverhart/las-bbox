import utilities as lasutils
import header as lasheader

if __name__ == "__main__":
    # ini template path
    inipath = r'C:\Development\geospatialdm\src\las\config\las.ini'

    # Get system path from the user
    lasdir = lasutils.getlaspath()

    # Initialize the project, including get or create output path
    lasutils.initproject(lasdir, inipath)

    # List of LAS/Z file path values
    laspaths = lasutils.readlasdir(lasdir)

    # Iterate LAS/Z path values, get header fields
    for laspath in laspaths:
        lasval = lasheader.getheaderfields(laspath)
