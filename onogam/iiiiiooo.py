import cv2
import numpy as np
import PySimpleGUI as sg
from PIL import Image
import os

dir_path =r"C:\Users\60837\Desktop\fu"
os.chdir(dir_path)
file_name = os.listdir()
count = 0
total = len(file_name)

for i in file_name:
    count += 1
    img = cv2.imread(i)
    height, width, channels = img.shape[:3]
    print(height,width)
    cv2.putText(img=img,text="{0}/{1}".format(count,total),org=(width-120,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,color=(250,0,0),thickness=2)

    cv2.imshow("",img)
    cv2.waitKey(0)