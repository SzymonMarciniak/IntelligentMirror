from tkinter import *

from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass


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
                settingsIcon: PhotoImage) -> None:
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
    

        self.functions_activate = FunctionsActivateClass(self.tk, self.timeFrame, self.weatherFrame, self.gmailFrame)


    def OpenToolbar(self) -> None:
        """ 
        Display toolbar main buttons
        
        """
        toolbar = Toolbar(self.tk,self.toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.clockIcon, self.sunIcon, \
             self.homeIcon, self.contactsIcon, self.settingsIcon)

        clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightbackground='black', bg='black', command=toolbar.time_function)
        weather_button = Button(self.toolbarFrame, image=self.sunIcon, highlightbackground='black', bg='black', command=toolbar.weather_function)      
        home_button = Button(self.toolbarFrame, image=self.homeIcon, highlightbackground='black', bg='black', command=toolbar.gmail_function)         #to change
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
        Show toolbar 
        """
        for x_pos in range(-200,1,10):
            self.toolbarFrame.place(x=x_pos, y=0)
            self.toolbarFrame.update()
    
    def OpenToolbarAnimation_DF(toolbarFrame: Frame) -> None:
        """
        Show toolbar from diffrent file
        Paramets
        --------
        toolbarFrame: Frame
            Frame for toolbar
        """
        for x_pos in range(-200,1,10):
            toolbarFrame.place(x=x_pos, y=0)
            toolbarFrame.update()
    
    def HideToolbarAnimation(self) -> None:
        """
        Hide toolbar
        """
        for x_pos in range(1,-200,-1):
            self.toolbarFrame.place(x=x_pos, y=0)
            self.toolbarFrame.update()
    
    def HideToolbarAnimation_DF(toolbarFrame: Frame) -> None:
        """
        Hide toolbar from diffrent file
        Paramets
        --------
        toolbarFrame: Frame
            Frame for toolbar
        """
        for x_pos in range(1,-200,-3):
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
    
