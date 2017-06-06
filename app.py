# IMPORTS
# local imports
from wind import Wind
from plot import Plot
from store import Store
# other imports
import datetime
import rfc822


def remove_old(data):
    """
    remove old observations from wind data
    :param wind_data:
    :return: new wind_data dictionary with old entries deleted
    """
    new_data = {}
    # loop through current wind data dict
    for station, d in data.iteritems():
        # get difference in time between now and the observation time from
        # the station
        timediff = datetime.datetime.now() \
                   - datetime.datetime.fromtimestamp(
            rfc822.mktime_tz(rfc822.parsedate_tz(
                d['current_observation']['observation_time_rfc822'])))
        # check if observation has occured within the last 30 minutes
        if abs(timediff.total_seconds()) < 1800:
            new_data[station] = d

    return new_data


def main():
    # create wind instance
    wunderground_api_key = 'f36e51a5064819a4'
    windy = Wind(wunderground_api_key)

    # set wind stations
    # limit to ten per wunderground api per minute request limitations
    # full
    # station_list = [
    #      'KMNDULUT5', 'KDLH', 'KMNDULUT69', 'KMNHERMA5', 'KMNDULUT32',
    #      'KMNDULUT34', 'KMNDULUT23', 'KMNDULUT7', 'KMNDULUT17', 'KMNDULUT71',
    #      'KMNDULUT86', 'KMNDULUT63', 'KMNDULUT83'
    #       ]
    station_list = [
        'KMNDULUT5', 'KDLH', 'KMNDULUT69', 'KMNHERMA5', 'KMNDULUT32',
        'KMNDULUT7', 'KMNDULUT71', 'KMNDULUT63', 'KMNDULUT83'
         ]
    windy.set_stations(station_list)

    # create plot instance
    plotly_creds = {
        'username': 'rumski20',
        'api_key': 'WU2Nl3dIlOoWkNQqEdDC'
    }
    plotter = Plot(plotly_creds)

    # create store instance
    csv_file = r'F:\Data\wind_data\wind_data.csv'
    storage = Store(csv_file)

    # test plot
    # plotter.test_plot()

    # get wind data
    wind_data = windy.get_data()

    # remove observations that are not recent
    wind_data = remove_old(wind_data)

    # wind plot
    plotter.wind_plot(wind_data)

    # store wind data
    storage.addrecord(wind_data)


# RUN IT
if __name__ == '__main__':
    main()
