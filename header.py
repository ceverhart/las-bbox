'''
LAS/LAZ file heder tools
'''
import laspy

def getheader(laspath):
    lasfile = laspy.open(laspath)
    return lasfile.header

def getfield(laspath, fieldname):
    header = getheader(laspath)
    headerval = getattr(header,fieldname)
    return headerval

def getheaderfields(laspath):
    header = getheader(laspath)
    lasfields = dir(header)
    lasfields.sort()
    return lasfields

def getboundingcoords(laspath):
    header = getheader(laspath)
    mins = header.mins
    maxs = header.maxs
    boundingcoords = {'minx': mins[0].item(), 'miny': mins[1].item(),'maxx': maxs[0].item(),'maxy': maxs[1].item()}
    return boundingcoords

def collectheaderdata(laspath):
    # Collect file data, name and bounding coordinates default
    headerdata = {'filename':'','boundingcoords':None}
    
    headerdata['boundingcoords'] = getboundingcoords(laspath)

    return headerdata
    
