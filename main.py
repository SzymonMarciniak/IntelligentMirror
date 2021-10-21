from tkinter import *
from toolbar.display_toolbar import *
from time import *


tk = Tk()
tk.configure(background="black")
tk.attributes("-fullscreen", True)
tk.bind("<Escape>", exit)

toolbarFrame = Frame(tk)


prefix = "/home/szymonm/Desktop/VSC_projects/Mirror/IntelligentMirror/icons/"

clockIcon = PhotoImage(file=f"{prefix}clock_black.png") 
sunIcon = PhotoImage(file=f"{prefix}sun_black.png") 
homeIcon = PhotoImage(file=f"{prefix}home_black.png") 
contactsIcon = PhotoImage(file=f"{prefix}contacts_black.png") 
settingsIcon = PhotoImage(file=f"{prefix}settings_black.png") 


def toolbar_animation(x):
    """
    Turn on toolbar animation
    """
    OpenToolbarAnimation(toolbarFrame)


OpenToolbar(toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon)
tk.bind("<Right>", toolbar_animation)

tk.mainloop()
