import cv2
import PySimpleGUI as sg
import tempfile

#画像分類実行
def main_start(cascade_file, img_path):
    # カスケード分類器を読み込む
    cascade = cv2.CascadeClassifier(r"{}".format(cascade_file))

    # 入力画像の読み込み&グレースケール変換
    img = cv2.imread(r"{}".format(img_path))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # "▲"を物体検出する
    triangle = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # 検出した領域を赤色の矩形で囲む
    for (x, y, w, h) in triangle:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

    # 結果画像を保存
    #cv2.imwrite("result_triangle.jpg",img)
    

    
    #結果画像を表示
    cv2.imshow('image', img)

    # 何かのキーを押したら処理を終了させる
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return img
    

sg.theme("Default")

   
   
lay = [
    [sg.Text("1.カスケードファイルを選択")],
    [sg.InputText(tooltip="カスケードファイルを選択",key="input_cascade"),sg.FileBrowse("選択")],
    [sg.Text("2.画像を選択")],
    [sg.InputText(tooltip="画像認識する画像を選択",key="img_path"),sg.FileBrowse("選択")],
    [sg.Button("START", key="start")],
    [sg.Image("",key="image",)],
]




window = sg.Window("",lay)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "start":
        img = main_start(cascade_file=value["input_cascade"],img_path=value["img_path"])
        window["image"].update(img)