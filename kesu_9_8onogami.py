import PySimpleGUIQt as sg
import os
import subprocess
from PySimpleGUIQt.PySimpleGUIQt import TRANSPARENT_BUTTON

system = sg.SystemTray(menu=["",["メニュー",["OK","b"],"終了"]])
system.show_message("python","test")

lay = [
    [sg.Multiline(key="in",enable_events=True)],
    [sg.Listbox(values=[],key="list",enable_events=True,)],
    [sg.Output(key="out")],
    [sg.OK()]
]



window = sg.Window("",lay,finalize=True)
list = {}


while True:
    event,values = window.read()
    try:

        if event == None:
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

    except:
        pass