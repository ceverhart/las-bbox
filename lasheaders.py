import utilities as lasutils
import header as lasheader

if __name__ == "__main__":
    #lasdir = r'C:\Development\Data\ColoradoLiDAR'
    lasdir = lasutils.getlaspath()
    laspaths = lasutils.readlasdir(lasdir)
    print(laspaths)

    for laspath in laspaths:
        lasval = lasheader.getheaderfields(laspath)

        print(lasheader.getboundingcoords(laspath))

        print(lasheader.getfield(laspath, 'point_count'))
    
