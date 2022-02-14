from tkinter import *
import json
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
    
    def check_functions_position(self, function, RFace):

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            if RFace == None: 
                RFace = data["db"]["camera"]["actuall_user"]

            x = data["db"]["accounts"][RFace]["positions"][function]["x"]
            y = data["db"]["accounts"][RFace]["positions"][function]["y"]
        return x, y
        
    def functions_position_refresh(self, RFace):

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            timeOn = data["db"]["accounts"][RFace]["positions"]["time"]["event"]
            weatherOn = data["db"]["accounts"][RFace]["positions"]["weather"]["event"]
            gmailOn = data["db"]["accounts"][RFace]["positions"]["gmail"]["event"]
        
        if timeOn == "True":
            TimeToRefresh = True
        else:
            TimeToRefresh = False
            self.time.destroy_time()

        if weatherOn == "True":
            WeatherToRefresh = True
        else:
            WeatherToRefresh = False 
            self.weather.destroy_weather()

        if gmailOn == "True":
            GmailToRefresh = True
        else:
            GmailToRefresh = False 
            self.gmail.destroy_gmail() 
        
        self.function_refreshing(RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh)
    
    def function_refreshing(self, RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh):
        
        smoothening = 35

        endX_time, endY_time = self.check_functions_position("time", RFace)
        plocX_time, plocY_time = 0,0
        if TimeToRefresh:
            clocX_time, clocY_time = 1,1
        else:
            clocX_time, clocY_time = 0,0
        

        endX_weather, endY_weather = self.check_functions_position("weather", RFace)
        plocX_weather, plocY_weather = 0,0
        if WeatherToRefresh:
            clocX_weather, clocY_weather = 1,1
        else:
            clocX_weather, clocY_weather = 0,0
        

        endX_gmail, endY_gmail = self.check_functions_position("gmail", RFace)
        plocX_gmail, plocY_gmail = 0,0
        if GmailToRefresh:
            clocX_gmail, clocY_gmail = 1,1
        else:
            clocX_gmail, clocY_gmail = 0,0
        
       
        while (int(plocX_time) != int(clocX_time) and int(plocY_time) != int(clocY_time)):
            
            if TimeToRefresh:
                plocX_time = self.timeFrame.winfo_x()
                plocY_time = self.timeFrame.winfo_y()

                clocX_time = plocX_time + (endX_time - plocX_time) / smoothening
                clocY_time = plocY_time + (endY_time - plocY_time) / smoothening

                x_time = int(clocX_time)
                y_time = int(clocY_time)

                self.timeFrame.place_configure(x=x_time,y=y_time)
                self.timeFrame.update()
            
            if WeatherToRefresh:
                plocX_weather = self.weatherFrame.winfo_x()
                plocY_weather = self.weatherFrame.winfo_y()

                clocX_weather = plocX_weather + (endX_weather - plocX_weather) / smoothening
                clocY_weather = plocY_weather + (endY_weather - plocY_weather) / smoothening

                x_weather = int(clocX_weather)
                y_weather = int(clocY_weather)

                self.weatherFrame.place_configure(x=x_weather,y=y_weather)
                self.weatherFrame.update()
            
            if GmailToRefresh:
                plocX_gmail = self.gmailFrame.winfo_x()
                plocY_gmail = self.gmailFrame.winfo_y()

                clocX_gmail = plocX_gmail + (endX_gmail - plocX_gmail) / smoothening
                clocY_gmail = plocY_gmail + (endY_gmail - plocY_gmail) / smoothening

                x_gmail = int(clocX_gmail)
                y_gmail = int(clocY_gmail)

                self.gmailFrame.place_configure(x=x_gmail,y=y_gmail)
                self.gmailFrame.update()
        
        if TimeToRefresh:
            self.timeFrame.place_configure(x=endX_time,y=endY_time)
            self.timeFrame.update()

        if WeatherToRefresh:
            self.weatherFrame.place_configure(x=endX_weather,y=endY_weather)
            self.weatherFrame.update()
        
        if GmailToRefresh:
            self.gmailFrame.place_configure(x=endX_gmail,y=endY_gmail)
            self.gmailFrame.update()


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
    
    