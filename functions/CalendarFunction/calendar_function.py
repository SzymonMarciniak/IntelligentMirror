from tkinter import * 
import os

from IntelligentMirror.DataBase.data_base import DataBase

prefix = os.getcwd()

base = DataBase()

connection_data = base.create_db_connection("localhost","szymon", "dzbanek", "mirror")
query = "select date, name from event"
events = base.read_query(connection_data, query)
connection_data.close()

class Calendar:
    def __init__(self, tk: Frame, toolbarFrame:Frame , calendarFrame: LabelFrame, timeFrame:Frame = None, weatherFrame:Frame = None,\
         gmailFrame: Frame = None, quoteFrame: Frame = None, photosFrame:Frame = None, spotifyFrame: Frame= None) -> None:

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame 
        self.photosFrame = photosFrame
        self.spotifyFrame = spotifyFrame

        self.calendar_header = Label(self.calendarFrame, text="Calendar", font=("Arial", 30), bg="black", fg="white")

        self.calendar_body = LabelFrame(self.calendarFrame,  bg="black", bd=1)
        self.event_1 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_2 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_3 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_4 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_5 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_6 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")
        self.event_7 = Label(self.calendar_body, font=("Arial", 20), bg="black", fg="white", borderwidth=1, relief="ridge")

        self.calendar_header.bind("<Button-1>", self.drag_start_frame)
        self.calendar_header.bind("<B1-Motion>", self.drag_motion_frame)
        self.calendar_header.bind("<ButtonRelease-1>", self.drag_stop)

        self.calendar_body.bind("<Button-1>", self.drag_start_frame)
        self.calendar_body.bind("<B1-Motion>", self.drag_motion_frame)
        self.calendar_body.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_1.bind("<Button-1>", self.drag_start_frame)
        self.event_1.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_1.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_2.bind("<Button-1>", self.drag_start_frame)
        self.event_2.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_2.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_3.bind("<Button-1>", self.drag_start_frame)
        self.event_3.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_3.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_4.bind("<Button-1>", self.drag_start_frame)
        self.event_4.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_4.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_5.bind("<Button-1>", self.drag_start_frame)
        self.event_5.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_5.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_6.bind("<Button-1>", self.drag_start_frame)
        self.event_6.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_6.bind("<ButtonRelease-1>", self.drag_stop)

        self.event_7.bind("<Button-1>", self.drag_start_frame)
        self.event_7.bind("<B1-Motion>", self.drag_motion_frame)
        self.event_7.bind("<ButtonRelease-1>", self.drag_stop)


    def calendarMain(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection,"select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET calendar_event=1 WHERE id={RFace}")
        toolbar_status = base.read_query(connection,"select toolbar from camera")[0][0]
        connection.close()

        x,y = Calendar.check_position(self)

        if toolbar_status == "on" and x <= 210:
            x = 210
            
        self.calendarFrame.place(x=x,y=y)
        

        events_amount = len(events)

        if not events_amount:
            self.event_1.config(text="No events") 
            self.event_1.pack(side=BOTTOM)
        
        if events_amount >= 1:
            event_01 = events[0]
            event_1_date = event_01[0]
            event_1_body = event_01[1]
            self.event_1.config(text=f"{event_1_date}\n{event_1_body}", width=20)
            self.event_1.pack(side=TOP)
        
        if events_amount >= 2:
            event_02 = events[1]
            event_2_date = event_02[0]
            event_2_body = event_02[1]
            self.event_2.config(text=f"{event_2_date}\n{event_2_body}", width=20)
            self.event_2.pack(side=TOP)

        if events_amount >= 3:
            event_03 = events[2]
            event_3_date = event_03[0]
            event_3_body = event_03[1]
            self.event_3.config(text=f"{event_3_date}\n{event_3_body}", width=20)
            self.event_3.pack(side=TOP)

        if events_amount >= 4:
            event_04 = events[3]
            event_4_date = event_04[0]
            event_4_body = event_04[1]
            self.event_4.config(text=f"{event_4_date}\n{event_4_body}", width=20)
            self.event_4.pack(side=TOP)

        if events_amount >= 5:
            event_05 = events[4]
            event_5_date = event_05[0]
            event_5_body = event_05[1]
            self.event_5.config(text=f"{event_5_date}\n{event_5_body}", width=20)
            self.event_5.pack(side=TOP)
        
        if events_amount >= 6:
            event_06 = events[5]
            event_6_date = event_06[0]
            event_6_body = event_06[1]
            self.event_6.config(text=f"{event_6_date}\n{event_6_body}", width=20)
            self.event_6.pack(side=TOP)
        
        if events_amount >= 7:
            event_07 = events[6]
            event_7_date = event_07[0]
            event_7_body = event_07[1]
            self.event_7.config(text=f"{event_7_date}\n{event_7_body}", width=20)
            self.event_7.pack(side=TOP)
        
        self.calendar_header.pack(side=TOP)
        self.calendar_body.pack(side=BOTTOM)

    
    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual calendar position
        Returns
        -------
        x: int
            Value of "x" calendar position
        y: int 
            value of "y" calendar position
        """

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        coor = base.read_query(connection, f"select calendar_x, calendar_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y
    
    def destroy_calendar(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET calendar_event=0 WHERE id={RFace}")
        connection.close()

        for pack in self.calendarFrame.pack_slaves():
            pack.pack_forget()

        self.calendarFrame.place_forget() 

    
    def drag_start_frame(self, event):
        self.calendarFrame.startX = event.x
        self.calendarFrame.startY = event.y
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        
        if toolbar_event == "on":
            self.calendarFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame,self.calendarFrame,self.photosFrame, self.spotifyFrame, NoMove="calendar")

        else:
            self.calendarFrame.ToOn = False
        
    
    def drag_motion_frame(self, event):
        x = self.calendarFrame.winfo_x() - self.calendarFrame.startX + event.x
        y = self.calendarFrame.winfo_y() - self.calendarFrame.startY + event.y
        
        tk_width = 1920
        tk_height = 1080
        frame_width = self.calendarFrame.winfo_width()
        frame_height = self.calendarFrame.winfo_height()

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

        self.calendarFrame.place(x=x, y=y)

        self.calendarFrame.stopX = x
        self.calendarFrame.stopY = y


       

    def drag_stop(self, event=None):

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET calendar_x={self.calendarFrame.stopX} WHERE id={RFace}")
        base.execute_query(connection, f"update user SET calendar_y={self.calendarFrame.stopY} WHERE id={RFace}")
        connection.close()

        if self.calendarFrame.ToOn == True: 
       
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
