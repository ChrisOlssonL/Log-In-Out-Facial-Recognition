import cv2, tkinter, os
import PIL.Image, PIL.ImageTk
import numpy

class VideoCapture:
    def __init__(self, v_source=0, size=4):
        #Open video source (cam = 0(default))
        self.vid = cv2.VideoCapture(v_source)
        self.pred = []
        self.datasets = '../users'
        self.haar_file = '../haarcascade_frontalface_default.xml'
        if not self.vid.isOpened():
            raise ValueError("Unable to open source", v_source)
        
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
        
    def create_data(self, user):
        sub_data = str(user)
        path = os.path.join(self.datasets, sub_data)
        if not os.path.isdir(path):
            os.mkdir(path)
        
        (width, height) = (130, 100)
        face_cascade = cv2.CascadeClassifier(self.haar_file)
        count = 1
        while count < 50:
            (_, im) = self.vid.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (width, height))
                cv2.imwrite('% s/% s.png' % (path, count), face_resize)
            count += 1
            
            # cv2.imshow('Opencv', im)
            key = cv2.waitKey(10)
            if key == 27:
                break
    
    def recogniziation(self):
        (images, lables, names, id) = ([], [], {}, 0)
        for (subdirs, dirs, files) in os.walk(self.datasets):
            for subdir in dirs:
                names[id] = subdir
                subjectpath = os.path.join(self.datasets, subdir)
                for filename in os.listdir(subjectpath):
                    path = subjectpath + '/' + filename
                    lable = id
                    images.append(cv2.imread(path, 0))
                    lables.append(int(lable))
                id += 1
        (width, height) = (130, 100)
        
        (images, lables) = [numpy.array(lis) for lis in [images, lables]]
        
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(images, lables)
        
        face_cascade = cv2.CascadeClassifier(self.haar_file)
        while True:
            (_, im) = self.vid.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (width, height))
                # Try to recognize the face
                prediction = model.predict(face_resize)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

                if prediction[1]<500:
                    cv2.putText(im, '% s - %.0f' % (names[prediction[0]], prediction[1]), (x-10, y-10),cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                    self.pred.append(prediction[0])
                    c = 0
                    if c < 1:
                        name = names[prediction[0]]
                        c += 1
                else:
                  cv2.putText(im, 'not recognized',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

            cv2.imshow('OpenCV', im)

            key = cv2.waitKey(10)
            if key == 27:
                break
            return name
        
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            
