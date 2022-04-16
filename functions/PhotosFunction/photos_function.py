from tkinter import * 
from PIL import ImageTk, Image
import os

from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()

prefix = os.getcwd()
photos_prefix = f"{prefix}/IntelligentMirror/PhotosFunction/photos_fuction/"
icons_prefix = f"{prefix}/IntelligentMirror/icons/"

class Photos:
    def __init__(self,tk: Frame, toolbarFrame:Frame,photosFrame:Frame ,timeFrame:Frame = None, weatherFrame:Frame = None,\
         gmailFrame: Frame = None, quoteFrame: Frame = None, calendarFrame:Frame = None) -> None:

        self.tk = tk
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.toolbarFrame = toolbarFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame

        self.mainButton = Button(self.photosFrame,bg="gray", command=self.takePhotos)

        self.photosFrame.bind("<Button-1>", self.drag_start_frame)
        self.photosFrame.bind("<B1-Motion>", self.drag_motion_frame)
        self.photosFrame.bind("<ButtonRelease-1>", self.drag_stop)

        self.mainButton.bind("<Button-1>", self.drag_start_frame)
        self.mainButton.bind("<B1-Motion>", self.drag_motion_frame)
        self.mainButton.bind("<ButtonRelease-1>", self.drag_stop)

    def get_image(self):
        photos_icon_old = Image.open(f"{icons_prefix}camera.png")
        photos_icon_new = photos_icon_old.resize((140,140))
        self.photos_icon = ImageTk.PhotoImage(photos_icon_new)
        

    def takePhotos(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        base.execute_query(connection, "update camera SET photo=1")
        connection.close()
    
    
    def photos(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection, f"update user SET photos_event=1 WHERE id={RFace}")
        toolbar_status = base.read_query(connection,"select toolbar from camera")[0][0]
        connection.close()

        x,y = Photos.check_position(self)

        if toolbar_status == "on" and x <= 210:
            x = 210

        self.photosFrame.place(x=x, y=y, width=150, height=150)

        def photos_loading(ToOn = False):
            
            self.get_image()
            self.mainButton.config(image=self.photos_icon, bg="black")

            if ToOn:
                ToOn = False
                self.mainButton.place(x=0,y=0)
        
        photos_loading(True)
    

    def destroy_photos(self):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        base.execute_query(connection,f"update user SET photos_event=0 WHERE id={RFace}")
        connection.close()
        
        for pack in self.photosFrame.place_slaves():
            pack.place_forget()
      
        self.photosFrame.place_forget()
    
    def check_position(self, RFace=None) -> int:
        """
        This function is responsible for checking actual photos position
        Returns
        -------
        x: int
            Value of "x" time position
        y: int 
            value of "y" time position
        """


        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        if RFace == None:
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
        coor = base.read_query(connection, f"select photos_x, photos_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y
    
    def photos_refresh(self, RFace):   #????
        x,y = self.check_position(RFace)
        self.photosFrame.place_configure(x=x, y=y)
        self.photosFrame.update()
    


    def drag_start_frame(self, event):

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        self.toolbar_event = base.read_query(connection, "select toolbar from camera")[0][0]
        connection.close()

        if self.toolbar_event == "on":

            self.photosFrame.startX = event.x
            self.photosFrame.startY = event.y

            self.photosFrame.ToOn = True 
            from IntelligentMirror.toolbar.display_toolbar import Toolbar
            Toolbar.HideToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                 self.gmailFrame, self.quoteFrame, self.calendarFrame,self.photosFrame,NoMove="photos")

        else:
            #self.photosFrame.ToOn = False
            self.photos()


    
    
    def drag_motion_frame(self, event):
        if self.toolbar_event == "on":
            x = self.photosFrame.winfo_x() - self.photosFrame.startX + event.x
            y = self.photosFrame.winfo_y() - self.photosFrame.startY + event.y

            tk_width = 1920
            tk_height = 1080
            frame_width = self.photosFrame.winfo_width()
            frame_height = self.photosFrame.winfo_height()

            max_x = tk_width - frame_width
            max_y = tk_height - frame_height

            if x > max_x:
                x = max_x
            elif x < 0:
                x = 0

            if y > max_y:
                y = max_y
            elif y < 0:
                y = 0

            self.photosFrame.place(x=x, y=y)

            self.photosFrame.stopX = x
            self.photosFrame.stopY = y

    
    def drag_stop(self, event=None):

        if self.toolbar_event == "on":
            
            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            RFace = base.read_query(connection, "select actuall_user from camera")[0][0]
            base.execute_query(connection, f"update user SET photos_x={self.photosFrame.stopX} WHERE id={RFace}")
            base.execute_query(connection, f"update user SET photos_y={self.photosFrame.stopY} WHERE id={RFace}")
            connection.close()

            if self.photosFrame.ToOn == True: 
        
                from IntelligentMirror.toolbar.display_toolbar import Toolbar
                Toolbar.OpenToolbarAnimation_DF(self.toolbarFrame, self.timeFrame, self.weatherFrame,\
                    self.gmailFrame, self.quoteFrame, self.calendarFrame,self.photosFrame)





