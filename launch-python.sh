#!/bin/bash - 
#===============================================================================
#
#          FILE: launch-python.sh
# 
#         USAGE: ./launch-python.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Raphael EHRET (), raphael[dot]ehret[at]gmail[dot]com
#       CREATED: 03/31/2017 05:17:02 PM
#===============================================================================


FILES=()
FILES+=("$@")

if [ -z "$FILES" ]; then
    echo "Expected argument for files to run"
    echo ""
    echo "Usage : "
    echo "   $0 python_files"
    exit 1
fi

if [ -z "$PYSPARK_PYTHON" ]; then
    if which python2 > /dev/null; then
        echo "Running spark with Python 2"
        PYSPARK_PYTHON="/usr/bin/python2"
    else
        echo "Trying to run with Python 3, this may work badly"
        PYSPARK_PYTHON="/usr/bin/python3"
    fi
fi

export SPARK_LOCAL_IP=127.0.0.1

exec lib/spark/bin/spark-submit "${FILES[@]}"

find src -name "*.pyc" -exec rm {} \;
