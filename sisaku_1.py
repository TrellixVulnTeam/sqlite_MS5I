import PySimpleGUI as sg
import os
import test_sginsert

lay = [
    [sg.InputText(key="in"),sg.FileBrowse()],
    [sg.Button("データ取り込み",key="insert"),sg.Button("更新",key="update"),sg.Button("得る",key="get")],
    [sg.Table(values=test_sginsert.select_act(),headings=test_sginsert.colum_name(),auto_size_columns=False,
    def_col_width=30,key="table")]
]

window = sg.Window("test", lay)

while True:
    event, values = window.read()

    if event == None:
        break
    
    if event == "insert":
        if values["in"] == "":
            sg.popup("データを選択してください")
            continue
        else:

            test_sginsert.insert_act(os.path.basename(os.path.splitext(values["in"])[0]))
            window["table"].update(values=test_sginsert.select_act())
    if event == "update":
        window["table"].update(values=test_sginsert.select_act())

    if event == "get":
        x = window["table"].get()
        print(x)