import cv2
import face_recognition
import numpy as np 
import os 
import time 
import pyautogui
from tkinter import * 
import json

from IntelligentMirror.camera.modules.HandTrackingModule import *
from IntelligentMirror.toolbar.display_toolbar import Toolbar

detector = HandDetector(detectionCon=0.65, maxHands=1)

class Camera:
    def __init__(self, tk, toolbarFrame) -> None:
        self.cap = cv2.VideoCapture(0)
        self.toolbarFrame = toolbarFrame
        self.tk = tk
        


        prefix = os.getcwd()
        self.db = f"{prefix}/IntelligentMirror/DataBase.json"
        self.prefix = f"{prefix}/IntelligentMirror/camera"

        persons = [person for person in os.listdir(f"{self.prefix}/data")]

        self.known_face_encodings = []
        self.known_face_names = []

        for person_img in persons:

            name =  person_img[:-4]
            name = name+"_nazwisko"

            someone = face_recognition.load_image_file(f"{self.prefix}/data/{person_img}") 
            someone_face_encoding = face_recognition.face_encodings(someone)[0]

            self.known_face_encodings.append(someone_face_encoding)
            self.known_face_names.append(name)

        self.process_this_frame = True
        self.no_face = 0

        self.RFace = "None"
        self.no_hand = 0 

        self.nick = Label(self.tk, font=("Arial", 30), bg="black", fg="white", text=self.RFace)
        self.nick.pack(side=BOTTOM,anchor=SE)
    

    def FaceRecognition(self):

        def gesture(hands):
            hand = hands[0]
            fingers_up= detector.fingers_up(hand)

            if fingers_up[0] == [1,0,0,0,1]:
                return True 
            else: 
                return False 
     
        
        while True:
            _, img = self.cap.read()
            img = cv2.flip(img, 1)
            hands, img_gest = detector.find_hands(img, flipType=False)
            

            def face_recognition_module():
                try:
                    small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

                    rgb_small_frame = small_frame[:, :, ::-1]

                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


                    if self.process_this_frame:
                                
                        face_locations = face_recognition.face_locations(rgb_small_frame)
                        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                        face_names = []
                        for face_encoding in face_encodings:
                                    
                            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                            name = "None"
                            if name == "None":
                                self.no_face = self.no_face + 1
                                #print(self.no_face)
                                if self.no_face == 1:
                                    self.RFace = name
                                            
                                    
                            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                        
                                if name == self.RFace:
                                    self.no_face = 0
                                else:
                                    
                                    if self.RFace == "Unnown" or self.RFace == "None":
                                        self.RFace = name
                                        self.nick.config(text=self.RFace)
                                        self.no_face = 0
                            else:
                                if self.RFace == "Unnown" or self.RFace == "None":
                                    self.RFace = "Unknown"
                                    self.nick.config(text=self.RFace)
                                    self.no_face = self.no_face + 1
                                    if self.no_face > 20:
                                        self.RFace = "None"

                            face_names.append(name)
                    else:
                        self.no_face = self.no_face + 1
                        #print(self.no_face)
                                
                        if self.no_face == 40:
                            self.RFace = "None"
                            self.nick.config(text=self.RFace)
                    

                    with open(self.db, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        data["db"]["camera"]["actuall_user"] = self.RFace
                    
                    with open(self.db, "w", encoding="utf-8") as user_file:
                        json.dump(data, user_file, ensure_ascii=False, indent=4)
                   
                       

                    print(self.RFace)
                    time.sleep(0.25)
                                
                    self.process_this_frame = not self.process_this_frame


                except:
                    print("Face Recognition error")
            
            if hands:
                isgesture = gesture(hands)
                if isgesture:
                    Camera.Mouse(self)
                else:
                    self.no_hand = 0
                    face_recognition_module()
            else:
                self.no_hand = 0
                face_recognition_module()
                    

            

            #cv2.imshow("Image", img)
            cv2.waitKey(1)
    
    def Mouse(self):

        
        """
        This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
        """
         
        wCam, hCam = 640, 480
        frameR = 100 # Frame Reduction
        smoothening = 6

       
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0

        detector = HandDetector(maxHands=1)
        wScr, hScr = 1920, 1080

        toolbar_animation = False 

        no_fingers = 0 

            
        while self.no_hand < 50:
                
                
            try:
              
                _, img = self.cap.read()
               

                def click(x: int,y: int) -> None:
                    pyautogui.moveTo(x, y)
                    pyautogui.click(x=x, y=y)
                        

                    with open(self.db, "r", encoding="utf-8") as file0:
                        data = json.load(file0)
                        data["db"]["camera"]["mouse_event"]["event"] = "True"

                    with open(self.db, "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                   

                # Find hand Landmarks    
                hands, img = detector.find_hands(img, draw=False)

                if not hands:
                    self.no_hand += 1
                else:
                    self.no_hand = 0

                lmList, bbox = detector.find_position(img, draw=False)
               

                    # Get the tip of the finger up
                if len(lmList) != 0:
                    fingers, _ = detector.fingers_up(hands[0])
                    if fingers[1] == 1:
                        x1, y1 = lmList[8][1:]
                    elif fingers[2] == 1:
                        x1, y1 = lmList[12][1:]
                    elif fingers[3] == 1:
                        x1, y1 = lmList[16][1:]
                    elif fingers[0] == 1:
                        x1, y1 = lmList[4][1:]
                    else:
                        x1, y1 = lmList[20][1:] 
                        
                    
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
                        
                        no_fingers += 1
                        if no_fingers >= 10:
                          

                            pyautogui.mouseUp(button="left")

                                
                            #Save mouse mode
                            with open(self.db, "r", encoding="utf-8") as file0:
                                data = json.load(file0)
                                data["db"]["camera"]["mouse_event"]["event"] = "False"
                            file0.close()


                            with open(self.db, "w", encoding="utf-8") as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                            file.close()

                                
                            pyautogui.moveTo(x, y)
                            plocX, plocY = clocX, clocY

                            #save mouse coordinates
                            with open(self.db, "r", encoding="utf-8") as file0:
                                data = json.load(file0)
                                data["db"]["functions"]["positions"]["mouse"]["x"] = x
                                data["db"]["functions"]["positions"]["mouse"]["y"] = Y

                            with open(self.db, "w", encoding="utf-8") as file: 
                                json.dump(data, file, ensure_ascii=False, indent=4)
                            file.close()

                            #Show/Hide toolbar 
                            if x <=205:
                                if toolbar_animation:
                                    pass
                                else: 
                                    toolbar_animation = True
                                    Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame)
                            else: 
                                if toolbar_animation:
                                    toolbar_animation = False
                                    Toolbar.HideToolbarAnimation_DF(self.toolbarFrame)
                                else:
                                    pass

                            
                    # Clicking Mode
                    else:
                        x = wScr - clocX
                        x = int(x)
                        y = int(clocY)

                        no_fingers = 0

                        with open(self.db, "r", encoding="utf-8") as file0:
                            data = json.load(file0)
                            data["db"]["functions"]["positions"]["mouse"]["x"] = x
                            data["db"]["functions"]["positions"]["mouse"]["y"] = Y

                        with open(self.db, "w", encoding="utf-8") as file: 
                            json.dump(data, file, ensure_ascii=False, indent=4)
                        file.close()

                        with open(self.db, "r", encoding="utf-8") as file:
                            data = json.load(file)
                            activate = data["db"]["camera"]["mouse_event"]["event"]
                        file.close()
                            

                        if activate == "False":
                            click(x, y)
                            toolbar_animation = False
                            if x <= 200:
                                for x_pos in range(1,-200,-3):
                                    self.toolbarFrame.place(x=x_pos, y=0)
                                    self.toolbarFrame.update()
                        else:
                            pyautogui.mouseDown(button="left")
                            pyautogui.moveTo(x, y)
                            plocX, plocY = clocX, clocY
                            
                        with open(self.db, "r", encoding="utf-8") as file0:
                            data = json.load(file0)
                            data["db"]["camera"]["mouse_event"]["event"] = "True"
                        file0.close()



                   

                    # Display
                    #cv2.imshow("Image", img)
                cv2.waitKey(1)
            except ValueError:
                print("Value Error")
            except FileNotFoundError as Error:
                raise Error
        


if __name__ == "__main__":
    ObjectFace = Camera()
    ObjectFace.FaceRecognition()