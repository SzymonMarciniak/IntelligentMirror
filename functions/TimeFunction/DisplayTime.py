from tkinter import *
from datetime import date
import calendar
import time
import json 
import os

class CurrentTime:
    """
    This class is responsible for the display and correct operation of the clock 
    """
    def __init__(self, tk: Frame, timeFrame:Frame) -> None:
        """
        Parametrs
        ---------
        tk: Frame
            Main window frame
        timeFrame: Frame
            Frame for clock label and date label
        """

        self.timeFrame = timeFrame
        self.clockLabel = Label(timeFrame, font=("Arial", 60), bg="black", fg="white")
        self.dateLabel = Label(timeFrame, font=("Arial", 30), bg="black", fg="white")
    
    def clock_date(self) -> None:
        """
        Clock displaying
        """
        
        x,y = CurrentTime.check_position(self)
        self.timeFrame.place(x=x,y=y)

        def tick():
            """
            Clock operation
            """
           
            timeString = time.strftime(" %H:%M ")

            self.clockLabel.config(text=timeString)
            self.clockLabel.after(100, tick)  

            my_date = date.today()
            x = calendar.day_name[my_date.weekday()] 
            y = time.strftime("%b")
            z = time.strftime("%d")
            dateString = time.strftime(f"{x},  {y} {z}")

            self.dateLabel.config(text=dateString)
            self.dateLabel.after(900000, tick)

            self.dateLabel.pack(side=TOP)  
            self.clockLabel.pack(side=BOTTOM)

        tick()
    
    def check_position(self) -> int:
        """
        This function is responsible for checking actual time position
        Returns
        -------
        x: int
            Value of "x" time position
        y: int 
            value of "y" time position
        """

        prefix = os.getcwd()
        prefix = f"{prefix}/IntelligentMirror/functions/TimeFunction/"
        with open(f"{prefix}time_position.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            x = (data["position"]["x"])
            y = (data["position"]["y"])
        return x, y