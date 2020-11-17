import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock

import matplotlib.pyplot as plt
import numpy as np


class MyApp(App):

    def build(self):

        '''----------------I---nitialization Process----------------------'''
        self.fig, self.ax = plt.subplots()

        self.x_data = np.arange(11)
        self.y_data = np.arange(11)

        self.lines1, = self.ax.plot(self.x_data, self.y_data)
        self.lines2, = self.ax.plot(self.x_data, self.y_data)

        self.lines1.set_label('Line 1')
        self.lines2.set_label('Line 2')
        self.ax.legend()

        self.ax.set_ylim([0, 10])
        self.ax.set_xlim([0,10])
        self.ax.grid()

        self.units = 'Y axis'
        self.ax.set_ylabel(self.units, fontsize=10)

        self.graph = FigureCanvasKivyAgg(self.fig,)

        '''------------------Update data every self.n (seconds)--------------'''
        self.n = 2 # time interval of the update process
        Clock.schedule_interval(self.update_plot_data, self.n)

        return self.graph

    def update_plot_data(self, interval):
        '''-----------------------Update Plot Data--------------------------'''

        self.lines1.set_data(self.x_data, np.random.randint(10, size=(11)))
        self.lines2.set_data(self.x_data, np.random.randint(10, size=(11)))
        self.fig.canvas.draw()


if __name__ == '__main__':
    MyApp().run()
