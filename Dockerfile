FROM liebrand/gdal-spark:latest
LABEL Description="This image is used to run GDAL translations into tif using Spark parallelization"

# HDFS Installation
RUN mkdir hdfs && \
    cd hdfs && \
    curl https://pypi.python.org/packages/c5/5f/384c1cceab1aef413defda6e82758e71c7fcc670deff94faecd64a3dabc6/hdfs-2.0.16.tar.gz --output hdfs.tar.gz && \
    tar xvzf hdfs.tar.gz && \
    rm hdfs.tar.gz && \
    cd hdfs-2.0.16 && \
    python setup.py install 
    
# Install flask
RUN easy_install flask

ADD flask /flask
ADD src/ /files
WORKDIR /files
COPY ./init.sh /init.sh
RUN chmod +x /init.sh
ENTRYPOINT ["/init.sh"]
