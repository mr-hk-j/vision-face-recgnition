import cv2
import numpy as np
import os
import xlwt
import time
from PIL import Image


t = time.strftime("Attendence on %d_%m_%Y at %I_%M %p") + '.xls'
book = xlwt.Workbook()
sheet = book.add_sheet("Sheet 1", cell_overwrite_ok=True)


def entry(id, r):
    sheet.write(0, 0, "NAME")
    sheet.write(0, 1, "ATTENDANCE")
    sheet.write(r + 1, 0, id)
    sheet.write(r + 1, 1, 'Present')
    book.save(t)

def attendance():

    r = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0
    flag = 0
    id2 = 0

    # names related to ids
    names = ['None', 'Hari','Gayathri','Rahul','Prasanth']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:

        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



        faces = faceCascade.detectMultiScale(

            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            path = 'C:\\Users\\Hari\\Desktop\\REVIEW\\'
            cv2.imwrite(os.path.join(path, str(id) + '.jpg'), img)

            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            id2 = id

            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "Unknown Face"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (0, 0, 255), 2)
            cv2.putText(img, str(confidence), (x + w, y), font, 0.5, (0, 0, 255), 1)
            for i in range(1, 60):
                if (id2 == i):
                    entry(id, i)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            cam.release()
            cv2.destroyAllWindows()
            break

def snap():

    r = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0
    flag = 0
    id2 = 0

    # names related to ids
    names = ['None', 'Hari','Gayathri','Rahul','Prasanth']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height
    r, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    faces = faceCascade.detectMultiScale(

        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        path = 'C:\\Users\\Hari\\Desktop\\REVIEW\\Data'
        cv2.imwrite(os.path.join(path, str(id) + '.jpg'), img)
        cv2.imwrite("new.jpg", img)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        id2 = id

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "Unknown Face"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (0, 0, 255), 2)
        cv2.putText(img, str(confidence), (x + w, y), font, 0.5, (0, 0, 255), 1)

        for i in range(1, 60):
            if (id2 == i):
                entry(id, i)

    cam.release()

def report():

    file = "C:\\Users\\Hari\\Desktop\\REVIEW\\" + str(t)
    os.startfile(file)




def trainer(x):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width1
    cam.set(4, 480)  # set video height
    face_detector = cv2.CascadeClassifier('haarcascade.xml')

    # For each person, enter one numeric face id
    face_id = x


    count = 0

    while (True):

        ret, img = cam.read()
        img = cv2.flip(img, 1)  # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            cam.release()
            cv2.destroyAllWindows()
            break
        elif count >= 100:
            cam.release()
            cv2.destroyAllWindows()

            break

            # Path for face image database
    path = 'dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade.xml");

    # function to get the images and label data
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)

        return faceSamples, ids

    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml')  # recognizer.save() worked on Mac, but not on Pi

    # Print the number of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))