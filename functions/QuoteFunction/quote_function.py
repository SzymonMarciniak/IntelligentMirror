from tkinter import *
import json 
import os


prefix = os.getcwd()
db = f"{prefix}/IntelligentMirror/DataBase.json"


class QuoteMain:

    def __init__(self, tk: Frame, toolbarFrame:Frame, quoteFrame: Frame ,timeFrame:Frame = None, weatherFrame:Frame = None,\
         gmailFrame: Frame = None, calendarFrame:Frame = None, photosFrame:Frame= None) -> None:

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame 
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame

        self.text_label = Label(self.quoteFrame, font=("Arial", 30), bg="black", fg="white")

        self.quoteFrame.bind("<Button-1>", self.drag_start_frame)
        self.quoteFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.quoteFrame.bind("<ButtonRelease-1>", self.drag_stop)

        self.text_label.bind("<Button-1>", self.drag_start_frame)
        self.text_label.bind("<B1-Motion>", self.drag_motion_frame)
        self.text_label.bind("<ButtonRelease-1>", self.drag_stop)

        self.number = -1
    
    def main(self):

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            data["db"]["accounts"][RFace]["positions"]["quote"]["event"] = "True"
            toolbar_staus = data["db"]["toolbar"]
        
        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        x,y = QuoteMain.check_position(self)

        if toolbar_staus == "on" and x <= 210:
            x = 210
            
        self.quoteFrame.place(x=x,y=y)


        def new_quote(ToOn = False):
            
            self.number += 1
            with open(f"{prefix}/IntelligentMirror/functions/QuoteFunction/quotes.txt") as file:
                quotes = file.readlines()

                new_line = True
                my_quote = ""
                lenght = 0
                quote = quotes[self.number].split()
                max_len = len(quote)

                for i in range(max_len):
                    lenght += len(quote[i]) + 1
                    if lenght < 60:
                        my_quote += quote[i] + " "
                    else:
                        if new_line:
                            new_line = False
                            my_quote += "\n" + quote[i] + " "
                        else:
                            my_quote += quote[i] + " "
                        


            self.text_label.config(text=my_quote)
            self.text_label.after(60000,new_quote)

            if ToOn:
                ToOn = False 
                self.text_label.pack(side=BOTTOM)
        
        new_quote(True)

    
    def destroy_quote(self):
    
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            data["db"]["accounts"][RFace]["positions"]["quote"]["event"] = "False"
        
        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        for pack in self.quoteFrame.pack_slaves():
            pack.pack_forget()

        self.quoteFrame.place_forget() 
    
    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual quote position
        Returns
        -------
        x: int
            Value of "x" quote position
        y: int 
            value of "y" quote position
        """

    
        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            if RFace == None: 
                RFace = data["db"]["camera"]["actuall_user"]

            x = data["db"]["accounts"][RFace]["positions"]["quote"]["x"]
            y = data["db"]["accounts"][RFace]["positions"]["quote"]["y"]
        return x, y

    
    def drag_start_frame(self, event):
        self.quoteFrame.startX = event.x
        self.quoteFrame.startY = event.y

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            toolbar_event = data["db"]["toolbar"]
        
        if toolbar_event == "on":
            self.quoteFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame, self.calendarFrame,self.photosFrame, NoMove="quote")

        else:
            self.quoteFrame.ToOn = False
        
    
    def drag_motion_frame(self, event):
        x = self.quoteFrame.winfo_x() - self.quoteFrame.startX + event.x
        y = self.quoteFrame.winfo_y() - self.quoteFrame.startY + event.y
        
        tk_width = 1920
        tk_height = 1080
        frame_width = self.quoteFrame.winfo_width()
        frame_height = self.quoteFrame.winfo_height()

        max_x = tk_width - frame_width
        max_y = tk_height - frame_height

        if x > max_x:
            x = max_x
        elif x < 0:
            x = 0

        if y > max_y:
            y = max_y
        elif y < 0:
            y = 0

        self.quoteFrame.place(x=x, y=y)

        self.quoteFrame.stopX = x
        self.quoteFrame.stopY = y


       

    def drag_stop(self, event=None):

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            data["db"]["accounts"][RFace]["positions"]["quote"]["x"] = self.quoteFrame.stopX 
            data["db"]["accounts"][RFace]["positions"]["quote"]["y"] = self.quoteFrame.stopY 


        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        if self.quoteFrame.ToOn == True: 
       
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame)






