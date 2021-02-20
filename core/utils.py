from django.conf import settings
import logging
import requests


logger = logging.getLogger(__name__)

# import googlemaps

# This was originally written using googlemaps python lib.
# However it has been rewritten to request google's endpoint directly just for the sake of showcase understanding
# of the API request.


class InvalidCredentialsError(Exception):
    pass


def get_latlon(location_str):
    """
    :param location_str: String representing an adress (full address, city, any string)
    :return: tuple of two elements: lat, lon
    """

    url_params = {
        'address': location_str,
        'key': settings.GOOGLEMAPS_API_KEY,
    }
    if not settings.GOOGLEMAPS_API_KEY:
        raise InvalidCredentialsError

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    try:
        response = requests.get(url, params=url_params, timeout=2)
    except requests.exceptions.ConnectTimeout:
        logger.warning('Timeout trying to connect to google servers')
        return None, None

    if response.json()['status'] == 'REQUEST_DENIED':
        logger.warning('Invalid credentials')
        raise InvalidCredentialsError

    geocode_result = response.json()['results']

    # gmaps = googlemaps.Client(key=settings.GOOGLEMAPS_API_KEY)
    # geocode_result = gmaps.geocode(location_str)

    lat, lon = None, None

    if geocode_result:
        lat, lon = geocode_result[0]['geometry']['location'].values()

    return lat, lon
