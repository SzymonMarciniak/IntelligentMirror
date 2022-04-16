from tkinter import *
import os 
import time 

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

class Spotify:
    def __init__(self, tk, spotifyFrame) -> None:
        self.tk = tk
        self.spotifyFrame = spotifyFrame 

        # self.spotifyFrame.bind("<Button-1>", self.drag_start_frame)
        # self.spotifyFrame.bind("<B1-Motion>", self.drag_motion_frame)
        # self.spotifyFrame.bind("<ButtonRelease-1>", self.drag_stop)

    def main_spotify(self):
        pass 

    def next_song(self):
        os.system("""dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next""")
    
    def previous_song(self):
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")

    def pause_song(self):
        os.system("""dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
                    method return time=1650144091.131376 sender=:1.260 -> destination=:1.1043 serial=342 reply_serial=2""")

    def destroy_spotify(self):
        pass 

    # def check_position(self, RFace=None) -> int:
    #     """
    #     This function is responsible for checking actual time position
    #     Returns
    #     -------
    #     x: int
    #         Value of "x" time position
    #     y: int 
    #         value of "y" time position
    #     """
    
    #     connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
    #     if RFace == None:
    #         RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
    #     coor = base.read_query(connection, f"select time_x, time_y from user WHERE id={RFace}")[0]
    #     connection.close()

    #     x = coor[0]
    #     y = coor[1]

    #     return x, y

    # def drag_start_frame(self, event):
    #     self.timeFrame.startX = event.x
    #     self.timeFrame.startY = event.y

    #     connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
    #     toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
    #     connection.close()
        
    #     if toolbar_event == "on":
    #         self.timeFrame.ToOn = True 
    #         from IntelligentMirror.toolbar.display_toolbar import Toolbar
    #         Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
    #             self.gmailFrame, self.quoteFrame,self.calendarFrame,self.photosFrame, NoMove="time")

    #     else:
    #         self.timeFrame.ToOn = False
        
    
    # def drag_motion_frame(self, event):
    #     x = self.timeFrame.winfo_x() - self.timeFrame.startX + event.x
    #     y = self.timeFrame.winfo_y() - self.timeFrame.startY + event.y
        
    #     tk_width = 1920
    #     tk_height = 1080
    #     frame_width = self.timeFrame.winfo_width()
    #     frame_height = self.timeFrame.winfo_height()

    #     max_x = tk_width - frame_width
    #     max_y = tk_height - frame_height

    #     if x > max_x:
    #         x = max_x
    #     elif x < 0:
    #         x = 0

    #     if y > max_y:
    #         y = max_y
    #     elif y < 0:
    #         y = 0

    #     self.timeFrame.place(x=x, y=y)

    #     self.timeFrame.stopX = x
    #     self.timeFrame.stopY = y


       

    # def drag_stop(self, event=None):

    #     connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
    #     RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
    #     base.execute_query(connection, f"update user SET time_x={self.timeFrame.stopX} WHERE id={RFace}")
    #     base.execute_query(connection, f"update user SET time_y={self.timeFrame.stopY} WHERE id={RFace}")
    #     connection.close()

    #     if self.timeFrame.ToOn == True: 
       
    #         from IntelligentMirror.toolbar.display_toolbar import Toolbar
    #         Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
    #              self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame)


if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")

    spotifyFrame = LabelFrame(tk, bg="gray", bd=1)

    spotify = Spotify(tk, spotifyFrame)
    spotify.main_spotify()
    
