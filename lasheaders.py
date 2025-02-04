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
    lasdata = []
    for laspath in laspaths:
        lashead = lasheader.collectheaderdata(laspath)
        lashead['filename'] = lasutils.getfilename(laspath)
        lasdata.append(lashead)

    # Pass to function that will generate output
    print(lasdata)

    # Create the output folder
    outdirmsg = lasutils.createoutputdir(lasdir, dirname='las_bbox',dirype=None)
    print(outdirmsg)
