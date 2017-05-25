# plot.py

# --------------------------------------------------
#
#   Plot wind data
#   Kris Johnson -- rumski20@msn.com
#   24 May 2017
#
# --------------------------------------------------

# IMPORTS
# plotly imports
from plotly import plotly
from plotly import graph_objs
# other imports
import datetime


# plot class
class Plot(object):
    def __init__(self, creds):
        self.api_key = creds['api_key']
        self.username = creds['username']
        plotly.sign_in(self.username, self.api_key)

    def test_plot(self):

        trace0 = graph_objs.Scatter(
            x=[1, 2, 3, 4],
            y=[10, 15, 13, 17]
        )
        trace1 = graph_objs.Scatter(
            x=[1, 2, 3, 4],
            y=[16, 5, 11, 9]
        )
        data = graph_objs.Data([trace0, trace1])

        plotly.plot(data, filename='basic-line')

    def get_marker_symbol(self, dir):
        """
        return marker symbol (triangle) based on wind direction
        :param dir: 
        :return: symbol string, one of
        "triangle-" + 
        up, ne, right, se, down, sw, left, nw
        """
        if 338 < dir or dir < 23:
            return 'triangle-up'
        elif 23 < dir < 68:
            return 'triangle-ne'
        elif 68 < dir < 113:
            return 'triangle-right'
        elif 113 < dir < 158:
            return 'triangle-se'
        elif 158 < dir < 207:
            return 'triangle-down'
        elif 207 < dir < 252:
            return 'triangle-sw'
        elif 252 < dir < 297:
            return 'triangle-left'
        elif 297 < dir < 338:
            return 'triangle-nw'
        else:
            return 'circle'

    def wind_plot(self, wind_data):
        """
        plot wind data
        :param wind_data: 
        :return: 
        """
        plot_data = []
        # get current time
        currenttime = datetime.datetime.now().strftime('%H:%M')
        plot_file = 'windplot_' + datetime.datetime.now().strftime('%d%m%Y')
        # loop through stations and add data to plot data
        for station, d in wind_data.iteritems():
            # check for missing/incorrect data
            if d['current_observation']['wind_mph'] < 0:
                continue
            # add data
            plot_data.append(graph_objs.Scatter(
                x=currenttime,
                y=d['current_observation']['wind_mph'],
                name=station,
                mode='lines+markers',
                marker={
                    'symbol': self.get_marker_symbol(d['current_observation'][
                                                         'wind_degrees']),
                    'size': 15,
                }
            ))
        # create plot
        # extend current plot (if exists) and don't open it browser
        plotly.plot(plot_data, filename=plot_file, fileopt='extend',
                    auto_open=False)


# RUN IT
# if __name__ == '__main__':