FROM liebrand/gdal-spark:latest
LABEL Description="This image is used to run GDAL translations into tif using Spark parallelization"

# HDFS Installation
RUN curl https://pypi.python.org/packages/c5/5f/384c1cceab1aef413defda6e82758e71c7fcc670deff94faecd64a3dabc6/hdfs-2.0.16.tar.gz --output hdfs.tar.gz && \
    mkdir hdfs && \
    cd hdfs && \
    tar xvzf hdfs.tar.gz && \
    rm hdfs.tar.gz && \
    cd hdfs-2.0.16 && \
    python setup.py install && \

ADD src/main/python/ /files
WORKDIR /files
