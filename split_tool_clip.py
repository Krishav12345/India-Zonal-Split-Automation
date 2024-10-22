import arcpy
import os

# Define the paths
input_shapefile = r"D:\AGSRT_course\AGSRT_ArcPy\study_material\india_administrative_state_boundary\india_administrative_state_boundary.shp"
split_features = [
    r"C:\Users\HAVE A NICE DAY\OneDrive\Documents\ArcGIS\Projects\MyProject34\grid_1.shp",
    r"C:\Users\HAVE A NICE DAY\OneDrive\Documents\ArcGIS\Projects\MyProject34\grid_2.shp"
]

# Output directory for clipped shapefiles
output_directory = r"D:\AGSRT_course\AGSRT_ArcPy\ARCPro_file\output"

# Check if the output directory exists, create it if it doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each split feature and perform clipping
for feature in split_features:
    # Get the base name of the split feature to create output file name
    feature_name = feature.split("\\")[-1].replace(".shp", "")
    output_file = os.path.join(output_directory, f"{feature_name}_clipped.shp")

    # Clip the input shapefile using the current feature
    arcpy.analysis.Clip(input_shapefile, feature, output_file)
    print(f"Clipped {input_shapefile} with {feature} to {output_file}")

print("Clipping completed for all features.")
