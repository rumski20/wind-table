##################################################################################
#
#   wind.py
#   Kris Johnson
#   6 June 2016
#
#################################################################################


# Imports
import requests


class Wind:
    def __init__(self):
        self.api_key = 'f36e51a5064819a4'
        self.weather_dict = {}

        # get station list
        # self.set_stations()

    def set_stations(self, stations):
        """
        get stations from client
        :return: list of stations
        """
        self.station_list = stations

    def get_data(self):
        """
        gets wind data
        :return: return dict
        """
        # http://api.wunderground.com/api/f36e51a5064819a4/conditions/q/CA/San_Francisco.json
        # http://api.wunderground.com/api/f36e51a5064819a4/conditions/q/KDLH.json
        req = requests.get('http://api.wunderground.com/api/f36e51a5064819a4/conditions/q/KDLH.json')
        return req.json()

    def get_wind(self):
        """
        main function that gets and returns the wind to client
        :return: wind info
        """
        self.weather_dict = self.get_data()
        print '{0} : wind from {1} at {2} mph.'.format(self.weather_dict['current_observation']['station_id'],
                                                       self.weather_dict['current_observation']['wind_dir'],
                                                       self.weather_dict['current_observation']['wind_mph'])


if __name__ == '__main__':
    wind_class = Wind()
    # wind_class.set_stations(['KDLH'])
    wind_class.get_wind()
