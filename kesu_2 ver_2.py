
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, Checkbox, In, Text, Tree, pin
from plyer import notification
import time

ck_settings_list = ['ck_1', 'ck_2', 'ck_3', 'ck_4', 'ck_5', 'ck_6', 'ck_7', 'ck_8', 'ck_9', 'ck_10', 'ck_11', 'ck_12', 'ck_13', 'ck_14', 'ck_15', 'ck_16', 'ck_17', 'ck_18', 'ck_19', 'ck_20']
in_settings_list = ['in_1', 'in_2', 'in_3', 'in_4', 'in_5', 'in_6', 'in_7', 'in_8', 'in_9', 'in_10', 'in_11', 'in_12', 'in_13', 'in_14', 'in_15', 'in_16', 'in_17', 'in_18', 'in_19', 'in_20']
vs_settings_list = ['vs_1', 'vs_2', 'vs_3', 'vs_4', 'vs_5', 'vs_6', 'vs_7', 'vs_8', 'vs_9', 'vs_10', 'vs_11', 'vs_12', 'vs_13', 'vs_14', 'vs_15', 'vs_16', 'vs_17', 'vs_18', 'vs_19', 'vs_20']
bt_settings_list = ['bt_1', 'bt_2', 'bt_3', 'bt_4', 'bt_5', 'bt_6', 'bt_7', 'bt_8', 'bt_9', 'bt_10', 'bt_11', 'bt_12', 'bt_13', 'bt_14', 'bt_15', 'bt_16', 'bt_17', 'bt_18', 'bt_19', 'bt_20']

settings = sg.UserSettings()
settings.load()


def coll():
    #保存完了を通知
    notification.notify(
        title = "通知",
        message = "保存完了です",
        app_name = "アプリネーム",
        app_icon = "不具合.ico",
        timeout = None)

def search_vs_list():
    test_list ={}
    for i in vs_settings_list:
        test_list[i] = settings[i]

    return test_list



def search_in_list():
    test_list = {}
    for i in in_settings_list:
        test_list[i] = settings[i]

    return test_list

def search_bt_list():
    test_list = {}
    for i in bt_settings_list:
        test_list[i] = settings[i]

    return test_list



