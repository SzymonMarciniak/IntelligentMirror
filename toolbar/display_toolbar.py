from math import radians
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

        clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightbackground='black', bg='black', command=toolbar.time_function)
        weather_button = Button(self.toolbarFrame, image=self.sunIcon, highlightbackground='black', bg='black', command=toolbar.weather_function)      
        home_button = Button(self.toolbarFrame, image=self.homeIcon, highlightbackground='black', bg='black', command=toolbar.gmail_function)         #to change
        contact_button = Button(self.toolbarFrame, image=self.contactsIcon, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation)  #
        settings_button = Button(self.toolbarFrame, image=self.settingsIcon, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation) #
        

        clock_button.pack(anchor=NW)
        weather_button.pack(anchor=NW)
        home_button.pack(anchor=NW)
        contact_button.pack(anchor=NW)
        settings_button.pack(anchor=NW)

        self.arrowFrame = LabelFrame(self.toolbarFrame, bg="black", bd=0)
        self.arrow_button = Button(self.arrowFrame, image=self.rightArrow, highlightbackground='black', bg='black', command=toolbar.OpenToolbarAnimation)
        self.arrow_button.pack(side=RIGHT)
        self.arrowFrame.place(x=203, y=399)

        
        self.toolbarFrame.place(x=-201,y=0, width=420)

        


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
        self.functions_activate.time_function()
    
    def weather_function(self) -> None:
        """It is a bridge into a function activate"""
        self.functions_activate.weather_function()

    def gmail_function(self) -> None:
        """It is a bridge into a function activate"""
        self.functions_activate.gmail_function()
    
