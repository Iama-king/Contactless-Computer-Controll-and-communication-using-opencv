import cv2
import mediapipe as mp
import time
import math as m
dflag=[0] # detection
drawc=True # draw the circle
land=False # drawland marks
hlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def dist(x1,y1,x2,y2):
    n = m.sqrt(((x1-x2)**2) + ((y1-y2)**2))
    return n
def handtrack(img, hands):
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    mpDraw = mp.solutions.drawing_utils
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        dflag[0]=1
        for handslms in results.multi_hand_landmarks:
            for id, lm in enumerate(handslms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                hlist[id]=[cx,cy]
                if drawc and id==8:
                    cv2.circle(img, (cx, cy), 25, (25, 23, 255), 3)
           #mpDraw.draw_landmarks(img, handslms, mphands.HAND_CONNECTIONS)
        if land:
            mpDraw.draw_landmarks(img,handslms)
    else:
        dflag[0]=0
    return img

def fingers():
    flist=[]
    fingers=[4,8,12,16,20]
    if dflag[0] == 1:
        for i in fingers:
            x1 = hlist[i][0]
            y1 = hlist[i][1]
            if(i != 4):
                x2 = hlist[i-3][0]
                y2 = hlist[i - 3][1]
                x3 = hlist[0][0]
                y3 = hlist[0][1]
            if(i == 4):
                x2 = hlist[i+1][0]
                y2 = hlist[i+1][1]
                x3 = hlist[17][0]
                y3 = hlist[17][1]

            h1 = dist(x1,y1,x3,y3)
            h2 = dist(x2,y2,x3,y3)

            if(h1 > h2):
                    flist.append(int(i/4))
    return flist


def main():
    ct = 0
    pt = 0
    cap = cv2.VideoCapture(0)
    mpxhands = mp.solutions.hands
    hands = mpxhands.Hands()
    mpDraw = mp.solutions.drawing_utils
    while True:
        success, img = cap.read()
        img = handtrack(img, hands)
        ct = time.time()
        fps = 1 / (ct - pt)
        pt = ct
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

