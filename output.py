import geopandas
from shapely import box

# entrypoint for all output
def headeroutput(headerdata, outdir):
    outpath = outdir.joinpath("las_bbox.shp")
    headercount = len(headerdata['filename'])

    # Build box geometry
    bbox_data = []
    for ind in range(headercount):
        xmin = headerdata['boundingcoords'][ind]['minx']
        ymin = headerdata['boundingcoords'][ind]['miny']
        xmax = headerdata['boundingcoords'][ind]['maxx']
        ymax = headerdata['boundingcoords'][ind]['maxy']
        bbox_geom = box(xmin, ymin, xmax, ymax, ccw=True)

        bbox_data.append(bbox_geom)

    # Add geometry to header data
    headerdata['geometry'] = bbox_data

    gdf_bbox = geopandas.GeoDataFrame(headerdata, geometry='geometry', crs="EPSG:6428")
    gdf_bbox.drop(columns=['boundingcoords'], inplace=True)

    gdf_bbox.to_file(outpath)

