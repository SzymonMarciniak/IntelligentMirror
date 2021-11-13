from tkinter import *

from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass


class Toolbar:

    def __init__(self,
                tk: Frame,
                toolbarFrame: Tk, 
                clockIcon: PhotoImage,
                sunIcon: PhotoImage,
                homeIcon: PhotoImage,
                contactsIcon: PhotoImage,
                settingsIcon: PhotoImage,
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
        
        clockIcon: PhotoImage
            Clock image
        sunIcon: PhotoImage
            Sun image
        homeIcon: PhotoImage
            Home image
        contactsIcon: PhotoImage
            Contact image
        settingsIcon: PhotoImage
            Settings image
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
        self.toolbarFrame = toolbarFrame
        self.clockIcon = clockIcon
        self.sunIcon = sunIcon
        self.homeIcon = homeIcon
        self.contactsIcon = contactsIcon
        self.settingsIcon = settingsIcon
        self.clockLabel = clockLabel
        self.dateLabel = dateLabel
        self.timeFrame = timeFrame

        self.temp = temp
        self.pressure = pressure
        self.humidity = humidity
        self.image_weather = image_weather
        self.weatherFrame = weatherFrame

        self.functions_activate = FunctionsActivateClass(self.tk, self.clockLabel, self.dateLabel, self.timeFrame, \
                                    self.temp, self.pressure, self.humidity, self.image_weather, self.weatherFrame)


    def OpenToolbar(self) -> None:
        """ 
        Display toolbar main buttons
        
        """
        toolbar = Toolbar(self.tk,self.toolbarFrame, self.clockIcon, self.sunIcon, self.homeIcon, self.contactsIcon, self.settingsIcon, self.clockLabel, self.dateLabel,self.timeFrame, \
            self.temp, self.pressure, self.humidity, self.image_weather, self.weatherFrame)

        clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightbackground='black', bg='black', command=toolbar.time_function)
        weather_button = Button(self.toolbarFrame, image=self.sunIcon, highlightbackground='black', bg='black', command=toolbar.weather_function)       #
        home_button = Button(self.toolbarFrame, image=self.homeIcon, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation)         #to change
        contact_button = Button(self.toolbarFrame, image=self.contactsIcon, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation)  #
        settings_button = Button(self.toolbarFrame, image=self.settingsIcon, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation) #

        clock_button.pack(side=TOP)
        weather_button.pack(side=TOP)
        home_button.pack(side=TOP)
        contact_button.pack(side=TOP)
        settings_button.pack(side=TOP)

        
        self.toolbarFrame.place(x=-200,y=0)


    def OpenToolbarAnimation(self) -> None:
        """
        Create toolbar display animation 
        """
        for x_pos in range(-200,1,10):
            self.toolbarFrame.place(x=x_pos, y=0)
            self.toolbarFrame.update()
    
    
    def time_function(self):
        """It is a bridge into a function activate"""
        self.functions_activate.time_function()
    
    def weather_function(self):
        """It is a bridge into a function activate"""
        self.functions_activate.weather_function()
    
