'''TkInter App'''

from Tkinter import *
import wind

class App():
    '''
    Window for Wind App
    '''

    def __init__(self):
        # Assign additional class-level attributes
        self.master = Tk()  # Create Tk instance
        self.windgauge = wind.Wind()

        # Execute core methods
        self.config_app()
        self.config_widgets()
        self.run_app()


    def config_app(self):
        # Configure app
        self.master.title('Wind Table')

    def config_widgets(self):
        # Insert widgets
        # new_entry_box = Entry(self.master)
        # new_entry_box['width'] = 50
        # new_entry_box.grid(row=0, column=0)
        #
        # new_button = Button(self.master)
        # new_button['text'] = 'Click Me!'
        # new_button.grid(row=0, column=1)

    def run_app(self):
        # Run the mainloop
        self.master.mainloop()
        self.get_weather()

    def get_weather(self):
        """
        get current weather
        :return:
        """
        weather_dict = self.windgauge.get_data()



if __name__ == '__main__':
    new_window = App()
