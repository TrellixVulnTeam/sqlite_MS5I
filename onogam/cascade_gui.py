from PySimpleGUI.PySimpleGUI import FolderBrowse
import cv2
import numpy as np
import os
import PySimpleGUI as sg

count = 0
#オプション設定
sg.set_options(use_ttk_buttons=True)
#テーマの設定
sg.theme("DarkGrey2")
#ユーザーセッティング
settings = sg.UserSettings(filename="onogami_test")
settings.load()

#カレントディレクトリのパスを取得する
def get_path(path):
    file_list = []
    #カレントディレクトリを移動する
    os.chdir(path)
    #ディレクトリ内のファイルを取得
    file_path = os.listdir(path)
    #for i in file_path:
        #絶対パスで表示させる
        #x = os.path.abspath(i)
        #file_list.append(x)
    
    return file_path

#画面がぼやけるのを回避するコード
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


num = 1
def main(img_path):
    #写真データ読み込み
    img = cv2.imread(img_path)
    
    pt_1 = []
    pt_2 = [] 
    total = [] 
    num = [0]

    #マウスイベント関数        
    def event_mouse(event, x, y,a,b):
        global  count , aa , bb
        
        count = count

        if event == cv2.EVENT_LBUTTONDOWN:
            count += 1 #左クリックするとcountが1プラスされる
            
            #1クリック目のイベント処理
            if count == 1:
                pt_1.append((x,y))
                total.append(x)
                total.append(y)
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                
                cv2.imshow("",img)
                
            #2クリック目のイベント処理
            if count == 2:
                pt_2.append((x,y))
                total.append(x - pt_1[0][0])
                total.append(y - pt_1[0][1])
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                cv2.rectangle(img, pt_1[0],pt_2[0],(0,0,255),thickness=3)
                cv2.imshow("",img)
                #print(pt_1,pt_2)
                #print(total)
            
                #リセットする
                count = 0
                pt_1.clear()
                pt_2.clear()
                num[0] += 1
                
    
                
        if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
            if count == 0:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
                cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
                cv2.imshow("", img2) 
                
            if count == 1:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.rectangle(img2, pt_1[0], (x,y), (255,0,0),thickness=1)
                #cv2.line(img2, pt_1[0], (x, pt_1[0][1]), (255, 0, 0))
                #cv2.line(img2, pt_1[0], (pt_1[0][0], y), (255, 0, 0))
                cv2.imshow("", img2) 
                
    cv2.imshow("", img)

    #マウスイベント（コールバック関数）を定義
    cv2.setMouseCallback("", event_mouse,)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    return {"total" :total , "num" :num[0]}

#ファイルを一括リネーム
def file_rename(path,cas_name):
    
    count = 1
    file = os.listdir(path)
    
    for zname in file:
        under_name = os.path.splitext(zname)[1] #拡張子取得
        new_name = os.path.join(path,zname) #取得したファイル名を絶対パスに変更
 
        os.rename(new_name,os.path.join(path,f"{cas_name}{count}{under_name}"))#リネーム
        count +=1

#各種設定ウィンドウ
def set():
    
    
    
    layout = [
        [sg.Text("➀作業フォルダを選択してください")],
        [sg.InputText(key="input_path",default_text=settings["file_path"]),sg.FolderBrowse("選択")],
        [sg.Button("設定保存",key="save"),sg.Text("※フォルダ選択後設定保存を押してください",text_color="yellow")],
        [sg.Text("➁各種フォルダを作成"),sg.Button("作成",key="make_bt")],
        [sg.Text("'cascade'フォルダを作成しました",visible=False,key="T_cascade",text_color="blue")],
        [sg.Text("'neg'フォルダを作成しました",visible=False,key="T_neg",text_color="blue")],
        [sg.Text("'pos'フォルダを作成しました",visible=False,key="T_pos",text_color="blue")],
        [sg.Text("'vec'フォルダを作成しました",visible=False,key="T_vec",text_color="blue")],
        
    ]
    
    window = sg.Window("環境設定",layout)
    
    while True:
        event,value = window.read()
        
        def new_folder(path):
            os.chdir(path)
            file_list = os.listdir()
            #指定フォルダの中に["cascade","neg","pos","vec"のフォルダが無ければ新規作成する]
            cascade_j = "cascade" in file_list
            neg_j = "neg" in file_list
            pos_j = "pos" in file_list
            vec_j = "vec" in file_list
            if cascade_j == False:  
                os.mkdir(os.path.join(value["input_path"],"cascade"))
                
                window["T_cascade"].update(visible=True)
                
            if neg_j == False:
                os.mkdir(os.path.join(value["input_path"],"neg"))
                
                window["T_neg"].update(visible=True)
            if pos_j == False:
                os.mkdir(os.path.join(value["input_path"],"pos"))
                
                window["T_pos"].update(visible=True)
            if vec_j == False:
                os.mkdir(os.path.join(value["input_path"],"vec"))
                
                window["T_vec"].update(visible=True)
        
        if event == "make_bt":
            new_folder(value["input_path"])
        
        if event == "save":
            settings["file_path"] = value["input_path"]
        if event == None:
            break


rename = sg.Tab("ファイルリネーム",[
    [sg.Text("ファイル名一括リネームしたいフォルダを選択")],
    [sg.InputText(key="input_1"), sg.FolderBrowse("選択")],
    [sg.Text("ファイル名:"),sg.InputText(default_text="pos_",key="file_name",size=(20,10))],
    [sg.Text("※ファイル名がpos_の場合pos_1,pos_2という様になります",text_color="yellow",)],
    [sg.Button("開始",key="bt_start_1")],
    
])

#レイアウト
pos_file = sg.Tab("poslistファイル作成",[
    [sg.Text("画像ファイルが格納してあるフォルダを選択してください")],
    [sg.InputText(key="input_2"), sg.FolderBrowse(button_text="選択")],
    [sg.Text("出力先のフォルダを選択してください")],
    [sg.InputText(key="output"), sg.FolderBrowse(button_text="選択")],
    [sg.Text("出力ファイル名"),sg.InputText(default_text="poslist.txt",size=(20,10),key=("out_name"))],
    [sg.Button("開始",key="bt_start_2")],
    [sg.Menu(menu_definition=[["設定","設定"]],background_color="white")],
    
])


fin =[[ sg.TabGroup([[rename,pos_file]]),]]

window = sg.Window("画像　アノテーション　ツール",layout=fin,finalize=True,)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "設定":
        set()
    
    if event == "bt_start_1":
        if value["input_1"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["file_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        print(settings["file_path"])
        file_rename(value["input_1"],value["file_name"])
        
    if event == "bt_start_2":
        if value["input_2"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["output"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["out_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        file_path = get_path(value["input_2"])
        lec = ""
        #メイン
        for i in file_path:
            mes = main(i)
            total = mes["total"]
            num = mes["num"]
            for ff in total:
                lec = lec + f" {ff}"
            final = f"{num}",lec
            #テキストファイルに書き込み
            file_name = os.path.join(value["output"],value["out_name"])
            f = open(file_name, "a")
            f.write(f"{i} {final[0]}{final[1]}\n")
            f.close()
            #lecをクリア
            lec = ""
    