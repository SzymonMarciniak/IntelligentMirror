import threading
import Xlib.threaded
import cv2
import face_recognition
import glob
import numpy as np 
import os 
import time 
import pyautogui
from tkinter import * 

from IntelligentMirror.camera.modules.HandTrackingModule import HandDetector
from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain
from IntelligentMirror.functions.CalendarFunction.calendar_function import Calendar
from IntelligentMirror.functions.PhotosFunction.photos_function import Photos
from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

detector = HandDetector(detectionCon=0.65, maxHands=1)

pyautogui.FAILSAFE = False

class Camera:
    def __init__(self, tk:Frame, toolbarFrame:Frame, timeFrame:Frame, weatherFrame:Frame, gmailFrame:Frame,\
         quoteFrame:Frame,calendarFrame:Frame, photosFrame: Frame, no_finge_icon=None) -> None:
        
        self.cap = cv2.VideoCapture(0)   
        self.toolbarFrame = toolbarFrame
        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame
        self.no_finger_icon = no_finge_icon

        if self.no_finger_icon:
            self.no_finger_button = Button(self.tk, image=self.no_finger_icon, highlightthickness=0, bd=0,highlightbackground='black',borderwidth=0,\
                 bg='black',activebackground="black" ,command=self.mouse_off)

        self.Time = CurrentTime(self.tk, self.toolbarFrame, self.timeFrame)    
        self.Weather = CurrentWeather(self.tk, self.toolbarFrame, self.weatherFrame)
        self.Gmail = GmailMain(self.tk, self.toolbarFrame, self.gmailFrame)
        self.Calendar = Calendar(self.tk, self.toolbarFrame, self.calendarFrame) 
        self.Photos = Photos(self.tk, self.toolbarFrame, self.photosFrame)

        prefix = os.getcwd()
        self.db = f"{prefix}/IntelligentMirror/DataBase.json"
        self.prefix = f"{prefix}/IntelligentMirror/camera"
        self.photos_prefix = f"{prefix}/IntelligentMirror/functions/PhotosFunction/photos/"

        persons = [person for person in os.listdir(f"{self.prefix}/data")]

        self.known_face_encodings = []
        self.known_face_names = []
        for person_img in persons:

            name =  person_img[-8:-6] #user id
            someone = face_recognition.load_image_file(f"{self.prefix}/data/{person_img}") 
            someone_face_encoding = face_recognition.face_encodings(someone, num_jitters=5, model="large")[0]

            self.known_face_encodings.append(someone_face_encoding)
            self.known_face_names.append(name)

        self.process_this_frame = True
        self.no_face = 0

        self.RFace = 0
        self.no_hand = 0 

        self.nick = Label(self.tk, font=("Arial", 30), bg="black", fg="white", text="None")
        self.nick.pack(side=BOTTOM,anchor=SE)

        self.rgb_small_frame = None
        #pyautogui.moveTo(10, 10)
    
    def mouse_off(self):
        self.no_hand = 200

        
    def refresh_methods(self):

        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
        base.execute_query(connection, f"update camera set actuall_user = {self.RFace}")
        connection.close()

        from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
    
        refresh = FunctionsActivateClass(self.tk, self.toolbarFrame, self.timeFrame, self.weatherFrame, \
            self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame)

        refresh.functions_position_refresh(self.RFace)
       

    def FaceRecognition(self):

        def gesture(hands):
            hand = hands[0]
            fingers_up= detector.fingers_up(hand)

            if fingers_up[0] == [1,0,0,0,1]:
                self.no_hand = 0
                return True 
            else: 
                return False 
     
        
        while True:
            _, self.img = self.cap.read()
            self.img = cv2.flip(self.img, 1)
            hands, img_gest = detector.find_hands(self.img, flipType=False)
            

            def face_recognition_module():
                #try:
                    small_frame = cv2.resize(self.img, (0, 0), fx=0.25, fy=0.25)

                    rgb_small_frame = small_frame[:, :, ::-1]
                    self.rgb_small_frame = rgb_small_frame  # Preparation image

                    face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=3)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model="large") #Finding face on camera

                    for face_encoding in face_encodings:

                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, tolerance=0.5)
                        face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances) #Whitch face matches those in the database

                        if matches[best_match_index]:
                            name = self.known_face_names[best_match_index] #finding name
                        
                            if name == self.RFace: #if name now and then are the same 
                                self.no_face = 0

                            else:                           #if name now and then are not the same 
                                if  self.RFace == 0:

                                    self.RFace = name


                                    connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
                                    my_nick = base.read_query(connection, f"select nick FROM accounts WHERE user_id={self.RFace}")[0][0]
                                    connection.close()

                                    self.nick.config(text=my_nick)
                                    self.no_face = 0
                                    self.refresh_methods()

                    name = 0             #Counting how many times dont recognition any face 
                    if name == 0:
 
                        self.no_face = self.no_face + 1
                        print(f"{self.no_face} No name")
                        if self.no_face == 60:
                            if self.RFace != 0:
                                self.RFace = name

                                connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
                                my_nick = base.read_query(connection, f"select nick FROM accounts WHERE user_id={self.RFace}")[0][0]
                                connection.close()

                                self.nick.config(text=my_nick)
                                self.refresh_methods()
                            self.no_face = 0
                    
                    
                    connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
                    base.execute_query(connection, f"update camera SET actuall_user={int(self.RFace)}")
                    connection.close()

                    print(self.RFace)
                    time.sleep(0.25)

                # except:
                #     print("Face Recognition error")
            
            connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
            toolbar = base.read_query(connection, "select toolbar from camera")[0][0]
            camera_on = base.read_query(connection, "select camera_on from camera")[0][0]
            connection.close()
            print(f"cam {camera_on}")
            if not toolbar == "on":
                print("11")
                if hands:       #Detection gest
                    isgesture = gesture(hands)
                    if isgesture:
                        print("22")
                        Camera.Mouse(self)
                    else:
                        if camera_on:
                            print("33")
                            face_recognition_module() 
                else:
                    if camera_on:
                        print("44")
                        face_recognition_module()
            
                #cv2.imshow("Image", self.rgb_small_frame)
                cv2.waitKey(1)
            
            else:
                self.no_face = 0
        
    
    def Mouse(self):
        """
        This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
        """
         
        wCam, hCam = 640, 370
        frameR = 0 # Frame Reduction
        smoothening = 6

        plocX, plocY = 300, 300
        clocX, clocY = 0, 0

        wScr, hScr = 1920, 1080
        
        self.activate = False
        isDown = False

        self.no_finger_button.place(relx=.48, rely=.2)

        self.T = False 
        self.W = False 
        self.G = False 
        self.Q = False 
        self.C = False 
        self.B = False 
        self.P = False
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
        user_id = base.read_query(connection, "select actuall_user from camera")[0][0]
        self.user = base.read_query(connection, f"select name, lastname from user WHERE id={user_id}")[0]
        camera_on = base.read_query(connection, "select camera_on from camera")[0][0]
        base.execute_query(connection, "UPDATE camera SET instagram_on=0")
        connection.close()

        self.user = self.user[0] + "_" + self.user[1]

        self.photos = self.photos_prefix + self.user
        self.counterLabel = Label(self.tk, text="", font=("Arial", 60), bg="black", fg="white")

        to_up = 0 
        
        if camera_on:
            while self.no_hand < 80:
                #try:
                    _, self.img = self.cap.read()
                    hands, self.img = detector.find_hands(self.img, draw=False)

                    if hands:
                    
                        self.no_hand = 0
                        hand = hands[0]
                        lmList = hand["lmList"]
                

                        # Get the tip of the finger 
                        if len(lmList) != 0:
                            x1, y1 = lmList[8]
                        
                            # Check how many fingers are up
                            _, total_fingers = detector.fingers_up(hands[0])

                            # Convert Coordinates
                            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

                            # Smoothen Values
                            clocX = plocX + (x3 - plocX) / smoothening
                            clocY = plocY + (y3 - plocY) / smoothening
                                    
                            # Move Mouse
                            x = wScr - clocX
                            x = int(x)
                            y = int(clocY)
                            
                            # Moving Mode
                            if total_fingers >=3:
                                if isDown:
                                    to_up += 1
                                    if to_up == 3:
                                        to_up = 0
                                        pyautogui.mouseUp(button="left")
                                        isDown = False

                                    self.activate = False
                                    
                            # Clicking Mode
                            elif total_fingers < 3:
                                if self.activate == False:
                                    to_up = 0
                                    pyautogui.mouseDown(button="left")
                                    isDown = True
                                self.activate = True

                            plocX, plocY = clocX, clocY

                            print(x,y)
                            try:
                                t1 = threading.Thread(target=lambda:self.moveing_thread(x, y))
                                t1.start()
                            except: print("MOVEING ERROR")
                            
                    else:
                        self.no_hand +=1
                    
                    
                    connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
                    takephoto = base.read_query(connection, "select photo from camera")[0][0]
                    connection.close()
                
                    if takephoto:
                        
                        if self.timeFrame:
                            self.T = True
                            self.Tx,self.Ty = self.timeFrame.winfo_x(), self.timeFrame.winfo_y()
                            self.timeFrame.place_forget()

                        if self.weatherFrame:
                            self.W = True
                            self.Wx,self.Wy = self.weatherFrame.winfo_x(), self.weatherFrame.winfo_y()
                            self.weatherFrame.place_configure(x=-200,y=-300)
                        
                        if self.gmailFrame:
                            self.G = True
                            self.Gx,self.Gy = self.gmailFrame.winfo_x(), self.gmailFrame.winfo_y()
                            self.Gw, self.Gh = self.gmailFrame.winfo_width(), self.gmailFrame.winfo_height()
                            self.gmailFrame.place_forget()
                        
                        if self.quoteFrame:
                            self.Q = True
                            self.Qx,self.Qy = self.quoteFrame.winfo_x(), self.quoteFrame.winfo_y()
                            self.quoteFrame.place_forget() 
                        
                        if self.calendarFrame:
                            self.C = True
                            self.Cx,self.Cy = self.calendarFrame.winfo_x(), self.calendarFrame.winfo_y()
                            self.calendarFrame.place_forget() 
                        
                        if self.photosFrame:
                            self.P = True
                            self.Px,self.Py = self.photosFrame.winfo_x(), self.photosFrame.winfo_y()
                            self.photosFrame.place_forget() 
                        
                        if self.no_finger_button:
                            self.B = True
                            self.no_finger_button.place_forget()

                        self.Tolx,self.Toly = self.toolbarFrame.winfo_x(), self.toolbarFrame.winfo_y()
                        self.toolbarFrame.place_configure(x=-400)

                        connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
                        base.execute_query(connection, "update camera SET photo=0")
                        connection.close()

                        photoThreading = threading.Thread(target=lambda:self.takePhoto_function())
                        photoThreading.start()
                    
                        
            
                # except:
                #     print("ERROR")
                
            pyautogui.moveTo(1,1)
            self.no_finger_button.place_forget()

            connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")
            toolbar_on = base.read_query(connection, "select toolbar from camera")[0][0]
            RFace = base.read_query(connection,"select actuall_user from camera")[0][0]
            

            if toolbar_on == "on":
                from IntelligentMirror.toolbar.display_toolbar import Toolbar
                Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, \
                    self.calendarFrame, self.photosFrame)
            
            if base.read_query(connection,f"select instagram_event from accounts WHERE user_id={RFace}")[0][0] ==1:
                base.execute_query(connection, "UPDATE camera SET instagram_on=1")
            connection.close()

    def moveing_thread(self, x, y):
       
        pyautogui.moveTo(x, y)
    
    
    def takePhoto_function(self):
        self.no_hand = 81
        self.no_face = 0
        self.counterLabel.place(relx=0.5, rely=0.3)

        for i in range(5,0,-1):
            self.counterLabel.config(text=str(i))
            time.sleep(1)

        self.counterLabel.place_forget()

        
        photosArray = [photo_ for photo_ in glob.glob(f"{self.photos}/{self.user}*.jpg")]
        photo_nr = str(len(photosArray) + 1)
        self.photos = self.photos + "/" +self.user + photo_nr + ".jpg"
        print(self.photos)

        cv2.imwrite(self.photos, self.img)
        if self.T:
            self.T = False 
            self.timeFrame.place(x=self.Tx, y=self.Ty)
        
        if self.W:
            self.W = False 
            self.weatherFrame.place_configure(x=self.Wx, y=self.Wy, width=350) 
        
        if self.G:
            self.G = False 
            self.gmailFrame.place(x=self.Gx, y=self.Gy,width=self.Gw, height=self.Gh)
        
        if self.Q:
            self.Q = False 
            self.quoteFrame.place(x=self.Qx, y=self.Qy) 
        
        if self.C:
            self.C = False 
            self.calendarFrame.place(x=self.Cx, y=self.Cy)

        if self.P:
            self.P = False 
            self.photosFrame.place(x=self.Px, y=self.Py, width=150, height=150) 
        
        if self.B:
            self.B = False 
            
        
        self.toolbarFrame.place_configure(x=-210)

