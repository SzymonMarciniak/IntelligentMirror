from tkinter import *
import subprocess
import pyautogui
import threading
import time
import os 


from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

prefix = os.getcwd()

class Instagram:
    def __init__(self, tk: Frame = None, toolbarFrame:Frame = None ,timeFrame:Frame = None, weatherFrame:Frame = None,\
            gmailFrame: Frame = None, quoteFrame: Frame = None, calendarFrame:Frame = None, photosFrame:Frame = None, spotifyFrame:Frame = None) -> None:

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame 
        self.spotifyFrame = spotifyFrame

        self.coord = None
        os.environ["scrolling_on"] = "close"
        os.environ["scrolling_once"] = "False"
        self.go_click = False 
        self.wait_time = 5

        self.yy = [i for i in range(200,270)]
        self.xx = [i for i in range(1620, 1680)]

    def main_instargram(self):

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET instagram_event=1 WHERE id={RFace}")
        connection.close()

        def lounch():
            def open_ins():
                 subprocess.call(f"{prefix}/IntelligentMirror/applications/InstagramFunction/instagramLauncher.sh")
                

            self.t2 = threading.Thread(target=open_ins)
            self.t2.start()

            time.sleep(2)
            subprocess.call(f"{prefix}/IntelligentMirror/applications/InstagramFunction/instagramChangeSize.sh")

            def scrolling():
                connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                toolbar_on = base.read_query(connection, "select toolbar from camera")[0][0]
                instagram_on = base.read_query(connection, "select instagram_on from camera")[0][0]
                connection.close()

                print(f"inst: {instagram_on},,,,,,, {os.environ['scrolling_on']}")
                if toolbar_on == "off" and instagram_on == 1:
                    print(os.environ["scrolling_on"], os.environ["scrolling_once"])
                    print("LOKJHGB")
                    
                    connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                    RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
                    base.execute_query(connection, f"update user SET instagram_event=1 WHERE id={RFace}")
                    base.execute_query(connection, "update camera SET camera_on=0")
                    instagram_data = base.read_query(connection, f"select instagram_login, instagram_password from user WHERE id={RFace}")[0]
                    connection.close()
                    
                    if os.environ["scrolling_on"] == "close":
                        print("STARTTTT")
                        os.environ["scrolling_once"] = "True"

                        time.sleep(2)
                        pyautogui.click(1400, 320)
                        pyautogui.write(instagram_data[0])  #Login

                        pyautogui.click(1400, 365)
                        pyautogui.write(instagram_data[1]) # Password

                        pyautogui.click(1400, 418)  #Button for login


                        time.sleep(3.5)
                        pyautogui.click(1450, 595)  #No login safe

                        time.sleep(0.7)             #Scrolling
                        pyautogui.moveTo(1695, 925)
                        time.sleep(2)
                        os.environ["scrolling_on"] = "open"
                    
                    elif os.environ["scrolling_on"] == "again":
                        time.sleep(2)
                        pyautogui.moveTo(1695, 925)
                        print("AAAGAIN")
                        os.environ["scrolling_on"] = "open"
                    
                    else:
                        while instagram_on and os.environ["scrolling_on"] == "open":
                            self.coord = pyautogui.locateCenterOnScreen(f"{prefix}/IntelligentMirror/applications/InstagramFunction/kropki.png", confidence=0.65)

                            if self.coord != None:
                                print(self.coord)
                                how_many_click = ((self.coord[1] - 270) // 40) +1
                                if how_many_click < 0:
                                    how_many_click = -how_many_click

                                if self.coord[0] in self.xx and self.coord[1] in self.yy:
                                    connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                                    base.execute_query(connection, "update camera SET camera_on=1")

                                    time.sleep(self.wait_time)

                                    base.execute_query(connection, "update camera SET camera_on=0")
                                    connection.close()
                                    pyautogui.click(clicks=18, interval=0.1)
                                else:
                                    print(how_many_click)
                                    connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                                    base.execute_query(connection, "update camera SET camera_on=0")
                                    pyautogui.click(clicks=how_many_click, interval=0.1)
                                    base.execute_query(connection, "update camera SET camera_on=1")
                                    connection.close()
                                    time.sleep(0.2)
                            else:
                                connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                                base.execute_query(connection, "update camera SET camera_on=0")
                                pyautogui.click(clicks=8, interval=0.1)
                                time.sleep(0.2)
                                base.execute_query(connection, "update camera SET camera_on=1")
                                connection.close()
                            
                            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                            instagram_on = base.read_query(connection, "select instagram_on from camera")[0][0]
                            connection.close()

                        scrolling() 
                    scrolling() 
                else: 
                    connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                    base.execute_query(connection, "update camera SET camera_on=1")
                    connection.close()

                    print(os.environ["scrolling_on"], os.environ["scrolling_once"], instagram_on, toolbar_on)

                    if os.environ["scrolling_on"] == "open" and os.environ["scrolling_once"] == "True":
                        print("1111")
                        os.environ["scrolling_on"] = "again"

                        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                        base.execute_query(connection, "update camera SET camera_on=1")
                        connection.close()

                    elif os.environ["scrolling_on"] == "close":
                        print("222")
                        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
                        base.execute_query(connection, "update camera SET camera_on=1")
                        connection.close()
                        os.environ["scrolling_on"] = "close"
                        os.environ["scrolling_once"] = "False"

                    elif os.environ["scrolling_on"] == "again": print(f"444444444444444 {os.environ['scrolling_on'], os.environ['scrolling_once'], instagram_on, toolbar_on}") 

                    else: 
                        print("333333")
                        os.environ["scrolling_on"], os.environ["scrolling_once"] = "close", "False" 

                    print(os.environ["scrolling_on"])
                    time.sleep(2) 
                    scrolling() 

            if os.environ.get("was_instagram_open") == "False":
                os.environ["was_instagram_open"] = "True"
                os.environ["scrolling_on"], os.environ["scrolling_once"] = "close", "False" 
                self.t3 = threading.Thread(target=scrolling)
                self.t3.start()

        lounch()
    
    def destroy_instagram(self):
        os.environ["scrolling_on"] = "close"
        os.environ["scrolling_once"] = "False" 
        self.coord = None
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET instagram_event=0 WHERE id={RFace}")
        base.execute_query(connection,"update camera set camera_on = 1")
        base.execute_query(connection,"update camera set instagram_on = 0")
        connection.close()

        pyautogui.click(1655, 175)
        time.sleep(0.2)
        pyautogui.click(1550, 365)
        time.sleep(0.5)

        os.system("pkill istekram")

        print(os.environ["scrolling_on"], os.environ["scrolling_once"])
