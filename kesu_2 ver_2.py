
from ntpath import join
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button, Checkbox, In, Input, Text, Tree, pin
from plyer import notification
import time

open_layout_file = open("layout.txt","r")
read_layout_file = open_layout_file.read()
open_layout_file.close()

ck_settings_list = ['ck_1', 'ck_2', 'ck_3', 'ck_4', 'ck_5', 'ck_6', 'ck_7', 'ck_8', 'ck_9', 'ck_10', 'ck_11', 'ck_12', 'ck_13', 'ck_14', 'ck_15', 'ck_16', 'ck_17', 'ck_18', 'ck_19', 'ck_20']
in_settings_list = ['in_1', 'in_2', 'in_3', 'in_4', 'in_5', 'in_6', 'in_7', 'in_8', 'in_9', 'in_10', 'in_11', 'in_12', 'in_13', 'in_14', 'in_15', 'in_16', 'in_17', 'in_18', 'in_19', 'in_20']
vs_settings_list = ['vs_1', 'vs_2', 'vs_3', 'vs_4', 'vs_5', 'vs_6', 'vs_7', 'vs_8', 'vs_9', 'vs_10', 'vs_11', 'vs_12', 'vs_13', 'vs_14', 'vs_15', 'vs_16', 'vs_17', 'vs_18', 'vs_19', 'vs_20']
bt_settings_list = ['bt_1', 'bt_2', 'bt_3', 'bt_4', 'bt_5', 'bt_6', 'bt_7', 'bt_8', 'bt_9', 'bt_10', 'bt_11', 'bt_12', 'bt_13', 'bt_14', 'bt_15', 'bt_16', 'bt_17', 'bt_18', 'bt_19', 'bt_20']

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
             ["追加",["タスクを追加","aaa","seting"]],])],
    [sg.Column(layout=

    [],key="col")],


]

print(lay)





window = sg.Window("test",layout=lay,enable_close_attempted_event=True,icon="不具合.ico",finalize=True)


count = 0
while True :
    event, values = window.read()
    #for i in vs_settings_list:
        #if settings[i] == False:
            #window[i].hide_row()
    
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

    
    if event == "seting":
        print(lay)

    if event == "上書き保存":
        for ck, iin in zip(ck_settings_list,in_settings_list):
            settings[ck] = values[ck]
            settings[iin] = values[iin]
       
        coll()
    if event == "タスクを追加":
        window.extend_layout(window["col"],[[sg.Text("テスト"),sg.InputText(key=f"input_{count}")]])
        count += 1
        settings.save()
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
        for iii in kk:
            print(values[iii])

        print(uu)
        print(kk)
        print(mm)
        print(ff)
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
        
        #window[res_now_list].update(visible=True)
        #window[mes_now_list].update(visible=True)
        #window[fes_now_list].update(visible=True)
        
        
        
        settings[res_now_list] = False
        print(res_now_list)
        window[res_now_list].update("")
        window[res_now_list].unhide_row()
    
    
    
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
