import face_recognition, imutils, pickle, time, cv2, os, sys, numpy, random, tkinter, time
import PIL.Image, PIL.ImageTk

from VideoHandler.Video_Capture import VideoCapture


class GUI:
    def __init__(self, window, w_title, v_source=0):
        self.window = window
        self.window.title(w_title)
        self.v_source = v_source
        self.vid = VideoCapture(self.v_source)
        
        
        
    def gui_video(self):
        #self.vid = VideoCapture(self.v_source)
        self.canvas = tkinter.Canvas(self.window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.btn_snapshot = tkinter.Button(self.window, text = "Snapshot", width = 50, command = self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
        # self.btn_status = tkinter.Button(self.window, text = "Login/Logout", width = 50, command = self.status)
        # self.btn_status.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_recognize = tkinter.Button(self.window, text="Recognize", width = 50, command = self.recognize)
        self.btn_recognize.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_createData = tkinter.Button(self.window, text="Create Data", width = 50, command = self.create_data)
        self.btn_createData.pack(anchor=tkinter.CENTER, expand=True)
        self.delay = 15
        self.update()
        self.window.mainloop()
    
    def create_data(self):
        create = self.vid.create_data("Liam")
        print("Created user: \t")
        # self.rec = VideoCapture.create_data(self.v_source, "Liam")
    
    def recognize(self):
        create = self.vid.recogniziation("")
        print(create)
        # self.rec = VideoCapture.recogniziation(self.v_source)
    
    def snapshot(self):
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    
    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
        
        self.window.after(self.delay, self.update)