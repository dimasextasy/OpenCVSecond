import os
import cv2

print(cv2.__version__)

folder = 'test12345'
os.mkdir(folder)
camera = cv2.VideoCapture("Test.mp4")
count = 0
while True:
    success, image1 = camera.read()
    if not success: break
    cv2.imwrite(os.path.join(folder, "frame{:d}.jpg".format(count)), image1)
    count += 1
    print("{}images are extacted in {}".format(count, folder))