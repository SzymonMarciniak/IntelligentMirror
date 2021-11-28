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
        self.prefix = f"{self.prefix}/IntelligentMirror/camera/"
        self.frame = frame

    def move(self) -> None:
        """Method responsible for moveing and keep an eye on the boundaries"""
        

        with open(f"{self.prefix}mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.load(file1)
                activate = (data1["event"]["event"])
        file1.close()

        while activate == "True":
            with open(f"{self.prefix}mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.load(file1)
                activate = (data1["event"]["event"])
                selected_frame = (data1["event"]["frame"])
            file1.close()

            time.sleep(0.01)
            with open(f"{self.prefix}mouse_position.json", "r", encoding="utf-8") as file2:
                data2 = json.loads(file2.read())
                x_pos = (data2["position"]["x"])
                y_pos = (data2["position"]["y"])
            file2.close()

            if selected_frame == "time":
                if y_pos >=960:
                    y_pos = 960
                
                if x_pos >= 1630:
                    x_pos = 1630
            
            elif selected_frame == "weather":
                if y_pos >=900:
                    y_pos = 900
                
                if x_pos >= 1570:
                    x_pos = 1570

        
            self.frame.place(x=x_pos, y=y_pos)
            self.frame.update()
        self.frame.update()
        

