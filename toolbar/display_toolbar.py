from tkinter import *
 


def OpenToolbar(tk) -> Frame:
    """ 
    Display a main toolbar buttons
    
    Parametrs
    ---------
    tk: Tk()
        Name of main window

    """
    
    toolbarFrame = Frame(tk)

    prefix = "/home/szymonm/Desktop/VSC_projects/Mirror/IntelligentMirror/icons/"

    clockIcon = PhotoImage(file=f"{prefix}clock_black.png") 
    sunIcon = PhotoImage(file=f"{prefix}sun_black.png") 
    homeIcon = PhotoImage(file=f"{prefix}home_black.png") 
    contactsIcon = PhotoImage(file=f"{prefix}contacts_black.png") 
    settingsIcon = PhotoImage(file=f"{prefix}settings_black.png") 

    clock_button = Button(toolbarFrame, image=clockIcon, highlightbackground='black', bg='black')
    weather_button = Button(toolbarFrame, image=sunIcon, highlightbackground='black', bg='black')
    home_button = Button(toolbarFrame, image=homeIcon, highlightbackground='black', bg='black')
    contact_button = Button(toolbarFrame, image=contactsIcon, highlightbackground='black', bg='black')
    settings_button = Button(toolbarFrame, image=settingsIcon, highlightbackground='black', bg='black')


    clock_button.pack(side=TOP)
    weather_button.pack(side=TOP)
    home_button.pack(side=TOP)
    contact_button.pack(side=TOP)
    settings_button.pack(side=TOP)

    return toolbarFrame
