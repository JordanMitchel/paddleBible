from geopy import Nominatim

from PreProcessing.update_coordinates import is_in_biblical_geo_square


def queryOneLat(name):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(name)
    relevant = is_in_biblical_geo_square(location.latitude, location.longitude)
    if location is not None and relevant:
        print("The latitude of the location is: ", location.latitude)
        print("The longitude of the location is: ", location.longitude)

queryOneLat("Aphek")


