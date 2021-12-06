import cv2
import numpy as np
import os
import PySimpleGUI as sg

count = 0
sg.set_options(use_ttk_buttons=True)
sg.theme("DarkGrey2")

#カレントディレクトリのパスを取得する
def get_path(path):
    file_list = []
    #カレントディレクトリを移動する
    os.chdir(path)
    #ディレクトリ内のファイルを取得
    file_path = os.listdir(path)
    for i in file_path:
        #絶対パスで表示させる
        x = os.path.abspath(i)
        file_list.append(x)
    
    return file_list

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

#レイアウト
lay = [
    [sg.Text("画像ファイルが格納してあるフォルダを選択してください")],
    [sg.InputText(key="input"), sg.FolderBrowse(button_text="選択")],
    [sg.Text("出力先のフォルダを選択してください")],
    [sg.InputText(key="output"), sg.FolderBrowse(button_text="選択")],
    [sg.Text("出力ファイル名"),sg.InputText(default_text="poslist.txt",size=(20,10),key=("out_name"))],
    [sg.Button("開始",key="bt_start")]
    
]


window = sg.Window("画像　アノテーション　ツール", lay)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "bt_start":
        if value["input"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["output"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["out_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        file_path = get_path(value["input"])
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