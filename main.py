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


x = 0
def MainOpenToolbar(x):
    
    OpenToolbar(toolbarFrame, clockIcon, sunIcon, homeIcon, contactsIcon, settingsIcon)
    #OpenToolarAnimation

tk.bind("<Right>", MainOpenToolbar)

tk.mainloop()
