import os
import sys
from osgeo import gdal
from gdalconst import *

"""
Opens an image and load it into memory
This code is separated from the rest of the architecture as it is
likely to change depending on the file structure are going to use
"""

def get_dataset(fname):
        return (fname, os.path.splitext(fname)[0] + '.tiff')

def get_multiple_datasets(fnames):
    dataset_list = []
    for fname in fnames:
        dataset_list.append(get_dataset(fname))
    return dataset_list
