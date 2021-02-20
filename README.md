CORUJA technical test
============


How to install
-------------

Create a virtual environment and install dependencies from requirements.txt

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Run migrations to create the database and start development server

    python manage.py migrate
    python manage.py runserver

You may edit ```coruja_test/settings.py``` and set **GOOGLEMAPS_API_KEY** or pass as an environment variable when
importing clients to geocode their address.

Now it's ready to run!

Geocoding addresses
-------------
In order to get addresses correctly geocoded when importing clients from CSV, you'll need to
[get a Google Maps api key](https://developers.google.com/maps/documentation/maps-static/get-api-key) and provide it as 
either an environment variable or set it manually in settings.py  
If you don't set ```GOOGLEMAPS_API_KEY```, the contacts will be imported but geocoding won't happen, and lat/lon
attributes will be set as *null*. You'll also get a warning.


Import contacts from csv
-------------
Set GOOGLEMAPS_API_KEY environment variable and run `importcsv` management command to import a CSV file. This command
takes as its only argument the path of the CSV file to read. (The key below is an example, it wont work.)  

    GOOGLEMAPS_API_KEY=YOUR_API_KEY python manage.py importcsv customers.csv
  
**Important:** Field names must be according to the provided CSV sample ```customers.csv```.


One-command setup
-------------
By running the included ```setup.sh``` shell script, an interactive bash script does all the setup work.

    ./setup.sh


Optional: Docker container 
-------------
Run docker and set the ```GOOGLEMAPS_API_KEY``` environment variable. You may not set it, then geocoding won't happen.

    sudo docker build -t coruja-test .
    sudo docker run -p 8000:8000 -e GOOGLEMAPS_API_KEY=your_key coruja-test 

**Please note**:
The customers.csv file will be imported on the entrypoint. This should take 3-4 minutes. If you want to
speed things up, you may replace customers.csv file with a smaller list.


REST API and endpoints
-------------
Run development server:
    manage.py runserver

* Access http://localhost:8000/swagger for the swagger interface

Direct URL For API endpoints are:

* Access http://localhost:8000/api/customer to return a listing of customers
* Access http://localhost:8000/api/customer/[customer_id] to retrieve a specific customer


Misc. comments
-------------

* As requested, Google Maps api was used. However, for speed (and cost) optimization, I would suggest another provider
  such as MapQuest that allows for multiple addresses per query.
* In this demo project, the ```google maps api key``` isn't needed to access the REST API endpoints. It is used only by
  the management command.
* At first, docker container was set to use gunicorn instead of django's development server. But in order to avoid the
need of a docker-compose file to serve static content for the swagger interface, I went back to running django's own
  server for the purpose of this test.
* In production, maybe we shouldn't trust the ID to be unique.