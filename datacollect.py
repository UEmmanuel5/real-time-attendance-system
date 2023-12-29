# pip install opencv-python==4.5.2

import cv2 
import time

def what_position(index):
    pos = positions[0];
    if (index < len(positions)):
        pos = positions[index]
    return pos

video=cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
positions = ['Look Straight', 'Look Extreme Left', 'Look Extreme Right', 'Look Up', 'Look Down']
position_index = 0
taking_images = False
num = 500
max_images = 2500
per_image = num



id = input("Enter Your ID: ")
# id = int(id)
count=1


while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    if not taking_images:
        current_pos = what_position(position_index);
        print('index {}'.format(position_index))
        text = "{} . s to start:".format(current_pos)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2
        font_color = (0, 255, 0)  

        # Get the size of the text box
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

        # Calculate the position to center the text in the frame
        text_x = (frame.shape[1] - text_size[0]) // 2
        text_y = (frame.shape[0] + text_size[1]) // 2

        # Put the green text on the frame
        
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, font_thickness)
        cv2.imshow("Frame",frame)
    
        _key = cv2.waitKey(0);

        if _key == ord('s') or _key == ord('S'):
            taking_images = True 

    for (x,y,w,h) in faces:
        if taking_images:
            
            cv2.imwrite('datasets/User.'+str(id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
            count=count+1

        if (count > 1 and count % per_image == 0):
            taking_images = False;
            position_index +=1    
            

    cv2.imshow("Frame",frame)

    k=cv2.waitKey(1)

    if count>max_images:
        break

video.release()
cv2.destroyAllWindows()
print("Dataset Collection Done..................")