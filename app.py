import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("/dev/video0")

while True:
    success, img = cap.read()


    cv2.imshow("Iriun Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
