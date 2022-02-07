from tkinter import *
import json 
import os 

from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain
from IntelligentMirror.camera.move_functions import MoveFunction

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
        self.weather = CurrentWeather(self.tk, self.weatherFrame)
        self.gmail = GmailMain(self.tk, self.gmailFrame)

        self.prefix = os.getcwd()
        self.db = f"{self.prefix}/IntelligentMirror/DataBase.json"





    def time_function(self) -> None:
        """Activates time function"""
        self.move_function = MoveFunction(self.timeFrame)

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["camera"]["mouse_event"]["event"] = "False"
            data["db"]["camera"]["mouse_event"]["frame"] = "time"

        with open(self.db, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

        self.time.clock_date()
        self.move_function.move()

    def weather_function(self) -> None:
        """Activates weather function"""
        self.move_function = MoveFunction(self.weatherFrame)

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["camera"]["mouse_event"]["event"] = "False"
            data["db"]["camera"]["mouse_event"]["frame"] = "weather"

        with open(self.db, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

        self.weather.weather()
        self.move_function.move()
    
    def gmail_function(self) -> None:
        """Activates gmail function"""
        self.move_function = MoveFunction(self.gmailFrame)

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["camera"]["mouse_event"]["event"] = "False"
            data["db"]["camera"]["mouse_event"]["frame"] = "gmail"

        with open(self.db, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

        self.gmail.main()
        self.move_function.move()
    
    