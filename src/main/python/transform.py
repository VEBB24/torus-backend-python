from pyspark import SparkContext

def transform(imageList, transformation):
    sc = SparkContext("local", "Parallelized Transformation")
    rdd = sc.parallelize(imageList)
    transformedImages = rdd.map(transformation).collect()
    return transformedImages
