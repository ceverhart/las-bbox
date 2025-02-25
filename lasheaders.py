import utilities as lasutils
import header as lasheader
import output as lasoutput

# ini template path
inipath = r'C:\Development\geospatialdm\src\las\config\las.toml'

if __name__ == "__main__":

    # Get system path from the user
    lasdir = lasutils.getlaspath()

    # Initialize the project, including get or create output path
    lasutils.initproject(lasdir, inipath)

    # List of LAS/Z file path values
    laspaths = lasutils.readlasdir(lasdir)

    # Iterate LAS/Z path values, get header fields
    lasdata = lasheader.getheaderdatashell()
    for laspath in laspaths:
        lashead = lasheader.collectheaderdata(laspath)
        for key in lashead.keys():
            if key == 'filename':
                lasname = lasutils.getfilename(laspath)
                lasdata['filename'].append(lasname)
            else:
                lasdata[key].append(lashead[key])

    # Create the output folder
    outdir = lasutils.createoutputdir(lasdir, dirname='las_bbox',dirype=None)
    print(outdir)

    # Pass to function that will generate output
    lasoutput.headeroutput(lasdata, outdir)
