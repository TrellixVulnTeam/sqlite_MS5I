
from tkinter import Event
from tkinter.constants import FALSE
import PySimpleGUI as sg
from plyer import notification
import time
from psgtray import SystemTray
import re
#画面がぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


settings = sg.UserSettings()
settings.load()



demo_layout = [[sg.Text("テスト"),sg.InputText()]]

def coll():
    #保存完了を通知
    notification.notify(
        title = "通知",
        message = "保存完了です",
        app_name = "アプリネーム",
        app_icon = "不具合.ico",
        timeout = None)



lay = [
    [sg.Menu([["メニュー",["上書き保存"]],
             ["追加",["タスクを追加","aaa","seting","values"]],])],
             
    [sg.pin(sg.Column(layout=

    [],key="col",vertical_scroll_only=True,scrollable=True,size=(580,200)))],


]







window = sg.Window("タスク管理",layout=lay,enable_close_attempted_event=True,finalize=True,use_custom_titlebar=True,keep_on_top=True,grab_anywhere=True)

menu = ['', ['メニュー',["上書き保存"],"追加",["タスクを追加","aaa","seting","values"]]]
tray = SystemTray(menu=menu,tooltip="タスク管理",single_click_events=False,window=window)


count = 1#settings["count"]
while True :
    event, values = window.read()
    #for i in vs_settings_list:
        #if settings[i] == False:
            #window[i].hide_row()

    def count():
        window.refresh()
        ok_list=[]
        ng_list=[]
        all_list=[]
        
        value_key = values.keys()
        for i in value_key:
            all_list.append(i)

        for i in all_list:
            if bool(re.search("input_",str(i))) == True:
                ok_list.append(i)
            elif bool(re.search("input_",str(i))) == False:
                ng_list.append(i)
        return int(len(ok_list)) #GUI上の要素の数
    
    if event == sg.WIN_X_EVENT:
        break
    
    #システムトレイのメニューコマンドを使えるようにする記述
    if event == tray.key:
            event = values[event] 

    if event == None:
        print(event)
        break

    
    if event == "seting":
        print(settings)
        

    if event == "上書き保存":
        coll()
<<<<<<< HEAD:kesu_2 ver_2.py

    if event == "values":
        print(values)
    if event == "タスクを追加":
        print(count())
        try:
            window.extend_layout(window["col"],[([sg.Text(f"No.{count()}",key=f"No._{count()}"),sg.InputText(default_text=settings[f"contents_{count()}"],key=f"input_{count()}"),sg.Button("完了",key=f"ok_{count()}")])])
            #countの値をユーザー設定に追加
            settings["count"] = count()
            settings[f"input_{count()}"] = True
            settings[f"ok_{count()}"] = True
            settings[f"No._{count()}"] = True
            count += 1
            #下記の一文を追加しないと更新されずスクロールバーが機能しない
            window["col"].contents_changed()
        except:
            pass
        
    if event == "aaa":
        print(count())
    



    if bool(re.search("ok_*",event)) == True:
        no = re.split("ok_",event)[1]
        [window[f"{i}{no}"].hide_row() for i in ["input_","ok_","No._"]]
        settings[f"input_{no}"] = False
        settings[f"ok_{no}"] = False
        settings[f"No._{no}"] = False
        settings.delete_entry(f"input_{no}")
        settings.delete_entry(f"ok_{no}")
        settings.delete_entry(f"No._{no}")
        settings["count"] = count()
        del values[f"input_{no}"]
        window.visibility_changed()
        window["col"].contents_changed()
        
        
=======
    try:

        if event == "タスクを追加":
            window.extend_layout(window["col"],[([sg.Text(f"No.{count}",key=f"No._{count}"),sg.InputText(default_text=settings[f"contents_{count}"],key=f"input_{count}"),sg.Button("完了",key=f"ok_{count}")])])
            #countの値をユーザー設定に追加
            settings["count"] = count
            settings[f"input_{count}"] = True
            settings[f"ok_{count}"] = True
            settings[f"No._{count}"] = True
            count += 1
            #下記の一文を追加しないと更新されずスクロールバーが機能しない
            window["col"].contents_changed()
    except:
        pass    
        
    if event == "aaa":
       print(values)
       print(window["col"].get_size())
    try:

        if bool(re.search("ok_*",event)) == True:
            no = re.split("ok_",event)[1]
            [window[f"{i}{no}"].hide_row() for i in ["input_","ok_","No._"]]
            settings[f"input_{no}"] = False
            settings[f"ok_{no}"] = False
            settings[f"No._{no}"] = False
            count -= 1
            window["col"].contents_changed()
    except:
        pass   
>>>>>>> e8d4b13ec01b04d82063bc2aac52573b618db806:kesu_2_ver_2.py

    #print(event)
    #print(bool(re.search("ok_*",event)))