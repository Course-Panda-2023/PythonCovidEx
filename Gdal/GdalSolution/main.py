from osgeo import ogr

file = ogr.Open("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\AFG_adm2.shp")
# shape = file.GetLayer(0)
#first feature of the shapefile
# feature = shape.GetFeature(0)
#first = feature.ExportToJson()
layer = file.GetLayer()

for feature in layer:
    geom = feature.GetGeometryRef()
    area = geom.GetArea()
    if (area>1):
        print ('NAME2: ' + str(feature.Name_2))
        print ('area: ' + str(area))
        print ('FID: ' + str(feature.GetFID()))

        # Make sure the geometry is a polygon
        if geom.GetGeometryName() == 'POLYGON':

            # Get the number of rings in the polygon
            num_rings = geom.GetGeometryCount()

            # Iterate over the rings in the polygon
            for i in range(num_rings):

                # Get the points in the ring
                ring = geom.GetGeometryRef(i)
                num_points = ring.GetPointCount()

                # Iterate over the points in the ring
                for j in range(num_points):
                    point = ring.GetPoint(j)
                    print("Vertex ", j, ": ", point)
                print()