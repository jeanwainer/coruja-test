#!/bin/bash

VIRTUALENV_DIR=venv
CSVFILE=customers.csv

if ! hash virtualenv 2>/dev/null; then
  echo "virtualenv is not installed. Please install and try again."
  exit 1
fi

if [ ! -d "$VIRTUALENV_DIR" ]; then
  virtualenv ${VIRTUALENV_DIR}
else
  echo "Creating directory $VIRTUALENV_DIR"
fi

source ${VIRTUALENV_DIR}/bin/activate
echo "Installing dependencies"
pip install -r requirements.txt

echo "Creating databases"
python manage.py migrate

echo
echo "=========================================================="

if [ ! -f "$CSVFILE" ]; then
  echo "$CSVFILE not found. No importing will be done."
  IMPORT_CSV='N'
else

  echo "$CSVFILE found. Would you like to import it right now?"
  echo "PS: You will need a Google Maps Api Key if you want to geocode customers addresses"
  read -p 'Y/n: ' -n 1 -r IMPORT_CSV
  echo
fi

if [[ ! $IMPORT_CSV =~ ^[Nn]$ ]]; then
  echo "Please enter Google Maps Api Key. If you enter none or a non-working one, lat/lon will stay null."
  read -p 'Google maps api key: '  API_KEY
  GOOGLEMAPS_API_KEY=$API_KEY python manage.py importcsv $CSVFILE
fi

read -p "Start dev server now? (y/N) " -n 1 -r
echo
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  python manage.py runserver
else
  echo "OK! You can start the server whenever you want."
fi

exit 0