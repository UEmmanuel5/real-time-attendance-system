# pip install opencv-python==4.5.2

import cv2 
# from controller import doorAutomate
import time
from datetime import datetime
from db import is_attendance_marked, mark_attendance

def calculate_predictions(total,correct):
    prediction_rate =  (correct / total) * 100
    print("correct {}".format(correct))
    print("total {}".format(total))
    print("Recognition Rate {:.2f}".format(prediction_rate))
    print("Smallest Confidence {}".format(min(confidences)))

video=cv2.VideoCapture(0)



facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

# name_list = ["", "Amos", "Emmanuel", "Christine"]
name_list = ["", "Amos", "Emmanuel"]
imgBackground = cv2.imread("background.png")
number_of_predictions = 0;
number_of_correct = 0;
start_time = time.time();
subject = 1
confidences = []
course = 'Image Understanding'
while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        number_of_predictions +=1
        confidences.append(conf)
        print(serial,conf)
        # 60
        if serial == subject and conf <= 60:
                number_of_correct +=1
        # let's check the attendance
        attendance_time = datetime.now()
        attendance_date = attendance_time.date()        
        check_attendance = is_attendance_marked(serial,course,attendance_date)
        if not check_attendance:
             mark_attendance(serial,course, attendance_time)

        if conf <= 200:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv2.putText(frame, name_list[serial], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
            
        else:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv2.putText(frame, "Unknown", (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

    frame=cv2.resize(frame, (640, 480))
    imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame",imgBackground)
    end_time = time.time();
    elapsed_time = end_time - start_time

    if (elapsed_time >= 360):
        calculate_predictions(number_of_predictions, number_of_correct)
        video.release()
        cv2.destroyAllWindows()
        break


    k=cv2.waitKey(1)
    
    # if k==ord('o') and conf>50:
        # doorAutomate(0)
        # time.sleep(10)
        # doorAutomate(1)
    if k==ord("q"):
        prediction_rate =  (number_of_correct / number_of_predictions) * 100
        print("Recognition Rate {}.2f".format(prediction_rate))
        break

video.release()
cv2.destroyAllWindows()
