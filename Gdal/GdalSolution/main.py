from osgeo import ogr
def ex1():
    #ex1
    file = ogr.Open("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\AFG_adm2.shp", 1)
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

def ex2():
    #ex2
    # Open connection to file
    file = ogr.Open("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\AFG_adm2.shp", 1)
    layer = file.GetLayer()

    # Define a new field for the layer
    field_defn = ogr.FieldDefn("Distance_B", ogr.OFTInteger)

    # Add the field to the layer
    layer.CreateField(field_defn)

    # Commit the changes to the shapefile
    file.SyncToDisk()

    # Get the index of the new field
    new_field_index = layer.GetLayerDefn().GetFieldIndex("Distance_B")

    # Get the index of the NAME_2 field
    name2_index = layer.GetLayerDefn().GetFieldIndex("NAME_2")

    # Iterate over the features in the layer
    for feature in layer:

        # Get the geometry of the feature
        geometry = feature.GetGeometryRef()

        # Get the name in the NAME_2 field
        name2 = feature.GetField(name2_index)

        # Calculate the distance to the name1_geometry if the name2 matches 'Char Burjak'
        if name2 == 'Char Burjak':
            for current_featureidx in range(len(layer)):
                current_feature = layer.GetFeature(current_featureidx)
                current_geom = current_feature.GetGeometryRef()
                dist = geometry.Distance(current_geom)

            # Set the value of the new field to 1 if the distance is shorter than 1
                if dist < 1:
                    current_feature.SetField('Distance_B', 1)
                else:
                    current_feature.SetField('Distance_B', 0)

            # Save the changes to the feature
                layer.SetFeature(current_feature)

    # Commit the changes to the shapefile
    file.SyncToDisk()
    print('finished updating distance_b values ex2')

def ex_2_b():
    # Open connection to file
    file = ogr.Open("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\AFG_adm2.shp", 1)
    layer = file.GetLayer()

    # Define a new field for the layer
    field_defn = ogr.FieldDefn("ne_counter", ogr.OFTInteger)

    # Add the field to the layer
    layer.CreateField(field_defn)

    for feature in layer:
        neighbor_counter = 0
        geom = feature.GetGeometryRef()

        for i in range(len(layer)):
            comp_feature = layer.GetFeature(i)
            comp_geom = comp_feature.GetGeometryRef()

            if geom.Intersect(comp_geom) and comp_geom != geom:
                neighbor_counter += 1
                
        feature.SetField("ne_counter", neighbor_counter)
        layer.SetFeature(feature)
def ex3():
    #ex3
    file = ogr.Open("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\AFG_adm2.shp", 1)
    source_layer = file.GetLayer()

    # Create a new shapefile for the line-strings
    new_shapefile = ogr.GetDriverByName("ESRI Shapefile").CreateDataSource("C:\\Users\\training\\Desktop\\pandaCourse\\Python\\PythonCovidEx\\Gdal\\Targil1\\newshapefile.shp")

    # Create a new layer in the new shapefile
    new_layer = new_shapefile.CreateLayer("new_layer", geom_type=ogr.wkbLineString)

    # Copy the fields from the source layer to the new layer
    for i in range(source_layer.GetLayerDefn().GetFieldCount()):
        field_defn = source_layer.GetLayerDefn().GetFieldDefn(i)
        new_layer.CreateField(field_defn)

    # Copy the features from the source layer to the new layer
    for source_feature in source_layer:
        source_geometry = source_feature.GetGeometryRef()
        area = source_geometry.GetArea()
        if (area > 1):
            new_feature = ogr.Feature(new_layer.GetLayerDefn())
            new_feature.SetGeometry(source_geometry.Clone())
            for i in range(new_feature.GetFieldCount()):
                new_feature.SetField(i, source_feature.GetField(i))
            new_layer.CreateFeature(new_feature)
            new_feature = None

    # Close the shapefiles
    source_shapefile = None
    new_shapefile = None
