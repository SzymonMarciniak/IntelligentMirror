import requests
import shutil
from tkinter import *
from PIL import ImageTk, Image
import os

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

prefix_ = os.getcwd()

class CurrentWeather:
    """This class is responsible for correctly displaying the current weather"""
    def __init__(self,tk:Frame, toolbarFrame:Frame, weatherFrame: Frame, timeFrame: Frame = None,\
         gmailFrame: Frame = None, quoteFrame:Frame = None, calendarFrame:Frame = None, photosFrame:Frame= None) -> None:
        """
        Parametrs
        ---------
        tk: Frame
            Main window frame 
        toolbarFrame: 
            Toolbar frame
        weatherFrame: Frame 
            Frame for all weather labels 
        """

        self.weatherFrame = weatherFrame
        self.tk = tk
        self.toolbarFrame = toolbarFrame
        self.timeFrame = timeFrame
        self.gmailFrame = gmailFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame

        self.temp = Label(self.weatherFrame, font=("Arial", 50))
        self.humidity = Label(self.weatherFrame, font=("Arial", 25))
        self.image = Label(self.weatherFrame, font=("Arial", 40))

        self.weatherFrame.bind("<Button-1>", self.drag_start_frame)
        self.weatherFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.weatherFrame.bind("<ButtonRelease-1>", self.drag_stop)

        self.temp.bind("<Button-1>", self.drag_start_frame)
        self.temp.bind("<B1-Motion>", self.drag_motion_frame)
        self.temp.bind("<ButtonRelease-1>", self.drag_stop)

        self.humidity.bind("<Button-1>", self.drag_start_frame)
        self.humidity.bind("<B1-Motion>", self.drag_motion_frame)
        self.humidity.bind("<ButtonRelease-1>", self.drag_stop)

        self.image.bind("<Button-1>", self.drag_start_frame)
        self.image.bind("<B1-Motion>", self.drag_motion_frame)
        self.image.bind("<ButtonRelease-1>", self.drag_stop)

        
        self.prefix = f"{prefix_}/IntelligentMirror/functions/WeatherFunction/"

    def get_image(self):
        weather_icon_old = Image.open(f"{self.prefix}weather_img.png")
        weather_icon_new = weather_icon_old.resize((140,140))
        self.weather_icon = ImageTk.PhotoImage(weather_icon_new)

    def weather(self) -> None:
        """Enables the weather display function"""


        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET weather_event=1 WHERE id={RFace}")
        toolbar_status = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        x,y = CurrentWeather.check_position(self)

        if toolbar_status == "on" and x <= 210:
            x = 210

        self.weatherFrame.place(x=x, y=y, width=350, height=179)
            
        def weather_loading(ToOn = False):
            """Checking the current weather"""
            api_key = "2e45239b1a0c0bd073f2c968d78cc172"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "kalisz"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            w = response.json()

            
            if w["cod"] != "404":

                q = w["main"]

                current_temperature = q["temp"]

                current_pressure = q["pressure"]

                current_humidity = q["humidity"]

                z = w["weather"]


                icon_id = z[0]["icon"]
                url_i = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)
                response_i = requests.get(url_i, stream=True)
                if response_i.status_code == 200:
                    with open(f"{self.prefix}weather_img.png", "wb") as img:
                        shutil.copyfileobj(response_i.raw, img)
                
                try:
                    self.image.place_forget()
                    self.temp.place_forget()
                    self.humidity.pack_forget()
                except: pass 
                            

                current_temperature = int(current_temperature) - 273
                self.temp.config(text=str(current_temperature) + "°C")
                self.temp.configure(bg="black", fg="white")
                self.temp.after(900000, weather_loading)

                self.humidity.config(text="HUM " + str(current_humidity) + " %  |  " + str(current_pressure) + " hPa")
                self.humidity.configure(bg="black", fg="white")
                self.humidity.after(900000, weather_loading)

                self.get_image()
                self.image.config(image=self.weather_icon, bg="black")
                self.image.after(900000, weather_loading)

                if ToOn:
                    ToOn = False 
                    self.image.place(x=1,y=1)
                    self.temp.place(x=160, y=35)
                    self.humidity.pack(side=BOTTOM)

            else:
                print("Weather not found")
        
        weather_loading(True)
    
    def destroy_weather(self):
    
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET weather_event=0 WHERE id={RFace}")
        connection.close()
        
        for pack in self.weatherFrame.pack_slaves():
            pack.pack_forget()
      
        self.weatherFrame.place_forget()
    
    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual weather position
        Returns
        -------
        x: int
            Value of "x" weather position
        y: int 
            value of "y" weather position
        """


        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        coor = base.read_query(connection, f"select weather_x, weather_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y
    
    def weather_refresh(self, RFace):
        x,y = self.check_position(RFace)
        self.weatherFrame.place_configure(x=x, y=y, width=350, height=179)
        self.weatherFrame.update()

   
    def drag_start_frame(self, event):
        self.weatherFrame.startX = event.x
        self.weatherFrame.startY = event.y

        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        
        if toolbar_event == "on":
            self.weatherFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame,self.photosFrame,NoMove="weather")

        else:
            self.weatherFrame.ToOn = False
    
    
    def drag_motion_frame(self, event):
        x = self.weatherFrame.winfo_x() - self.weatherFrame.startX + event.x
        y = self.weatherFrame.winfo_y() - self.weatherFrame.startY + event.y

        tk_width = 1920
        tk_height = 1080
        frame_width = self.weatherFrame.winfo_width()
        frame_height = self.weatherFrame.winfo_height()

        max_x = tk_width - frame_width
        max_y = tk_height - frame_height

        if x > max_x:
            x = max_x
        elif x < 0:
            x = 0

        if y > max_y:
            y = max_y
        elif y < 0:
            y = 0

        self.weatherFrame.place(x=x, y=y, width=350, height=179)

        self.weatherFrame.stopX = x
        self.weatherFrame.stopY = y

    
    def drag_stop(self, event=None):


        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET weather_x={self.weatherFrame.stopX} WHERE id={RFace}")
        base.execute_query(connection, f"update user SET weather_y={self.weatherFrame.stopY} WHERE id={RFace}")
        connection.close()
        
        if self.weatherFrame.ToOn == True: 
       
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame)