lay = [
    [sg.Menu([["メニュー",["上書き保存"]],
             ["追加",["タスクを追加","aaa"]],])],
    [sg.Column(layout=

    [[sg.Checkbox("",default=settings["ck_1"],key="ck_1",visible=settings["vs_1"]),sg.In(default_text=settings["in_1"],key="in_1",size=(40,0.5),visible=settings["vs_1"]),sg.Button("完了",key="bt_1",visible=settings["vs_1"])],
    [sg.Checkbox("",default=settings["ck_2"],key="ck_2",visible=settings["vs_2"]),sg.In(default_text=settings["in_2"],key="in_2",size=(40,0.5),visible=settings["vs_2"]),sg.Button("完了",key="bt_2",visible=settings["vs_2"])],
    [sg.Checkbox("",default=settings["ck_3"],key="ck_3",visible=settings["vs_3"]),sg.In(default_text=settings["in_3"],key="in_3",size=(40,0.5),visible=settings["vs_3"]),sg.Button("完了",key="bt_3",visible=settings["vs_3"])],
    [sg.Checkbox("",default=settings["ck_4"],key="ck_4",visible=settings["vs_4"]),sg.In(default_text=settings["in_4"],key="in_4",size=(40,0.5),visible=settings["vs_4"]),sg.Button("完了",key="bt_4",visible=settings["vs_4"])],
    [sg.Checkbox("",default=settings["ck_5"],key="ck_5",visible=settings["vs_5"]),sg.In(default_text=settings["in_5"],key="in_5",size=(40,0.5),visible=settings["vs_5"]),sg.Button("完了",key="bt_5",visible=settings["vs_5"])],
    [sg.Checkbox("",default=settings["ck_6"],key="ck_6",visible=settings["vs_6"]),sg.In(default_text=settings["in_6"],key="in_6",size=(40,0.5),visible=settings["vs_6"]),sg.Button("完了",key="bt_6",visible=settings["vs_6"])],
    [sg.Checkbox("",default=settings["ck_7"],key="ck_7",visible=settings["vs_7"]),sg.In(default_text=settings["in_7"],key="in_7",size=(40,0.5),visible=settings["vs_7"]),sg.Button("完了",key="bt_7",visible=settings["vs_7"])],
    [sg.Checkbox("",default=settings["ck_8"],key="ck_8",visible=settings["vs_8"]),sg.In(default_text=settings["in_8"],key="in_8",size=(40,0.5),visible=settings["vs_8"]),sg.Button("完了",key="bt_8",visible=settings["vs_8"])],
    [sg.Checkbox("",default=settings["ck_9"],key="ck_9",visible=settings["vs_9"]),sg.In(default_text=settings["in_9"],key="in_9",size=(40,0.5),visible=settings["vs_9"]),sg.Button("完了",key="bt_9",visible=settings["vs_9"])],
    [sg.Checkbox("",default=settings["ck_10"],key="ck_10",visible=settings["vs_10"]),sg.In(default_text=settings["in_10"],key="in_10",size=(40,0.5),visible=settings["vs_10"]),sg.Button("完了",key="bt_10",visible=settings["vs_10"])],
    [sg.Checkbox("",default=settings["ck_11"],key="ck_11",visible=settings["vs_11"]),sg.In(default_text=settings["in_11"],key="in_11",size=(40,0.5),visible=settings["vs_11"]),sg.Button("完了",key="bt_11",visible=settings["vs_11"])],
    [sg.Checkbox("",default=settings["ck_12"],key="ck_12",visible=settings["vs_12"]),sg.In(default_text=settings["in_12"],key="in_12",size=(40,0.5),visible=settings["vs_12"]),sg.Button("完了",key="bt_12",visible=settings["vs_12"])],
    [sg.Checkbox("",default=settings["ck_13"],key="ck_13",visible=settings["vs_13"]),sg.In(default_text=settings["in_13"],key="in_13",size=(40,0.5),visible=settings["vs_13"]),sg.Button("完了",key="bt_13",visible=settings["vs_13"])],
    [sg.Checkbox("",default=settings["ck_14"],key="ck_14",visible=settings["vs_14"]),sg.In(default_text=settings["in_14"],key="in_14",size=(40,0.5),visible=settings["vs_14"]),sg.Button("完了",key="bt_14",visible=settings["vs_14"])],
    [sg.Checkbox("",default=settings["ck_15"],key="ck_15",visible=settings["vs_15"]),sg.In(default_text=settings["in_15"],key="in_15",size=(40,0.5),visible=settings["vs_15"]),sg.Button("完了",key="bt_15",visible=settings["vs_15"])],
    [sg.Checkbox("",default=settings["ck_16"],key="ck_16",visible=settings["vs_16"]),sg.In(default_text=settings["in_16"],key="in_16",size=(40,0.5),visible=settings["vs_16"]),sg.Button("完了",key="bt_16",visible=settings["vs_16"])],
    [sg.Checkbox("",default=settings["ck_17"],key="ck_17",visible=settings["vs_17"]),sg.In(default_text=settings["in_17"],key="in_17",size=(40,0.5),visible=settings["vs_17"]),sg.Button("完了",key="bt_17",visible=settings["vs_17"])],
    [sg.Checkbox("",default=settings["ck_18"],key="ck_18",visible=settings["vs_18"]),sg.In(default_text=settings["in_18"],key="in_18",size=(40,0.5),visible=settings["vs_18"]),sg.Button("完了",key="bt_18",visible=settings["vs_18"])],
    [sg.Checkbox("",default=settings["ck_19"],key="ck_19",visible=settings["vs_19"]),sg.In(default_text=settings["in_19"],key="in_19",size=(40,0.5),visible=settings["vs_19"]),sg.Button("完了",key="bt_19",visible=settings["vs_19"])],
    [sg.Checkbox("",default=settings["ck_20"],key="ck_20",visible=settings["vs_20"]),sg.In(default_text=settings["in_20"],key="in_20",size=(40,0.5),visible=settings["vs_20"]),sg.Button("完了",key="bt_20",visible=settings["vs_20"])],
    ])],

    
  
    [sg.Button("",image_data="",key="bt",button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0)],

]





window = sg.Window("test",layout=lay,enable_close_attempted_event=True,icon="不具合.ico",finalize=True)



