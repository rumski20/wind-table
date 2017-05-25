

# IMPORTS
# local imports
from wind import Wind
from plot import Plot
from store import Store
#other imports
import datetime

def main():
    # create wind instance
    wunderground_api_key = 'f36e51a5064819a4'
    windy = Wind(wunderground_api_key)

    # set wind stations
    windy.set_stations(
        ['KDLH', 'KMNDULUT5', 'KMNHERMA5', 'KMNDULUT32', 'KMNDULUT34',
         'KMNDULUT23', 'KMNDULUT7', 'KMNDULUT17'])

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

    # wind plot
    plotter.wind_plot(wind_data)

    # store wind data
    storage.addrecord(wind_data)

# RUN IT
if __name__ == '__main__':
    main()