from tkinter import * 
import os 
import json
import time 

class MoveFunction:
    """This function is responsible for moveing labelframe of choosing function"""
    def __init__(self, frame: LabelFrame) -> None:
        """
        Parametrs
        ---------
        frame: LabelFrame
            Choosing function LabelFrame
        """
        self.prefix = os.getcwd() 
        self.frame = frame

    def move(self) -> None:
        """Method responsible for moveing"""

        with open(f"{self.prefix}/IntelligentMirror/mouse/mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.load(file1)
                activate = (data1["event"])
        file1.close()

        while activate == "True":
            print(self.frame)
            with open(f"{self.prefix}/IntelligentMirror/mouse/mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.load(file1)
                activate = (data1["event"])
            file1.close()

            time.sleep(0.01)
            with open(f"{self.prefix}/IntelligentMirror/mouse/mouse_position.json", "r", encoding="utf-8") as file2:
                data2 = json.loads(file2.read())
                x_pos = (data2["position"]["x"])
                y_pos = (data2["position"]["y"])
            file2.close()
            self.frame.place(x=x_pos, y=y_pos)
            self.frame.update()
        self.frame.update()
        

