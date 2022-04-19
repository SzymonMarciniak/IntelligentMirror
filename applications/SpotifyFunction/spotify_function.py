from tkinter import *
import os 
from PIL import ImageTk, Image

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

prefix = os.getcwd()
icons_prefix = f"{prefix}/IntelligentMirror/icons/"

class Spotify:
    def __init__(self, tk: Frame = None, toolbarFrame:Frame = None, spotifyFrame: Frame = None, timeFrame:Frame = None, weatherFrame:Frame = None,\
            gmailFrame: Frame = None, quoteFrame: Frame = None, calendarFrame:Frame = None, photosFrame:Frame = None) -> None:

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame 
        self.spotifyFrame = spotifyFrame 

        next_icon_old = Image.open(f"{icons_prefix}next.png")
        next_icon_new = next_icon_old.resize((100,100))
        self.next_icon = ImageTk.PhotoImage(next_icon_new)

        pauseS_icon_old = Image.open(f"{icons_prefix}pauseS.png")
        pauseS_icon_new = pauseS_icon_old.resize((100,100))
        self.pauseS_icon = ImageTk.PhotoImage(pauseS_icon_new)

        previous_icon_old = Image.open(f"{icons_prefix}previous.png")
        previous_icon_new = previous_icon_old.resize((100,100))
        self.previous_icon = ImageTk.PhotoImage(previous_icon_new)

        self.nextButton = Button(self.spotifyFrame,bg="gray" , image=self.next_icon, command=self.next_song)
        self.previousButton = Button(self.spotifyFrame,bg="gray", image=self.previous_icon, command=self.previous_song)
        self.pauseButton = Button(self.spotifyFrame,bg="gray",image=self.pauseS_icon, command=self.pause_song)

        self.spotifyFrame.bind("<Button-1>", self.drag_start_frame)
        self.spotifyFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.spotifyFrame.bind("<ButtonRelease-1>", self.drag_stop)

        self.nextButton.bind("<Button-1>", self.drag_start_frame)
        self.nextButton.bind("<B1-Motion>", self.drag_motion_frame)
        self.nextButton.bind("<ButtonRelease-1>", self.drag_stop)

        self.previousButton.bind("<Button-1>", self.drag_start_frame)
        self.previousButton.bind("<B1-Motion>", self.drag_motion_frame)
        self.previousButton.bind("<ButtonRelease-1>", self.drag_stop)

        self.pauseButton.bind("<Button-1>", self.drag_start_frame)
        self.pauseButton.bind("<B1-Motion>", self.drag_motion_frame)
        self.pauseButton.bind("<ButtonRelease-1>", self.drag_stop)

        self.to_move = False 

    def main_spotify(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET spotify_event=1 WHERE id={RFace}")
        toolbar_status = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        x,y = Spotify.check_position(self)

        if toolbar_status == "on" and x <= 210:
            x = 210

        self.spotifyFrame.place(x=x, y=y)

        def display(ToOn=False):

            if ToOn:
                self.previousButton.grid(column=0, row=0)
                self.pauseButton.grid(column=1, row=0)
                self.nextButton.grid(column=2, row=0)

        display(True)

    def next_song(self):
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_on = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        if toolbar_on == "off":
            os.system("""dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next""")
    
    def previous_song(self):
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_on = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        if toolbar_on == "off":
            os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
            os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")

    def pause_song(self):
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_on = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        if toolbar_on == "off":
            os.system("""dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
                        method return time=1650144091.131376 sender=:1.260 -> destination=:1.1043 serial=342 reply_serial=2""")

    def destroy_spotify(self):
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET spotify_event=0 WHERE id={RFace}")
        connection.close()

        for pack in self.spotifyFrame.grid_slaves():
            pack.grid_forget()

        self.spotifyFrame.place_forget()  

    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual spotify position
        Returns
        -------
        x: int
            Value of "x" spotify position
        y: int 
            value of "y" spotify position
        """
    
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        coor = base.read_query(connection, f"select spotify_x, spotify_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y

    def drag_start_frame(self, event):
        print("Drag start")
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()
        
        if toolbar_event == "on":
            print("CHeck start")
            self.to_move = True 
            self.spotifyFrame.startX = event.x
            self.spotifyFrame.startY = event.y

            self.spotifyFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame,self.calendarFrame,self.photosFrame,self.spotifyFrame ,NoMove="spotify")

        else:
            print("Nieieee pozwwalana ")
            self.spotifyFrame.ToOn = False
            self.to_move = False 
             
        
    
    def drag_motion_frame(self, event):
    
        if self.to_move:
            x = self.spotifyFrame.winfo_x() - self.spotifyFrame.startX + event.x
            y = self.spotifyFrame.winfo_y() - self.spotifyFrame.startY + event.y
            
            tk_width = 1920
            tk_height = 1080
            frame_width = self.spotifyFrame.winfo_width()
            frame_height = self.spotifyFrame.winfo_height()

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

            self.spotifyFrame.place(x=x, y=y)

            self.spotifyFrame.stopX = x
            self.spotifyFrame.stopY = y
       

    def drag_stop(self, event=None):
        if self.to_move:
            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
            base.execute_query(connection, f"update user SET spotify_x={self.spotifyFrame.stopX} WHERE id={RFace}")
            base.execute_query(connection, f"update user SET spotify_y={self.spotifyFrame.stopY} WHERE id={RFace}")
            connection.close()

            if self.spotifyFrame.ToOn == True: 
        
                from IntelligentMirror.toolbar.display_toolbar import Toolbar
                Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                    self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)

    
