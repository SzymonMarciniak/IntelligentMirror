import os 
import time  

class Light:
    def __init__(self) -> None:
        self.ip = "192.168.0.6"

    def light_on(self):
        os.system(f"links -source {self.ip}/On")
        
    def light_off(self):
        os.system(f"links -source {self.ip}/Off")

    def rollerShuttersUp(self):
        os.system(f"links -source {self.ip}/Up")
    
    def rollerShuttersDown(self):
        os.system(f"links -source {self.ip}/Down")

    def rollerShuttersStop(self):
        os.system(f"links -source {self.ip}/Stop") 

if __name__ == "__main__":
    light = Light()
    light.light_on()
    time.sleep(3)
    light.light_off()
