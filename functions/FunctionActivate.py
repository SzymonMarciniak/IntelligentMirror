import time 
from tkinter import *
import threading
import os 

from IntelligentMirror.functions.TimeFunction.DisplayTime import CurrentTime
from IntelligentMirror.functions.WeatherFunction.weather_function import CurrentWeather
from IntelligentMirror.functions.GmailFunction.gmail_function import GmailMain
from IntelligentMirror.functions.QuoteFunction.quote_function import QuoteMain
from IntelligentMirror.functions.CalendarFunction.calendar_function import Calendar
from IntelligentMirror.functions.PhotosFunction.photos_function import Photos
from IntelligentMirror.applications.InstagramFunction.instargram_function import Instagram
from IntelligentMirror.functions.LightAndRollerShutters.light_and_rollershutters import Light
from IntelligentMirror.applications.SpotifyFunction.spotify_function import Spotify
from IntelligentMirror.DataBase.data_base import DataBase
base = DataBase()


class FunctionsActivateClass:
    """This class is responsible for activating the functions"""

    def __init__(self,
                tk: Frame,
                toolbarFrame: Frame,
                timeFrame: Frame,
                weatherFrame: Frame,
                gmailFrame: Frame,
                quoteFrame: Frame,
                calendarFrame: Frame,
                photosFrame:Frame,
                spotifyFrame: Frame) -> None:

        """
        Parametrs
        ---------
        tk: Tk()
            Name of main window
        toolbarFrame: Frame
            Toolbar frame
        timeFrame: Frame
            Frame for clock label and date label
        weatherFrame: Frame 
            Frame for all weather labels 
        gmailFrame: Frame
            Frame for all gmail labels
        """
        self.tk = tk
        self.toolbarFrame = toolbarFrame
        self.timeFrame = timeFrame
        self.weatherFrame = weatherFrame
        self.gmailFrame = gmailFrame
        self.quoteFrame = quoteFrame
        self.calendarFrame = calendarFrame
        self.photosFrame = photosFrame
        self.spotifyFrame = spotifyFrame

        self.time = CurrentTime(self.tk, toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
        self.weather = CurrentWeather(self.tk, toolbarFrame, self.weatherFrame, self.timeFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
        self.gmail = GmailMain(self.tk, toolbarFrame, self.gmailFrame ,self.timeFrame, self.weatherFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
        self.quote = QuoteMain(self.tk, toolbarFrame, self.quoteFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
        self.calendar = Calendar(self.tk, toolbarFrame, self.calendarFrame,self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.photosFrame, self.spotifyFrame)
        self.photos = Photos(self.tk, toolbarFrame, self.photosFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame, self.spotifyFrame)
        self.instagram = Instagram(self.tk, toolbarFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame, self.spotifyFrame)
        self.light = Light() 
        self.spotify = Spotify(self.tk, toolbarFrame, self.spotifyFrame, self.timeFrame, self.weatherFrame, self.gmailFrame, self.quoteFrame, self.calendarFrame, self.photosFrame)

        self.prefix = os.getcwd()

        self.instagram_open_once = False
    
    def check_functions_position(self, function, RFace):

        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")

        if RFace == None:
            RFace = base.read_query(connection,"select actuall_user from camera")[0][0]

        coor = base.read_query(connection,f"select {function}_x, {function}_y from user WHERE id={RFace}")[0]
        connection.close()

        x = coor[0]
        y = coor[1]

        return x, y
        
    def functions_position_refresh(self, RFace):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        data = base.read_query(connection, f"select time_event, weather_event, gmail_event, quote_event, calendar_event, photos_event, instagram_event, spotify_event from user WHERE id={RFace}")[0]
        connection.close()

        timeOn = data[0]
        weatherOn = data[1]
        gmailOn = data[2]
        quoteOn = data[3]
        calendarOn = data[4]
        photosOn = data[5]
        instagramOn = data[6]
        spotifyOn = data[7]

        if timeOn:
            TimeToRefresh = True
        else:
            TimeToRefresh = False
            self.time.destroy_time()

        if weatherOn:
            WeatherToRefresh = True
        else:
            WeatherToRefresh = False 
            self.weather.destroy_weather()

        if gmailOn:
            GmailToRefresh = True
        else:
            GmailToRefresh = False 
            self.gmail.destroy_gmail() 
        
        if quoteOn:
            QuoteToRefresh = True
        else:
            QuoteToRefresh = False 
            self.quote.destroy_quote() 
        
        if calendarOn:
            CalendarToRefresh = True
        else:
            CalendarToRefresh = False 
            self.calendar.destroy_calendar() 
        
        if photosOn:
            PhotosToRefresh = True
        else:
            PhotosToRefresh = False 
            self.photos.destroy_photos() 
        
        if spotifyOn:
            SpotifyToRefresh = True 
        else:
            SpotifyToRefresh = False 
            self.spotify.destroy_spotify()
        
        if instagramOn:
            InstagramToRefresh = True
        else:
            InstagramToRefresh = False 

            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            base.execute_query(connection,"update camera set instagram_on = 0")
            connection.close()

            self.instagram.destroy_instagram() 
        
      
        self.function_refreshing(RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh, QuoteToRefresh,CalendarToRefresh, PhotosToRefresh, InstagramToRefresh, SpotifyToRefresh)
    
    def function_refreshing(self, RFace, TimeToRefresh, WeatherToRefresh, GmailToRefresh, QuoteToRefresh, CalendarToRefresh, PhotosToRefresh, InstagramToRefresh, SpotifyToRefresh):
        
        connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
        data = base.read_query(connection,f"select time_event, weather_event, gmail_event, quote_event, calendar_event, photos_event, instagram_event, spotify_event from user WHERE id=1")[0]
        connection.close()
        
        PtimeOn = data[0]
        PweatherOn = data[1]
        PgmailOn = data[2]
        PquoteOn = data[3]
        PcalendarOn = data[4]
        PphotosOn = data[5]
        PinstagramOn = data[6]
        PspotifyOn = data[7]
        
        smoothening = 11

        endX_time, endY_time = self.check_functions_position("time", RFace)
        self.plocX_time, self.plocY_time = 0,0
        if TimeToRefresh:
            self.clocX_time, self.clocY_time = 1,1
            if not PtimeOn:
                self.time_function()
        else:
            self.clocX_time, self.clocY_time = 0,0
        

        endX_weather, endY_weather = self.check_functions_position("weather", RFace)
        self.plocX_weather, self.plocY_weather = 0,0
        if WeatherToRefresh:
            self.clocX_weather, self.clocY_weather = 1,1
            if not PweatherOn:
                self.weather_function()
        else:
            self.clocX_weather, self.clocY_weather = 0,0
        
        endX_quote, endY_quote = self.check_functions_position("quote", RFace)
        self.plocX_quote, self.plocY_quote = 0,0
        if QuoteToRefresh:
            self.clocX_quote, self.clocY_quote = 1,1
            if not PquoteOn:
                self.quote_function()
        else:
            self.clocX_quote, self.clocY_quote = 0,0
        
        endX_calendar, endY_calendar = self.check_functions_position("calendar", RFace)
        self.plocX_calendar, self.plocY_calendar = 0,0
        if CalendarToRefresh:
            self.clocX_calendar, self.clocY_calendar = 1,1
            if not PcalendarOn:
                self.calendar_function()
        else:
            self.clocX_calendar, self.clocY_calendar = 0,0
        
        endX_photos, endY_photos = self.check_functions_position("photos", RFace)
        self.plocX_photos, self.plocY_photos = 0,0
        if PhotosToRefresh:
            self.clocX_photos, self.clocY_photos = 1,1
            if not PphotosOn:
                self.photos_function()
        else:
            self.clocX_photos, self.clocY_photos = 0,0

        endX_spotify, endY_spotify = self.check_functions_position("spotify", RFace)
        self.plocX_spotify, self.plocY_spotify = 0,0
        if SpotifyToRefresh:
            self.clocX_spotify, self.clocY_spotify = 1,1
            if not PspotifyOn:
                self.spotify_function()
        else:
            self.clocX_spotify, self.clocY_spotify = 0,0
        
        if InstagramToRefresh:
            if PinstagramOn: instagram_to_close = True
            else: instagram_to_close = False 

            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            instagram_to_open = base.read_query(connection,f"select instagram_event from user WHERE id={RFace}")[0][0]
            connection.close()        
       
        
        if TimeToRefresh:
            TimeThread = threading.Thread(target=lambda: self.TimeRefreshing(smoothening, endX_time, endY_time))
            TimeThread.start()
        
        if WeatherToRefresh:
            WeatherThread = threading.Thread(target=lambda: self.WeatherRefreshing(smoothening, endX_weather, endY_weather))
            WeatherThread.start()
        
        if QuoteToRefresh:
            QuoteThread = threading.Thread(target=lambda:self.QuoteRefreshing(smoothening, endX_quote, endY_quote))
            QuoteThread.start()
        
        if CalendarToRefresh:
            CalendarThread = threading.Thread(target=lambda:self.CalendarRefreshing(smoothening, endX_calendar, endY_calendar))
            CalendarThread.start()
        
        if GmailToRefresh:
            GmailThread = threading.Thread(target=lambda:self.GmailRefreshing(PgmailOn))
            GmailThread.start()
        
        if PhotosToRefresh:
            PhotosThread = threading.Thread(target=lambda:self.PhotosRefreshing(smoothening,endX_photos, endY_photos))
            PhotosThread.start()
        
        if InstagramToRefresh:
            InstagramThread = threading.Thread(target=lambda:self.InstagramRefreshing(instagram_to_close, instagram_to_open))
            InstagramThread.start()
        
        if SpotifyToRefresh:
            SpotifyThread = threading.Thread(target=lambda:self.SpotifyRefreshing(smoothening, endX_spotify, endY_spotify))
            SpotifyThread.start()
    
    
    def InstagramRefreshing(self, to_close, to_open):
        if to_close:
            self.instagram.destroy_instagram()
        
        if to_open:
            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            base.execute_query(connection,"update camera set instagram_on = 1")
            connection.close()

            self.instagram.main_instargram()


    def GmailRefreshing(self, PgmailOn):
        self.gmail_function(on=False)
        self.gmail_function()
        if not PgmailOn:
            self.gmail_function()

    def CalendarRefreshing(self, smoothening, endX_calendar, endY_calendar):
        while int(self.plocX_calendar) != int(self.clocX_calendar) and int(self.plocY_calendar) != int(self.clocY_calendar):
            self.plocX_calendar = self.calendarFrame.winfo_x()
            self.plocY_calendar = self.calendarFrame.winfo_y()

            self.clocX_calendar = self.plocX_calendar + (endX_calendar - self.plocX_calendar) / smoothening
            self.clocY_calendar = self.plocY_calendar + (endY_calendar - self.plocY_calendar) / smoothening

            x_calendar = int(self.clocX_calendar)
            y_calendar = int(self.clocY_calendar)

            self.calendarFrame.place_configure(x=x_calendar,y=y_calendar)
            self.calendarFrame.update()

            time.sleep(0.015)

        self.calendarFrame.place_configure(x=endX_calendar,y=endY_calendar)
        self.calendarFrame.update()

    def QuoteRefreshing(self, smoothening, endX_quote, endY_quote):
        while int(self.plocX_quote) != int(self.clocX_quote) and int(self.plocY_quote) != int(self.clocY_quote):
            self.plocX_quote = self.quoteFrame.winfo_x()
            self.plocY_quote = self.quoteFrame.winfo_y()

            self.clocX_quote = self.plocX_quote + (endX_quote - self.plocX_quote) / smoothening
            self.clocY_quote =self.plocY_quote + (endY_quote - self.plocY_quote) / smoothening

            x_quote = int(self.clocX_quote)
            y_quote = int(self.clocY_quote)

            self.quoteFrame.place_configure(x=x_quote,y=y_quote)
            self.quoteFrame.update()

            time.sleep(0.015)
        
        self.quoteFrame.place_configure(x=endX_quote,y=endY_quote)
        self.quoteFrame.update()

    def WeatherRefreshing(self, smoothening, endX_weather, endY_weather):
        while int(self.plocX_weather) != int(self.clocX_weather) and int(self.plocY_weather) != int(self.clocY_weather):
            self.plocX_weather = self.weatherFrame.winfo_x()
            self.plocY_weather = self.weatherFrame.winfo_y()

            self.clocX_weather = self.plocX_weather + (endX_weather - self.plocX_weather) / smoothening
            self.clocY_weather = self.plocY_weather + (endY_weather - self.plocY_weather) / smoothening

            x_weather = int(self.clocX_weather)
            y_weather = int(self.clocY_weather)

            self.weatherFrame.place_configure(x=x_weather,y=y_weather)
            self.weatherFrame.update()

            time.sleep(0.015)

        self.weatherFrame.place_configure(x=endX_weather,y=endY_weather)
        self.weatherFrame.update()

    def TimeRefreshing(self, smoothening, endX_time, endY_time):
        while int(self.plocX_time) != int(self.clocX_time) and int(self.plocY_time) != int(self.clocY_time):
            self.plocX_time = self.timeFrame.winfo_x()
            self.plocY_time = self.timeFrame.winfo_y()

            self.clocX_time = self.plocX_time + (endX_time - self.plocX_time) / smoothening
            self.clocY_time = self.plocY_time + (endY_time - self.plocY_time) / smoothening

            x_time = int(self.clocX_time)
            y_time = int(self.clocY_time)

            self.timeFrame.place_configure(x=x_time,y=y_time)
            self.timeFrame.update()

            time.sleep(0.017)
        
        self.timeFrame.place_configure(x=endX_time,y=endY_time)
        self.timeFrame.update()
    
    def PhotosRefreshing(self, smoothening, endX_photos, endY_photos):
        while int(self.plocX_photos) != int(self.clocX_photos) and int(self.plocY_photos) != int(self.clocY_photos):
            self.plocX_photos = self.photosFrame.winfo_x()
            self.plocY_photos = self.photosFrame.winfo_y()

            self.clocX_photos = self.plocX_photos + (endX_photos - self.plocX_photos) / smoothening
            self.clocY_photos = self.plocY_photos + (endY_photos - self.plocY_photos) / smoothening

            x_photos = int(self.clocX_photos)
            y_photos = int(self.clocY_photos)

            self.photosFrame.place_configure(x=x_photos,y=y_photos)
            self.photosFrame.update()

            time.sleep(0.017)
        
        self.photosFrame.place_configure(x=endX_photos,y=endY_photos)
        self.photosFrame.update()
    
    
    def SpotifyRefreshing(self, smoothening, endX_spotify, endY_spotify):
        while int(self.plocX_spotify) != int(self.clocX_spotify) and int(self.plocY_spotify) != int(self.clocY_spotify):
            self.plocX_spotify = self.spotifyFrame.winfo_x()
            self.plocY_spotify = self.spotifyFrame.winfo_y()

            self.clocX_spotify = self.plocX_spotify + (endX_spotify - self.plocX_spotify) / smoothening
            self.clocY_spotify = self.plocY_spotify + (endY_spotify - self.plocY_spotify) / smoothening

            x_spotify = int(self.clocX_spotify)
            y_spotify = int(self.clocY_spotify)

            self.spotifyFrame.place_configure(x=x_spotify,y=y_spotify)
            self.spotifyFrame.update()

            time.sleep(0.015)

        self.spotifyFrame.place_configure(x=endX_spotify,y=endY_spotify)
        self.spotifyFrame.update() 
        


    def time_function(self, on=True) -> None:
        """Activates time function"""
        if on:
            self.time.clock_date()
        else:
            self.time.destroy_time()

    def weather_function(self, on=True) -> None:
        """Activates weather function"""
        if on:
            self.weather.weather()
        else:
            self.weather.destroy_weather() 
        
    def gmail_function(self, on=True) -> None:
        """Activates gmail function"""
        if on:
            self.gmail.main()
        else:
            self.gmail.destroy_gmail()
    
    def quote_function(self, on=True) -> None:
        """Activates quote function"""
        if on:
            self.quote.main()
        else:
            self.quote.destroy_quote()
        
    def calendar_function(self, on=True) -> None:
        """Activates calendar function"""
        if on:
            self.calendar.calendarMain()
        else:
            self.calendar.destroy_calendar()

    def photos_function(self, on=True) -> None:
        """Activates photos function"""
        if on:
            self.photos.photos()
        else:
            self.photos.destroy_photos()
    
        
    def instagram_function(self, on=True) -> None:
        """Activates instargram function"""
        if on:
            self.instagram.main_instargram()  

        else:
            connection = base.create_db_connection("localhost","szymon","dzbanek","mirror")
            base.execute_query(connection,"update camera set instagram_on = 0")
            base.execute_query(connection,"update camera set camera_on = 1")
            connection.close()
            self.instagram.destroy_instagram()
    
    def light_function(self, on=True):
        if on:
            self.light.light_on()
        else:
            self.light.light_off()
    
    def roller_shutters_down_function(self):
        self.light.rollerShuttersDown()
    
    def roller_shutters_up_function(self):
        self.light.rollerShuttersUp()

    def roller_shutters_pause_function(self):
        self.light.rollerShuttersStop()
    
    def spotify_function(self, on=True) -> None:
        if on:
            self.spotify.main_spotify()
        else:
            self.spotify.destroy_spotify()

