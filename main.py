import PIL.Image, PIL.ImageTk
from tkinter import *
from time import *
import threading
import os
 
from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.camera.video_capture import Camera
from IntelligentMirror.DataBase.data_base import DataBase

base = DataBase()

prefix = os.getcwd()
icon_prefix = f"{prefix}/IntelligentMirror/icons/"

tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.config(cursor="fleur")
tk.bind("<Escape>", exit)

toolbarFrame = Frame(tk, bg="black")

timeFrame = LabelFrame(tk, bg="black", bd=0)
weatherFrame = LabelFrame(tk, bg="black", bd=0)
gmailFrame = LabelFrame(tk, bg="black", bd=0)
quoteFrame = LabelFrame(tk, bg="black", bd=0)
calendarFrame = LabelFrame(tk, bg="black", bd=0)
photosFrame = LabelFrame(tk, bg="black", bd=1)
spotifyFrame = LabelFrame(tk, bg="black", bd=0)


clockIcon = PhotoImage(file=f"{icon_prefix}clock.png") 
sunIcon = PhotoImage(file=f"{icon_prefix}weather.png") 
homeIcon = PhotoImage(file=f"{icon_prefix}home.png") 
calendarIcon = PhotoImage(file=f"{icon_prefix}calendar.png") 
quoteIcon = PhotoImage(file=f"{icon_prefix}quote.png") 
gmailIcon = PhotoImage(file=f"{icon_prefix}mail.png")
returnIcon = PhotoImage(file=f"{icon_prefix}return.png")
test1Icon = PhotoImage(file=f"{icon_prefix}apps2.png")
test2Icon = PhotoImage(file=f"{icon_prefix}web apps.png")
bulbOnIcon = PhotoImage(file=f"{icon_prefix}bulb.png")
rollerShuttersUpIcon = PhotoImage(file=f"{icon_prefix}up.png")
pauseIcon = PhotoImage(file=f"{icon_prefix}pause.png")
rollerShuttersDownIcon = PhotoImage(file=f"{icon_prefix}down.png")
instagramIcon = PhotoImage(file=f"{icon_prefix}instagram.png")
spotifyIcon = PhotoImage(file=f"{icon_prefix}spotify.png")
cameraIcon = PhotoImage(file=f"{icon_prefix}camera.png")

left_arrow = PIL.Image.open(f"{icon_prefix}left.png")
left_arrow = left_arrow.resize((150,150))
left_arrow = PIL.ImageTk.PhotoImage(left_arrow)
right_arrow = PIL.Image.open(f"{icon_prefix}right.png")
right_arrow = right_arrow.resize((150,150))
right_arrow = PIL.ImageTk.PhotoImage(right_arrow)

no_move_icon = PIL.Image.open(f"{icon_prefix}finger.png")
no_move_icon = no_move_icon.resize((120,120))
no_move_icon = PIL.ImageTk.PhotoImage(no_move_icon)

                
camera = Camera(tk, toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame ,calendarFrame,photosFrame,spotifyFrame, no_move_icon)

toolbar = Toolbar(tk,toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame, calendarFrame, photosFrame, spotifyFrame, \
    clockIcon, sunIcon, homeIcon, calendarIcon, quoteIcon, left_arrow, right_arrow, gmailIcon,returnIcon, test1Icon, test2Icon, \
        bulbOnIcon, rollerShuttersUpIcon, pauseIcon, rollerShuttersDownIcon, instagramIcon, spotifyIcon, cameraIcon)

if __name__ == "__main__":
    connection = DataBase.create_db_connection("localhost", "szymon", "dzbanek", "mirror")
    base.execute_query(connection,"update camera set actuall_user = 1")
    base.execute_query(connection,"update camera set camera_on = 1")
    connection.close()

    os.environ["was_instagram_open"] = "False"

    toolbar.OpenPreToolbar()
    Toolbar.HideToolbarAnimation_DF(toolbarFrame)

MouseThread = threading.Thread(target=camera.FaceRecognition)
MouseThread.start() 


tk.mainloop()