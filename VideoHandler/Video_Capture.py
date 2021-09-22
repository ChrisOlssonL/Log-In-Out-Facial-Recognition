import cv2, tkinter
import PIL.Image, PIL.ImageTk

class VideoCapture:
    def __init__(self, v_source=0):
        #Open video source (cam = 0(default))
        self.vid = cv2.VideoCapture(v_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open source", v_source)
        
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            
