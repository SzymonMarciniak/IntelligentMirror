from tkinter import *
import json
import os

from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass

prefix_ = os.getcwd()
db = f"{prefix_}/IntelligentMirror/DataBase.json"
class Toolbar:

    def __init__(self,
                tk: Frame,
                toolbarFrame: Tk, 
                timeFrame: Frame,
                weatherFrame: Frame,
                gmailFrame: Frame,
                clockIcon: PhotoImage,
                sunIcon: PhotoImage,
                homeIcon: PhotoImage,
                contactsIcon: PhotoImage,
                settingsIcon: PhotoImage,
                leftArrow: PhotoImage,
                rightArrow: PhotoImage) -> None:
        """
        Parametrs
        ---------
        tk: Tk()
            Name of main window
        toolbarFrame: Frame
            Frame for toolbar buttons
        timeFrame: Frame
            Frame for clock label and date label
        weatherFrame: Frame 
            Frame for all weather labels 
        gmailFrame: Frame
            Frame for all gmails labels
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
        """

        self.tk = tk
        self.toolbarFrame = toolbarFrame

        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame

        self.clockIcon = clockIcon
        self.sunIcon = sunIcon
        self.homeIcon = homeIcon
        self.contactsIcon = contactsIcon
        self.settingsIcon = settingsIcon

        self.leftArrow = leftArrow
        self.rightArrow = rightArrow

        self.time_on = False
        self.weather_on = False
        self.gmail_on = False

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["toolbar"] = "off"

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


        self.functions_activate = FunctionsActivateClass(self.tk, self.toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame)


    def OpenToolbar(self) -> None:
        """ 
        Display toolbar main buttons
        
        """
        toolbar = Toolbar(self.tk,self.toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.clockIcon, self.sunIcon, \
             self.homeIcon, self.contactsIcon, self.settingsIcon, self.leftArrow, self.rightArrow)
        
        self.toolbar = toolbar

        self.clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightthickness=2, highlightbackground='black', bg='black', command=self.time_function)
        self.weather_button = Button(self.toolbarFrame, image=self.sunIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.weather_function)      
        self.home_button = Button(self.toolbarFrame, image=self.homeIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.gmail_function)         #to change
        self.contact_button = Button(self.toolbarFrame, image=self.contactsIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenToolbarAnimation)  #
        self.settings_button = Button(self.toolbarFrame, image=self.settingsIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenToolbarAnimation) #
        

        self.clock_button.pack(anchor=NW)
        self.weather_button.pack(anchor=NW)
        self.home_button.pack(anchor=NW)
        self.contact_button.pack(anchor=NW)
        self.settings_button.pack(anchor=NW)

        self.arrowFrame = LabelFrame(self.toolbarFrame, bg="black", bd=0)
        self.arrow_button = Button(self.arrowFrame, image=self.rightArrow, bd=0, highlightbackground='black',borderwidth=0, bg='black', \
             highlightthickness=0, command=self.OpenToolbarAnimation)
        self.arrow_button.pack(side=RIGHT)
        self.arrowFrame.place(x=209, y=420)

        
        self.toolbarFrame.place(x=-201,y=0, width=420)

        self.OpenToolbarAnimation()
        self.HideToolbarAnimation()

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            timeOn = data["db"]["accounts"]["None"]["positions"]["time"]["event"]
            weatherOn = data["db"]["accounts"]["None"]["positions"]["weather"]["event"]
            gmailOn = data["db"]["accounts"]["None"]["positions"]["gmail"]["event"]
        
        if timeOn == "True":
            self.time_function()
        if weatherOn == "True":
            self.weather_function()
        if gmailOn == "True":
            self.gmail_function()
        

    def OpenToolbarAnimation(self) -> None:
        """
        Show toolbar 
        """        
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            
        if data["db"]["toolbar"] != "on":
            data["db"]["toolbar"] = "on"

            with open(db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            for x_pos in range(-200,1,10):
                self.toolbarFrame.place(x=x_pos, y=0)
                self.toolbarFrame.update()

            
            self.arrow_button.config(image=self.leftArrow, command=self.HideToolbarAnimation)
        
    
            
        
    
    def OpenToolbarAnimation_DF(toolbarFrame: Frame) -> None:
        """
        Show toolbar from diffrent file
        Paramets
        --------
        toolbarFrame: Frame
            Frame for toolbar
        """        
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        if data["db"]["toolbar"] != "on":
            data["db"]["toolbar"] = "on"

            with open(db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            for x_pos in range(-200,1,10):
                toolbarFrame.place(x=x_pos, y=0)
                toolbarFrame.update()
            
        
            
           
    
    def HideToolbarAnimation(self) -> None:
        """
        Hide toolbar
        """        
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        if data["db"]["toolbar"] != "off":
            data["db"]["toolbar"] = "off"

            with open(db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            for x_pos in range(1,-211,-1):
                self.toolbarFrame.place(x=x_pos, y=0)
                self.toolbarFrame.update()

            
            self.arrow_button.config(image=self.rightArrow, command=self.OpenToolbarAnimation)
        
            



    
    def HideToolbarAnimation_DF(toolbarFrame: Frame) -> None:
        """
        Hide toolbar from diffrent file
        Paramets
        --------
        toolbarFrame: Frame
            Frame for toolbar
        """
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)

        if data["db"]["toolbar"] != "off":
            data["db"]["toolbar"] = "off"

            with open(db, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            for x_pos in range(1,-211,-3):
                toolbarFrame.place(x=x_pos, y=0)
                toolbarFrame.update()
            
            


    
    def time_function(self) -> None:
        """It is a bridge into a function activate"""
        if self.time_on == False:
            self.time_on = True
            self.clock_button.config(highlightbackground="blue")
        else:
            self.time_on = False
            self.clock_button.config(highlightbackground="black")
        self.functions_activate.time_function(self.time_on)
            
    
    def weather_function(self) -> None:
        """It is a bridge into a function activate"""
        if self.weather_on == False:
            self.weather_on = True
            self.weather_button.config(highlightbackground="blue")
        else:
            self.weather_on = False
            self.weather_button.config(highlightbackground="black")
        self.functions_activate.weather_function(self.weather_on)

    def gmail_function(self) -> None:
        """It is a bridge into a function activate"""
        if self.gmail_on == False:
            self.gmail_on = True
            self.home_button.config(highlightbackground="blue")
        else:
            self.gmail_on = False
            self.home_button.config(highlightbackground="black")
        self.functions_activate.gmail_function(self.gmail_on)
    
