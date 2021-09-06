import PySimpleGUI as sg
import subprocess
import os
import glob
import re
import datetime
import shutil
from PySimpleGUI.PySimpleGUI import InputText

import pyperclip
import test_sginsert_2 as ts
import sisaku_2
from select_excel import select
from psgtray import SystemTray

#画面がぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

# coding: utf-8
#GUIテーマを設定
sg.theme("Default")
#Excel(2010)APPのファイルpath
excel_path = r"{0}".format(ts.path("Excel(2010)_path"))
#Acrobat(2010)APPのファイルpath
pdf_path = r"{0}".format(ts.path("Acrobat(2010)_path"))
#不具合指示書送付Excelファイルのpath
ex_souhu_path = r"{0}".format(ts.path("不具合指示書送付Excel"))
#金型修理履歴Excelファイルのpath
ex_lireki_path = r"{0}".format(ts.path("金型修理履歴Excel"))
#手配No.管理表Excelファイルのpath
ex_kanri_path = r"{0}".format(ts.path("手配No.管理表Excel"))
#フォルダpath(辞書型)
file_list = {"home":r"{0}".format(ts.path("コメントあり")),
             "shusa":r"{0}".format(ts.path("岩田主査確認")),
             "butho_mae":r"{0}".format(ts.path("部長(確認前)")),
             "butho_go":r"{0}".format(ts.path("部長(確認済み)")),
             "tantou":r"{0}".format(ts.path("担当者確認")),
             "souhu":r"{0}".format(ts.path("指示書送付フォルダ"))}

#grabでフォルダの中のファイルを検出
def main(name):
    #*[(（]と記載する事で()の大文字と小文字両方引っかけれる
    
    uu_no = []
    uuu_yes = []
    x = glob.glob("{}/*-*[(（)）]*[.xlsx.xls.pdf]?".format(file_list[name]))
    for ii in x:
        if re.search("[~$]", ii): #re.search("[~$]")で~$を含むファイルを抽出している
            uu_no.append(ii)
        else:
            uuu_yes.append(ii)
    return uuu_yes
    
#出力窓に結果を表示させる
def display():
    uu_1 = []
    for i in main("home"):
        y = os.path.split(i)[1]
        uu_1.append(y)
    window_1["out_1"].update(uu_1)
    window_1["in_1"].update(len(main("home")))

    uu_2 = []  
    for i in main("shusa"):
        y = os.path.split(i)[1]
        uu_2.append(y)
    window_1["out_2"].update(uu_2)
    window_1["in_2"].update(len(main("shusa")))

    uu_3 = []
    for i in main("butho_mae"):
        y = os.path.split(i)[1]
        uu_3.append(y)
    window_1["out_3"].update(uu_3)
    window_1["in_3"].update(len(main("butho_mae")))

    uu_4 = []
    for i in main("butho_go"):
        y = os.path.split(i)[1]
        uu_4.append(y)
    window_1["out_4"].update(uu_4)
    window_1["in_4"].update(len(main("butho_go")))
    
    uu_5 = []
    for i in main("tantou"):
        y = os.path.split(i)[1]
        uu_5.append(y)
    window_1["out_5"].update(uu_5)
    window_1["in_5"].update(len(main("tantou")))

#更新時刻を表示する
def now_time():
    d = datetime.datetime.now()
    return "{0:%Y年%m月%d日 %H時%M分%S秒}".format(d)

#画面の表示を消す
def clear():
    window_1["out_1"].update("")
    window_1["out_2"].update("")
    window_1["out_3"].update("")
    window_1["out_4"].update("")
    window_1["out_5"].update("")
    window_1["out_time"].update("")
    

#実行ループ
def roop():
    display()
    window_1["out_time"].update(now_time())

