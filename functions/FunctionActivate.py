from tkinter import *
import json
import os 

from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain
from IntelligentMirror.functions.QuoteFunction.quote_function import QuoteMain
from IntelligentMirror.functions.CalendarFunction.calendar_function import Calendar


class FunctionsActivateClass:
    """This class is responsible for activating the functions"""

    def __init__(self,
                tk: Frame,
                toolbarFrame: Frame,
                timeFrame: Frame,
                weatherFrame: Frame,
                gmailFrame: Frame,
                quoteFrame: Frame,
                calendarFrame: Frame) -> None:

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
        self.toolbarFrame = toolbarFrame
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame

        self.time = CurrentTime(self.tk, toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame)
        self.weather = CurrentWeather(self.tk, toolbarFrame, self.weatherFrame, self.timeFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame)
        self.gmail = GmailMain(self.tk, toolbarFrame, self.gmailFrame ,self.timeFrame, self.weatherFrame, self.quoteFrame, self.calendarFrame)
        self.quote = QuoteMain(self.tk, toolbarFrame, self.quoteFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.calendarFrame)
        self.calendar = Calendar(self.tk, self.toolbarFrame, self.calendarFrame,self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame )

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
            quoteOn = data["db"]["accounts"][RFace]["positions"]["quote"]["event"]
            calendarOn = data["db"]["accounts"][RFace]["positions"]["calendar"]["event"]
        
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
        
        if quoteOn == "True":
            QuoteToRefresh = True
        else:
            QuoteToRefresh = False 
            self.quote.destroy_quote() 
        
        if calendarOn == "True":
            CalendarToRefresh = True
        else:
            CalendarToRefresh = False 
            self.calendar.destroy_calendar() 
        
        self.function_refreshing(RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh, QuoteToRefresh,CalendarToRefresh)
    
    def function_refreshing(self, RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh, QuoteToRefresh, CalendarToRefresh):

        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            PtimeOn = data["db"]["accounts"]["None"]["positions"]["time"]["event"]
            PweatherOn = data["db"]["accounts"]["None"]["positions"]["weather"]["event"]
            PgmailOn = data["db"]["accounts"]["None"]["positions"]["gmail"]["event"]
            PquoteOn = data["db"]["accounts"]["None"]["positions"]["quote"]["event"]
            PcalendarOn = data["db"]["accounts"]["None"]["positions"]["calendar"]["event"]        
        
        smoothening = 35

        endX_time, endY_time = self.check_functions_position("time", RFace)
        plocX_time, plocY_time = 0,0
        if TimeToRefresh:
            clocX_time, clocY_time = 1,1
            if PtimeOn == "False":
                self.time_function()
        else:
            clocX_time, clocY_time = 0,0
        

        endX_weather, endY_weather = self.check_functions_position("weather", RFace)
        plocX_weather, plocY_weather = 0,0
        if WeatherToRefresh:
            clocX_weather, clocY_weather = 1,1
            if PweatherOn == "False":
                self.weather_function()
        else:
            clocX_weather, clocY_weather = 0,0
        
        endX_quote, endY_quote = self.check_functions_position("quote", RFace)
        plocX_quote, plocY_quote = 0,0
        if QuoteToRefresh:
            clocX_quote, clocY_quote = 1,1
            if PquoteOn == "False":
                self.quote_function()
        else:
            clocX_quote, clocY_quote = 0,0
        
        endX_calendar, endY_calendar = self.check_functions_position("calendar", RFace)
        plocX_calendar, plocY_calendar = 0,0
        if CalendarToRefresh:
            clocX_calendar, clocY_calendar = 1,1
            if PcalendarOn == "False":
                self.calendar_function()
        else:
            clocX_calendar, clocY_calendar = 0,0
        
       
        while ((int(plocX_time) != int(clocX_time) and int(plocY_time) != int(clocY_time)) or \
               (int(plocX_weather) != int(clocX_weather) and int(plocY_weather) != int(clocY_weather)) or \
                  (int(plocX_quote) != int(clocX_quote) and int(plocY_quote) != int(clocY_quote)) or \
                  (int(plocX_calendar) != int(clocX_calendar) and int(plocY_calendar) != int(clocY_calendar))):
            
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
            
            if QuoteToRefresh:
                plocX_quote = self.quoteFrame.winfo_x()
                plocY_quote = self.quoteFrame.winfo_y()

                clocX_quote = plocX_quote + (endX_quote - plocX_quote) / smoothening
                clocY_quote = plocY_quote + (endY_quote - plocY_quote) / smoothening

                x_quote = int(clocX_quote)
                y_quote = int(clocY_quote)

                self.quoteFrame.place_configure(x=x_quote,y=y_quote)
                self.quoteFrame.update()
            
            if CalendarToRefresh:
                plocX_calendar = self.calendarFrame.winfo_x()
                plocY_calendar = self.calendarFrame.winfo_y()

                clocX_calendar = plocX_calendar + (endX_calendar - plocX_calendar) / smoothening
                clocY_calendar = plocY_calendar + (endY_calendar - plocY_calendar) / smoothening

                x_calendar = int(clocX_calendar)
                y_calendar = int(clocY_calendar)

                self.calendarFrame.place_configure(x=x_calendar,y=y_calendar)
                self.calendarFrame.update()
        
        
        if TimeToRefresh:
            self.timeFrame.place_configure(x=endX_time,y=endY_time)
            self.timeFrame.update()

        if WeatherToRefresh:
            self.weatherFrame.place_configure(x=endX_weather,y=endY_weather)
            self.weatherFrame.update()
        
        if QuoteToRefresh:
            self.quoteFrame.place_configure(x=endX_quote,y=endY_quote)
            self.quoteFrame.update()
        
        if CalendarToRefresh:
            self.calendarFrame.place_configure(x=endX_calendar,y=endY_calendar)
            self.calendarFrame.update()
        
        if GmailToRefresh:
            self.gmail_function(on=False)
            self.gmail_function()
            if PgmailOn == "False":
                self.gmail_function()
        


    def time_function(self, on=True) -> None:
        """Activates time function"""
        if on:
            self.time.clock_date()
        else:
            self.time.destroy_time()

    def weather_function(self, on=True) -> None:
        """Activates weather function"""
        if on:
            self.weather.weather()
        else:
            self.weather.destroy_weather() 
        
    def gmail_function(self, on=True) -> None:
        """Activates gmail function"""
        if on:
            self.gmail.main()
        else:
            self.gmail.destroy_gmail()
    
    def quote_function(self, on=True) -> None:
        """Activates quote function"""
        if on:
            self.quote.main()
        else:
            self.quote.destroy_quote()
        
    def calendar_function(self, on=True) -> None:
        """Activates calendar function"""
        if on:
            self.calendar.calendarMain()
        else:
            self.calendar.destroy_calendar()
    
    
        

