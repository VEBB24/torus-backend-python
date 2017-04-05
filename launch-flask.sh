set -e

export FLASK_APP=flask_server.py
if ! which flask > /dev/null; then
    echo "Please install 'flask' before trying to run $0"
    exit 1
fi
flask run
