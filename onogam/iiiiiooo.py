import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image

img = cv2.imread("onono.jpg")
cv2.putText(img=img,text="hellow",org=(100,100),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.5,color=(0,250,0))

cv2.imshow("",img)
cv2.waitKey(0)