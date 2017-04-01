from osgeo import gdal
from gdalconst import *

source_file = '/home/Saphirel/Desktop/toto.jp2'
dest_file = '/home/Saphirel/Desktop/test.tiff'

dataset = gdal.Open(source_file, GA_ReadOnly)
x = dataset.RasterXSize
y = dataset.RasterYSize
nbBands = dataset.RasterCount
target_ds = gdal.GetDriverByName('GTiff').Create(dest_file, x, y, nbBands, gdal.GDT_Float32)

source_file = None
dest_file = None
