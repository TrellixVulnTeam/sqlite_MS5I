from tkinter.constants import FALSE, X
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import TRANSPARENT_BUTTON, InputText

settings = sg.UserSettings()
settings.load()

def insert ():
    x =[sg.InputText(),sg.Button("ok")],
    return x

lay = [[ [sg.Button("ok" )]]]

window = sg.Window("",lay,finalize=True)
while True:
    event , values = window.read(timeout=1000)
    if event == None:
        break
    print(event)
    print(values)
    if event == "ok":
        window[0].update(visible = True)
    elif event == "ok1":
        window[1].update(visible = True)
    elif event == "ok2":
        window[2].update(visible = True)
    elif event == "ok3":
        window[3].update(visible = True)

    if event == "015":
        window[0].update(visible = False)
    elif event == "116":
        window[1].update(visible = False)
    elif event == "217":
        window[2].update(visible = False)
    elif event == "318":
        window[3].update(visible = False)

    if event == "ok14":
        sg.cprint

    print(event)
    if event == "__TIMEOUT__":
        window.add_row(insert())
