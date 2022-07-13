
import cv2
import PySimpleGUI as sg

import os
import numpy as np

#画像分類実行
def main_start(cascade_file, img_path):
    # カスケード分類器を読み込む
    
    cascade = cv2.CascadeClassifier(r"{}".format(cascade_file))
    
    # 入力画像の読み込み&グレースケール変換
    #img = cv2.imread(r"{}".format(img_path))
    #numpyで開く事で日本語を含むpathを通す(opencvは日本語pathに対応していない)
    buf = np.fromfile(r"{}".format(img_path), np.uint8)
    img = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED) 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    # "▲"を物体検出する
    triangle = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    uui = np.array(triangle).any()

    
    # 検出した領域を赤色の矩形で囲む
    for (x, y, w, h) in triangle:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)
    

 
    
    # 結果画像を保存
    #cv2.imwrite("result_triangle.jpg",img)
    #img = cv2.resize(img, dsize=(200,200)) #リサイズ
    #with tempfile.NamedTemporaryFile(delete=True) as tf:
    #    cv2.imwrite(f"{tf.name}.jpg", img)
        
    #    tf.seek(0)
    #    os.chdir(os.path.split(tf.name)[0])
    #    iii = cv2.imread(f"{tf.name}.jpg")

        
    
    
    #結果画像を表示
    cv2.imshow('image', img)

    # 何かのキーを押したら処理を終了させる
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
        #out = os.path.join(os.path.split(tf.name)[0],f"{tf.name}.jpg")
        
        #return out
    


#画像分類実行
def folder_start(cascade_file, folder_path):
    # カスケード分類器を読み込む
    
    cascade = cv2.CascadeClassifier(r"{}".format(cascade_file))
    
    #カレントディレクトリを移動する
    os.chdir(folder_path)
    
    #結果を格納する二次元配列
    act_list = [[]]
    
    file_list = os.listdir(folder_path)
    lsiin = [s for s in file_list if ".txt" not in s] #poslist.txt以外をリストに格納
    for file in lsiin:
        
    
        # 入力画像の読み込み&グレースケール変換
        #img = cv2.imread(r"{}".format(folder_path))
        #numpyで開く事で日本語を含むpathを通す(opencvは日本語pathに対応していない)
        buf = np.fromfile(r"{}".format(file), np.uint8)
        img = cv2.imdecode(buf, cv2.IMREAD_UNCHANGED) 
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        # "▲"を物体検出する
        triangle = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
        
        #cascade分類機にて検知したか判定
        uui = np.array(triangle).any() #二次元配列はbool関数で処理出来ない為arrayに一度変換
        result_file = bool(uui)

        #tableに表示する二次元配列を作成
        act_list.append(["{}".format(file),"{}".format(result_file)])
        
        
        # 検出した領域を赤色の矩形で囲む
        for (x, y, w, h) in triangle:
            cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)
        
        #結果画像を表示
       # cv2.imshow('image', img)

        # 何かのキーを押したら処理を終了させる
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    
    #初期値の空欄を削除する
    act_list.pop(0)
    
    return act_list




sg.theme("Default")
sg.set_options(use_ttk_buttons=True, dpi_awareness=True,font=('Meiryo UI',9))
   
   
lay = [
    [sg.Text("1.カスケードファイルを選択")],
    [sg.InputText(tooltip="カスケードファイルを選択",key="input_cascade"),sg.FileBrowse("選択")],
    [sg.Text("2.処理画像フォルダを選択")],
    [sg.InputText(key="folder_path"),sg.FolderBrowse("選択")],
    [sg.Button("START", key="start")],
    [sg.Table(values=[],headings=["ファイル名","結果"],auto_size_columns=False,key="table",
              def_col_width=20,)],
    [sg.Text("検知画像数"),sg.InputText(key="true",size=(5,1)),sg.Text("未検知画像数"),sg.InputText(key="false",size=(5,1))],
    [sg.Button("選択画像を表示",key="OPEN")],
]




window = sg.Window("",lay)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "start":
        
        if value["input_cascade"] == "":
            sg.popup("カスケードファイルを選択して下さい")
            continue
        if value["folder_path"] == "":
            sg.popup("フォルダを選択して下さい")
            continue
        
        result_list = [[]]
        
        Folder_start = folder_start(cascade_file=value["input_cascade"],folder_path=value["folder_path"])
        
        
        #検知数と未検知数を検出する
        Detection = []
        for i in Folder_start:
            Detection.append(i[1])
        #検知画像数   
        True_count = Detection.count("True")
        #未検知画像数
        False_count = len(Detection) - int(True_count)
        
        window["true"].update(True_count)
        window["false"].update(False_count)

        
        #テーブルに反映させる様にする
        window["table"].update(Folder_start)
        
        
   
        
    if event == "OPEN":
        if value["table"] == []:
            sg.popup("選択してください")
            continue
        
        #tableの全データを二次元配列で取得
        out_table = window["table"].get()
        
        #tableからファイル名を取得
        table_file_name = out_table[value["table"][0]][0]
        
        main_start(cascade_file=value["input_cascade"],img_path=table_file_name)
        #sg.execute_command_subprocess("start",table_file_name)