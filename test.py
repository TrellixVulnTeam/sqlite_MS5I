from sys import winver
import PySimpleGUI as sg

#画面がぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

settings = sg.UserSettings()
settings.load()

lay =[
    [sg.Listbox(values=["aaaaaaaaaaaaaaaaaaaaa","bbbbbbbbbbbbbbbbb","1","2","3","4","5","6","7","8","9","10"],auto_size_text=False,size=(30,10))]
]

window = sg.Window("タスク管理",lay)

while True:
    event,values = window.read()

    if event in (None):
        break