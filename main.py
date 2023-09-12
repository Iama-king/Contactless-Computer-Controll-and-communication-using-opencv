# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image as im
import cv2
import playsound as p
import mediapipe as mp
import time
import htm as h
import speech_recognition as sr
from pynput.mouse import Button, Controller as Controller
from pynput.keyboard import Key, Controller as kbc
import recog as r1
r = sr.Recognizer()
mouse = Controller()
keyboard=kbc()
xf=1920//440
yf=1080//270
ct = 0
pt = 0
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils
#h.land = True
while True:
    fingers = [4, 8, 12, 16, 20]
    success, img = cap.read()
    img = h.handtrack(img,hands)
    if h.dflag[0] == 1:
        fg = h.fingers()
        if(2 in fg and len(fg)==1):
            #print("mouse move")
            mouse.position = (xf*h.hlist[8][0]-20,yf*h.hlist[8][1]-20)
        if(2 in fg and 3 in fg and len(fg)==2):
            n = h.dist(h.hlist[8][0],h.hlist[8][1],h.hlist[12][0],h.hlist[12][1])
            if(n<40):
                mouse.press(Button.left)
            if(n>40 and n<50):
                mouse.release(Button.left)
        if(2 in fg and 1 in fg and len(fg)==2):
            n = h.dist(h.hlist[8][0], h.hlist[8][1], h.hlist[4][0], h.hlist[4][1])
        if(2 in fg and 1 in fg and 5 in fg and len(fg)==3):
           r1.rec()
        #if(3 in fg and len(fg)==1):
         #   g = im.open(r"C:\Users\sanja\Downloads\warning.png")
          #  g.show()
           # break
        if (1 in fg and len(fg) == 1):
            keyboard.press(Key.page_down)
            keyboard.release(Key.page_down)
            time.sleep(2)
        if (5 in fg and len(fg) == 1):
            keyboard.press(Key.page_up)
            keyboard.release(Key.page_up)
            time.sleep(2)
        #if(5 in fg and 1 in fg and len(fg)==2):
           # p.playsound(r'C:\Users\sanja\Downloads\Phone.mp3')
    ct = time.time()
    fps = 1 / (ct - pt)
    pt = ct
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)