
from tkinter import Image
from typing import List
import cv2
import mediapipe as mp
import time
import math


class HandDetector():
    """
    This class includes modules responsible for: finding hands and their positions, counting fingers up and the distance between them.
    """

    def __init__(self, mode=False, maxHands=2,model_complexity=1, detectionCon=0.6, trackCon=0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.model_complexity= model_complexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.model_complexity ,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def find_hands(self, img: Image, draw=True) -> Image:
        """
        This function finding hands in given image

        Parametrs
        ---------
        img: Image

        draw: Bool
            If you want to draw landmarks, set this parametr to True

        Return
        ------
        img: Image
            Image with marked hands
        """

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)

        return img

    def find_position(self, img: Image,draw=True) -> List:
        """
        This function is responsible for finding hand position in given image

        Parametrs
        ---------
        img: Image

        draw: Bool
            If you want to draw circle and rectangle, set this parametr to True
        
        Return
        ------
        lmlist: List
            List of ID and position each finger
        bbox: Tuple
            Tuple of minimal nad maximal x and y position of all fingers
        """

        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)

        return self.lmList, bbox

    def fingers_up(self) -> int:
        """
        This function counts fingers up

        Return
        ------
        totalFingers: Int
            Number of fingers up
        fingers: List
            The list contains a boolean value for each finger. 0 if the finger is down, 1 if the finger is up 
        """

        fingers = []

        # Thumb
        if len(self.lmList) != 0:
            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Fingers
            for id in range(1, 5):

                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        totalFingers = fingers.count(1)

        return totalFingers, fingers

    def find_distance(self, p1: int, p2: int, img: Image, draw=True,r=15, t=3) -> float:
        """
        This function is responsible for counting the distance between two fingers

        Parametrs
        ---------
        p1: Int
            Id of finger number 1 
        p2: Int
            Id of finger number 2
        img: Image
            Image
        draw: Bool
            Set to True if you want to draw circles and a line between these two fingers 
        r: Int
            Radius of drawing circle
        t: Int
            Thickness of drawing line
        
        Return
        ------
        length: Float
            Length between two fingers
        img: Image
            Image
        list: List
            List of first and second finger positions and the position of the middle between them


        """
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    """
    Turn on entire HandDetector class and display camera preview 
    """
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lmList, bbox = detector.find_position(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()