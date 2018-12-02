import cv2
import numpy as np

def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        print(x, y)


cap = cv2.VideoCapture(0)
_, first_frame = cap.read()
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)
cap = cv2.VideoCapture("lft.mp4")
_, first_frame = cap.read()
cv2.namedWindow("first frame")
cv2.setMouseCallback("first frame", mouse_drawing)

while True:
    _, frame = cap.read()

    cv2.imshow("Frame", frame)
    cv2.imshow("first frame", first_frame)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()