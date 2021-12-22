import requests
import shutil
from tkinter import *
from PIL import ImageTk, Image
import os
import json

class CurrentWeather:
    """This class is responsible for correctly displaying the current weather"""
    def __init__(self,tk:Frame, weatherFrame: Frame) -> None:
        """
        Parametrs
        ---------
        tk: Frame
            Main window frame 
        weatherFrame: Frame 
            Frame for all weather labels 
        """

        
        self.weatherFrame = weatherFrame
        self.tk = tk

        self.temp = Label(weatherFrame, font=("Arial", 50))
        self.pressure = Label(weatherFrame, font=("Arial", 35))
        self.humidity = Label(weatherFrame, font=("Arial", 25))
        self.image = Label(weatherFrame, font=("Arial", 40))


        prefix = os.getcwd()
        self.prefix = f"{prefix}/IntelligentMirror/functions/WeatherFunction/"

        weather_icon_old = Image.open(f"{self.prefix}weather_img.png")
        weather_icon_new = weather_icon_old.resize((140,140))
        self.weather_icon = ImageTk.PhotoImage(weather_icon_new)

    def weather(self) -> None:
        """Enables the weather display function"""
       
        x,y = CurrentWeather.check_position(self)
        self.weatherFrame.place(x=x, y=y, width=350, height=179)
           
        def weather_loading():
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
                    with open(f"{self.prefix}/weather_img.png", "wb") as img:
                        shutil.copyfileobj(response_i.raw, img)
                            

                current_temperature = int(current_temperature) - 273
                self.temp.config(text=str(current_temperature) + "°C")
                self.temp.configure(bg="black", fg="white")
                self.temp.after(900000, weather_loading)

                self.pressure.config(text=str(current_pressure) + " hPa")
                self.pressure.configure(bg="black", fg="white")
                self.pressure.after(900000, weather_loading)

                self.humidity.config(text="HUM " + str(current_humidity) + " %  |  " + str(current_pressure) + " hPa")
                self.humidity.configure(bg="black", fg="white")
                self.humidity.after(900000, weather_loading)

                self.image.config(image=self.weather_icon, bg="black")
                self.image.after(900000, weather_loading)

                self.image.place(x=1,y=1)
                self.temp.place(x=160, y=35)
                self.humidity.pack(side=BOTTOM)

            else:
                print("Weather not found")
        
        weather_loading()
    
    def check_position(self) -> int:
        """
        This function is responsible for checking actual weather position
        Returns
        -------
        x: int
            Value of "x" time position
        y: int 
            value of "y" time position
        """

        prefix = os.getcwd()
        prefix = f"{prefix}/IntelligentMirror/functions/WeatherFunction/"
        with open(f"{prefix}weather_position.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            x = (data["position"]["x"])
            y = (data["position"]["y"])
        return x, y

        
