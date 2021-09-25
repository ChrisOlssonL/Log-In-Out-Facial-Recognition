import face_recognition, imutils, pickle, time, cv2, os, sys, numpy, random, tkinter, time
import PIL.Image, PIL.ImageTk

# from Graphics import GUI
from Graphics import GUI

class Main:
    def __init__(self):
        self.title = "Face Recognizer"
        print("Starting")
        graphic = GUI(tkinter.Tk(), self.title)
        graphic.gui_video()
        # ROOT_DIR = pathlib.Path().resolve()

Main()
