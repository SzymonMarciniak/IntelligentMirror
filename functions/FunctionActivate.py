from tkinter import *
import json 
import os 

from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.camera.move_functions import MoveFunction

class FunctionsActivateClass:
    """This class is responsible for activating the functions"""

    def __init__(self,
                tk: Frame,
                clockLabel: Label,
                dateLabel: Label,
                timeFrame: Frame,
                temp: Label,
                pressure: Label,
                humidity:Label,
                image_weather: Label,
                weatherFrame: Frame) -> None:

        """
        Parametrs
        ---------
        tk: Tk()
            Name of main window
            
        clockLabel: Label
            Label for clock
        dateLabel: Label
            Label for date
        timeFrame: Frame
            Frame for clock label and date label
        
        temp: Label
            Label for current temerature 
        pressure: Label
            Label for current pressure
        humidity: Label 
            Label for current humidity 
        image_weather: Label 
            Label for current weather image 
        weatherFrame: Frame 
            Frame for all weather labels 
        """
        self.tk = tk
        self.clockLabel = clockLabel
        self.dateLabel = dateLabel
        self.timeFrame = timeFrame

        self.temp = temp 
        self.pressure = pressure
        self.humidity = humidity
        self.image_weather = image_weather
        self.weatherFrame = weatherFrame

        self.time = CurrentTime(self.clockLabel, self.dateLabel, self.timeFrame)
        self.weather = CurrentWeather(self.temp, self.pressure, self.humidity, self.image_weather, self.weatherFrame)

        self.prefix = os.getcwd()




    def time_function(self):
        """Activates time function"""
        self.move_function = MoveFunction(self.timeFrame)
       
        with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "w", encoding="utf-8") as file:
            data = {"event": "True"}
            json.dump(data, file)
        file.close()

        self.time.clock_date()
        self.move_function.move()

    
    def weather_function(self):
        """Activates weather function"""
        self.move_function = MoveFunction(self.weatherFrame)

        with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "w", encoding="utf-8") as file:
            data = {"event": "True"}
            json.dump(data, file)
        file.close()

        self.weather.weather()
        self.move_function.move()
    
    