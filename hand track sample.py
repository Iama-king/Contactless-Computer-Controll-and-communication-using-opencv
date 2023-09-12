import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphands=mp.solutions.hands
hands=mphands.Hands()
mpDraw= mp.solutions.drawing_utils
ct=0
pt=0
while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    imgRGB= cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handslms in results.multi_hand_landmarks:
            for id,lm in enumerate(handslms.landmark):
                h , w, c = img.shape
                cx,cy= int(lm.x*w),int(lm.y*h)
                if id==8:
                    cv2.circle(img,(cx,cy),25,(25,23,255),3)
            mpDraw.draw_landmarks(img,handslms,mphands.HAND_CONNECTIONS)

    ct=time.time()
    fps=1/(ct-pt)
    pt=ct
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
