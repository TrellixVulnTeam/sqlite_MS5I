import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image

img = cv2.imread("onono.jpg")
height, width, channels = img.shape[:3]
print(height,width)
cv2.putText(img=img,text="1/300",org=(width-180,50),fontFace=cv2.FONT_ITALIC,
            fontScale=1.5,color=(250,0,0),thickness=2)

cv2.imshow("",img)
cv2.waitKey(0)