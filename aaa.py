import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


name = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
day_name = ["日","月","火","水","木","金","土"]
lay = [
    [sg.CalendarButton("日付選択",month_names=name,day_abbreviations=day_name,auto_size_button=True),sg.InputText()]
]

window = sg.Window("",lay).read()