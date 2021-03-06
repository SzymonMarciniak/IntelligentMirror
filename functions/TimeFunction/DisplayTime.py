from tkinter import *
from datetime import date
import calendar
import time
import os

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

prefix = os.getcwd()
      
class CurrentTime:
    """
    This class is responsible for the display and correct operation of the clock 
    """
    def __init__(self, tk: Frame, toolbarFrame:Frame ,timeFrame:Frame, weatherFrame:Frame = None,\
         gmailFrame: Frame = None, quoteFrame: Frame = None, calendarFrame:Frame = None, photosFrame:Frame = None, spotifyFrame:Frame = None) -> None:
        """
        Parametrs
        ---------
        tk: Frame
            Main window frame
        toolbarFrame: Frame
            Toolbar frame     
        timeFrame: Frame
            Frame for clock label and date label
        """

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame
        self.spotifyFrame= spotifyFrame
       
        self.clockLabel = Label(timeFrame, font=("Arial", 60), bg="black", fg="white")
        self.dateLabel = Label(timeFrame, font=("Arial", 30), bg="black", fg="white")

        self.timeFrame.bind("<Button-1>", self.drag_start_frame)
        self.timeFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.timeFrame.bind("<ButtonRelease-1>", self.drag_stop)

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
        
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET time_event=1 WHERE id={RFace}")
        toolbar_status = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        x,y = CurrentTime.check_position(self)

        if toolbar_status == "on" and x <= 210:
            x = 210

        self.timeFrame.place(x=x,y=y)

        def tick(ToOn = False):
            """
            Clock operation
            """
           
            timeString = time.strftime(" %H:%M ")

            self.clockLabel.config(text=timeString)
            self.clockLabel.after(5000, tick)  

            my_date = date.today()
            x = calendar.day_name[my_date.weekday()] 
            y = time.strftime("%b")
            z = time.strftime("%d")
            dateString = time.strftime(f"{x},  {y} {z}")

            self.dateLabel.config(text=dateString)
            self.dateLabel.after(900000, tick)
            
            if ToOn:
                ToOn = False 
                self.dateLabel.pack(side=TOP)  
                self.clockLabel.pack(side=BOTTOM)

        tick(True)
    
    def destroy_time(self):
    
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET time_event=0 WHERE id={RFace}")
        connection.close()

        for pack in self.timeFrame.pack_slaves():
            pack.pack_forget()

        self.timeFrame.place_forget() 
    
    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual time position
        Returns
        -------
        x: int
            Value of "x" time position
        y: int 
            value of "y" time position
        """
    
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        coor = base.read_query(connection, f"select time_x, time_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y

    
    def drag_start_frame(self, event):
        self.timeFrame.startX = event.x
        self.timeFrame.startY = event.y

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        
        if toolbar_event == "on":
            self.timeFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame,self.calendarFrame,self.photosFrame, self.spotifyFrame, NoMove="time")

        else:
            self.timeFrame.ToOn = False
        
    
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


       

    def drag_stop(self, event=None):

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET time_x={self.timeFrame.stopX} WHERE id={RFace}")
        base.execute_query(connection, f"update user SET time_y={self.timeFrame.stopY} WHERE id={RFace}")
        connection.close()

        if self.timeFrame.ToOn == True: 
       
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)


