from osgeo import ogr

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

#ex2
# Define a new field for the layer
# field_defn = ogr.FieldDefn("Distance_B", ogr.OFTInteger)

# Add the field to the layer
#layer.CreateField(field_defn)

# Commit the changes to the shapefile
#file.SyncToDisk()

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
        print('found char burjak')
        for current_featureidx in range(len(layer)):
            current_feature = layer.GetFeature(current_featureidx)
            current_geom = current_feature.GetGeometryRef()
            dist = geometry.Distance(current_geom)
            print('calculated distance with '+ current_feature.Name_2 + ' distance: '+str(dist))

        # Set the value of the new field to 1 if the distance is shorter than 1
            if dist < 1:
                current_feature.SetField('Distance_B', 1)
                print('set to 1')
            else:
                current_feature.SetField('Distance_B', 0)
                print('set to 0')

        # Save the changes to the feature
            layer.SetFeature(current_feature)

# Commit the changes to the shapefile
file.SyncToDisk()
print('finished running ex2')
