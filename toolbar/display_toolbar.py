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
                calendarIcon: PhotoImage = None,
                quoteIcon: PhotoImage = None,
                leftArrow: PhotoImage = None,
                rightArrow: PhotoImage = None,
                gmailIcon:PhotoImage = None,
                returnIcon:PhotoImage = None,
                test1Icon:PhotoImage = None,
                test2Icon:PhotoImage = None,
                bulbOnIcon: PhotoImage = None,
                rollerShuttersUpIcon: PhotoImage = None,
                pauseIcon: PhotoImage = None,
                rollerShuttersDownIcon: PhotoImage = None,
                instagramIcon: PhotoImage = None,
                spotifyIcon: PhotoImage = None,
                cameraIcon:PhotoImage = None) -> None:
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
        self.calendarIcon = calendarIcon
        self.quoteIcon = quoteIcon
        self.gmailIcon = gmailIcon
        self.returnIcon = returnIcon
        self.test1Icon = test1Icon
        self.test2Icon = test2Icon
        self.bulbOnIcon = bulbOnIcon
        self.rollerShuttersUpIcon = rollerShuttersUpIcon
        self.pauseIcon = pauseIcon
        self.rollerShuttersDownIcon = rollerShuttersDownIcon
        self.instagramIcon = instagramIcon
        self.spotifyIcon = spotifyIcon
        self.cameraIcon = cameraIcon

        self.leftArrow = leftArrow
        self.rightArrow = rightArrow

        self.time_on = False
        self.weather_on = False
        self.gmail_on = False
        self.quote_on = False
        self.calendar_on = False
        self.bulb_on = False 
        self.roller_shutters_up_on = False
        self.roller_shutters_down_on = False
        self.instagram_on = False 
        self.spotify_on = False 

        self.home_button = Button(self.toolbarFrame, image=self.homeIcon, highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenHomeToolbar)
        self.labels_button = Button(self.toolbarFrame, image=self.test1Icon, highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenToolbar)
        self.internet_button = Button(self.toolbarFrame, image=self.test2Icon, highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenInternetToolbar)

        self.clock_button = Button(self.toolbarFrame, image=self.clockIcon, highlightthickness=2, highlightbackground='black', bg='black', command=self.time_function)
        self.weather_button = Button(self.toolbarFrame, image=self.sunIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.weather_function)      
        self.return_button = Button(self.toolbarFrame, image=self.returnIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.OpenPreToolbar)        
        self.calendar_button = Button(self.toolbarFrame, image=self.calendarIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.calendar_function)  
        self.quote_buton = Button(self.toolbarFrame, image=self.quoteIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.quote_function) 
        
        self.bulb_on_button = Button(self.toolbarFrame, image=self.bulbOnIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.bulb_on_function)
        self.roller_shutters_up_button = Button(self.toolbarFrame, image=self.rollerShuttersUpIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.roller_shutters_up_function)
        self.roller_shutters_pause_button = Button(self.toolbarFrame, image=self.pauseIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.roller_shutters_pause_function)
        self.roller_shutters_down_button = Button(self.toolbarFrame, image=self.rollerShuttersDownIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.roller_shutters_down_function)

        self.gmail_button = Button(self.toolbarFrame, image=self.gmailIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.gmail_function)    
        self.instagram_button = Button(self.toolbarFrame, image=self.instagramIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.instagram_function)
        self.spotify_button = Button(self.toolbarFrame, image=self.spotifyIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.spotify_function)
        self.camera_button = Button(self.toolbarFrame, image=self.cameraIcon,highlightthickness=2, highlightbackground='black', bg='black', command=self.camera_function)

        self.arrowFrame = LabelFrame(self.toolbarFrame, bg="black", bd=0)
        self.arrow_button = Button(self.arrowFrame, image=self.rightArrow, bd=0, highlightbackground='black',borderwidth=0, bg='black', \
            highlightthickness=0, command=self.OpenToolbarAnimation)

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["toolbar"] = "off"
            data["db"]["accounts"]["None"]["positions"]["time"]["event"] = "False"
            data["db"]["accounts"]["None"]["positions"]["weather"]["event"] = "False"
            data["db"]["accounts"]["None"]["positions"]["gmail"]["event"] = "False"
            data["db"]["accounts"]["None"]["positions"]["quote"]["event"] = "False"
            data["db"]["accounts"]["None"]["positions"]["calendar"]["event"] = "False"

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


        self.functions_activate = FunctionsActivateClass(self.tk, self.toolbarFrame, self.timeFrame, self.weatherFrame, \
            self.gmailFrame, self.quoteFrame, self.calendarFrame)

        self.check_buttons()
    

    def ForgetPreToolbar(self):
        self.labels_button.pack_forget()
        self.home_button.pack_forget()
        self.internet_button.pack_forget()
        self.arrow_button.pack_forget()
    
    def OpenPreToolbar(self):

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["toolbar"] = "on"

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        self.ForgretToolbar()
        self.ForgetHomeToolbar()
        self.ForgetInternetToolbar()

        self.labels_button.pack(anchor=NW)
        self.home_button.pack(anchor=NW)
        self.internet_button.pack(anchor=NW)
        self.arrow_button.pack(side=RIGHT)

        self.arrowFrame.place(x=209, y=230)
        self.toolbarFrame.place(y=200, width=420)
    
    def ForgretToolbar(self):
        self.clock_button.pack_forget()
        self.weather_button.pack_forget()
        self.calendar_button.pack_forget()
        self.quote_buton.pack_forget()
        self.return_button.pack_forget()

    def OpenToolbar(self) -> None:
        """ 
        Display toolbar main buttons
        
        """
        self.ForgetPreToolbar()
        self.clock_button.pack(anchor=NW)
        self.weather_button.pack(anchor=NW)
        self.calendar_button.pack(anchor=NW)
        self.quote_buton.pack(anchor=NW)
        self.return_button.pack(anchor=NW)
        self.toolbarFrame.place(y=20)
    
    def ForgetHomeToolbar(self):
        self.bulb_on_button.pack_forget()
        self.return_button.pack_forget()
        self.roller_shutters_up_button.pack_forget()
        self.roller_shutters_pause_button.pack_forget()
        self.roller_shutters_down_button.pack_forget()

    def OpenHomeToolbar(self):
        self.ForgetPreToolbar()
        self.bulb_on_button.pack(anchor=NW)
        self.roller_shutters_up_button.pack(anchor=NW)
        self.roller_shutters_pause_button.pack(anchor=NW)
        self.roller_shutters_down_button.pack(anchor=NW)
        self.return_button.pack(anchor=NW)
        self.toolbarFrame.place(y=20)
    
    def ForgetInternetToolbar(self):
        self.gmail_button.pack_forget()
        self.instagram_button.pack_forget()
        self.spotify_button.pack_forget()
        self.camera_button.pack_forget()
        self.return_button.pack_forget() 

    def OpenInternetToolbar(self):
        self.ForgetPreToolbar()
        self.gmail_button.pack(anchor=NW)
        self.instagram_button.pack(anchor=NW)
        self.spotify_button.pack(anchor=NW)
        self.camera_button.pack(anchor=NW)
        self.return_button.pack(anchor=NW)
        self.toolbarFrame.place(y=20) 
        

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

            y_pos= 200

            for x_pos in range(-200,1,10):
                self.toolbarFrame.place(x=x_pos, y=y_pos)

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
            print(weather, timeFrame)
            for x_pos in range(-200,1,10):
                toolbarFrame.place(x=x_pos)

                if timeFrame:
                    if time:
                        Tcx = timeFrame.winfo_x()
                        if Tcx < 210:
                            timeFrame.place(x=x_pos+Tcx+200)
                
                if weatherFrame:
                    if weather:
                        Wcx = weatherFrame.winfo_x()
                        if Wcx < 210:
                            weatherFrame.place(x=x_pos+Wcx+200)

                if gmailFrame:
                    if gmail:
                        Gcx = gmailFrame.winfo_x()
                        if Gcx < 210:
                            gmailFrame.place(x=x_pos+Gcx+200)
                
                if quoteFrame:
                    if quote:
                        Qcx = quoteFrame.winfo_x()
                        if Qcx < 210:
                            quoteFrame.place(x=x_pos+Qcx+200)
                
                if calendarFrame:
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

            y_pos= 200

            for x_pos in range(1,-211,-1):
                self.toolbarFrame.place(x=x_pos, y=y_pos)

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
                toolbarFrame.place(x=x_pos)

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
            self.gmail_button.config(highlightbackground="blue")
        else:
            self.gmail_on = False
            self.gmail_button.config(highlightbackground="black")
        self.functions_activate.gmail_function(self.gmail_on) 
    
    def quote_function(self) -> None:
        if self.quote_on == False:
            self.quote_on = True
            self.quote_buton.config(highlightbackground="blue")
        else:
            self.quote_on = False 
            self.quote_buton.config(highlightbackground="black")
        self.functions_activate.quote_function(self.quote_on)
    
    def calendar_function(self) -> None:
        if self.calendar_on == False:
            self.calendar_on = True 
            self.calendar_button.config(highlightbackground="blue")
        else:
            self.calendar_on = False 
            self.calendar_button.config(highlightbackground="black")
        self.functions_activate.calendar_function(self.calendar_on)
    
    def bulb_on_function(self): 
        if self.bulb_on == False:
            print("Bulb on!!!")
            self.bulb_on = True 
            self.bulb_on_button.config(highlightbackground="blue")
        else:
            print("Bulb off!!!")
            self.bulb_on = False 
            self.bulb_on_button.config(highlightbackground="black")
        #self.functions_activate.bulb_function(self.bulb_on)
        
    def roller_shutters_up_function(self):
        print("Roller shutter up")

    def roller_shutters_pause_function(self):
        print("Roller shutter pause")

    def roller_shutters_down_function(self):
        print("Roller shutter down")
    
    def instagram_function(self):
        if self.instagram_on == False:
            print("Open Instagram")
            self.instagram_on = True 
            self.instagram_button.config(highlightbackground="blue")
        else:
            print("Close Instagram")
            self.instagram_on = False 
            self.instagram_button.config(highlightbackground="black")
        #self.functions_activate.instagram_function(self.instagram_on)
    
    def spotify_function(self):
        if self.spotify_on == False:
            print("Open spotify")
            self.spotify_on = True 
            self.spotify_button.config(highlightbackground="blue")
        else:
            print("Close spotify")
            self.spotify_on = False 
            self.spotify_button.config(highlightbackground="black")
        #self.functions_activate.spotify_function(self.spotify_on)
    
    def camera_function(self):
        print("Taking picture")
        self.functions_activate.camera_function()
      
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
            self.gmail_button.config(highlightbackground="blue")
            self.gmail_on = True
        else:
            self.gmail_button.config(highlightbackground="black")
            self.gmail_on = False 
        
        if quote == "True":
            self.quote_buton.config(highlightbackground="blue")
            self.quote_on = True
        else:
            self.quote_buton.config(highlightbackground="black")
            self.quote_on = False 
        
        if calendar == "True":
            self.calendar_button.config(highlightbackground="blue")
            self.calendar_on = True
        else:
            self.calendar_button.config(highlightbackground="black")
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
    
   
        
        
