import cv2
import numpy as np
import time
import pyautogui
from tkinter import * 

import IntelligentMirror.mouse.modules.HandTrackingModule as htm
from IntelligentMirror.toolbar.display_toolbar import Toolbar


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
        
    def virtual_mouse(self):
        """
        This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
        """
        
        wCam, hCam = 640, 480
        frameR = 100 # Frame Reduction
        smoothening = 6

        pTime = 0
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0

        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)
        detector = htm.HandDetector(maxHands=1)
        wScr, hScr = 1920, 1080

        toolbar_animation = False 
        

        while True:

            def click(x: int,y: int) -> None:
                pyautogui.moveTo(x, y)
                pyautogui.click(x=x, y=y)

            # Find hand Landmarks
            success, img = cap.read()
            img = detector.find_hands(img)
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
            
                # Moving Mode
                if total_fingers >=3:

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
                    pyautogui.moveTo(x, y)
                    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    plocX, plocY = clocX, clocY

                    #Turn on toolbar animation
                    if x <=205:
                        if toolbar_animation:
                            pass
                        else: 
                            toolbar_animation = True
                            Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame)
                    else: 
                        pass

                    
                # Clicking Mode
                else:
                    x = wScr - clocX
                    x = int(x)
                    y = int(clocY)
                    click(x, y)

            # Display
            #cv2.imshow("Image", img)
            cv2.waitKey(1)


if __name__ == "__main__":
    mouse.virtual_mouse()