from database.locations_pdo import Locations


class LocationService:
    def __init__(self):
        pass

    def get_all_locations(self, lat, lon, distance):
        return "All locations with lat %s lon %s distance %s" % (lat, lon, distance)

    def get_location(self, id):
        location = Locations.get
        return "Location with id %s" % id