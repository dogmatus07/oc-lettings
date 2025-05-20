#!/bin/bash
# This script is used to export data to fixtures files
# It will create a directory called fixtures in the current directory

# create a directory called fixtures
mkdir -p fixtures

# export the data from the database to fixtures files
python3 manage.py dumpdata auth.User --indent 2 --output fixtures/users.json
python3 manage.py dumpdata profiles --indent 2 --output fixtures/profiles.json
python3 manage.py dumpdata lettings --indent 2 --output fixtures/lettings.json

echo "Fixtures files created in the fixtures directory"