#ポップアップウィンドウ
def second_window(name):
    lay = [[sg.Text("送り先を選択して下さい", text_color="red")],
           [sg.Radio(text="コメント有り",group_id="A",key="pop_r1",enable_events=True)],
           [sg.Radio(text="岩田主査確認",group_id="A",key="pop_r2",enable_events=True)],
           [sg.Radio(text="担当者確認",group_id="A",key="pop_r5",enable_events=True),sg.Radio(text="指示書送付", group_id="A", key="pop_r6", enable_events=True, pad=((30,0),(0,0)))],
           [sg.Radio(text="部長(確認前)",group_id="A",key="pop_r3",enable_events=True)],
           [sg.Radio(text="部長(確認済み)",group_id="A",key="pop_r4",enable_events=True)],
           [sg.Button(button_text="OK",key="pop_ok"), sg.Button(button_text="キャンセル",key="pop_cancel")]]

    window =  sg.Window("送り先選択",layout=lay, modal=True, size= (255, 230),
                      keep_on_top=True, finalize=True)#modal = Trueでホップアップウィンドウしか操作できない様固定
    
    #自らの送り先をリストから消す
    if name == "home":
                window["pop_r1"].update(disabled =True)
                window["pop_r6"].update(disabled =True)
    if name == "shusa":
                window["pop_r2"].update(disabled =True)
                window["pop_r6"].update(disabled =True)
    if name == "butho_mae":
                window["pop_r3"].update(disabled =True)
                window["pop_r6"].update(disabled =True)
    if name == "butho_go":
                window["pop_r4"].update(disabled =True)
    if name == "tantou":
                window["pop_r5"].update(disabled =True)
                window["pop_r6"].update(disabled =True)
    keys = []

    
    while True:
        event, values = window.read()
        if event == "pop_ok":
            #ラジオボタンで選択されたkeyを戻り値として返す
            keys = [k for k, v in values.items() if v == True]
            break
        if event in (None, sg.WIN_CLOSED,"pop_cancel"):
            break
            
    window.close()
    
    return keys


