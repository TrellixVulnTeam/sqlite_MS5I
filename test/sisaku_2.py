import PySimpleGUI as sg
import os

from PySimpleGUI.PySimpleGUI import InputText
import test_sginsert_2

lay = [
    
    [sg.Button("更新",key="update"),sg.Button("削除",key="del"),sg.Button("追加",key="insert"),sg.InputText(key="file_out")],
    [sg.Table(values=test_sginsert_2.select_act(),headings=test_sginsert_2.colum_name(),auto_size_columns=False,
    def_col_width=30,key="table",enable_events=True,justification="left")]
]

window = sg.Window("test", lay)

while True:
    event, values = window.read()

    if event == None:
        break
    
    if event == "insert":
        file_name = sg.popup_get_text("追加する名称を入力して下さい")
        path_name = sg.popup_get_text("追加するpathを入力して下さい")
        if bool(file_name or path_name) != "" or None:
            sg.popup("入力がありません")
            continue
        else:

            test_sginsert_2.insert_act(file_name,path_name)
            window["table"].update(values=test_sginsert_2.select_act())
            print(bool(file_name))
            print(bool(path_name))
        


    if event == "table":
        x = window["table"].get()
        filepath_name = x[values["table"][0]][1]
        dir_name = x[values["table"][0]][0]
        window["file_out"].update(filepath_name)
        
    if event == "update":
        if values["table"] == []:
            sg.popup_error("テーブルを選択して下さい")
            continue
        if event == "Cancel":
            continue
        pw = sg.popup_get_text("パスワードを入力してください",password_char="*")
        if pw == "onogami27":
                
            path = sg.popup_get_text("変更するpathを入力してください")
            if path == None:
                continue
            if path == "":
                sg.popup_error("入力がありません")
                continue
            else:
                yes_or_no = sg.popup_yes_no("変更内容を更新しますか？")
                if yes_or_no == "No":
                    continue
                else:

                    test_sginsert_2.updete_act(path, dir_name)
                    window["table"].update(values=test_sginsert_2.select_act())
                    print(yes_or_no)

        else:
            sg.popup_error("パスワードが間違っています")
            continue    

    if event  == "del":
        if values["table"] == []:
            continue
        else:
            pw = sg.popup_get_text("パスワードを入力してください",password_char="*")
            if pw == "onogami27":
                
                yes_or_no = sg.popup_yes_no("選択した項目を削除しますか？")
                if yes_or_no == "No":
                    continue
                else:
                    x = window["table"].get()
                    file_name = x[values["table"][0]]
                    f_1 = file_name[1]
                    f_2 = file_name[0]
                    window["val"].update(f_2)
                    test_sginsert_2.del_act(f_2)
                    window["table"].update(values=test_sginsert_2.select_act())

            else:
                sg.popup_error("パスワードが間違っています")
                continue     
   