##################################################################################
#
#   wind.py
#   Kris Johnson
#   6 June 2016
#
#################################################################################


# Imports
import requests


class Wind(object):
    def __init__(self, key):
        self.api_key = key
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
        data_dict = {}
        url = 'http://api.wunderground.com/api/f36e51a5064819a4/conditions/q/{0}.json'
        # loop through stations and add to dictionary
        for station in self.station_list:
            # airport code
            if len(station) == 4:
                data_dict[station] = requests.get(url.format(station)).json()
            # personal station
            else:
                data_dict[station] = requests.get(
                    url.format('pws:' + station)).json()

        return data_dict

    def get_wind(self):
        """
        main function that gets and returns the wind to client
        :return: wind info
        """
        self.weather_dict = self.get_data()
        # loop through and print results
        for key, value in self.weather_dict.iteritems():
            if value['current_observation']['wind_mph'] > 0:
                print '{0} : wind from {1} at {2} mph.' \
                    .format(key,
                            value['current_observation']['wind_dir'],
                            value['current_observation']['wind_mph'])


if __name__ == '__main__':
    wunderground_api_key = 'f36e51a5064819a4'
    wind_class = Wind(wunderground_api_key)
    wind_class.set_stations(
        ['KDLH', 'KMNDULUT5', 'KMNHERMA5', 'KMNDULUT32', 'KMNDULUT34',
         'KMNDULUT23', 'KMNDULUT7', 'KMNDULUT17'])
    wind_class.get_wind()