#メインとなるウィンドウ
def main_1_window():

        
    lay_1 =sg.Frame(title="コメント有り" ,layout=[[sg.Text("ファイル数"),sg.InputText("", key="in_1",size=(4, 1)),sg.Button("フォルダを開く", key="open_start_1", pad=((50,0), (0,0)))],
        [sg.Radio(text="開く", group_id="A",key="r1_open",enable_events=True), sg.Radio(text="送る", group_id="A",key="r1_send",enable_events=True),sg.Radio(text="詳細",default=True,group_id="A",key="r1_detail",enable_events=True),sg.Button("クリア",key="ok_1",button_color="red"), sg.Checkbox(text="通知あり",default=True,key="ckb_1",enable_events=True,pad=((0,0),(0,0)))],
        [sg.Listbox(values=main("home"),key="out_1",size=(45,15), background_color="#FFDBC9" ,enable_events=True)]],title_color="blue")

    lay_2 =sg.Frame(title="岩田主査確認" ,layout=[[sg.Text("ファイル数"),sg.InputText("", key="in_2",size=(4, 1)),sg.Button("フォルダを開く", key="open_start_2", pad=((50,0), (0,0)))],
        [sg.Radio(text="開く", group_id="B",key="r2_open",enable_events=True), sg.Radio(text="送る", group_id="B",key="r2_send",enable_events=True),sg.Radio(text="詳細",default=True,group_id="B",key="r2_detail",enable_events=True),sg.Button("クリア",key="ok_2",button_color="red"), sg.Checkbox(text="通知あり",default=True,key="ckb_2",enable_events=True,pad=((0,0),(0,0)))],
        [sg.Listbox(values=main("shusa"),key="out_2", size=(45,15), background_color="#CBFFD3",enable_events=True) ]],title_color="blue")

    lay_3 =sg.Frame(title="部長(確認前)" ,layout=[[sg.Text("ファイル数"),sg.InputText("", key="in_3",size=(4, 1)),sg.Button("フォルダを開く", key="open_start_3", pad=((50,0), (0,0)))],
        [sg.Radio(text="開く", group_id="C",key="r3_open",enable_events=True), sg.Radio(text="送る", group_id="C",key="r3_send",enable_events=True),sg.Radio(text="詳細",default=True,group_id="C",key="r3_detail",enable_events=True),sg.Button("クリア",key="ok_3",button_color="red"), sg.Checkbox(text="通知あり",default=True,key="ckb_3",enable_events=True,pad=((0,0),(0,0)))],
        [sg.Listbox(values=main("butho_mae"),key="out_3", size=(45,15), background_color="#EDFFBE",enable_events=True) ]],title_color="blue")

    lay_4 =sg.Frame(title="部長(確認済み)" ,layout=[[sg.Text("ファイル数"),sg.InputText("", key="in_4",size=(4, 1)),sg.Button("フォルダを開く", key="open_start_4", pad=((50,0), (0,0)))],
        [sg.Radio(text="開く", group_id="D",key="r4_open",enable_events=True), sg.Radio(text="送る", group_id="D",key="r4_send",enable_events=True),sg.Radio(text="詳細",default=True,group_id="D",key="r4_detail",enable_events=True),sg.Button("クリア",key="ok_4",button_color="red"), sg.Checkbox(text="通知あり",default=True,key="ckb_4",enable_events=True,pad=((0,0),(0,0)))],
    
        [sg.Listbox(values=main("butho_go"),key="out_4", size=(45,15), background_color="#DDDDDD", enable_events=True) ]],title_color="blue")

    lay_5 =sg.Frame(title="担当者確認" ,layout=[[sg.Text("ファイル数"),sg.InputText("", key="in_5",size=(4, 1)),sg.Button("フォルダを開く", key="open_start_5", pad=((50,0), (0,0)))],
        [sg.Radio(text="開く", group_id="E",key="r5_open",enable_events=True), sg.Radio(text="送る", group_id="E",key="r5_send",enable_events=True),sg.Radio(text="詳細",default=True,group_id="E",key="r5_detail",enable_events=True),sg.Button("クリア",key="ok_5",button_color="red"), sg.Checkbox(text="通知あり",default=True,key="ckb_5",enable_events=True,pad=((0,0),(0,0)))],
        [sg.Listbox(values=main("tantou"),key="out_5", size=(45,15), background_color="#B384FF", enable_events= True) ]],title_color="blue")

    lay_6 = sg.Frame(title="その他",layout=[[sg.Text("更新日時",text_color="red"), sg.InputText(size=(28,10), key="out_time")],
        [sg.Text("ファイル名",pad=((0,0),(0,0)),text_color="red"),sg.InputText(size=(35,10), key="list_out",right_click_menu=["",["コピー"]],pad=((10,0),(0,0)))],
        [sg.Text("品番",text_color="red"),sg.InputText(size=(20,10),key="hinban",right_click_menu=["",["コピー"]]),sg.Text("型番",text_color="red"),sg.InputText(size=(5,10),key="kataban")],
        [sg.Text("取数",text_color="red"),sg.InputText(size=(5,10),key="torisu"),sg.Text("月産数",text_color="red"),sg.InputText(size=(10,10),key="gesan")],
        [sg.Text("成形加工区",text_color="red"),sg.InputText(size=(20,10),key="kakouku")],
        [sg.Text("修理メーカー",text_color="red"),sg.InputText(size=(20,10),key="syuuri")],
        [sg.Text("開始日",text_color="red"),InputText(size=(20,10),key="kaishi")],
        [sg.Text("型納期",text_color="red"),InputText(size=(20,10),key="nouki")],
        [sg.Text("手配ナンバー",text_color="red"),InputText(size=(20,10),key="tehai_NO")],
        [sg.Text("ショットカウンタ",text_color="red"),InputText(size=(20,10),key="shot_count")]
        
        ],title_color="blue",)

    #GUIレイアウト　　[["設定",["PATHの設定"]],
    layout = [
    [sg.MenuBar([["メニュー",["指示書送付フォルダ","不具合指示書送付","金型修理履歴","手配No.管理表","ツチヒラ専用PDF変換"]],
                  ["設定",["PATHの設定"]]])],
    [[lay_1,lay_2,lay_5]],[[lay_3,lay_4,lay_6]
    ]]

    #ウィンドウの作成(タイトル、レイアウト、サイズ、画面リサイズ可、画面移動可)
    return sg.Window("不具合指示書確認", layout, size=(1100, 700), resizable=True, finalize= True, grab_anywhere=False,
            element_justification="left",icon=r"C:\Users\onoga\OneDrive\Desktop\MyDocker\woman-grayscale.jpg")

#ウィンドウを定義
window_1 = main_1_window() 

#システムトレイを定義
menu = ['', ['メニュー',["指示書送付フォルダ","不具合指示書送付","金型修理履歴","手配No.管理表","ツチヒラ専用PDF変換"],"設定",["PATHの設定"],"終了"]]
tray = SystemTray(menu=menu,tooltip="タスク管理",single_click_events=False,window=window_1)

