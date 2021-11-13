from tkinter import *
from datetime import date
import calendar
import time

class CurrentTime:
    """
    This class is responsible for the display and correct operation of the clock 
    """
    def __init__(self,
                clockLabel: Label, 
                dateLabel: Label, 
                timeFrame: Frame) -> None:
        """
        Parametrs
        ---------
        clockLabel: Label
            Label for clock
        
        dateLabel: Label
            Label for date
        
        timeFrame: Frame
            Frame for clock label and date label
        """


        self.clockLabel = clockLabel
        self.dateLabel = dateLabel
        self.timeFrame = timeFrame
    
    def clock_date(self) -> None:
        """
        Clock displaying
        """

        self.timeFrame.place(x=1500,y=10)

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