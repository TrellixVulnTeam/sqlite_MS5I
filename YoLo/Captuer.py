import cv2
import PySimpleGUI as sg
import os

sg.theme("SystemDefault")
cd = os.getcwd()
sg.set_options(dpi_awareness=True,use_ttk_buttons=True,font="NSimSun")

lay = [
    [sg.Text("保存するフォルダを指定"),sg.InputText(key="in",default_text=cd),sg.FolderBrowse("選択")],
    [sg.Text("ファイル名を指定"),sg.InputText(key="file_name",default_text="img_")],
    [sg.Text("カメラ設定変更"),sg.Button("設定変更",key="change")],
    [sg.Image("",key="IMG")],
    [sg.Button(button_text="画像撮影",key="shot",font=("UD デジタル 教科書体 NK-B",30),button_color="red")],
]
window = sg.Window("",layout=lay)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


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
    key = cv2.waitKey(1) & 0xFF
    #写真撮影
    if event == "shot":
        cv2.imwrite(f"{os.path.join(value['in'],value['file_name'])}{count}.jpg",frame)
        count += 1
    #ブレイク
    if key == ord("q"):
        break
    
    if event == "change":
        cap.set(cv2.CAP_PROP_SETTINGS,0)
    
    