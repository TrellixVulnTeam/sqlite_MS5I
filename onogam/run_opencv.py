
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

    print(bool(uui))
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
    

sg.theme("Default")
sg.set_options(use_ttk_buttons=True, dpi_awareness=True,font=('Meiryo UI',9))
   
   
lay = [
    [sg.Text("1.カスケードファイルを選択")],
    [sg.InputText(tooltip="カスケードファイルを選択",key="input_cascade"),sg.FileBrowse("選択")],
    [sg.Text("2.画像を選択")],
    [sg.InputText(tooltip="画像認識する画像を選択",key="img_path"),sg.FileBrowse("選択")],
    [sg.Button("START", key="start")],
    [sg.Image(r"",key="image",size=(300,300))],
]




window = sg.Window("",lay)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "start":
        img = main_start(cascade_file=value["input_cascade"],img_path=value["img_path"])
        
        #window["image"].update(img)