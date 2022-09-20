
import cv2
import datetime
import PySimpleGUI as sg

count = 1

sg.theme("SystemDefaultForReal")
sg.set_options(dpi_awareness=True,use_ttk_buttons=True)

#ファイル名（日付）
def date_name():
    DD = datetime.datetime.now()
    Year = DD.year
    Month = DD.month
    Day = DD.day
    Hour = DD.hour
    Minute = DD.minute
    Second = DD.second
    
    Out_name = f"{Year}_{Month}_{Day}_{Hour}_{Minute}_{Second}"
    return Out_name


layout = [
    [sg.Text("動画保存先フォルダ"),sg.InputText(key="IN_DIR",size=(20,1)),sg.FolderBrowse("選択")],
    [sg.Radio("START",group_id="A",default=False,key="START",text_color="blue"),sg.Radio("STOP",group_id="A",default=True,key="STOP",text_color="red")],
    [sg.Image("",key="IMAGE")],
]

window = sg.Window("",layout=layout)

# VideoCapture を作成する。
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#解像度変更  
cap.set(cv2.CAP_PROP_FPS, 30) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100) 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# VideoWriter を作成する。
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
writer = cv2.VideoWriter(f"{count}__{date_name()}.mp4", fourcc, fps, (width, height))

d = datetime.datetime.now()
while True:
    event,value = window.read(timeout=0)
    if event == None:
        break
    # 1フレームずつ取得する。
    
    
    
    if value["START"] == True:
        ret, frame = cap.read()
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        window["IMAGE"].update(imgbytes)
        
        if not ret:
            break  # 取得に失敗した場合
        if ret == True:
            writer.write(frame)
            
            if (datetime.datetime.now() -d).seconds >= 6:
                writer.release()
                count+=1
                writer = cv2.VideoWriter(f"{count}__{date_name()}.mp4", fourcc, fps, (width, height))
                
                d = datetime.datetime.now()
                writer.write(frame)
                
                continue
            
            
    
    
    
    
    
    

writer.release()
cap.release()