import PIL.Image, PIL.ImageTk
from tkinter import *
from time import *
import json 
import threading
import os
 
from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.camera.video_capture import Camera

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


clockIcon = PhotoImage(file=f"{icon_prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{icon_prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{icon_prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{icon_prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{icon_prefix}settings_black.png") 

left_arrow = PIL.Image.open(f"{icon_prefix}left-arrow_black.png")
left_arrow = left_arrow.resize((150,150))
left_arrow = PIL.ImageTk.PhotoImage(left_arrow)
right_arrow = PIL.Image.open(f"{icon_prefix}right-arrow_black.png")
right_arrow = right_arrow.resize((150,150))
right_arrow = PIL.ImageTk.PhotoImage(right_arrow)

no_move_icon = PIL.Image.open(f"{icon_prefix}finger.png")
no_move_icon = no_move_icon.resize((120,120))
no_move_icon = PIL.ImageTk.PhotoImage(no_move_icon)

toolbar = Toolbar(tk,toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, left_arrow, right_arrow)
                
camera = Camera(tk, toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame ,no_move_icon)


if __name__ == "__main__":
    with open(db, "r", encoding="utf-8") as file: 
        data = json.load(file)
        data["db"]["camera"]["actuall_user"] = "None"
    
    with open(db, "w", encoding="utf-8") as user_file:
        json.dump(data, user_file, ensure_ascii=False, indent=4)

    toolbar.OpenToolbar()


MouseThread = threading.Thread(target=camera.FaceRecognition)
MouseThread.start() 


tk.mainloop()