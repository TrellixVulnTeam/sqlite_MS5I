import PySimpleGUI as sg
import os
import test_sginsert

lay = [
    [sg.InputText(key="in"),sg.FileBrowse()],
    [sg.Button("データ取り込み",key="insert")],
    [sg.Table(values=test_sginsert.select_act(),headings=test_sginsert.colum_name(),auto_size_columns=True)]
]

window = sg.Window("test", lay)

while True:
    event, values = window.read()

    if event == None:
        break
    
    if event == "insert":
        test_sginsert.insert_act(os.path.basename(os.path.splitext(values["in"])[0]))