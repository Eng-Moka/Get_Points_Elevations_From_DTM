# Elevation Extraction for Points Intersecting with DTM

This repository contains a Python script designed to efficiently extract elevation values for specific points intersecting with a Digital Terrain Model (DTM) using GeoPandas and Rasterio. This solution is particularly useful for geospatial data analysis and Geographic Information Systems (GIS) applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

When working with geospatial data, it's often necessary to determine the elevation of specific points based on a DTM. Traditional methods can be extremely slow, especially when dealing with large datasets. This repository provides an efficient and accurate method to perform this task using Python.

## Features

- **Speed**: Utilizes vectorized operations for fast processing.
- **Accuracy**: Ensures precise elevation extraction for each point.
- **Flexibility**: Supports both Shapefiles and FeatureClasses from Geodatabases.

## Installation

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/Eng-Moka/Get_Points_Elevations_From_DTM/tree/main
cd Get_Points_Elevations_From_DTM
pip install -r requirements.txt
```

Ensure you have the following libraries installed:
geopandas
rasterio
## Usage
The main script, Get_Points_Elevations_From_DTM.py, includes functions for reading points features, reading DTM rasters, and extracting elevations.

**Example Usage**
import geopandas as gpd
import rasterio

# Define your file paths
YOUR_POINTS_FEATURE = r"path_to_your_points_feature.shp"
YOUR_DTM_RASTER = r"path_to_your_dtm_raster.tif"

# Read points feature and DTM raster
points_gdf, points_feature_type = reading_the_points_feature(YOUR_POINTS_FEATURE)
DTM_raster = reading_the_DTM(YOUR_DTM_RASTER)

# Extract elevations
points_gdf_with_elevations = get_points_elevations_from_DTM(points_gdf, DTM_raster, elevations_field="Z_DTM", edit_in_place=False)

# Save the results
save_as_new_file(YOUR_POINTS_FEATURE, points_gdf_with_elevations, points_feature_type)


Run the script:
python Get_Points_Elevations_From_DTM.py
# Functions
-**reading_the_points_featuer(YOUR_POINTS_FEATUER)**: Reads points feature from a Shapefile or Geodatabase.
-**reading_the_DTM(YOUR_DTM_RASTER)**: Reads DTM raster file.
-**get_points_elevations_from_DTM(points_gdf, DTM_raster, elevations_field="Z_DTM", edit_in_place=0)**: Extracts elevations for points.
-**save_in_place(YOUR_POINTS_FEATUER, points_gdf_with_elevations, points_featuers_type)**: Saves the updated points feature in place.
-**save_as_new_file(YOUR_POINTS_FEATUER, points_gdf_with_elevations, points_featuers_type)**: Saves the updated points feature as a new file.
# Example
Here's an example of how to use the script:

import geopandas as gpd
import rasterio

** Define your file paths**
YOUR_POINTS_FEATUER = r"path_to_your_points_feature.shp"
YOUR_DTM_RASTER = r"path_to_your_dtm_raster.tif"

** Read points feature and DTM raster**
points_gdf, points_featuers_type = reading_the_points_featuer(YOUR_POINTS_FEATUER)
DTM_raster = reading_the_DTM(YOUR_DTM_RASTER)

** Extract elevations**
points_gdf_with_elevations = get_points_elevations_from_DTM(points_gdf, DTM_raster, elevations_field="Z_DTM", edit_in_place=0)

**Save the results**
save_as_new_file(YOUR_POINTS_FEATUER, points_gdf_with_elevations, points_featuers_type)
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

##Acknowledgements
This project utilizes the following libraries:

GeoPandas
Rasterio
os

Feel free to contact me for any questions or feedback!
