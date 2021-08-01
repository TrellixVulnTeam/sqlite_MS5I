import PySimpleGUI as sg
import os
import test_sginsert

lay = [
    [sg.InputText(key="in"),sg.FileBrowse()],
    [sg.Button("データ取り込み",key="insert"),sg.Button("更新",key="update"),sg.Button("削除",key="del"),sg.InputText(key="file_out")],
    [sg.Table(values=test_sginsert.select_act(),headings=test_sginsert.colum_name(),auto_size_columns=False,
    def_col_width=30,key="table",enable_events=True,justification="left")]
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

    if event == "table":
        x = window["table"].get()
        file_name = x[values["table"][0]][1]
        window["file_out"].update(file_name)

    if event  == "del":
        if values["table"] == []:
            continue
        else:

            x = window["table"].get()
            file_name = x[values["table"][0]]
            f_1 = file_name[1]
            f_2 = file_name[1]
            test_sginsert.del_act(f_1)
            window["table"].update(values=test_sginsert.select_act())
        
   