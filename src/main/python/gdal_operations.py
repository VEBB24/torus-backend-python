from osgeo import gdal
from gdalconst import *

# Writes a translation of an input dataset based on a given format
def gdal_translate(input_name, output_name):
    dataset = gdal.Open(input_name, GA_ReadOnly)
    if dataset == None:
        return 1
    driver = gdal.GetDriverByName('GTiff')
    sizeX = dataset.RasterXSize
    sizeY = dataset.RasterYSize
    nbBands = dataset.RasterCount
    target = driver.Create(output_name, sizeX, sizeY, nbBands, gdal.GDT_Byte) 
    if target != None:
        return_code = 0
        target = None
    else:
        return_code = 2
    dataset = None
    return return_code

# Apply different transformations on a dataset
def gdal_transformations(tuple_name):
    input_name, output_name = tuple_name[0], tuple_name[1]
    return gdal_translate(input_name, output_name)
