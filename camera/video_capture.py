import cv2
import face_recognition
import numpy as np 
import os 
import time 
import pyautogui
from tkinter import * 
import json

import IntelligentMirror.camera.modules.HandTrackingModule as htm
from IntelligentMirror.toolbar.display_toolbar import Toolbar

global frame 
frame = None 

class Camera:
    global frame

    cap = cv2.VideoCapture(0)
    
    class FaceRecognition:
        
        """This class is resposible for recognition user's face"""
        def __init__(self) -> None:
            

            prefix = os.getcwd()
            self.prefix = f"{prefix}/IntelligentMirror/camera"

            persons = [p for p in os.listdir(f"{self.prefix}/data")]

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

            self.RFace = "Unknown"

        def recognition(self):
            global frame
            """This function detecting faces"""

            while True:
                _, frame = Camera.cap.read()
                try:
                    
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                    rgb_small_frame = small_frame[:, :, ::-1]

                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


                    if self.process_this_frame:
                        
                        face_locations = face_recognition.face_locations(rgb_small_frame)
                        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                        face_names = []
                        for face_encoding in face_encodings:
                            
                            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                            name = "unknown"
                            if name == "unknown":
                                self.no_face = self.no_face + 1
                                #print(self.no_face)
                                if self.no_face == 1:
                                    self.RFace = name
                                    
                            
                            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                                self.RFace = name
                                self.no_face = 0

                            face_names.append(name)
                    else:
                        self.no_face = self.no_face + 1
                        #print(self.no_face)
                        
                        if self.no_face == 100:
                            self.RFace = "unknown"
                    
                    print(self.RFace)
                    #time.sleep(0.01)
                        
                    self.process_this_frame = not self.process_this_frame

                    #cv2.imshow('Video', frame)

                except:
                    pass 
                

                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
               

           
            cv2.destroyAllWindows()
    






    class mouse: 
        """Virtual mouse class responsible for moveing and clicking with hand"""
        def __init__(self, toolbarFrame: Frame) -> None:
            """
            Parametrs
            ---------
            toolbarFrame: Frame 
                Frame for toobar 
            """
            self.toolbarFrame = toolbarFrame 
            self.mouse_event_var = False
            self.prefix = os.getcwd()
        
        
            
        def virtual_mouse(self):
            """
            This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
            """
            global frame 
            
            wCam, hCam = 640, 480
            frameR = 100 # Frame Reduction
            smoothening = 6

            pTime = 0
            plocX, plocY = 0, 0
            clocX, clocY = 0, 0

            detector = htm.HandDetector(maxHands=1)
            wScr, hScr = 1920, 1080

            toolbar_animation = False 

            no_fingers = 0 
            
            while True:
                
                try:
                

                    def click(x: int,y: int) -> None:
                        pyautogui.moveTo(x, y)
                        pyautogui.click(x=x, y=y)
                        

                        with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "r", encoding="utf-8") as file0:
                            data = json.load(file0)
                            data["event"]["event"] = "True"
                        file0.close()

                        with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "w", encoding="utf-8") as file:
                            json.dump(data, file)
                        file.close()


                    # Find hand Landmarks
                    
                    img = detector.find_hands(frame)
                    lmList, bbox = detector.find_position(img)

                    # Get the tip of the finger up
                    if len(lmList) != 0:
                        _, fingers = detector.fingers_up()
                        if fingers[1] == 1:
                            x1, y1 = lmList[8][1:]
                        elif fingers[2] == 1:
                            x1, y1 = lmList[12][1:]
                        elif fingers[3] == 1:
                            x1, y1 = lmList[16][1:]
                        elif fingers[0] == 1:
                            x1, y1 = lmList[4][1:]
                        elif fingers [4] == 1:
                            x1, y1 = lmList[20][1:] 
                        
                        
                        # Check how many fingers are up
                        total_fingers, _ = detector.fingers_up()

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
                                with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "r", encoding="utf-8") as file0:
                                    data = json.load(file0)
                                    data["event"]["event"] = "False"
                                file0.close()

                                with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "w", encoding="utf-8") as file:
                                    json.dump(data, file)
                                file.close()

                                
                                pyautogui.moveTo(x, y)
                                plocX, plocY = clocX, clocY

                                #save mouse coordinates
                                with open(f"{self.prefix}/IntelligentMirror/camera/mouse_position.json", "w", encoding="utf-8") as file: 
                                    data = {"position":
                                    {"x":x,
                                    "y":y}}
                                    json.dump(data, file)
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

                            with open(f"{self.prefix}/IntelligentMirror/camera/mouse_position.json", "w", encoding="utf-8") as file: 
                                data = {"position":
                                {"x":x,
                                "y":y}}
                                json.dump(data, file)
                            file.close()

                            with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "r", encoding="utf-8") as file:
                                data = json.load(file)
                                activate = (data["event"]["event"])  
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
                            
                            with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "r", encoding="utf-8") as file0:
                                data = json.load(file0)
                                data["event"]["event"] = "True"
                            file0.close()

                            with open(f"{self.prefix}/IntelligentMirror/camera/mouse_event.json", "w", encoding="utf-8") as file: #Over 
                                json.dump(data, file)
                            file.close()
                    
                    #print(no_fingers)

                    # Display
                    #cv2.imshow("Image", img)
                    cv2.waitKey(1)
                except:
                    print("error")

if __name__ == "__main__":
    fr = Camera.FaceRecognition()
    fr.recognition()
