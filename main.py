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
db = f"{prefix}/IntelligentMirror/DataBase.json"

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
photosFrame = LabelFrame(tk, bg="gray", bd=1)


clockIcon = PhotoImage(file=f"{icon_prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{icon_prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{icon_prefix}home_black.png") 
calendarIcon = PhotoImage(file=f"{icon_prefix}calendar_black.png") 
quoteIcon = PhotoImage(file=f"{icon_prefix}quote_black.png") 
gmailIcon = PhotoImage(file=f"{icon_prefix}gmail_black.png")
returnIcon = PhotoImage(file=f"{icon_prefix}return_black.png")
test1Icon = PhotoImage(file=f"{icon_prefix}external_black.png")
test2Icon = PhotoImage(file=f"{icon_prefix}briefcase_black.png")
bulbOnIcon = PhotoImage(file=f"{icon_prefix}bulb.png")
rollerShuttersUpIcon = PhotoImage(file=f"{icon_prefix}up.png")
pauseIcon = PhotoImage(file=f"{icon_prefix}pause_black.png")
rollerShuttersDownIcon = PhotoImage(file=f"{icon_prefix}down.png")
instagramIcon = PhotoImage(file=f"{icon_prefix}instagram_black.png")
spotifyIcon = PhotoImage(file=f"{icon_prefix}spotify_black.png")
cameraIcon = PhotoImage(file=f"{icon_prefix}camera.png")

left_arrow = PIL.Image.open(f"{icon_prefix}left-arrow_black.png")
left_arrow = left_arrow.resize((150,150))
left_arrow = PIL.ImageTk.PhotoImage(left_arrow)
right_arrow = PIL.Image.open(f"{icon_prefix}right-arrow_black.png")
right_arrow = right_arrow.resize((150,150))
right_arrow = PIL.ImageTk.PhotoImage(right_arrow)

no_move_icon = PIL.Image.open(f"{icon_prefix}finger.png")
no_move_icon = no_move_icon.resize((120,120))
no_move_icon = PIL.ImageTk.PhotoImage(no_move_icon)

                
camera = Camera(tk, toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame ,calendarFrame,photosFrame, no_move_icon)

toolbar = Toolbar(tk,toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame, calendarFrame, photosFrame, \
    clockIcon, sunIcon, homeIcon, calendarIcon, quoteIcon, left_arrow, right_arrow, gmailIcon,returnIcon, test1Icon, test2Icon, \
        bulbOnIcon, rollerShuttersUpIcon, pauseIcon, rollerShuttersDownIcon, instagramIcon, spotifyIcon, cameraIcon)

if __name__ == "__main__":
    # with open(db, "r", encoding="utf-8") as file: 
    #     data = json.load(file)
    #     data["db"]["camera"]["actuall_user"] = "None"
    
    # with open(db, "w", encoding="utf-8") as user_file:
    #     json.dump(data, user_file, ensure_ascii=False, indent=4)

    connection = DataBase.create_db_connection("localhost", "szymon", "dzbanek", "mysql_mirror")
    base.execute_query(connection,"update camera set actuall_user = 0")
    connection.close()

    toolbar.OpenPreToolbar()


MouseThread = threading.Thread(target=camera.FaceRecognition)
MouseThread.start() 


tk.mainloop()