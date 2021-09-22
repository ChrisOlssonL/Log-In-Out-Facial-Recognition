import sys, os, mysql.connector
from mysql.connector import Error


from OutputHandler import Output

class Database:
    def __init__(self):
        self.db_host = "localhost"
        self.db_name = "pyfacerec"
        self.db_user = "root"
        self.db_pwd = ""
        self.connect()
    
    def connect(self):
        global connection, cursor
        try:
            connection = mysql.connector.connect(
                host = self.db_host,
                database = self.db_name,
                user = self.db_user,
                password = self.db_pwd
            )
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to mysql")
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Connected to database!")
        except Error as e:
            print("Error: ", e)

    def disconnect(self):
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("Closed")
        except Error as e:
            print("Error while disconnecting: ", e)
    
    def add_user(self, information):
        fname = information["fname"]
        lname = information["lname"]
        code = information["code"]
        print(fname, lname, code)

        try:
            if connection.is_connected():
                cursor.execute(
                    "INSERT INTO `users` (`firstname`, `lastname`, `code`, `status`) VALUES ('" + str(fname) + "', " + "'" +  str(lname) + "', " + "'" +  str(code) + "', " + "'False');"
                    )
                connection.commit()
        except Error as e:
            print("Error while creating user: ", e)

    def status(self, prediction):
        try:
            if prediction > 100:
                print("Above 100")
                try:
                    if  connection.is_connected():
                        print("test")
                except Error as e:
                    print("Error while something")
        except Error as e:
            print("Error while logging in/out")
    
    
        
