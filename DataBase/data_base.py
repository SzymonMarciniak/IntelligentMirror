import mysql.connector
from mysql.connector import Error 



class DataBase:

    def __init__(self) -> None:
        pass

    def create_database(self,connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error as err:
            print(f"Faild: {err}")

    @staticmethod
    def create_server_connection(host_name, user_name, user_password):
        connection = None 
        try:
            connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)
        except Error as err:
            print(f"FAILD {err}")
        return connection

    @staticmethod
    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None 
        try:
            connection = mysql.connector.connect(host =host_name, user = user_name, passwd = user_password, database = db_name)
        except Error as err:
            print(f"Error: {err}")
        return connection


    def execute_query(self,connection, query):
        cursor = connection.cursor() 
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(f"Error: {err}")


    def read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    base = DataBase()
    # connection = base.create_server_connection("localhost", "szymon", "dzbanek")
    # base.create_database(connection, "Create database mysql_mirror")

    connection = base.create_db_connection("localhost","szymon","dzbanek","mysql_mirror")

    # create_user_table_query = """
    # create table user(
    #     id INT(6) UNSIGNED PRIMARY KEY,
    #     name VARCHAR(30) NOT NULL,
    #     lastname VARCHAR(30) NOT NULL,
    #     password VARCHAR(30) NOT NULL,
    #     email VARCHAR(50) NOT NULL,
    #     nick VARCHAR(10) NOT NULL
    # )""" 

    # create_pictures_table_query = """
    # create table pictures(
    #     id INT(4) UNSIGNED PRIMARY KEY,
    #     userid INT(3) UNSIGNED NOT NULL,
    #     name VARCHAR(30) NOT NULL
    # )"""

    # create_event_table_query = """
    # create table event(
    #     id INT(11) UNSIGNED PRIMARY KEY,
    #     userid INT(11) UNSIGNED NOT NULL,
    #     name text NOT NULL,
    #     howlong INT(3) NOT NULL,
    #     date datetime NOT NULL
    # )
    # """

    # base.execute_query(connection, create_user_table_query)
    # base.execute_query(connection, create_pictures_table_query)
    # base.execute_query(connection, create_event_table_query)

    # create_camera_table_query = """
    # create table camera(
    #     toolbar VARCHAR(3) NOT NULL,
    #     actuall_user INT(3) NOT NULL,
    #     photo BIT NOT NULL,

    #     mouse_event BIT NOT NULL,
    #     mouse_frame VARCHAR(10) NOT NULL,
    #     mouse_x INT(5) NOT NULL,
    #     mouse_y INT(5) NOT NULL
    # )"""

    # create_accounts_table_query = """
    # create table accounts(
    #     user_id INT(6) UNSIGNED PRIMARY KEY,
    #     nick VARCHAR(10) NOT NULL,

    #     time_event BIT NOT NULL,
    #     time_x INT(4) NOT NULL,
    #     time_y INT(4) NOT NULL,

    #     weather_event BIT NOT NULL,
    #     weather_x INT(4) NOT NULL,
    #     weather_y INT(4) NOT NULL,

    #     gmail_event BIT NOT NULL,
    #     gmail_x INT(4) NOT NULL,
    #     gmail_y INT(4) NOT NULL,
    #     gmail_login VARCHAR(30),
    #     gmail_password VARCHAR(30),

    #     quote_event BIT NOT NULL,
    #     quote_x INT(4) NOT NULL,
    #     quote_y INT(4) NOT NULL,

    #     calendar_event BIT NOT NULL,
    #     calendar_x INT(4) NOT NULL,
    #     calendar_y INT(4) NOT NULL,

    #     photos_event BIT NOT NULL,
    #     photos_x INT(4) NOT NULL,
    #     photos_y INT(4) NOT NULL
    # )"""
    
    #base.execute_query("DROP TABLE IF EXISTS camera")
    #base.execute_query(create_camera_table_query)
    # base.execute_query(create_accounts_table_query)

    # add_users_query = """
    # insert into accounts values
    # (0, 'None', 0, 789, 36, 0, 62, 169, 0, 498, 29, 'None', 'None', 0, 444, 990, 0, 1530, 311, 0, 1342, 132),
    # (1, 'M4RC1N', 1, 1577, 18, 1, 1570, 223, 1, 1306, 0, 'szymonmarciniak24@gmail.com', 'haslo123', 1, 416, 975, 1, 1634, 489, 1, 145, 805)
    # """

    # base.execute_query(add_users_query)

    # add_user_query = """
    # insert into user values
    # (0, 'None', 'None', 'haslo123','None', 'None'),
    # (1, 'Szymon', 'Marciniak', 'haslo321', 'szymonmarciniak24@gmail.com', 'M4RC1N')
    # """

    # add_camera_query = """
    # insert into camera values
    # ('off', 0, 0, 0, 'time', 100, 100)
    # """

    #base.execute_query(add_user_query)
    #base.execute_query(add_camera_query)

    # q = """
    # ALTER TABLE camera ADD instagram_on bit NOT NULL
    # """

    # q2 = """
    # UPDATE camera set instagram_on=0
    # """

    # base.execute_query(connection, q)
    # base.execute_query(connection, q2)

    # q3 = """
    # ALTER TABLE camera ADD camera_on bit NOT NULL
    # """

    # q4 = """
    # UPDATE camera set camera_on=1
    # """

    # base.execute_query(connection, q3)
    # base.execute_query(connection, q4)

    # q5 = """
    # ALTER TABLE accounts ADD instagram_event bit NOT NULL
    # """
    # q8 = """
    # UPDATE accounts set instagram_event=0
    # """
    # q6 = """
    # ALTER TABLE user ADD instagram_login text 
    # """
    # q7 = """
    # ALTER TABLE user ADD instagram_password text
    # """
    # base.execute_query(connection, q5)
    # base.execute_query(connection, q6)
    # base.execute_query(connection, q7)
    # base.execute_query(connection, q8)

    # q9 = """
    # UPDATE user set instagram_login='szymonmarciniak24@gmail.com' WHERE id=1
    # """
    # q10 = """
    # UPDATE user set instagram_password='' WHERE id=1
    # """
    # base.execute_query(connection, q9)
    # base.execute_query(connection, q10)

    print("\n\n")
    print(base.read_query(connection,"select * from accounts"))
    print("\n\n")
    print(base.read_query(connection,"select * from user"))
    print("\n\n")
    print(base.read_query(connection,"select * from camera"))
   
    