#通知有りの処理関数
def message(name,file_name):
    num_1 = len(main("home"))
    if name == "home":
        ui_1 = len(window_1["out_1"].get_list_values())
        if ui_1 < num_1:
            tray.show_message("不具合指示書ファイル追加",f"【コメント有り】フォルダにファイルが追加されました\n {file_name}")

    num_2 = len(main("shusa"))
    if name == "shusa":
        ui_2 = len(window_1["out_2"].get_list_values())
        if ui_2 < num_2:
            tray.show_message("不具合指示書ファイル追加",f"【岩田主査確認】フォルダにファイルが追加されました\n {file_name}")

    num_3 = len(main("butho_mae"))
    if name == "butho_mae":
        ui_3 = len(window_1["out_3"].get_list_values())
        if ui_3 < num_3:
            tray.show_message("不具合指示書ファイル追加",f"【部長(確認前)】フォルダにファイルが追加されました\n {file_name}")

    num_4 = len(main("butho_go"))
    if name == "butho_go":
        ui_4 = len(window_1["out_4"].get_list_values())
        if ui_4 < num_4:
            tray.show_message("不具合指示書ファイル追加",f"【部長(確認済み)】フォルダにファイルが追加されました\n {file_name}")   

    num_5 = len(main("tantou"))
    if name == "tantou":
        ui_5 = len(window_1["out_5"].get_list_values())
        if ui_5 < num_5:
            tray.show_message("不具合指示書ファイル追加",f"【担当者確認】フォルダにファイルが追加されました\n {file_name}")
    
listbox_list = ["out_1", "out_2", "out_3", "out_4", "out_5"]

count = True



