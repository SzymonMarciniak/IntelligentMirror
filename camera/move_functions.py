from tkinter import * 
import os 
import json
 
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
        self.db = f"{self.prefix_}/IntelligentMirror/DataBase.json"
        self.prefix = f"{self.prefix_}/IntelligentMirror/camera/"
        self.frame = frame


    def move(self) -> None:
        """Method responsible for moveing and keep an eye on the boundaries"""
        
        with open(self.db, "r", encoding="utf-8") as file1:
            data1 = json.loads(file1.read())
            activate = data1["db"]["camera"]["mouse_event"]["event"]
        file1.close()
        

        while activate == "True":

            with open(self.db, "r", encoding="utf-8") as file1:
                data1 = json.loads(file1.read())
                activate = data1["db"]["camera"]["mouse_event"]["event"]
                widget = data1["db"]["camera"]["mouse_event"]["frame"]
            file1.close()


            with open(self.db, "r", encoding="utf-8") as file:
                data = json.load(file)
                x_pos = data["db"]["functions"]["positions"][widget]["x"]
                y_pos = data["db"]["functions"]["positions"][widget]["y"]

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
       
        

