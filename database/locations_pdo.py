import pandas as pandas
import psycopg2
import sqlalchemy as sal
import pandas

from utils.parameters import Parameters


class LocationsPDO:
    def __init__(self):
        self.__eng = None

        pass

    def connect(self):
        parameters = Parameters()

        user = parameters.get_parameter('database_user')
        password = parameters.get_parameter('database_password')
        host = parameters.get_parameter('database_host')
        name = parameters.get_parameter('database_name')
        port = parameters.get_parameter('database_port')

        self.__eng = sal.create_engine("redshift+psycopg2://%s:%s@%s:%s/%s" % (user, password, host, port, name),
                                       encoding='latin1')
        self.__eng.connect()

    def get_locations(self, lat, lon):
        result = pandas.read_sql_query("SELECT venue_id as id, venue_name as name, type as description, latitude as lat, longitude as lon, rating as score from public.test LIMIT 10", self.__eng)

        return result.to_dict(orient='records')