while True:
    
    #タイムアウトを設定することで永続的なイベントループが可能となる
    event , values = window_1.read(timeout=400)
    
    #システムトレイのメニューコマンドを使えるようにする記述
    if event == tray.key:
            event = values[event] 


    #下段のcountループよりも先に記載しないとウィンドウクラッシュでエラーになる
    if event in ("test_1", "Quit", None, "終了"): #　×ボタンを押したら終了
        break
    

    #メニューバーのPATHの設定をクリック時にパス設定を開く
    if event == "PATHの設定":
        sisaku_2.sisaku()
   

    #リストボックスの要素が選択されたら"list_out"に表示させる
    for i in listbox_list:
        
        if values[i]:
            name = window_1[i].get()[0]
            window_1["list_out"].update(name)
            
    #フォルダを開くプログラム
    if event == "open_start_1":
        subprocess.Popen(["explorer", file_list["home"]], shell=True)
        continue
    elif event == "open_start_2":
        subprocess.Popen(["explorer", file_list["shusa"]], shell=True)
        continue
    elif event == "open_start_3":
        subprocess.Popen(["explorer", file_list["butho_mae"]], shell=True)
        continue
    elif event == "open_start_4":
        subprocess.Popen(["explorer", file_list["butho_go"]], shell=True)
        continue
    elif event == "open_start_5":
        subprocess.Popen(["explorer", file_list["tantou"]], shell=True)
        continue
    #指示書送付フォルダを開く
    elif event == "指示書送付フォルダ":
        subprocess.Popen(["explorer", file_list["souhu"]], shell=True)
        continue
    
    #ファイルを開くプログラム
    if event == "out_1":
        if values["r1_open"]:
            if bool(window_1["out_1"].get_list_values()) == True: #window["指定のwindow"].get_list_values()でリストボックス内の要素を取得出来る
                jj = os.path.split(main("home")[0])             #window["指定のwindow"].get()で選択されているリストボックスの要素を取得出来る
                name = window_1["out_1"].get()[0] #get()[0]と表記する事でリストボックスの名前を取得出来る[0]を付けないと{"選択要素"}となる
                #os.path.splitext()[1]で選択ファイルの拡張子を取得　拡張子が.pdfであればAcrobatでファイルを開く
                if os.path.splitext(name)[1] == ".pdf":
                    subprocess.Popen([pdf_path, os.path.join(jj[0],name)],shell=True)
                #拡張子が.xls, .xlsxであればExcelでファイルを開く
                elif os.path.splitext(name)[1] == ".xls" or ".xlsx":
                    #os.path.join()でディレクトリpathとファイルpathを結合する
                    subprocess.Popen([excel_path, os.path.join(jj[0],name)], shell=True)

        elif values["r1_send"]:
            #リストボックスの中身が空の場合はsecond_window関数を起動させない様に設定(リストの中が空というエラーが出る)
            if bool(window_1["out_1"].get_list_values()) == True:
                #コメントありのファイルを送る
                win_2 = second_window("home")
                #win_2を要素を選択せずに終了した時にエラーを表示させない為
                if win_2 == []:
                    continue
            
                if win_2[0] == "pop_r1":
                    name = window_1["out_1"].get()[0]
                    shutil.move(os.path.join(file_list["home"],name), file_list["home"])
                        
                elif win_2[0] == "pop_r2":
                    name = window_1["out_1"].get()[0]
                    shutil.move(os.path.join(file_list["home"],name), file_list["shusa"])

                elif win_2[0] == "pop_r3":
                    name = window_1["out_1"].get()[0]
                    shutil.move(os.path.join(file_list["home"],name), file_list["butho_mae"])

                elif win_2[0] == "pop_r4":
                    name = window_1["out_1"].get()[0]
                    shutil.move(os.path.join(file_list["home"],name), file_list["butho_go"])
                        
                elif win_2[0] == "pop_r5":
                    name = window_1["out_1"].get()[0]
                    shutil.move(os.path.join(file_list["home"],name), file_list["tantou"])


        elif values["r1_detail"]:
            if bool(window_1["out_1"].get_list_values()) == True:

                detail_name = window_1["out_1"].get()[0]
                detail_list = select(os.path.join(file_list["home"],detail_name))
                if detail_list == None:
                    window_1["hinban"].update("None")
                    window_1["kataban"].update("None")
                    window_1["torisu"].update("None")
                    window_1["gesan"].update("None")
                    window_1["kakouku"].update("None")
                    window_1["syuuri"].update("None")
                    window_1["kaishi"].update("None")
                    window_1["nouki"].update("None")
                    window_1["tehai_NO"].update("None")
                    window_1["shot_count"].update("None")
                    continue
                else:
                    window_1["hinban"].update(detail_list["品番"])
                    window_1["kataban"].update(detail_list["型番"])
                    window_1["torisu"].update(detail_list["取数"])
                    window_1["gesan"].update(detail_list["月産数"])
                    window_1["kakouku"].update(detail_list["成形加工区"])
                    window_1["syuuri"].update(detail_list["修理メーカー"])
                    window_1["kaishi"].update(detail_list["開始日"])
                    window_1["nouki"].update(detail_list["型納期"])
                    window_1["tehai_NO"].update(detail_list["手配ナンバー"])
                    window_1["shot_count"].update(detail_list["ショットカウンタ"])



    if event == "out_2":
        if values["r2_open"]:
            if bool(window_1["out_2"].get_list_values()) == True:
                jj = os.path.split(main("shusa")[0])
                name = window_1["out_2"].get()[0]
                if os.path.splitext(name)[1] == ".pdf":
                    subprocess.Popen([pdf_path, os.path.join(jj[0],name)],shell=True)
                elif os.path.splitext(name)[1] == ".xls" or ".xlsx":
                    subprocess.Popen([excel_path, os.path.join(jj[0],name)], shell=True)

        elif values["r2_send"]:
            if bool(window_1["out_2"].get_list_values()) == True:
                #コメントありのファイルを送る
                win_2 = second_window("shusa")
                if win_2 == []:
                    continue

                if win_2[0] == "pop_r1":
                    name = window_1["out_2"].get()[0]
                    shutil.move(os.path.join(file_list["shusa"],name), file_list["home"])
                
                elif win_2[0] == "pop_r2":
                    name = window_1["out_2"].get()[0]
                    shutil.move(os.path.join(file_list["shusa"],name), file_list["shusa"])

                elif win_2[0] == "pop_r3":
                    name = window_1["out_2"].get()[0]
                    shutil.move(os.path.join(file_list["shusa"],name), file_list["butho_mae"])

                elif win_2[0] == "pop_r4":
                    name = window_1["out_2"].get()[0]
                    shutil.move(os.path.join(file_list["shusa"],name), file_list["butho_go"])
                    
                elif win_2[0] == "pop_r5":
                    name = window_1["out_2"].get()[0]
                    shutil.move(os.path.join(file_list["shusa"],name), file_list["tantou"])

        elif values["r2_detail"]:
            if bool(window_1["out_2"].get_list_values()) == True:

                detail_name = window_1["out_2"].get()[0]
                detail_list = select(os.path.join(file_list["shusa"],detail_name))
                if detail_list == None:
                    window_1["hinban"].update("None")
                    window_1["kataban"].update("None")
                    window_1["torisu"].update("None")
                    window_1["gesan"].update("None")
                    window_1["kakouku"].update("None")
                    window_1["syuuri"].update("None")
                    window_1["kaishi"].update("None")
                    window_1["nouki"].update("None")
                    window_1["tehai_NO"].update("None")
                    window_1["shot_count"].update("None")
                    continue
                else:
                    window_1["hinban"].update(detail_list["品番"])
                    window_1["kataban"].update(detail_list["型番"])
                    window_1["torisu"].update(detail_list["取数"])
                    window_1["gesan"].update(detail_list["月産数"])
                    window_1["kakouku"].update(detail_list["成形加工区"])
                    window_1["syuuri"].update(detail_list["修理メーカー"])
                    window_1["kaishi"].update(detail_list["開始日"])
                    window_1["nouki"].update(detail_list["型納期"])
                    window_1["tehai_NO"].update(detail_list["手配ナンバー"])
                    window_1["shot_count"].update(detail_list["ショットカウンタ"])



    if event == "out_3":
        if values["r3_open"]:
            if bool(window_1["out_3"].get_list_values()) == True:
                jj = os.path.split(main("butho_mae")[0])
                name = window_1["out_3"].get()[0] #get()[0]と表記する事でリストボックスの名前を取得出来る[0]を付けないと{"選択要素"}となる
                if os.path.splitext(name)[1] == ".pdf":
                    subprocess.Popen([pdf_path, os.path.join(jj[0],name)],shell=True)
                elif os.path.splitext(name)[1] == ".xls" or ".xlsx":
                    subprocess.Popen([excel_path, os.path.join(jj[0],name)], shell=True)
    
        elif values["r3_send"]:
            if bool(window_1["out_3"].get_list_values()) == True:
                #コメントありのファイルを送る
                win_2 = second_window("butho_mae")
                if win_2 == []:
                    continue

                if win_2[0] == "pop_r1":
                    name = window_1["out_3"].get()[0]
                    shutil.move(os.path.join(file_list["butho_mae"],name), file_list["home"])
                
                elif win_2[0] == "pop_r2":
                    name = window_1["out_3"].get()[0]
                    shutil.move(os.path.join(file_list["butho_mae"],name), file_list["shusa"])

                elif win_2[0] == "pop_r3":
                    name = window_1["out_3"].get()[0]
                    shutil.move(os.path.join(file_list["butho_mae"],name), file_list["butho_mae"])

                elif win_2[0] == "pop_r4":
                    name = window_1["out_3"].get()[0]
                    shutil.move(os.path.join(file_list["butho_mae"],name), file_list["butho_go"])
                    
                elif win_2[0] == "pop_r5":
                    name = window_1["out_3"].get()[0]
                    shutil.move(os.path.join(file_list["butho_mae"],name), file_list["tantou"])


        elif values["r3_detail"]:
            if bool(window_1["out_3"].get_list_values()) == True:

                detail_name = window_1["out_3"].get()[0]
                detail_list = select(os.path.join(file_list["butho_mae"],detail_name))
                if detail_list == None:
                    window_1["hinban"].update("None")
                    window_1["kataban"].update("None")
                    window_1["torisu"].update("None")
                    window_1["gesan"].update("None")
                    window_1["kakouku"].update("None")
                    window_1["syuuri"].update("None")
                    window_1["kaishi"].update("None")
                    window_1["nouki"].update("None")
                    window_1["tehai_NO"].update("None")
                    window_1["shot_count"].update("None")
                    continue
                else:
                    window_1["hinban"].update(detail_list["品番"])
                    window_1["kataban"].update(detail_list["型番"])
                    window_1["torisu"].update(detail_list["取数"])
                    window_1["gesan"].update(detail_list["月産数"])
                    window_1["kakouku"].update(detail_list["成形加工区"])
                    window_1["syuuri"].update(detail_list["修理メーカー"])
                    window_1["kaishi"].update(detail_list["開始日"])
                    window_1["nouki"].update(detail_list["型納期"])
                    window_1["tehai_NO"].update(detail_list["手配ナンバー"])
                    window_1["shot_count"].update(detail_list["ショットカウンタ"])


    if event == "out_4":
        if values["r4_open"]:
            if bool(window_1["out_4"].get_list_values()) == True:
                jj = os.path.split(main("butho_go")[0])
                name = window_1["out_4"].get()[0] #get()[0]と表記する事でリストボックスの名前を取得出来る[0]を付けないと{"選択要素"}となる
                if os.path.splitext(name)[1] == ".pdf":
                    subprocess.Popen([pdf_path, os.path.join(jj[0],name)],shell=True)
                elif os.path.splitext(name)[1] == ".xls" or ".xlsx":
                    subprocess.Popen([excel_path, os.path.join(jj[0],name)], shell=True)

        elif values["r4_send"]:
            if bool(window_1["out_4"].get_list_values()) == True:
                #コメントありのファイルを送る
                win_2 = second_window("butho_go")
                if win_2 == []:
                    continue

                if win_2[0] == "pop_r1":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["home"])
                
                elif win_2[0] == "pop_r2":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["shusa"])

                elif win_2[0] == "pop_r3":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["butho_mae"])

                elif win_2[0] == "pop_r4":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["butho_go"])
                    
                elif win_2[0] == "pop_r5":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["tantou"])

                elif win_2[0] == "pop_r6":
                    name = window_1["out_4"].get()[0]
                    shutil.move(os.path.join(file_list["butho_go"],name), file_list["souhu"])

        elif values["r4_detail"]:
            if bool(window_1["out_4"].get_list_values()) == True:

                detail_name = window_1["out_4"].get()[0]
                detail_list = select(os.path.join(file_list["butho_go"],detail_name))
                if detail_list == None:
                    window_1["hinban"].update("None")
                    window_1["kataban"].update("None")
                    window_1["torisu"].update("None")
                    window_1["gesan"].update("None")
                    window_1["kakouku"].update("None")
                    window_1["syuuri"].update("None")
                    window_1["kaishi"].update("None")
                    window_1["nouki"].update("None")
                    window_1["tehai_NO"].update("None")
                    window_1["shot_count"].update("None")
                    continue
                else:
                    window_1["hinban"].update(detail_list["品番"])
                    window_1["kataban"].update(detail_list["型番"])
                    window_1["torisu"].update(detail_list["取数"])
                    window_1["gesan"].update(detail_list["月産数"])
                    window_1["kakouku"].update(detail_list["成形加工区"])
                    window_1["syuuri"].update(detail_list["修理メーカー"])
                    window_1["kaishi"].update(detail_list["開始日"])
                    window_1["nouki"].update(detail_list["型納期"])
                    window_1["tehai_NO"].update(detail_list["手配ナンバー"])
                    window_1["shot_count"].update(detail_list["ショットカウンタ"])


    if event == "out_5":
        if values["r5_open"]:
            if bool(window_1["out_5"].get_list_values()) == True:
                jj = os.path.split(main("tantou")[0])
                name = window_1["out_5"].get()[0] #get()[0]と表記する事でリストボックスの名前を取得出来る[0]を付けないと{"選択要素"}となる
                if os.path.splitext(name)[1] == ".pdf":
                    subprocess.Popen([pdf_path, os.path.join(jj[0],name)],shell=True)
                elif os.path.splitext(name)[1] == ".xls" or ".xlsx":
                    subprocess.Popen([excel_path, os.path.join(jj[0],name)], shell=True)
        
        elif values["r5_send"]:
            if bool(window_1["out_5"].get_list_values()) == True:
                #コメントありのファイルを送る
                win_2 = second_window("tantou")
                if win_2 == []:
                    continue
                
                if win_2[0] == "pop_r1":
                    name = window_1["out_5"].get()[0]
                    shutil.move(os.path.join(file_list["tantou"],name), file_list["home"])
                
                elif win_2[0] == "pop_r2":
                    name = window_1["out_5"].get()[0]
                    shutil.move(os.path.join(file_list["tantou"],name), file_list["shusa"])

                elif win_2[0] == "pop_r3":
                    name = window_1["out_5"].get()[0]
                    shutil.move(os.path.join(file_list["tantou"],name), file_list["butho_mae"])

                elif win_2[0] == "pop_r4":
                    name = window_1["out_5"].get()[0]
                    shutil.move(os.path.join(file_list["tantou"],name), file_list["butho_go"])
                    
                elif win_2[0] == "pop_r5":
                    name = window_1["out_5"].get()[0]
                    shutil.move(os.path.join(file_list["tantou"],name), file_list["tantou"])


        elif values["r5_detail"]:
            if bool(window_1["out_5"].get_list_values()) == True:

                detail_name = window_1["out_5"].get()[0]
                detail_list = select(os.path.join(file_list["tantou"],detail_name))
                if detail_list == None:
                    window_1["hinban"].update("None")
                    window_1["kataban"].update("None")
                    window_1["torisu"].update("None")
                    window_1["gesan"].update("None")
                    window_1["kakouku"].update("None")
                    window_1["syuuri"].update("None")
                    window_1["kaishi"].update("None")
                    window_1["nouki"].update("None")
                    window_1["tehai_NO"].update("None")
                    window_1["shot_count"].update("None")
                    continue
                else:

                    window_1["hinban"].update(detail_list["品番"])
                    window_1["kataban"].update(detail_list["型番"])
                    window_1["torisu"].update(detail_list["取数"])
                    window_1["gesan"].update(detail_list["月産数"])
                    window_1["kakouku"].update(detail_list["成形加工区"])
                    window_1["syuuri"].update(detail_list["修理メーカー"])
                    window_1["kaishi"].update(detail_list["開始日"])
                    window_1["nouki"].update(detail_list["型納期"])
                    window_1["tehai_NO"].update(detail_list["手配ナンバー"])
                    window_1["shot_count"].update(detail_list["ショットカウンタ"])

    #クリアボタンを押すとラジオボタンの入力がキャンセルされる
    if event == "ok_1":
        window_1.FindElement("r1_open").update(False)
        window_1.FindElement("r1_send").update(False)
        window_1.FindElement("r1_detail").update(False)
    
    if event == "ok_2":
        window_1.FindElement("r2_open").update(False)
        window_1.FindElement("r2_send").update(False)
        window_1.FindElement("r2_detail").update(False)

    if event == "ok_3":
        window_1.FindElement("r3_open").update(False)
        window_1.FindElement("r3_send").update(False)
        window_1.FindElement("r3_detail").update(False)

    if event == "ok_4":
        window_1.FindElement("r4_open").update(False)
        window_1.FindElement("r4_send").update(False)
        window_1.FindElement("r4_detail").update(False)

    if event == "ok_5":
        window_1.FindElement("r5_open").update(False)
        window_1.FindElement("r5_send").update(False)
        window_1.FindElement("r5_detail").update(False)    
    
    #list_outの右クリックメニューコピー"が選択されたら中身をコピーする
    if event == "コピー":
        pyperclip.copy("{}".format(values["list_out"]))
    
    #不具合指示書送付、金型修理履歴、手配No.管理表を起動する(ボタン入力があった場合)
    if event == "不具合指示書送付":
        subprocess.Popen([excel_path,ex_souhu_path],shell=True)
    elif event == "金型修理履歴":
        subprocess.Popen([excel_path,ex_lireki_path],shell=True)
    elif event == "手配No.管理表":
        subprocess.Popen([excel_path,ex_kanri_path],shell=True)
    elif event == "ツチヒラ専用PDF変換":
        subprocess.Popen(["start","{0}".format(ts.path("ツチヒラ専用PDF変換"))],shell=True)

    #タイムアウトが発生したタイミングでループ処理を開始する（この処理をしないとリストボックスの要素が選択認識されなかったりする）
    if event == "__TIMEOUT__":
        
        #リストボックスの要素が選択されたらタイムアウトの処理を一度ストップする（リストボックスの要素を選択中にタイムアウトが発生すると選択が解除されたり、選択が先頭になったりする）
        #if bool(window_1["out_1"].get()) or bool(window_1["out_2"].get()) or bool(window_1["out_3"].get()) or bool(window_1["out_4"].get()) or bool(window_1["out_5"].get())== True:
            #window_1.read()
        
        #通知ありのチェックボックスにチェックしたらmessage関数を起動
        for i in listbox_list:
        
            if values[i]:
                name = window_1[i].get()[0]
                if values["ckb_1"] == True:
                    message("home",name)
                if values["ckb_2"] == True:
                    message("shusa",name)
                if values["ckb_3"] == True:
                    message("butho_mae",name)
                if values["ckb_4"] == True:
                    message("butho_go",name)
                if values["ckb_5"] == True:
                    message("tantou",name)

        #メインループ
        if count:
            roop()
        
window_1.close()