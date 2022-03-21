from tkinter import * 
import json 
import os 

class Camera:
    def __init__(self) -> None:
        prefix = os.getcwd()
        self.db = f"{prefix}/IntelligentMirror/DataBase.json"
        self.prefix = f"{prefix}/IntelligentMirror/camera"

    def takePicture(self):
        with open(self.db, "r", encoding="utf-8") as file:
            data = json.load(file)
            data["db"]["camera"]["photo"] = "true"
            
        with open(self.db, "w", encoding="utf-8") as user_file:
            json.dump(data, user_file, ensure_ascii=False, indent=4)













