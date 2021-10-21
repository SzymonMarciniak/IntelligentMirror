from tkinter import *


def OpenToolbar(toolbarFrame: Tk, 
                clockIcon: PhotoImage,
                sunIcon: PhotoImage,
                homeIcon: PhotoImage,
                contactsIcon: PhotoImage,
                settingsIcon: PhotoImage) -> None:
    """ 
    Display toolbar main buttons
    
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

    
    toolbarFrame.place(x=-200,y=0)

    
  
def OpenToolbarAnimation(toolbarFrame: Frame) -> None:
    """
    Create toolbar display animation 

    Parametrs
    ---------
    toolbarFrame: Frame
        Name of toolbar frame
    """

    for x_pos in range(-200,1,10):
        toolbarFrame.place(x=x_pos, y=0)
        toolbarFrame.update()
    
        
        