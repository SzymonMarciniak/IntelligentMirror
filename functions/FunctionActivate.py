from tkinter import *
import os 

from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain


class FunctionsActivateClass:
    """This class is responsible for activating the functions"""

    def __init__(self,
                tk: Frame,
                toolbarFrame: Frame,
                timeFrame: Frame,
                weatherFrame: Frame,
                gmailFrame: Frame) -> None:

        """
        Parametrs
        ---------
        tk: Tk()
            Name of main window
        toolbarFrame: Frame
            Toolbar frame
        timeFrame: Frame
            Frame for clock label and date label
        weatherFrame: Frame 
            Frame for all weather labels 
        gmailFrame: Frame
            Frame for all gmail labels
        """
        self.tk = tk

        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame


        self.time = CurrentTime(self.tk, toolbarFrame, self.timeFrame)
        self.weather = CurrentWeather(self.tk, toolbarFrame, self.weatherFrame)
        self.gmail = GmailMain(self.tk, toolbarFrame, self.gmailFrame)

        self.prefix = os.getcwd()
        self.db = f"{self.prefix}/IntelligentMirror/DataBase.json"





    def time_function(self, on=True) -> None:
        """Activates time function"""
        print(on)
        if on == True:
            self.time.clock_date()
        else:
            self.time.destroy_time()

    def weather_function(self, on=True) -> None:
        """Activates weather function"""
        if on == True:
            self.weather.weather()
        else:
            self.weather.destroy_weather() 
        
    def gmail_function(self, on=True) -> None:
        """Activates gmail function"""
        if on == True:
            self.gmail.main()
        else:
            self.gmail.destroy_gmail()
    
    