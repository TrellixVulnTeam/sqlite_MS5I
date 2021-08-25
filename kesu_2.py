import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

settings = sg.UserSettings()
settings.load()
lay = [
    [sg.Menu([["メニュー",["上書き保存"]]])],
    [sg.Checkbox(""),sg.Multiline(default_text=settings["file_name"],key="in",size=(40,1))],
    [sg.Multiline(size=(40,1))]

]

window = sg.Window("test",lay,enable_close_attempted_event=True)

while True :
    event, values = window.read()
    if event == sg.WIN_X_EVENT:
        if  sg.popup_yes_no("変更を保存しますか？") == "Yes":
            settings["file_name"] = values["in"]
            print(values)
            break
        else:
            break
    if event == None:
        print(values)
        break
    if event == "上書き保存":
        settings["file_name"] = values["in"]
        

window.close()
    
    
        

