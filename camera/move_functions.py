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
        self.prefix_ = os.getcwd() 
        self.prefix = f"{self.prefix_}/IntelligentMirror/camera/"
        self.frame = frame


    def move(self) -> None:
        """Method responsible for moveing and keep an eye on the boundaries"""
        
        with open(f"{self.prefix}mouse_event.json", "r", encoding="utf-8") as file1:
            data1 = json.loads(file1.read())
            activate = (data1["event"]["event"])
        file1.close()
        

        while activate == "True":

            with open(f"{self.prefix}mouse_event.json", "r", encoding="utf-8") as file1:
                data1 = json.loads(file1.read())
                activate = (data1["event"]["event"])
                widget = (data1["event"]["frame"])
            file1.close()


           
                
            with open(f"{self.prefix_}/IntelligentMirror/functions/{widget.capitalize()}Function/{widget}_position.json", "r", encoding="utf-8") as file2:
                data2 = json.loads(file2.read())
                x_pos = (data2["position"]["x"])
                y_pos = (data2["position"]["y"])
            file2.close()


            tk_width = 1920
            tk_height = 1080
            frame_width = self.frame.winfo_width()
            frame_height = self.frame.winfo_height()

            max_x = tk_width - frame_width
            max_y = tk_height - frame_height

            if x_pos > max_x:
                x_pos = max_x
            elif x_pos < 0:
                x_pos = 0

            if y_pos > max_y:
                y_pos = max_y
            elif y_pos < 0:
                y_pos = 0
            
        
            self.frame.place(x=x_pos, y=y_pos)
            self.frame.update()
       
        

