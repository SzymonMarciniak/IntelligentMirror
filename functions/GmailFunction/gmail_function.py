import imaplib
import email
from email.header import decode_header
from typing import List
import os
from tkinter import *

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

global Subject_list, From_list
Subject_list = []
From_list = []

prefix = os.getcwd()

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


        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        connection.close()
            
        try: 
            if RFace != 0:

                connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                data = base.read_query(connection, f"select email, emailpassword from user WHERE id={RFace}")[0]
                connection.close()

                username = data[0]
                password = data[1]

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
        except: return False, False 
        
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
    def __init__(self, tk:Frame, toolbarFrame:Frame, gmailFrame:Frame, timeFrame:Frame = None, \
        weatherFrame: Frame=None, quoteFrame: Frame = None, calendarFrame:Frame = None, photosFrame:Frame= None) -> None:
        gmail = Gmail()
        self.gmail = gmail 
        self.data = gmail.start() 
        self.prefix = os.getcwd()
    
      
        self.gmailFrame= gmailFrame
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame

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

        self.failed_label = Label(self.gmailFrame, bg="black", fg="white", bd=1, text="Connection\n failed", font=("", 20))

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

        self.failed_label.bind("<Button-1>", self.drag_start_frame)
        self.failed_label.bind("<B1-Motion>", self.drag_motion_frame)
        self.failed_label.bind("<ButtonRelease-1>", self.drag_stop)

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
                length += len(sub[x]) + 1
                if length <19:
                    subject_words += sub[x] + " "
               
            Subjects.append(subject_words)
        return Subjects

    def main(self) -> None:
        """Function responsible for displaying gmail frame"""
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET gmail_event=1 WHERE id={RFace}")
        toolbar_staus = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        gm_data = self.gmail.start() 
        if gm_data[0] and gm_data[1]:

            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
            connection.close()
                    
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

            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            user = base.read_query(connection, f"select name, lastname from user WHERE id={RFace}")[0]
            connection.close()
    
            self.preGmail_Label.configure(text=f"{user[0].title()} \n {user[1].title()} ")
            self.preGmail_Label.pack(side=LEFT, padx=23)
                        

            self.preGmail.place(x=1, y=c, width=220, height=d+c)
            self.gmailLabelFrame.pack(side=RIGHT, padx=8)
            self.gm0.place(x=1, y=c+d,    width=220, height=82)
            self.gm1.place(x=1, y=b*1+c+d,width=220, height=82)
            self.gm2.place(x=1, y=b*2+c+d,width=220, height=82)
            self.gm3.place(x=1, y=b*3+c+d,width=220, height=82)

            try: self.failed_label.place_forget()
            except: pass 

            x_pos, y_pos = self.check_position()
            if toolbar_staus == "on" and x_pos <= 210:
                x_pos = 210

            self.gmailFrame.place(x=x_pos, y=y_pos,width=221, height=4*82+1+d)
        
        else:

            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
            connection.close()

            if RFace != 0:

                connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                user = base.read_query(connection, f"select name, lastname from user WHERE id={RFace}")[0]
                connection.close()

                self.preGmail_Label.configure(text=f"{user[0].title()} \n {user[1].title()} ")
            else:
                self.preGmail_Label.configure(text=f"    None")

            x_pos, y_pos = self.check_position()
            if toolbar_staus == "on" and x_pos <= 210:
                x_pos = 210

            self.gmailFrame.place(x=x_pos, y=y_pos,width=221, height=126)
            self.gmailLabelFrame.pack(side=RIGHT, padx=8)

            self.preGmail_Label.pack(side=LEFT, padx=30)
                        
            self.preGmail.place(x=1, y=1, width=220, height=44)
            self.failed_label.place(x=1, y=44,width=216, height=80)

            
    def destroy_gmail(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET gmail_event=0 WHERE id={RFace}")
        connection.close()

        self.gmailFrame.place_forget()

    def check_position(self, RFace = None):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]

        coor = base.read_query(connection, f"select gmail_x, gmail_y from user WHERE id={RFace}")[0]
        connection.close()

        x_pos = coor[0]
        y_pos = coor[1]

        return x_pos,y_pos
    
    def gmail_refresh(self, RFace):  #?
        x,y = self.check_position(RFace)
        self.gmailFrame.place(x=x, y=y)

        
    def drag_start_frame(self, event):
        self.gmailFrame.startX = event.x
        self.gmailFrame.startY = event.y
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        if toolbar_event == "on":
            self.gmailFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame,NoMove="gmail")

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
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection,"select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET gmail_x={self.gmailFrame.stopX} WHERE id={RFace}")
        base.execute_query(connection, f"update user SET gmail_y={self.gmailFrame.stopY} WHERE id={RFace}")
        connection.close()

        if self.gmailFrame.ToOn == True: 

            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, \
                self.gmailFrame, self.quoteFrame, self.calendarFrame,self.photosFrame)