from __future__ import print_function
# You *must* let this import on first place
from pyspark import SparkContext
import sys
from file_opening import *
from parallelize_transformation import *
from gdal_operations import *


def main():
    if len(sys.argv[1:]) == 0:
        err_log("Please provide filenames as input")
        sys.exit(1)
    fnames = sys.argv[1:]

    return_codes = parallelize_transformation(fnames, gdal_transformations)
    return_code = err_check(fnames, return_codes)
    return return_code

def err_check(dataset_list, return_codes):
    for dataset, return_code in zip(dataset_list, return_codes):
        if return_code:
            err_log("Could not write "  + dataset + 
                " transformations")
    return reduce(lambda r1, r2 : r1*r2, return_codes)

def err_log(text):
    print(text, file=sys.stderr)


if __name__ == '__main__':
    main()
