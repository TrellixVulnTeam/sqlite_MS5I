import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

ret, frame = cap.read()
print(ret)
