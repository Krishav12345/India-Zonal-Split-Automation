# India-Zonal-Split-Automation
Working with over 21 lakh records can be daunting, especially in QGIS. It can slow down processes and make data handling cumbersome.
## Purpose
This project aims to [briefly explain what the project does, its goals, and its significance. Include any specific problems it addresses or functionalities it provides.]

## Technologies Used
- **Programming Language:** Python
- **GIS Tools:** QGIS, ArcGIS
- **Libraries:** List any libraries or frameworks you used, e.g., Pandas, NumPy, etc.
  
The Multi-Value Input Clipping Tool is designed to streamline the process of clipping spatial datasets based on multiple input values. This tool enables users to efficiently manage and analyze large datasets by selecting specific features for targeted analysis.

## How to Run Your Code
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   
## Split Tool

import geopandas as gpd
import os

# Paths to the input files
roads_path = r"C:\Users\HAVE A NICE DAY\Downloads\Roads-India-www.gisenglish.com\gis_osm_roads_free_1.shp"
grid_path = r"D:\AGSRT_course\exercise_data\grid.shp"
output_folder = r"C:\Users\HAVE A NICE DAY\Downloads\Roads-India-www.gisenglish.com\output\gridwise"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

try:
    # Read the shapefiles using GeoPandas
    roads = gpd.read_file(roads_path)
    grid = gpd.read_file(grid_path)

    # Verify the columns in the grid shapefile
    print("Grid Columns:", grid.columns)

    # Use the correct field name ('Id')
    grid_id_field = 'Id'

    # Ensure the coordinate reference systems (CRS) match
    if roads.crs != grid.crs:
        grid = grid.to_crs(roads.crs)

    # Spatial join to assign each road feature the corresponding grid ID
    roads_with_id = gpd.sjoin(roads, grid[['geometry', grid_id_field]], how='inner', predicate='intersects')

    # Function to truncate column names to 10 characters
    def truncate_columns(gdf):
        gdf.columns = [col[:10] for col in gdf.columns]
        return gdf

    # Split the roads into separate shapefiles based on the 'Id' field
    unique_ids = roads_with_id[grid_id_field].unique()

    for grid_id in unique_ids:
        # Filter the records matching the current grid ID
        subset = roads_with_id[roads_with_id[grid_id_field] == grid_id]

        # Truncate column names to avoid the warning
        subset = truncate_columns(subset)

        # Define the output path for this subset
        output_path = os.path.join(output_folder, f"roads_{grid_id}.shp")

        # Save the subset as a new shapefile
        subset.to_file(output_path)

        print(f"Saved {len(subset)} records to {output_path}")

except Exception as e:
    print(f"An error occurred: {e}")
