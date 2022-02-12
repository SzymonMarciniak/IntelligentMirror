import imaplib
import email
from email.header import decode_header
from json import tool
from typing import List
import os
import json
from tkinter import *


global Subject_list, From_list
Subject_list = []
From_list = []

prefix = os.getcwd()
db = f"{prefix}/IntelligentMirror/DataBase.json"

class Gmail:
    """Gmail module"""

    global Subject_list, From_list

    def __init__(self) ->None:
        super().__init__()
        self.prefix = os.getcwd()
        self.db = f"{self.prefix}/IntelligentMirror/DataBase.json"


    def start(self) -> List:
        """
        Function responsible for getting 'From' and 'Subject' of gmails
        
        Return
        ------
        Subject_list: List
            List with subjects
        From_list: List
            List with senders
        """
        Subject_list = []
        From_list = []
        From_list_2 = []

        Rface = "szymon_marciniak"
                        

        with open(self.db, "r", encoding="utf-8") as gmail_f:
            gmail = json.load(gmail_f)
            

            if Rface != "unknown":
                username = gmail["db"]["accounts"][Rface]["positions"]["gmail"]["login"]
                password = gmail["db"]["accounts"][Rface]["positions"]["gmail"]["haslo"]


                From = " "
                encoding = " "
                response = " "
                subject = " "
                msg = " "
                i = " "
            
                N = 4

                imap = imaplib.IMAP4_SSL("imap.gmail.com")
                imap.login(username, password)


                status, messages = imap.select("INBOX")

                messages = int(messages[0])

                for i in range(messages, messages-N, -1):
                    res, msg = imap.fetch(str(i), "(RFC822)")
                    for response in msg:
                        if isinstance(response, tuple):
                            msg = email.message_from_bytes(response[1])
                            subject, encoding = decode_header(msg["Subject"])[0]
                            if isinstance(subject, bytes):
                                if encoding == None:
                                    encoding = str("utf-8")
                                subject = subject.decode(encoding)
                            From, encoding = decode_header(msg.get("From"))[0]
                            if isinstance(From, bytes):
                                if encoding == None:
                                    encoding = str("utf-8")
                                From = From.decode(encoding)

                            From_list_2 = From.split()
                            From_list_2.pop()
                            From_list_2 = " ".join(From_list_2)
                            # print("Subject:", subject)
                            # print("From:", From_list_2)
                            Subject_list.append(subject)
                            From_list.append(From_list_2)
                            From_list_2 = []
                # print(From_list)
                # print(Subject_list)
                imap.close()
                imap.logout()

                return Subject_list, From_list 


