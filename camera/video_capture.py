import cv2
import face_recognition
import numpy as np 
import os 
import time 
import pyautogui
from tkinter import * 
import json


from IntelligentMirror.camera.modules.HandTrackingModule import HandDetector
from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain

detector = HandDetector(detectionCon=0.65, maxHands=1)

class Camera:
    def __init__(self, tk, toolbarFrame, timeFrame, weatherFrame, gmailFrame, quoteFrame ,no_finge_icon=None) -> None:

        self.cap = cv2.VideoCapture(0)
        self.toolbarFrame = toolbarFrame
        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.quoteFrame = quoteFrame
        self.no_finger_icon = no_finge_icon

        if self.no_finger_icon:
            self.no_finger_button = Button(self.tk, image=self.no_finger_icon, highlightthickness=0, bd=0,highlightbackground='black',borderwidth=0,\
                 bg='black',activebackground="black" ,command=self.mouse_off)

        self.Time = CurrentTime(self.tk, self.toolbarFrame, self.timeFrame)
        self.Weather = CurrentWeather(self.tk, self.toolbarFrame, self.weatherFrame)
        self.Gmail = GmailMain(self.tk, self.toolbarFrame, self.gmailFrame)

        prefix = os.getcwd()
        self.db = f"{prefix}/IntelligentMirror/DataBase.json"
        self.prefix = f"{prefix}/IntelligentMirror/camera"

        persons = [person for person in os.listdir(f"{self.prefix}/data")]

        self.known_face_encodings = []
        self.known_face_names = []
        for person_img in persons:

            name =  person_img[:-5]
            name = name 
            someone = face_recognition.load_image_file(f"{self.prefix}/data/{person_img}") 
            someone_face_encoding = face_recognition.face_encodings(someone, num_jitters=5, model="large")[0]

            self.known_face_encodings.append(someone_face_encoding)
            self.known_face_names.append(name)

        self.process_this_frame = True
        self.no_face = 0

        self.RFace = "None"
        self.no_hand = 0 

        self.nick = Label(self.tk, font=("Arial", 30), bg="black", fg="white", text=self.RFace)
        self.nick.pack(side=BOTTOM,anchor=SE)

        self.rgb_small_frame = None
        pyautogui.moveTo(960, 1090)
    
    def mouse_off(self):
        self.no_hand = 60

        
    def refresh_methods(self):

        with open(self.db, "r", encoding="utf-8") as file: 
            data = json.load(file)
            data["db"]["camera"]["actuall_user"] = self.RFace
        
        with open(self.db, "w", encoding="utf-8") as user_file:
            json.dump(data, user_file, ensure_ascii=False, indent=4)

        from IntelligentMirror.functions.FunctionActivate import FunctionsActivateClass
    
        refresh = FunctionsActivateClass(self.tk, self.toolbarFrame, self.timeFrame, self.weatherFrame, \
            self.gmailFrame, self.quoteFrame)

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
            _, img = self.cap.read()
            img = cv2.flip(img, 1)
            hands, img_gest = detector.find_hands(img, flipType=False)
            

            def face_recognition_module():
                #try:
                    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

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
                                if  self.RFace == "None":

                                    self.RFace = name
                                    with open(self.db, "r", encoding="utf-8") as file:
                                        data = json.load(file)
                                        my_nick = data["db"]["accounts"][self.RFace]["login"]
                                    self.nick.config(text=my_nick)
                                    self.no_face = 0
                                    self.refresh_methods()

                    name = "None"               #Counting how many times dont recognition any face 
                    if name == "None":
 
                        self.no_face = self.no_face + 1
                        print(f"{self.no_face} No name")
                        if self.no_face == 60:
                            if self.RFace != "None":
                                self.RFace = name
                                self.nick.config(text=self.RFace)
                                self.refresh_methods()
                            self.no_face = 0
                    
                    

                    with open(self.db, "r", encoding="utf-8") as file:  #Save data
                        data = json.load(file)
                        data["db"]["camera"]["actuall_user"] = self.RFace
                    
                    with open(self.db, "w", encoding="utf-8") as user_file:
                        json.dump(data, user_file, ensure_ascii=False, indent=4)
                   
                       

                    print(self.RFace)
                    time.sleep(0.25)

                # except:
                #     print("Face Recognition error")
            
            if hands:       #Detection gest
                isgesture = gesture(hands)
                if isgesture:
                    Camera.Mouse(self)
                else:
                    face_recognition_module()
            else:
                face_recognition_module()
        
            #cv2.imshow("Image", self.rgb_small_frame)
            cv2.waitKey(1)
        
    
    def Mouse(self):
        """
        This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
        """
         
        wCam, hCam = 640, 480
        frameR = 0 # Frame Reduction
        smoothening = 6

        plocX, plocY = 300, 300
        clocX, clocY = 0, 0

        wScr, hScr = 1920, 1080
        
        self.activate = False
        isDown = False

        self.no_finger_button.place(relx=.48, rely=.2)
 
        while self.no_hand < 50:
            try:
                _, img = self.cap.read()
                hands, img = detector.find_hands(img, draw=False)

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
                                pyautogui.mouseUp(button="left")
                                isDown = False

                            self.activate = False
                                  
                        # Clicking Mode
                        else:
                            if self.activate == False:
                                pyautogui.mouseDown(button="left")
                                isDown = True
                            self.activate = True

                        plocX, plocY = clocX, clocY
                        pyautogui.moveTo(x, y)

                else:
                    self.no_hand +=1
          
            except:
                print("ERROR")
        
        pyautogui.moveTo(1,1)
        self.no_finger_button.place_forget()
