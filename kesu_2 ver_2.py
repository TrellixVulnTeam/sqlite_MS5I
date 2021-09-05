
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


settings = sg.UserSettings(autosave=True)
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
             ["追加",["タスクを追加","aaa","seting"]],])],
             
    [sg.pin(sg.Column(layout=

    [],key="col",vertical_scroll_only=True,scrollable=True,size=(580,200)))],


]







window = sg.Window("タスク管理",layout=lay,enable_close_attempted_event=True,finalize=True,use_custom_titlebar=True,keep_on_top=True,grab_anywhere=True)

menu = ['', ['メニュー',["上書き保存"],"追加",["タスクを追加","aaa","seting"]]]
tray = SystemTray(menu=menu,tooltip="タスク管理",single_click_events=False,window=window)



count = 1
while True :
    event, values = window.read()
    #for i in vs_settings_list:
        #if settings[i] == False:
            #window[i].hide_row()
    
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
    if event == "タスクを追加":
        settings[f"input{count}"] = ""
        window.extend_layout(window["col"],[([sg.Text(f"No.{count}",key=f"No._{count}"),sg.InputText(default_text=settings[f"input_{count}"],key=f"input_{count}"),sg.Button("完了",key=f"ok_{count}")])])
        #countの値をユーザー設定に追加
        settings["count"] = count
        count += 1
        #下記の一文を追加しないと更新されずスクロールバーが機能しない
        window["col"].contents_changed()
        
        
    if event == "aaa":
       print(values)

    if bool(re.search("ok_*",event)) == True:
        no = re.split("ok_",event)[1]
        [window[f"{i}{no}"].hide_row() for i in ["input_","ok_","No._"]]
        settings[f"input_{no}"] = False
        settings[f"ok_{no}"] = False
        settings[f"No._{no}"] = False
        window["col"].contents_changed()
        

    #print(event)
    #print(bool(re.search("ok_*",event)))