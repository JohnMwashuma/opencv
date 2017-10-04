import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    edges = cv2.Canny(frame, 50,50)

    cv2.imshow('edge', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 13:
        break

cv2.destroyAllWindows()
cap.release()