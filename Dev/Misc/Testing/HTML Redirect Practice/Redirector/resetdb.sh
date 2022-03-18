#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3

python manage.py makemigrations product
python manage.py migrate
python manage.py loaddata products