class GmailMain:
    """
    Display gmail frame

    Paramerts
    --------
    tk: Frame
        Frame of main window
    toolbarFrame: 
        Toolbar frame
    gmailFrame: Frame
        Frame for gmail labels 
    """
    def __init__(self, tk:Frame, toolbarFrame:Frame, gmailFrame:Frame) -> None:
        gmail = Gmail()
        self.data = gmail.start() 
        self.prefix = os.getcwd()
        self.db = f"{self.prefix}/IntelligentMirror/DataBase.json"

        tk.configure(background="black")

        self.gmailFrame= gmailFrame
        self.toolbarFrame = toolbarFrame

        self.preGmail = LabelFrame(self.gmailFrame, bg="gray", bd=1)
        self.preGmail_Label = Label(self.preGmail, font=("", 15),  bg="gray", fg="white")
        self.gm0 = LabelFrame(self.gmailFrame,  bg="black", bd=1)
        self.from_label_0 = Label(self.gm0, font=("", 25),  bg="black", fg="white")
        self.gm1 = LabelFrame(self.gmailFrame,  bg="black", bd=1)
        self.from_label_1 = Label(self.gm1, font=("", 25),  bg="black", fg="white")
        self.gm2 = LabelFrame(self.gmailFrame,  bg="black", bd=1)
        self.from_label_2 = Label(self.gm2, font=("", 25),  bg="black", fg="white")
        self.gm3 = LabelFrame(self.gmailFrame,  bg="black", bd=1)
        self.from_label_3 = Label(self.gm3, font=("", 25),  bg="black", fg="white")

        self.subject_label_0 = Label(self.gm0, font=("", 15),  bg="black", fg="white")
        self.subject_label_1 = Label(self.gm1, font=("", 15),  bg="black", fg="white")
        self.subject_label_2 = Label(self.gm2, font=("", 15),  bg="black", fg="white")
        self.subject_label_3 = Label(self.gm3, font=("", 15),  bg="black", fg="white")

        self.gmailLabelFrame = Frame(self.preGmail)

        self.gmailLogo = PhotoImage(file=f"{self.prefix}/IntelligentMirror/functions/GmailFunction/gmail_logo.png")
        self.GmailLogo = Label(self.gmailLabelFrame, image=self.gmailLogo, fg='gray', bg='gray')
        self.GmailLogo.pack(side=LEFT)

        self.gmailFrame.bind("<Button-1>", self.drag_start_frame)
        self.gmailFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.gmailFrame.bind("<ButtonRelease-1>", self.drag_stop)

        self.GmailLogo.bind("<Button-1>", self.drag_start_frame)
        self.GmailLogo.bind("<B1-Motion>", self.drag_motion_frame)
        self.GmailLogo.bind("<ButtonRelease-1>", self.drag_stop)
        
        self.gm0.bind("<Button-1>", self.drag_start_frame)
        self.gm0.bind("<B1-Motion>", self.drag_motion_frame)
        self.gm0.bind("<ButtonRelease-1>", self.drag_stop)

        self.from_label_0.bind("<Button-1>", self.drag_start_frame)
        self.from_label_0.bind("<B1-Motion>", self.drag_motion_frame)
        self.from_label_0.bind("<ButtonRelease-1>", self.drag_stop)

        self.gm1.bind("<Button-1>", self.drag_start_frame)
        self.gm1.bind("<B1-Motion>", self.drag_motion_frame)
        self.gm1.bind("<ButtonRelease-1>", self.drag_stop)

        self.from_label_1.bind("<Button-1>", self.drag_start_frame)
        self.from_label_1.bind("<B1-Motion>", self.drag_motion_frame)
        self.from_label_1.bind("<ButtonRelease-1>", self.drag_stop)

        self.gm2.bind("<Button-1>", self.drag_start_frame)
        self.gm2.bind("<B1-Motion>", self.drag_motion_frame)
        self.gm2.bind("<ButtonRelease-1>", self.drag_stop)

        self.from_label_2.bind("<Button-1>", self.drag_start_frame)
        self.from_label_2.bind("<B1-Motion>", self.drag_motion_frame)
        self.from_label_2.bind("<ButtonRelease-1>", self.drag_stop)

        self.gm3.bind("<Button-1>", self.drag_start_frame)
        self.gm3.bind("<B1-Motion>", self.drag_motion_frame)
        self.gm3.bind("<ButtonRelease-1>", self.drag_stop)

        self.from_label_3.bind("<Button-1>", self.drag_start_frame)
        self.from_label_3.bind("<B1-Motion>", self.drag_motion_frame)
        self.from_label_3.bind("<ButtonRelease-1>", self.drag_stop)

        self.subject_label_0.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_0.bind("<B1-Motion>", self.drag_motion_frame)
        self.subject_label_0.bind("<ButtonRelease-1>", self.drag_stop)

        self.subject_label_1.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_1.bind("<B1-Motion>", self.drag_motion_frame)
        self.subject_label_1.bind("<ButtonRelease-1>", self.drag_stop)

        self.subject_label_2.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_2.bind("<B1-Motion>", self.drag_motion_frame)
        self.subject_label_2.bind("<ButtonRelease-1>", self.drag_stop)

        self.subject_label_3.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_3.bind("<B1-Motion>", self.drag_motion_frame)
        self.subject_label_3.bind("<ButtonRelease-1>", self.drag_stop)

        self.preGmail.bind("<Button-1>", self.drag_start_frame)
        self.preGmail.bind("<B1-Motion>", self.drag_motion_frame)
        self.preGmail.bind("<ButtonRelease-1>", self.drag_stop)

        self.preGmail_Label.bind("<Button-1>", self.drag_start_frame)
        self.preGmail_Label.bind("<B1-Motion>", self.drag_motion_frame)
        self.preGmail_Label.bind("<ButtonRelease-1>", self.drag_stop)

        self.gmailLabelFrame.bind("<Button-1>", self.drag_start_frame)
        self.gmailLabelFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.gmailLabelFrame.bind("<ButtonRelease-1>", self.drag_stop)

    
    def set_from_gamil_headers(self) -> List:
        """
        Return 'from' from gmails

        Return
        ------
        Froms: List
            List of 'froms'
        """

        From = self.data[1]
        Froms = []

        for i in range(4):
            From_ = From[i].split()
            if not From_:
                From_.append("Unknown")
            Froms.append(From_[0])
        return Froms
    
    def set_subject_gmail_headers(self) -> List:
        """
        Returns 'subject' from gmails

        Return
        ------
        Subjects: List
            List of 'subjects'
        """

        Subject = self.data[0]
        Subjects= []
        for i in range(4):
            sub = Subject[i].split()
            if not sub:
                sub.append("Unknown")
            max_len = len(sub)
            length = 0
            subject_words = ""
            for x in range(max_len):
                length += len(sub[x])
                if length <19:
                    subject_words += sub[x] + " "
               
            Subjects.append(subject_words)
        return Subjects

    def main(self) -> None:
        """Function responsible for displaying gmail frame"""
                
        Froms = GmailMain.set_from_gamil_headers(self)

        self.from_label_0.configure(text = Froms[0])
        self.from_label_1.configure(text = Froms[1])
        self.from_label_2.configure(text = Froms[2])
        self.from_label_3.configure(text = Froms[3])

        self.from_label_0.pack(side=TOP)
        self.from_label_1.pack(side=TOP)
        self.from_label_2.pack(side=TOP)
        self.from_label_3.pack(side=TOP)


        Subjects = GmailMain.set_subject_gmail_headers(self)

        self.subject_label_0.configure(text=Subjects[0])
        self.subject_label_1.configure(text=Subjects[1])
        self.subject_label_2.configure(text=Subjects[2])
        self.subject_label_3.configure(text=Subjects[3])

        self.subject_label_0.pack(side= BOTTOM, pady=10)
        self.subject_label_1.pack(side= TOP)
        self.subject_label_2.pack(side= TOP)
        self.subject_label_3.pack(side= TOP)


        b = int(82)
        c = int(1)
        d = int(43)
        user = "Szymon_Marciniak".split("_")
        self.preGmail_Label.configure(text=f"{user[0].title()} \n {user[1].title()} ")
        self.preGmail_Label.pack(side=LEFT, padx=23)
                    

        self.preGmail.place(x=1, y=c, width=220, height=d+c)
        self.gmailLabelFrame.pack(side=RIGHT, padx=8)
        self.gm0.place(x=1, y=c+d,    width=220, height=82)
        self.gm1.place(x=1, y=b*1+c+d,width=220, height=82)
        self.gm2.place(x=1, y=b*2+c+d,width=220, height=82)
        self.gm3.place(x=1, y=b*3+c+d,width=220, height=82)

        x_pos, y_pos = self.check_position()

        self.gmailFrame.place(x=x_pos, y=y_pos,width=221, height=4*82+1+d)
    
    def destroy_gmail(self):
        self.gmailFrame.place_forget()

    def check_position(self, RFace = None):
        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            if RFace == None:
                 RFace = data["db"]["camera"]["actuall_user"]
            x_pos = data["db"]["accounts"][RFace]["positions"]["gmail"]["x"]
            y_pos = data["db"]["accounts"][RFace]["positions"]["gmail"]["y"]
        return x_pos,y_pos
    
    def gmail_refresh(self, RFace):
        x,y = self.check_position(RFace)
        self.gmailFrame.place(x=x, y=y)

        
    def drag_start_frame(self, event):
        self.gmailFrame.startX = event.x
        self.gmailFrame.startY = event.y

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            toolbar_event = data["db"]["toolbar"]

        if toolbar_event == "on":
            self.gmailFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame)

        else:
            self.gmailFrame.ToOn = False
    
    
    def drag_motion_frame(self, event):
        x = self.gmailFrame.winfo_x() - self.gmailFrame.startX + event.x
        y = self.gmailFrame.winfo_y() - self.gmailFrame.startY + event.y

        tk_width = 1920
        tk_height = 1080
        frame_width = self.gmailFrame.winfo_width()
        frame_height = self.gmailFrame.winfo_height()

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

        self.gmailFrame.place(x=x, y=y)

        self.gmailFrame.stopX = x
        self.gmailFrame.stopY = y

    def drag_stop(self, event=None):

        with open(db, "r", encoding="utf-8") as file:
            data = json.load(file)
            RFace = data["db"]["camera"]["actuall_user"]
            data["db"]["accounts"][RFace]["positions"]["gmail"]["x"] = self.gmailFrame.stopX 
            data["db"]["accounts"][RFace]["positions"]["gmail"]["y"] = self.gmailFrame.stopY 

        with open(db, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        if self.gmailFrame.ToOn == True: 
       
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame)