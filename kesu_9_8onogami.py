import re
import PySimpleGUIQt as sg
import os
import subprocess
from PySimpleGUIQt.PySimpleGUIQt import TRANSPARENT_BUTTON, InputCombo
import cv2
from PIL import Image
import sys

system = sg.SystemTray(menu=["",["メニュー",["OK","b"],"終了"]])


        
#system.show_message("python","test")

lay = [
    [sg.Text("Multiline"),sg.Multiline(key="in",enable_events=True),sg.Image(key="img")],
    [sg.Text("Listbox"),sg.Listbox(values=[],key="list",enable_events=True,),sg.Image(key="in_img"),sg.In(key="inin")],
    [sg.T("Output"),sg.Output(key="out")],
    [sg.OK(),sg.Button("b")]
]

#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

window = sg.Window("",lay,finalize=True)
list = {}


while True:
    event,values = window.read(timeout=50)
    try:
        #システムトレイの定義
        read = system.Read()
        
        if read == "終了":
            event = "終了"

        if event in (None,"終了"):
            system.close()
            break

       
        if bool(values["in"])==True:
            name = os.path.split(values["in"])[1]
            list[f"{name}"]=values["in"]
            window["in"].update("")
            window["list"].update(values = list)
        
        if event =="list":
            
            window["out"].update(list[window["list"].get()[0]])
    
        if event == "OK":
            subprocess.Popen(["start",list[window["list"].get()[0]]],shell=True)

        #ビデオキャプチャするコード
        #ret,frame = cap.read()
        #ing = cv2.imencode(".png",frame)[1].tobytes()
        #window["img"].update(data=ing)
        

    except:
        pass