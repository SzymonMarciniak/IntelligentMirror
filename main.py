from datetime import date
from tkinter import *
from time import *
import threading
import os

from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.mouse.VirtualMouse import mouse
from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
 
prefix = os.getcwd()
icon_prefix = f"{prefix}IntelligentMirror/icons/"

tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.config(cursor="fleur")
tk.bind("<Escape>", exit)

toolbarFrame = Frame(tk)

timeFrame = LabelFrame(tk, bg="black", bd=0)
weatherFrame = LabelFrame(tk, bg="black", bd=0)

clockLabel = Label(timeFrame, font=("Arial", 60), bg="black", fg="white")
dateLabel = Label(timeFrame, font=("Arial", 30), bg="black", fg="white")

temp = Label(weatherFrame, font=("Arial", 50))
pressure = Label(weatherFrame, font=("Arial", 35))
humidity = Label(weatherFrame, font=("Arial", 25))
image_weather = Label(weatherFrame, font=("Arial", 40))


clockIcon = PhotoImage(file=f"{icon_prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{icon_prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{icon_prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{icon_prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{icon_prefix}settings_black.png") 


function_activate = FunctionsActivateClass(tk,clockLabel, dateLabel, timeFrame, \
                                            temp, pressure, humidity, image_weather, weatherFrame)

toolbar = Toolbar(tk,toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, clockLabel, dateLabel, \
                timeFrame, temp, pressure, humidity, image_weather, weatherFrame)
                
Mouse = mouse(toolbarFrame)


def open_toolbar(x):
    """
    Open toolbar 
    """
    toolbar.OpenToolbarAnimation()

def close_toolbar(x):
    """
    Close toolbar
    """
    toolbar.HideToolbarAnimation()


tk.bind("<Right>", open_toolbar)
tk.bind("<Left>", close_toolbar)

if __name__ == "__main__":
    toolbar.OpenToolbar()

MouseThread = threading.Thread(target=Mouse.virtual_mouse)
MouseThread.start() 


tk.mainloop()