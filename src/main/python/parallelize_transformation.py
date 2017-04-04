from pyspark import SparkContext
from gdal_operations import *

def parallelize_transformation(imageList, transformation):
    with SparkContext('local', appName="MyApp") as sc:
        return_codes = [0]
        # Add python code into each node
        rdd = sc.parallelize(imageList)
        try:
            return_codes = rdd.map(transformation).collect()
        except Exception as e:
            print(e)
    return return_codes
