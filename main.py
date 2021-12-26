from tkinter import *
from time import *
import threading
import os

from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
from IntelligentMirror.camera.video_capture import Camera

prefix = os.getcwd()
icon_prefix = f"{prefix}/IntelligentMirror/icons/"

tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.config(cursor="fleur")
tk.bind("<Escape>", exit)


toolbarFrame = Frame(tk)

timeFrame = LabelFrame(tk, bg="black", bd=0)
weatherFrame = LabelFrame(tk, bg="black", bd=0)
gmailFrame = LabelFrame(tk, bg="black", bd=0)


clockIcon = PhotoImage(file=f"{icon_prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{icon_prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{icon_prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{icon_prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{icon_prefix}settings_black.png") 


function_activate = FunctionsActivateClass(tk, timeFrame, weatherFrame, gmailFrame)

toolbar = Toolbar(tk,toolbarFrame, timeFrame, weatherFrame, gmailFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon)
                
camera = Camera(tk, toolbarFrame)

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