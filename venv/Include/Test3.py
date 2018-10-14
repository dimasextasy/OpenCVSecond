import cv2
import numpy as np
import math
import pylab
from matplotlib import mlab

img = cv2.imread("SOK1.jpg")
roi = img[120: 459, 342: 554]
x = 342
y = 120
width = 554 - x
height = 449 - y
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
s=[]
d=[]

<<<<<<< HEAD
cap = cv2.VideoCapture("car1.mp4")
=======
cap = cv2.VideoCapture("red_panda_snow.mp4")
>>>>>>> 4bce5266fcab2916491279ce929245e705203f26

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
<<<<<<< HEAD
    #print(ret)
    s.append(track_window[0])
    d.append(track_window[1])
    pylab.plot(s,d)
=======
    print(track_window)
    pylab.plot(track_window[0],track_window[1])
>>>>>>> 4bce5266fcab2916491279ce929245e705203f26
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(frame, [pts], True, (255, 0, 0), 2)
    cv2.imshow("mask", mask)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Roi",roi)
<<<<<<< HEAD
    if len(s)== 100 : pylab.show()
    key = cv2.waitKey(1)
    print(key)
=======
    #pylab.show()



    key = cv2.waitKey(30)
>>>>>>> 4bce5266fcab2916491279ce929245e705203f26
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

