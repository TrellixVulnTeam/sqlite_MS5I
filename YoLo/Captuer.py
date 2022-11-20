import cv2
import PySimpleGUI as sg
import os

sg.theme("SystemDefault")
cd = os.getcwd()
sg.set_options(dpi_awareness=True,use_ttk_buttons=True,font="NSimSun")

cap = cv2.VideoCapture(0,)
default_FRAME_HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
default_FRAME_WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

cap.set(cv2.CAP_PROP_FPS, 60) 
cap.set(cv2.CAP_PROP_ISO_SPEED, 10)



lay = [
    [sg.Text("保存するフォルダを指定"),sg.InputText(key="in",default_text=cd),sg.FolderBrowse("選択")],
    [sg.Text("保存するファイル名を指定"),sg.InputText(key="file_name",default_text="img_",size=(40,1))],
    [sg.Text("カメラ設定変更"),sg.Button("設定変更",key="change"),sg.Text("フレームレート"),sg.InputText(size=(5,1),key="FPS"),sg.Text("シャッタースピード"),sg.InputText(size=(5,1),key="ISO_SPEED")],
    [sg.Text("解像度変更"),sg.Text("【高さ】"),sg.InputText(default_text=f"{int(default_FRAME_HEIGHT)}",size=(8,1),key="HEIGHT"),sg.Text("×"),sg.Text("【幅】"),sg.InputText(default_text=f"{int(default_FRAME_WIDTH)}",size=(8,1),key="WIDTH"),sg.Button("解像度変更",key="resize")],
    [sg.Image("",key="IMG")],
    [sg.Button(button_text="画像撮影",key="shot",font=("UD デジタル 教科書体 NK-B",30),button_color="red")],
]
window = sg.Window("",layout=lay)



count = 1
while True:
    event,value = window.read(timeout=0) 
    if event == None:
        break
    
    ret, frame = cap.read()
    #frameをエンコードしないとpysimpleguiに埋め込めない
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window["IMG"].update(imgbytes)
    #cv2.imshow("cap",frame)
    
    #フレームレートを取得してGUIに表示
    window["FPS"].update(cap.get(cv2.CAP_PROP_FPS))
    
    window["ISO_SPEED"].update(cap.get(cv2.CAP_PROP_ISO_SPEED))
    
    key = cv2.waitKey(1) & 0xFF
    
    
    
    #写真撮影
    if event == "shot":
        cv2.imwrite(f"{os.path.join(value['in'],value['file_name'])}{count}.jpg",frame)
        count += 1
    #ブレイク
    if key == ord("q"):
        break
    
    #カメラ設定変更
    if event == "change":
        cap.set(cv2.CAP_PROP_SETTINGS,0)
    
    #解像度変更
    if event == "resize":
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,int(value["HEIGHT"]))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,int(value["WIDTH"]))
        
        default_FRAME_HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        default_FRAME_WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        window["HEIGHT"].update(int(default_FRAME_HEIGHT))
        window["WIDTH"].update(int(default_FRAME_WIDTH))
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.release()#この記述が無いとリサイズ後プログラムが終わらない
cv2.destroyAllWindows()