#!/bin/sh
python manage.py migrate
echo "Importing and geocoding all data from customers.csv. This may take a while..."
python manage.py importcsv customers.csv
python manage.py runserver 0.0.0.0:8000
# gunicorn coruja_test.wsgi:application --bind 0.0.0.0:8000