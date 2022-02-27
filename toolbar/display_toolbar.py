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
                quoteFrame: Frame,
                calendarFrame: Frame,
                clockIcon: PhotoImage = None,
                sunIcon: PhotoImage = None,
                homeIcon: PhotoImage = None,
                contactsIcon: PhotoImage = None,
                settingsIcon: PhotoImage = None,
                leftArrow: PhotoImage = None,
                rightArrow: PhotoImage = None) -> None:
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
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame

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
        self.quote_on = False
        self.calendar_on = False

        self.clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightthickness=2, highlightbackground='black', bg='black', command=self.time_function)
        self.weather_button = Button(self.toolbarFrame, image=self.sunIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.weather_function)      
        self.home_button = Button(self.toolbarFrame, image=self.homeIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.gmail_function)        
        self.contact_button = Button(self.toolbarFrame, image=self.contactsIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.quote_function)  
        self.settings_button = Button(self.toolbarFrame, image=self.settingsIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.calendar_function) 
        
        self.arrowFrame = LabelFrame(self.toolbarFrame, bg="black", bd=0)
        self.arrow_button = Button(self.arrowFrame, image=self.rightArrow, bd=0, highlightbackground='black',borderwidth=0, bg='black', \
            highlightthickness=0, command=self.OpenToolbarAnimation)

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["toolbar"] = "off"

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


        self.functions_activate = FunctionsActivateClass(self.tk, self.toolbarFrame, self.timeFrame, self.weatherFrame, \
            self.gmailFrame, self.quoteFrame, self.calendarFrame)

        self.check_buttons()

    def OpenToolbar(self) -> None:
        """ 
        Display toolbar main buttons
        
        """
      
        self.clock_button.pack(anchor=NW)
        self.weather_button.pack(anchor=NW)
        self.home_button.pack(anchor=NW)
        self.contact_button.pack(anchor=NW)
        self.settings_button.pack(anchor=NW)

        
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
            quoteOn = data["db"]["accounts"]["None"]["positions"]["quote"]["event"]
            calendarOn = data["db"]["accounts"]["None"]["positions"]["calendar"]["event"]
        
        if timeOn == "True":
            self.time_function()
        if weatherOn == "True":
            self.weather_function()
        if gmailOn == "True":
            self.gmail_function()
        if quoteOn == "True":
            self.quote_function()
        if calendarOn == "True":
            self.calendar_function()
        

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

            time, weather, gmail, quote, calendar = self.displacement_function()
            for x_pos in range(-200,1,10):
                self.toolbarFrame.place(x=x_pos, y=0)

                if time:
                    Tcx = self.timeFrame.winfo_x()
                    if Tcx < 210:
                        self.timeFrame.place(x=x_pos+Tcx+200)
                
                if weather:
                    Wcx = self.weatherFrame.winfo_x()
                    if Wcx < 210:
                        self.weatherFrame.place(x=x_pos+Wcx+200)
                    
                if gmail:
                    Gcx = self.gmailFrame.winfo_x()
                    if Gcx < 210:
                        self.gmailFrame.place(x=x_pos+Gcx+200)
                
                if quote:
                    Qcx = self.quoteFrame.winfo_x()
                    if Qcx < 210:
                        self.quoteFrame.place(x=x_pos+Qcx+200)
                
                if calendar:
                    Ccx = self.calendarFrame.winfo_x()
                    if Ccx < 210:
                        self.calendarFrame.place(x=x_pos+Ccx+200)

                self.toolbarFrame.update()
            self.arrow_button.config(image=self.leftArrow, command=self.HideToolbarAnimation)
        
    
            
        
    
    def OpenToolbarAnimation_DF(toolbarFrame: Frame, timeFrame: Frame = None, weatherFrame: Frame = None, \
        gmailFrame: Frame = None, quoteFrame: Frame = None, calendarFrame:Frame = None) -> None:
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

            time, weather, gmail, quote, calendar = Toolbar.displacement_function()
            for x_pos in range(-200,1,10):
                toolbarFrame.place(x=x_pos, y=0)

                if timeFrame:
                    if time:
                        Tcx = timeFrame.winfo_x()
                        if Tcx < 210:
                            timeFrame.place(x=x_pos+Tcx+200)
                    
                    if weather:
                        Wcx = weatherFrame.winfo_x()
                        if Wcx < 210:
                            weatherFrame.place(x=x_pos+Wcx+200)
                        
                    if gmail:
                        Gcx = gmailFrame.winfo_x()
                        if Gcx < 210:
                            gmailFrame.place(x=x_pos+Gcx+200)
                    if quote:
                        Qcx = quoteFrame.winfo_x()
                        if Qcx < 210:
                            quoteFrame.place(x=x_pos+Qcx+200)
                    
                    if calendar:
                        Ccx = calendarFrame.winfo_x()
                        if Ccx < 210:
                            calendarFrame.place(x=x_pos+Ccx+200)

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

            time,timeX, weather,weatherX, gmail,gmailX, quote, quoteX, calendar, calendarX = self.displacement_function(val=True)
            for x_pos in range(1,-211,-1):
                self.toolbarFrame.place(x=x_pos, y=0)

                if time:
                    if timeX < 210:
                        self.timeFrame.place(x=x_pos+timeX+211)
                
                if weather:
                    if weatherX < 210:
                        self.weatherFrame.place(x=x_pos+weatherX+211)
                    
                if gmail:
                    if gmailX < 210:
                        self.gmailFrame.place(x=x_pos+gmailX+211)
                
                if quote:
                    if quoteX < 210:
                        self.quoteFrame.place(x=x_pos+quoteX+211)
                
                if calendar:
                    if calendarX < 210:
                        self.calendarFrame.place(x=x_pos+calendarX+211)

                self.toolbarFrame.update()

            
            self.arrow_button.config(image=self.rightArrow, command=self.OpenToolbarAnimation)
        
            



    
    def HideToolbarAnimation_DF(toolbarFrame: Frame, timeFrame: Frame = None, weatherFrame: Frame = None, \
        gmailFrame: Frame = None,quoteFrame: Frame = None,calendarFrame:Frame=None, NoMove = None) -> None:
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

                time,timeX, weather,weatherX, gmail,gmailX, quote, quoteX, calendar, calendarX = Toolbar.displacement_function(val=True)
                if timeFrame:
                    if not NoMove == "time":
                        if time:
                            if timeX < 210:
                                timeFrame.place(x=x_pos+timeX+211)

                    if not NoMove == "weather":
                        if weather:
                            if weatherX < 210:
                                weatherFrame.place(x=x_pos+weatherX+211)
                    
                    if not NoMove == "gmail":
                        if gmail:
                            if gmailX < 210:
                                gmailFrame.place(x=x_pos+gmailX+211)
                    
                    if not NoMove == "quote":
                        if quote:
                            if quoteX < 210:
                                quoteFrame.place(x=x_pos+quoteX+211)
                
                    if not NoMove == "calendar":
                            if calendar:
                                if calendarX < 210:
                                    calendarFrame.place(x=x_pos+calendarX+211)

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
    
    def quote_function(self) -> None:
        if self.quote_on == False:
            self.quote_on = True
            self.contact_button.config(highlightbackground="blue")
        else:
            self.quote_on = False 
            self.contact_button.config(highlightbackground="black")
        self.functions_activate.quote_function(self.quote_on)
    
    def calendar_function(self) -> None:
        if self.calendar_on == False:
            self.calendar_on = True 
            self.settings_button.config(highlightbackground="blue")
        else:
            self.calendar_on = False 
            self.settings_button.config(highlightbackground="black")
        self.functions_activate.calendar_function(self.calendar_on)
    
    def check_buttons(self):
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            time = data["db"]["accounts"][RFace]["positions"]["time"]["event"]
            weather = data["db"]["accounts"][RFace]["positions"]["weather"]["event"]
            gmail = data["db"]["accounts"][RFace]["positions"]["gmail"]["event"]
            quote = data["db"]["accounts"][RFace]["positions"]["quote"]["event"]
            calendar = data["db"]["accounts"][RFace]["positions"]["calendar"]["event"]
            toolbar = data["db"]["toolbar"]
        
        if time == "True":
            self.clock_button.config(highlightbackground="blue")
            self.time_on = True
        else:
            self.clock_button.config(highlightbackground="black")
            self.time_on = False 
        
        if weather == "True":
            self.weather_button.config(highlightbackground="blue")
            self.weather_on = True
        else:
            self.weather_button.config(highlightbackground="black")
            self.weather_on = False 
        
        if gmail == "True":
            self.home_button.config(highlightbackground="blue")
            self.gmail_on = True
        else:
            self.home_button.config(highlightbackground="black")
            self.gmail_on = False 
        
        if quote == "True":
            self.contact_button.config(highlightbackground="blue")
            self.quote_on = True
        else:
            self.contact_button.config(highlightbackground="black")
            self.quote_on = False 
        
        if calendar == "True":
            self.settings_button.config(highlightbackground="blue")
            self.calendar_on = True
        else:
            self.settings_button.config(highlightbackground="black")
            self.calendar_on = False 

        if toolbar == "on":
            self.arrow_button.config(image=self.leftArrow, command=self.HideToolbarAnimation)
        else:
            self.arrow_button.config(image=self.rightArrow, command=self.OpenToolbarAnimation)
        
        self.tk.after(2000, self.check_buttons)

    @staticmethod
    def displacement_function(val=False,*args):
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            timeX = data["db"]["accounts"][RFace]["positions"]["time"]["x"]
            weatherX = data["db"]["accounts"][RFace]["positions"]["weather"]["x"]
            gmailX = data["db"]["accounts"][RFace]["positions"]["gmail"]["x"]
            quoteX = data["db"]["accounts"][RFace]["positions"]["quote"]["x"]
            calendarX = data["db"]["accounts"][RFace]["positions"]["calendar"]["x"]

        Dtime, Dweather, Dgmail, Dquote, Dcalendar = False, False, False, False, False 
        if timeX <= 200:
            Dtime = True 
        if weatherX <=200:
            Dweather = True
        if gmailX <=200:
            Dgmail = True 
        if quoteX <= 200:
            Dquote = True
        if calendarX <= 200:
            Dcalendar = True
        
        if val: return Dtime,timeX, Dweather,weatherX, Dgmail,gmailX, Dquote,quoteX, Dcalendar, calendarX
        else: return Dtime, Dweather, Dgmail, Dquote, Dcalendar
        
        
