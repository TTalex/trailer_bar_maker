import numpy as np
import cv2
from scipy.stats import itemfreq


cap = cv2.VideoCapture('src.mp4')
img_res = np.zeros((100,1000,3), np.uint8)
frame_counter = 0
while(cap.isOpened()):
    frame_counter += 1
    ret, frame = cap.read()
    if frame is None:
        break;
    if frame_counter % 25 == 0:
        img = frame
        avg_color_per_row = np.average(img, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        print avg_color
        cv2.line(img_res,(frame_counter/5, 0),(frame_counter/5,100),avg_color,5)
        cv2.imshow("img_res", img_res)
        cv2.waitKey(1)

cap.release()
trim = []
for i in img_res:
    trim.append(i[0:frame_counter/5])
img_res = np.array(trim)
cv2.imshow("img_res", img_res)
cv2.waitKey(1)
cv2.imwrite("res.png", img_res)
#cv2.destroyAllWindows()
