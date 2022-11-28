#23
import cv2
import cvzone
import numpy as np
#import keyboard

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
lips_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

emoji = cv2.imread('emoji1.jpg', cv2.IMREAD_UNCHANGED)
lips_sticker = cv2.imread('Kiss-mouth.png', cv2.IMREAD_UNCHANGED)
eye_sticker = cv2.imread('emoji-eye.png', cv2.IMREAD_UNCHANGED)

#def remove_back(emj , position):
    
    #image_gray = cv2.cvtColor(emj , cv2.COLOR_BGR2GRAY)
    #convert img to black & white
    #thresh, image_edges = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)
    

videoCap = cv2.VideoCapture(0)

while True:
    ret, frame = videoCap.read()
    if ret == False:
        break
    
    effect = cv2.waitKey(100)
    #key = cv2.waitKey(50)

    if effect == 49: #press 1
        faces = face_detector.detectMultiScale(frame, 2)   
        for i , face in enumerate(faces):
            x,y,w,h = face
            new_emoji = cv2.resize(emoji, (w,h))
            frame[y:y+h , x:x+w] = new_emoji
    
    elif effect == 50: #press 2
        lips = lips_detector.detectMultiScale(frame, 2.3, 15, minSize=(50,50))
        for i , lip in enumerate(lips):
            x,y,w,h = lip
            Nlips_sticker = cv2.resize(lips_sticker, (w,h))
            frame[y:y+h , x:x+w] = Nlips_sticker
        
        eyes = eyes_detector.detectMultiScale(frame, 3, minSize=(40,40))
        for i , eye in enumerate(eyes):
            x,y,w,h = eye
            Neye_sticker = cv2.resize(eye_sticker, (w,h))
            frame[y:y+h , x:x+w] = Neye_sticker
    
    elif effect == 51: #press 3
        faces = face_detector.detectMultiScale(frame, 1.3)
        for x,y,w,h in faces:
           frame[y:y+h , x:x+w] = cv2.rotate(frame[y:y+h , x:x+w], cv2.ROTATE_180)
    
    elif effect == 52: #press 4
        faces = face_detector.detectMultiScale(frame, 1.3)
        for x,y,w,h in faces:
            mat = frame[y:y+h , x:x+w]
            mat_resized = cv2.resize(mat, (15,15) ,interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(mat_resized, (w,h), interpolation= cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = output
    
    elif effect == 27: #esc
       break        
       
    cv2.imshow('output', frame)
    