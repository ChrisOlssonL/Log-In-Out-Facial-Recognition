import cv2, sys, numpy, os, pathlib

class Recognize:
    def __init__(self, pred, datasets, haar_file, size=4):
        # self.name = name
        self.pred = []
        self.datasets = 'users'
        self.haar_file = 'haarcascade_frontalface_default.xml'
        self.ROOT_DIR = pathlib.Path().resolve().parent
        #recognization()
    
    def recognization(self):
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

        # Create a Numpy array from the two lists above
        (images, lables) = [numpy.array(lis) for lis in [images, lables]]

        # OpenCV trains a model from the images
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(images, lables)

        # Part 2: Use fisherRecognizer on camera stream
        face_cascade = cv2.CascadeClassifier(self.haar_file)
        webcam = cv2.VideoCapture(0)
        while True:
            (_, im) = webcam.read()
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
    
Recognize()