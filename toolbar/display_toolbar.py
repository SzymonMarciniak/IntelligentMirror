from tkinter import *
from time import sleep


def OpenToolbar(toolbarFrame: Tk, 
                clockIcon: PhotoImage,
                sunIcon: PhotoImage,
                homeIcon: PhotoImage,
                contactsIcon: PhotoImage,
                settingsIcon: PhotoImage) -> None:
    """ 
    Display a main toolbar buttons
    
    Parametrs
    ---------
    tk: Tk()
        Name of main window
    
    clockIcon: PhotoImage
        Clock image
    
    sunIcon: PhotoImage
        Sun image
    
    homeIcon: PhotoImage
        Home image

    contactsIcon: PhotoImage
        Contact image

    settingsIcon: PhotoImage
        Settings image

    """
    
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

    toolbarFrame.place(x=0,y=0)
    #toolbarFrame.place(x=-200,y=0)

    
    #toolbarFrame.pack(side=TOP, anchor=SW)
   

# def OpenToolbarAnimation(toolbarFrame: Frame) -> None:

#     x_pos = -200
        