while True :
    event, values = window.read(timeout=1000)
    
    if event == sg.WIN_X_EVENT:
        if  sg.popup_ok_cancel("変更を保存しますか？",) == "OK":
            for ck, iin in zip(ck_settings_list,in_settings_list):
                settings[ck] = values[ck]
                settings[iin] = values[iin]
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
        for ck, iin in zip(ck_settings_list,in_settings_list):
            settings[ck] = values[ck]
            settings[iin] = values[iin]
       
        coll()
    if event == "タスクを追加":
        print(search_bt_list())
        
    if event == "aaa":
        #ck_key
        res = {}
        #vs_key
        tes = {}
        #in_key
        mes = {}
        #bt_key
        fes = {}

        uu = search_vs_list()
        kk = ck_settings_list
        mm = search_in_list()
        ff = search_bt_list()
        for i,n in zip(uu,kk):
         if  settings[i] == False:
              res[n] = settings[i]
              tes[i] = settings[i]

        for i,n in zip(uu,mm):
            if settings[i] == False:
                mes[n] = settings[i]

        for i,n in zip(uu,ff):
            if settings[i] == False:
                fes[n] = settings[i]

        res_now_list = next(iter(res))
        tes_now_list = next(iter(tes))
        mes_now_list = next(iter(mes))
        fes_now_list = next(iter(fes))

        settings[tes_now_list] = True
        
        window[res_now_list].update(visible=True)
        window[mes_now_list].update(visible=True)
        #window[fes_now_list].update(visible=True)
        
        
        
        #settings[res_now_list] = False
        
        window[res_now_list].update("")
        
    
    
    
    #完了ボタンが押された時の処理
    if event == "bt_1":
        if values["ck_1"] == True:
            window["ck_1"].hide_row()
            settings["vs_1"] = False
        elif values["ck_1"] == False:
            pass

    elif event == "bt_2":
        if values["ck_2"] == True:
            window["ck_2"].hide_row()
            settings["vs_2"] = False
        elif values["ck_2"] == False:
            pass
    
    elif event == "bt_3":
        if values["ck_3"] == True:
            window["ck_3"].hide_row()
            settings["vs_3"] = False
        elif values["ck_3"] == False:
            pass
        
    elif event == "bt_4":
        if values["ck_4"] == True:
            window["ck_4"].hide_row()
            settings["vs_4"] = False
        elif values["ck_4"] == False:
            pass

    elif event == "bt_5":
        if values["ck_5"] == True:
            window["ck_5"].hide_row()
            settings["vs_5"] = False
        elif values["ck_5"] == False:
            pass
    
    elif event == "bt_6":
        if values["ck_6"] == True:
            window["ck_6"].hide_row()
            settings["vs_6"] = False
        elif values["ck_6"] == False:
            pass
    
    elif event == "bt_7":
        if values["ck_7"] == True:
            window["ck_7"].hide_row()
            settings["vs_7"] = False
        elif values["ck_7"] == False:
            pass
    
    elif event == "bt_8":
        if values["ck_8"] == True:
            window["ck_8"].hide_row()
            settings["vs_8"] = False
        elif values["ck_8"] == False:
            pass

    elif event == "bt_9":
        if values["ck_9"] == True:
            window["ck_9"].hide_row()
            settings["vs_9"] = False
        elif values["ck_9"] == False:
            pass

    elif event == "bt_10":
        if values["ck_10"] == True:
            window["ck_10"].hide_row()
            settings["vs_10"] = False
        elif values["ck_10"] == False:
            pass
    
    elif event == "bt_11":
        if values["ck_11"] == True:
            window["ck_11"].hide_row()
            settings["vs_11"] = False
        elif values["ck_11"] == False:
            pass
    
    elif event == "bt_12":
        if values["ck_12"] == True:
            window["ck_12"].hide_row()
            settings["vs_12"] = False
        elif values["ck_12"] == False:
            pass

    elif event == "bt_13":
        if values["ck_13"] == True:
            window["ck_13"].hide_row()
            settings["vs_13"] = False
        elif values["ck_13"] == False:
            pass
    
    elif event == "bt_14":
        if values["ck_14"] == True:
            window["ck_14"].hide_row()
            settings["vs_14"] = False
        elif values["ck_14"] == False:
            pass


    elif event == "bt_15":
        if values["ck_15"] == True:
            window["ck_15"].hide_row()
            settings["vs_15"] = False
        elif values["ck_15"] == False:
            pass

    elif event == "bt_16":
        if values["ck_16"] == True:
            window["ck_16"].hide_row()
            settings["vs_16"] = False
        elif values["ck_16"] == False:
            pass
    
    elif event == "bt_17":
        if values["ck_17"] == True:
            window["ck_17"].hide_row()
            settings["vs_17"] = False
        elif values["ck_17"] == False:
            pass

    elif event == "bt_18":
        if values["ck_18"] == True:
            window["ck_18"].hide_row()
            settings["vs_18"] = False
        elif values["ck_18"] == False:
            pass

    elif event == "bt_19":
        if values["ck_19"] == True:
            window["ck_19"].hide_row()
            settings["vs_19"] = False
        elif values["ck_19"] == False:
            pass

    elif event == "bt_20":
        if values["ck_20"] == True:
            window["ck_20"].hide_row()
            settings["vs_20"] = False
        elif values["ck_20"] == False:
            pass
    

    if event == "__TIMEOUT__":
        window.refresh()