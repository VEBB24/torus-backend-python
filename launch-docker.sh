#!/bin/bash - 
#===============================================================================
#
#          FILE: launch.sh
# 
#         USAGE: ./launch.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Raphael EHRET (), raphael[dot]ehret[at]gmail[dot]com
#       CREATED: 04/05/2017 05:16:45 PM
#===============================================================================

INPUT_FILES=()
INPUT_FILES=($@)
IMAGE_GDAL="$(docker images | grep -i spark-torus)"
[[ -z "$IMAGE_GDAL" ]] && docker build -t spark-torus .
docker run --rm -it spark-torus spark-submit main.py ${INPUT_FILES[@]}

