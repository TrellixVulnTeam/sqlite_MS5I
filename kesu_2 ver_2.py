
import PySimpleGUI as sg
from plyer import notification
import time

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
    [sg.Column(layout=

    [],key="col")],


]







window = sg.Window("test",layout=lay,enable_close_attempted_event=True,finalize=True,use_custom_titlebar=True,)


count = 1
while True :
    event, values = window.read()
    #for i in vs_settings_list:
        #if settings[i] == False:
            #window[i].hide_row()
    
    if event == sg.WIN_X_EVENT:
        break
    
    if event == None:
        print(event)
        break

    
    if event == "seting":
        print(settings)

    if event == "上書き保存":
        pass
    if event == "タスクを追加":
        window.extend_layout(window["col"],[[sg.Text(f"No.{count}"),sg.InputText(key=f"input_{count}"),sg.Button("完了",key=f"ok_{count}")]])
        count += 1
        
    if event == "aaa":
        pass
   