# Imports
from geopy.geocoders import Nominatim
import geocoder
import googlemaps
import math


class Route:
    def __init__(self, origin, dest, directions):
        self.origin = origin
        self.dest = dest
        self.directions = directions


def cruise_to(address):
    # Read file to get all the previous routes
    with open('cache') as cache:
        prev_routes = list()
        for line in cache.readlines():
            args = line[:-1].split(' ')
            prev_routes.append(Route(args[0].split(','), args[1].split(','), args[2]))

    # Check if the current route is near any previous routes
    pos = geocoder.ip('me')
    dest = Nominatim(user_agent="myGeocoder").geocode(address)

    for route in prev_routes:
        origin_magnitude = math.sqrt((pos.latlng[0] - float(route.origin[0])) ** 2 + (pos.latlng[1] - float(route.origin[1])) ** 2)
        dest_magnitude = math.sqrt((dest.latitude - float(route.dest[0])) ** 2 + (dest.longitude - float(route.dest[1])) ** 2)

        if origin_magnitude <= 0.0003 and dest_magnitude <= 0.0003:
            travel_along(route)
            #return

    # If nowhere near
    with open('api_key') as api_key:
        apikey = api_key.read()[:-1]

    directions_result = googlemaps.Client(key=apikey).directions(pos.latlng, address, "walking")
    print(directions_result)


def travel_along(route):
    # TODO: Travel alongside a route
    return

cruise_to("Smpokou 1 Heraklion Crete Greece")
