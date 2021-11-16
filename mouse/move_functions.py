from tkinter import * 
import os 
import json

class MoveFunction:
    def __init__(self) -> None:
        self.prefix = os.getcwd() 

    def move(self, frame: Frame) -> None:

        with open(f"{self.prefix}/IntelligentMirror/mouse/mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.load(file1)
                activate = (data1["event"])
            
        while activate == "True":
            with open(f"{self.prefix}/IntelligentMirror/mouse/mouse_position.json", "r", encoding="utf-8") as file2:
                data2 = json.load(file2)
                x = (data2["position"]["x"])
                y = (data2["position"]["y"])
            frame.place(x=x, y=y)
            frame.update()
        

