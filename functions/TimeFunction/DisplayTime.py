from tkinter import *
from datetime import date
import calendar
import time
import json 
import os


prefix = os.getcwd()
db = f"{prefix}/IntelligentMirror/DataBase.json"
      

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

        self.timeFrame.bind("<Button-1>", CurrentTime.drag_start)
        self.timeFrame.bind("<B1-Motion>", CurrentTime.drag_motion)
        self.timeFrame.bind("<ButtonRelease-1>", CurrentTime.drag_stop)

        self.clockLabel.bind("<Button-1>", self.drag_start_frame)
        self.clockLabel.bind("<B1-Motion>", self.drag_motion_frame)
        self.clockLabel.bind("<ButtonRelease-1>", self.drag_stop)

        self.dateLabel.bind("<Button-1>", self.drag_start_frame)
        self.dateLabel.bind("<B1-Motion>", self.drag_motion_frame)
        self.dateLabel.bind("<ButtonRelease-1>", self.drag_stop)
    
    
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

    
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            x = data["db"]["functions"]["positions"]["time"]["x"]
            y = data["db"]["functions"]["positions"]["time"]["y"]
        return x, y



    @staticmethod
    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
    
    @staticmethod
    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        
        tk_width = 1920
        tk_height = 1080
        frame_width = widget.winfo_width()
        frame_height = widget.winfo_height()

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
        
        widget.place(x=x, y=y)

        widget.stopX = x
        widget.stopY = y

    @staticmethod
    def drag_stop(event):
        widget = event.widget
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["functions"]["positions"]["time"]["x"] = widget.stopX 
            data["db"]["functions"]["positions"]["time"]["y"] = widget.stopY 

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)



    
    def drag_start_frame(self, event):
        self.timeFrame.startX = event.x
        self.timeFrame.startY = event.y
    
    
    def drag_motion_frame(self, event):
        x = self.timeFrame.winfo_x() - self.timeFrame.startX + event.x
        y = self.timeFrame.winfo_y() - self.timeFrame.startY + event.y
        
        tk_width = 1920
        tk_height = 1080
        frame_width = self.timeFrame.winfo_width()
        frame_height = self.timeFrame.winfo_height()

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

        self.timeFrame.place(x=x, y=y)

        self.timeFrame.stopX = x
        self.timeFrame.stopY = y


       

    def drag_stop(self, event):

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["functions"]["positions"]["time"]["x"] = self.timeFrame.stopX 
            data["db"]["functions"]["positions"]["time"]["y"] = self.timeFrame.stopY 

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


