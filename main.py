from datetime import date
from tkinter import *
from time import *
import threading

from IntelligentMirror.toolbar.display_toolbar import Toolbar
from IntelligentMirror.mouse.VirtualMouse import mouse
from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
 


prefix = "/home/szymon/Desktop/my_projects/Mirror/IntelligentMirror/icons/"

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


clockIcon = PhotoImage(file=f"{prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{prefix}settings_black.png") 


function_activate = FunctionsActivateClass(tk,clockLabel, dateLabel, timeFrame, \
                                            temp, pressure, humidity, image_weather, weatherFrame)

toolbar = Toolbar(tk,toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon, clockLabel, dateLabel, \
                timeFrame, temp, pressure, humidity, image_weather, weatherFrame)
                
Mouse = mouse(toolbarFrame)


def toolbar_animation(x):
    """
    Turn on toolbar animation
    """
    toolbar.OpenToolbarAnimation()


tk.bind("<Right>", toolbar_animation)

if __name__ == "__main__":
    toolbar.OpenToolbar()

MouseThread = threading.Thread(target=Mouse.virtual_mouse)
MouseThread.start() 


tk.mainloop()