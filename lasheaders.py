import utilities as lasutils
import header as lasheader

if __name__ == "__main__":
    # Get system path from the user
    lasdir = lasutils.getlaspath()

    # List of LAS/Z file path values
    laspaths = lasutils.readlasdir(lasdir)

    # Iterate LAS/Z path values, get header fields
    for laspath in laspaths:
        lasval = lasheader.getheaderfields(laspath)
