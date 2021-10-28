from tkinter import *
from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime

class FunctionsActivateClass:
    """This class is responsible for activating the functions"""

    def __init__(self,
                tk: Frame,
                clockLabel: Label,
                dateLabel: Label,
                timeFrame: Frame) -> None:

        """
        Parametrs
        ---------
        tk: Tk()
            Name of main window
            
        clockLabel: Label
            Label for clock
        
        dateLabel: Label
            Label for date
        
        timeFrame: Frame
            Frame for clock label and date label
        """
        self.tk = tk
        self.clockLabel = clockLabel
        self.dateLabel = dateLabel
        self.timeFrame = timeFrame

        self.time = CurrentTime(self.clockLabel, self.dateLabel, self.timeFrame)




    def time_function(self):
        """Activates the time function"""
        self.time.clock_date()