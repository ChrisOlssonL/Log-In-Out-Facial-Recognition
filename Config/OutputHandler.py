import sys, os
import datetime

class Output:
    def __init__(self, text):
        self.file_location = "../Logs/"
        self.text = text
        self.error(self.text)
    
    def error(self):
        self.file = self.create_file()
        self.file.write(self.text)
        self.file.close()
        

    def create_file(self):
        self.file = open(self.file_location + str(self.get_time()) + ".txt", "w")
        return(self.file)
        
    def get_time(self):
        self.date = datetime.datetime.now()
        self.date = self.date.strftime("%d%m%Y%H-%M-%S")
        self.date = self.date.replace("/", "-")
        return(self.date)
