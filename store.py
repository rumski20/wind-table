# store.py

# Write data to CSV file

import csv
import datetime

class Store(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def format_data(self, data):
        # get datestamp
        datestamp = datetime.datetime.now().strftime('%c')
        rows = []

        # loop through weather data and get wind data in list of lists
        for station, d in data.iteritems():
            rows.append([datestamp,
                         station,
                         d['current_observation']['wind_degrees'],
                         d['current_observation']['wind_dir'],
                         d['current_observation']['wind_gust_mph'],
                         d['current_observation']['wind_mph']
                         ])
        return rows

    def addrecord(self, wind_data):
        """
        format data for file, then
        add row to existing CSV file
        :param data: dict of wind data
        :return: nothing
        """
        # format data for CSV file
        rows = self.format_data(wind_data)
        # append rows to end of file
        with open(self.filepath, 'ab') as f:
            writer = csv.writer(f)
            writer.writerows(rows)