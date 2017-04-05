FROM liebrand/gdal-spark:latest
LABEL Description="This image is used to run GDAL translations into tif using Spark parallelization"

ADD src/main/python/ /files
WORKDIR /files
