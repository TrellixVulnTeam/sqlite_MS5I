import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Image, Window
from plyer import notification
import time
def coll():
    #保存完了を通知
    notification.notify(
        title = "通知",
        message = "保存完了です",
        app_name = "アプリネーム",
        app_icon = None,
        timeout = None)

settings = sg.UserSettings()
settings.load()
lay = [
    [sg.Menu([["メニュー",["上書き保存"]]])],
    [sg.Checkbox("",default=settings["check"],key="ck_1"),sg.Multiline(default_text=settings["file_name"],key="in",size=(40,1))],
    [sg.Multiline(size=(40,1))]

]

window = sg.Window("test",lay,enable_close_attempted_event=True)

while True :
    event, values = window.read()
    if event == sg.WIN_X_EVENT:
        if  sg.popup_ok_cancel("変更を保存しますか？",) == "OK":
            settings["file_name"] = values["in"]
            settings["check"] = values["ck_1"]
            if sg.popup_ok_cancel("ウィンドウを閉じますか？") == "OK":
                break
            else:
                continue
            
            
        elif event == "-WINDOW CLOSE ATTEMPTED-":
            if sg.popup_ok_cancel("ウィンドウを閉じますか？") == "OK":
                break
            else:
                continue
    
    if event == None:
        print(event)
        break


    if event == "上書き保存":
        settings["file_name"] = values["in"]
        settings["check"] = values["ck_1"]
        coll()
        


    
    
        

