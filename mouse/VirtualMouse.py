import cv2
import numpy as np
import mouse.modules.HandTrackingModule as htm
import time
import pyautogui


def virtual_mouse():
    """
    This function is responsible for control mouse (moveing and clicking). You control mouse with your hand.
    """
    
    wCam, hCam = 640, 480
    frameR = 100 # Frame Reduction
    smoothening = 7

    pTime = 0
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.HandDetector(maxHands=1)
    wScr, hScr = 1920, 1080
    while True:

        def click(x: int,y: int) -> None:
            pyautogui.moveTo(x, y)
            pyautogui.click(x=x, y=y)

        # Find hand Landmarks
        success, img = cap.read()
        img = detector.find_hands(img)
        lmList, bbox = detector.find_position(img)

        # Get the tip of the index and middle fingers
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            
            
        # Check which fingers are up
            fingers = detector.fingers_up()
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
            (255, 0, 255), 2)

            # Only Index Finger : Moving Mode
            if fingers[1] == 1 and fingers[2] == 0:

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
                
            # Both Index and middle fingers are up : Clicking Mode
            if fingers[1] == 1 and fingers[2] == 1:

                # Find distance between fingers
                length, img, lineInfo = detector.find_distance(8, 12, img)
               
                # Click mouse if distance short
                if length < 40:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]),
                    15, (0, 255, 0), cv2.FILLED)
                    x = wScr - clocX
                    x = int(x)
                    y = int(clocY)
                    click(x, y)

        # Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
        (255, 0, 0), 3)

        # Display
        #cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    virtual_mouse()