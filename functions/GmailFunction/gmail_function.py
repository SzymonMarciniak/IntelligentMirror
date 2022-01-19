
import imaplib
import email
from email.header import decode_header
from typing import List
import os
import json
from tkinter import *


global Subject_list, From_list
Subject_list = []
From_list = []

class Gmail:
    """Gmail module"""

    global Subject_list, From_list

    def __init__(self) ->None:
        super().__init__()
        self.prefix = os.getcwd()


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
                        

        with open(f"{self.prefix}/IntelligentMirror/functions/GmailFunction/gmail_accounts.json", "r", encoding="utf-8") as gmail_f:
            gmail = json.load(gmail_f)
            gmail_f.close()

            if Rface != "unknown":
                username = gmail["gmail"][Rface]["login"]
                password = gmail["gmail"][Rface]["haslo"]


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
    gmailFrame: Frame
        Frame for gmail labels
    """
    def __init__(self, tk:Frame, gmailFrame:Frame) -> None:
        gmail = Gmail()
        self.data = gmail.start() 
        self.prefix = os.getcwd()

        tk.configure(background="black")

        self.gmailFrame= gmailFrame

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

        self.gm0.bind("<Button-1>", self.drag_start_frame)
        self.gm0.bind("<B1-Motion>", self.drag_motion_frame)

        self.from_label_0.bind("<Button-1>", self.drag_start_frame)
        self.from_label_0.bind("<B1-Motion>", self.drag_motion_frame)

        self.gm1.bind("<Button-1>", self.drag_start_frame)
        self.gm1.bind("<B1-Motion>", self.drag_motion_frame)

        self.from_label_1.bind("<Button-1>", self.drag_start_frame)
        self.from_label_1.bind("<B1-Motion>", self.drag_motion_frame)

        self.gm2.bind("<Button-1>", self.drag_start_frame)
        self.gm2.bind("<B1-Motion>", self.drag_motion_frame)

        self.from_label_2.bind("<Button-1>", self.drag_start_frame)
        self.from_label_2.bind("<B1-Motion>", self.drag_motion_frame)

        self.gm3.bind("<Button-1>", self.drag_start_frame)
        self.gm3.bind("<B1-Motion>", self.drag_motion_frame)

        self.from_label_3.bind("<Button-1>", self.drag_start_frame)
        self.from_label_3.bind("<B1-Motion>", self.drag_motion_frame)

        self.gmailFrame.bind("<Button-1>", GmailMain.drag_start)
        self.gmailFrame.bind("<B1-Motion>", GmailMain.drag_motion)

        self.subject_label_0.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_0.bind("<B1-Motion>", self.drag_motion_frame)

        self.subject_label_1.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_1.bind("<B1-Motion>", self.drag_motion_frame)

        self.subject_label_2.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_2.bind("<B1-Motion>", self.drag_motion_frame)

        self.subject_label_3.bind("<Button-1>", self.drag_start_frame)
        self.subject_label_3.bind("<B1-Motion>", self.drag_motion_frame)

        self.preGmail.bind("<Button-1>", self.drag_start_frame)
        self.preGmail.bind("<B1-Motion>", self.drag_motion_frame)

        self.preGmail_Label.bind("<Button-1>", self.drag_start_frame)
        self.preGmail_Label.bind("<B1-Motion>", self.drag_motion_frame)

        self.gmailLabelFrame.bind("<Button-1>", self.drag_start_frame)
        self.gmailLabelFrame.bind("<B1-Motion>", self.drag_motion_frame)

    
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
        self.gmailLabelFrame.pack(side=RIGHT, padx=15)
        self.gm0.place(x=1, y=c+d,    width=220, height=82)
        self.gm1.place(x=1, y=b*1+c+d,width=220, height=82)
        self.gm2.place(x=1, y=b*2+c+d,width=220, height=82)
        self.gm3.place(x=1, y=b*3+c+d,width=220, height=82)

        with open(f"{self.prefix}/IntelligentMirror/functions/GmailFunction/gmail_position.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            x_pos = (data["position"]["x"])
            y_pos = (data["position"]["y"])

        self.gmailFrame.place(x=x_pos, y=y_pos,width=221, height=4*82+1+d)

    
    @staticmethod
    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y
    
    @staticmethod
    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y

        tk_width = 1920
        tk_height = 1080
        frame_width = widget.winfo_width()
        frame_height = widget.winfo_height()

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
        
        widget.place(x=x, y=y)

        data = {
            "position": {
                "x": x,
                "y": y
            }
        }
        
        prefix = os.getcwd()
        with open(f"{prefix}/IntelligentMirror/functions/GmailFunction/gmail_position.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
        file.close()

        
    def drag_start_frame(self, event):
        self.gmailFrame.startX = event.x
        self.gmailFrame.startY = event.y
    
    
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

        data = {
            "position": {
                "x": x,
                "y": y
            }
        }

        with open(f"{self.prefix}/IntelligentMirror/functions/GmailFunction/gmail_position.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
        file.close()
