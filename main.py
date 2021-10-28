from datetime import date
from tkinter import *
from time import *
import threading

from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
from IntelligentMirror.mouse.VirtualMouse import virtual_mouse 


tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.config(cursor="fleur")
tk.bind("<Escape>", exit)


toolbarFrame = Frame(tk)
timeFrame = Frame(tk)

clockLabel = Label(timeFrame, font=("", 60), bg="black", fg="white")
dateLabel = Label(timeFrame, font=("", 30), bg="black", fg="white")

prefix = "/home/szymonm/Desktop/VSC_projects/Mirror/IntelligentMirror/icons/"

clockIcon = PhotoImage(file=f"{prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{prefix}settings_black.png") 


function_activate = FunctionsActivateClass(tk,clockLabel, dateLabel, timeFrame)

def toolbar_animation(x):
    """
    Turn on toolbar animation
    """
    toolbar = Toolbar(tk,toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, clockLabel, dateLabel,timeFrame)
    toolbar.OpenToolbarAnimation()



tk.bind("<Right>", toolbar_animation)




if __name__ == "__main__":
    toolbar = Toolbar(tk, toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, clockLabel, dateLabel,timeFrame)
    toolbar.OpenToolbar()


MouseThread = threading.Thread(target=virtual_mouse)
MouseThread.start() 


tk.mainloop()