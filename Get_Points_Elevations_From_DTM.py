import geopandas as gpd
import rasterio
import os

def reading_the_points_feature(YOUR_POINTS_FEATURE):
    """
    Read the points feature file and return it as a GeoDataFrame.

    :param YOUR_POINTS_FEATURE: The path to the points feature file (either shapefile or feature class).
    :return: A tuple containing the GeoDataFrame of the points feature and the type of the points feature file.
    """
    feature = gpd.GeoDataFrame()
    
    if YOUR_POINTS_FEATURE.lower().endswith('.shp'):
        points_features_type = 'shapefile'
        feature = gpd.read_file(YOUR_POINTS_FEATURE, driver="ESRI Shapefile")
    elif '.gdb' in YOUR_POINTS_FEATURE.lower():
        GDB = YOUR_POINTS_FEATURE.split('gdb')[0] + 'gdb'  # get the fileGDB path
        layer = os.path.basename(YOUR_POINTS_FEATURE)  # get the feature class name
        feature = gpd.read_file(GDB, layer=layer)  # read feature class from geodatabase
        points_features_type = 'featureclass'
    return feature, points_features_type

def reading_the_DTM(YOUR_DTM_RASTER):
    """
    Read the DTM raster file and return the raster object.

    :param YOUR_DTM_RASTER: The path to the DTM raster file.
    :return: The raster object if the file is valid, otherwise None.
    """
    if YOUR_DTM_RASTER.lower().endswith('.tif'):
        try:
            DTM_raster = rasterio.open(YOUR_DTM_RASTER)
            return DTM_raster
        except Exception as e:
            print(f"Error: {e}")
            return None  
    else:
        print("Please provide a valid DTM raster file ending with ---> .tif")
        return None

def get_points_elevations_from_DTM(points_gdf, DTM_raster, elevations_field="DTM_Elev"):
    """
    Extract elevation values from the DTM raster and add them to the points GeoDataFrame.

    :param points_gdf: The GeoDataFrame containing point features.
    :param DTM_raster: The DTM raster object.
    :param elevations_field: The name of the field to store elevation values.
    :return: The GeoDataFrame with elevation values added.
    """
    # Create an empty column for elevation values with float dtype
    points_gdf[elevations_field] = 0.0

    # Extract coordinates
    coords = [(point.x, point.y) for point in points_gdf.geometry]

    # Sample the DTM raster at the point locations
    elevation_values = [val[0] for val in DTM_raster.sample(coords)]

    # Assign the elevation values to the GeoDataFrame
    points_gdf[elevations_field] = elevation_values

    return points_gdf

def save_in_place(YOUR_POINTS_FEATURE, points_gdf_with_elevations, points_features_type):
    """
    Save the points GeoDataFrame back to the original file.

    :param YOUR_POINTS_FEATURE: The path to the original points feature file.
    :param points_gdf_with_elevations: The GeoDataFrame with the elevation data added.
    :param points_features_type: The type of the points feature file (shapefile or feature class).
    """
    if points_features_type == 'shapefile':
        points_gdf_with_elevations.to_file(YOUR_POINTS_FEATURE, driver='ESRI Shapefile')
    elif points_features_type == 'featureclass':
        GDB = YOUR_POINTS_FEATURE.split('gdb')[0] + 'gdb'  # get the fileGDB path
        layer = os.path.basename(YOUR_POINTS_FEATURE)  # get the feature class name
        points_gdf_with_elevations.to_file(GDB, layer=layer, driver='FileGDB')

def save_as_new_file(YOUR_POINTS_FEATURE, points_gdf_with_elevations, points_features_type):
    """
    Save the points GeoDataFrame to a new file.

    :param YOUR_POINTS_FEATURE: The path to the original points feature file.
    :param points_gdf_with_elevations: The GeoDataFrame with the elevation data added.
    :param points_features_type: The type of the points feature file (shapefile or feature class).
    """
    base, ext = os.path.splitext(YOUR_POINTS_FEATURE)
    new_file = base + '_with_elevations' + ext
    
    if points_features_type == 'shapefile':
        new_file = base + '_with_elevations.shp'
        points_gdf_with_elevations.to_file(new_file, driver='ESRI Shapefile')
    elif points_features_type == 'featureclass':
        new_file = base + '_with_elevations.gdb'
        GDB = new_file.split('gdb')[0] + 'gdb'  # get the fileGDB path
        layer = os.path.basename(YOUR_POINTS_FEATURE)  # get the feature class name
        points_gdf_with_elevations.to_file(GDB, layer=layer, driver='FileGDB')

if '__main__' == __name__:
    
    YOUR_POINTS_FEATUER = r"your_points_feature."
    YOUR_DTM_RASTER = r"your_dtm_raster"
    elevations_field = "elevation"        #The name of the field to store elevation values
    edit_in_place = 0                     # enter (1) for YES & (0) for NO

    # Read the points feature file
    points_gdf, points_features_type = reading_the_points_feature(YOUR_POINTS_FEATUER)
    
    # Read the DTM raster file
    DTM_raster = reading_the_DTM(YOUR_DTM_RASTER)
    
    # Get elevation values from the DTM and add them to the points GeoDataFrame
    points_gdf_with_elevations = get_points_elevations_from_DTM(points_gdf,
                                                                 DTM_raster,
                                                                 elevations_field=elevations_field)
    
    # Save the updated points GeoDataFrame
    if edit_in_place == 1:
        save_in_place(YOUR_POINTS_FEATUER, points_gdf_with_elevations, points_features_type)
        print("ALL Done..")
    else:
        save_as_new_file(YOUR_POINTS_FEATUER, points_gdf_with_elevations, points_features_type)
        print("ALL Done..")

    
