
import mysql.connector
from mysql.connector import Error 
import os


prefix = os.getcwd()

class DataBase:

    def create_server_connection(self,host_name, user_name, user_password):
        connection = None 
        try:
            connection = mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)
        except Error as err:
            print(f"FAILD {err}")
        return connection

    #connection = create_server_connection("localhost", "szymon", "dzbanek")


    def create_database(self,connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error as err:
            print(f"Faild: {err}")

    # create_database_query = "Create database mysql_calendar"
    # create_database(connection, create_database_query)


    def create_db_connection(self,host_name, user_name, user_password, db_name):
        connection = None 
        try:
            connection = mysql.connector.connect(host =host_name, user = user_name, passwd = user_password, database = db_name)
        except Error as err:
            print(f"Error: {err}")
        return connection

    #connection = create_db_connection("localhost","szymon", "dzbanek", "mysql_calendar")


    def execute_query(self,connection, query):
        cursor = connection.cursor() 
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(f"Error: {err}")

    # events_table = """
    # create table events(
    #     date_event date not null,
    #     event_name varchar(20) not null);
    # """
    # execute_query(connection, events_table)

    # delete_events = """
    # delete from events;
    # """
    # execute_query(connection, delete_events)

    # data_events = """
    # insert into events values
    # ('2022-04-14', 'Techno-Granty'),
    # ('2022-02-26', 'Today'),
    # ('2022-02-28', 'Max char912344567892');
    # """

    # execute_query(connection, data_events)

    def read_query(self,connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: {err}")

    # query = "select * from events order by date_event;"    
    # results = read_query(connection, query)
