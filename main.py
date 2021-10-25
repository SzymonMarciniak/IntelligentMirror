from tkinter import *
from time import *
import threading

from toolbar.display_toolbar import OpenToolbar, OpenToolbarAnimation
from mouse.VirtualMouse import virtual_mouse 


tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.config(cursor="fleur")
tk.bind("<Escape>", exit)

toolbarFrame = Frame(tk)


prefix = "/home/szymonm/Desktop/VSC_projects/Mirror/IntelligentMirror/icons/"

clockIcon = PhotoImage(file=f"{prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{prefix}settings_black.png") 


OpenToolbar(toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon)


def toolbar_animation(x):
    """
    Turn on toolbar animation
    """
    OpenToolbarAnimation(toolbarFrame)

def cursor_config():
    tk.config(cursor="fleur")




tk.bind("<Right>", toolbar_animation)

MouseThread = threading.Thread(target=virtual_mouse)
MouseThread.start() 

tk.mainloop()
