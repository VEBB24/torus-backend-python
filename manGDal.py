import gdal
from gdalconst import *

dataset = gdal.Open(filename, GA_ReadOnly)
if dataset is None:
    # do something with error
    pass

# Getting dataset informations

dataset.GetDriver().ShortName  # Driver name
dataset.GetDrive().LongName # Driver full name

dataset.RasterXSize # X size of picture
dataset.RasterYSize # Y size of picture
dataset.RasterCount # Nombre de bandes ???

geotransform = dataset.GetGeoTransform()
if not geotransform is None:
    geotransform[0] # Origin X
    geotrasform[3]  # Origin Y
    geotransform[1] # Pixel size X
    geotransform[5] # Pixel size Y

# Bands
band = dataset.GetRasterBand(1) # Get first band
gdal.GetDataTypeName(band.DataType) # Get band data type

# Dunno what is for
min = band.GetMinimum()
max = band.GetMaximum()
if min is None or max is None:
    (min, max) = band.ComputeRasterMinMax(1)

# Read band's raster
scanline = band.ReadRaster(0, 0, band.XSize, 1, band.XSize, 1, GDT_Float32)  # <- Float32 a changer

# Open file and test Create() compatibility
format = "GTiff"
driver = gdal.GetDriverByName(format)
metadata = driver.GetMetadata()
if metadata.has_key(gdal.DCAP_CREATE) and metadata[gdal.DCAP_CREATE] == 'YES':
    # Driver supports Create() method
    pass
# Meme methode pour tester le CreateCopy()


# Le saint Create() avec un exemple
# Define pixel size and NoData value of new raster (a tester, je laisse les valeurs par defaut)
pixel_size = 25
NoData_value = -9999

# Filename of input
vector_fn = 'test.shp'
#Filename of output
raster_fn = 'test.tif'

# Open the data source and read in the extent
source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band.SetNoDataValue(NoData_value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values = [0])
