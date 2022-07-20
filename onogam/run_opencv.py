
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
    return img
#画像分類実行
def main_start_img(cascade_file, img_path):
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
    #cv2.imshow('image', img)

    # 何かのキーを押したら処理を終了させる
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
        
        #out = os.path.join(os.path.split(tf.name)[0],f"{tf.name}.jpg")
        
        #return out
    return img
    


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





sg.set_options( dpi_awareness=True,font=('Meiryo UI',9),use_ttk_buttons=True)
sg.theme("LightGrey1")
theme_list = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
  
lay_1 = [
    [sg.Text("1.カスケードファイルを選択")],
    [sg.InputText(tooltip="カスケードファイルを選択",key="input_cascade"),sg.FileBrowse("選択",)],
    [sg.Text("2.処理画像フォルダを選択")],
    [sg.InputText(key="folder_path"),sg.FolderBrowse("選択")],
    [sg.Button("START", key="start")],
    [sg.Table(values=[],headings=["ファイル名","結果"],auto_size_columns=False,key="table",
              def_col_width=20,)],
    [sg.Text("検知画像数"),sg.InputText(key="true",size=(5,1)),sg.Text("未検知画像数"),sg.InputText(key="false",size=(5,1)),sg.Text("正解比率"),sg.InputText(key="probability",size=(5,1))],
    [sg.Button("選択画像を表示",key="OPEN")],
]

lay_2 = [
    [sg.Text("1.カスケードファイルを選択")],
    [sg.InputText(tooltip="カスケードファイルを選択",key="input_cascade_file"),sg.FileBrowse("選択")],
    [sg.Text("2.処理画像を選択")],
    [sg.InputText(key="file_path"),sg.FileBrowse("選択")],
    [sg.Button("START", key="start_file")],
    [sg.Image(key="image",size=(350,250))],
]

layout = [
    
    [sg.TabGroup(
        [[
            sg.Tab("フォルダ内全て",lay_1),
            sg.Tab("ファイル単体",lay_2),

            ]],
    
        )]
    ]


window = sg.Window("画像検知",layout,ttk_theme="clam",)

while True:
    
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "start":
        
        if value["input_cascade"] == "":
            #sg.popup("カスケードファイルを選択して下さい")
            continue
        if value["folder_path"] == "":
            #sg.popup("フォルダを選択して下さい")
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
        #正解比率計算
        probability_value = True_count / len(Detection)
        
        window["true"].update(True_count)
        window["false"].update(False_count)
        #"{:.2f}".format(対象の値)fの前の数字を指定する事で表示する小数点以下の桁数を指定できる
        window["probability"].update("{:.2f}".format(probability_value))

        
        #テーブルに反映させる様にする
        window["table"].update(Folder_start)
        
        
   
        
    if event == "OPEN":
        if value["table"] == []:
            #sg.popup("選択してください")
            continue
        
        #tableの全データを二次元配列で取得
        out_table = window["table"].get()
        
        #tableからファイル名を取得
        table_file_name = out_table[value["table"][0]][0]
        
        main_start(cascade_file=value["input_cascade"],img_path=table_file_name)
        #sg.execute_command_subprocess("start",table_file_name)
        
    if event == "start_file":
        if value["input_cascade_file"] == "":
            #sg.popup("カスケードファイルを選択してください")
            continue
        if value["file_path"] == "":
            #sg.popup("画像を選択してください",)
            continue
        else:
            IMG =main_start_img(cascade_file=value["input_cascade_file"],img_path=value["file_path"])
            imgbytes = cv2.imencode('.png', IMG)[1].tobytes() 
            window["image"].update(source = imgbytes,size=(350,250),subsample=2)
            
    
        