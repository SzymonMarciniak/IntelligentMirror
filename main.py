import PIL.Image, PIL.ImageTk
from tkinter import *
from time import *
import json 
import threading
import os

from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
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

function_activate = FunctionsActivateClass(tk, toolbarFrame ,timeFrame, weatherFrame, gmailFrame)

toolbar = Toolbar(tk,toolbarFrame, timeFrame, weatherFrame, gmailFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, left_arrow, right_arrow)
                
camera = Camera(tk, toolbarFrame, timeFrame, weatherFrame, gmailFrame)

with open(db, "r", encoding="utf-8") as file: 
    data = json.load(file)
    data["db"]["camera"]["actuall_user"] = "None"

def open_toolbar(x) -> None:
    """
    Open toolbar 
    """
    toolbar.OpenToolbarAnimation()

def close_toolbar(x) -> None:
    """
    Close toolbar
    """
    toolbar.HideToolbarAnimation()

tk.bind("<Right>", open_toolbar)
tk.bind("<Left>", close_toolbar)

if __name__ == "__main__":
    toolbar.OpenToolbar()


MouseThread = threading.Thread(target=camera.FaceRecognition)
MouseThread.start() 


tk.mainloop()