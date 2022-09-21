
import cv2
import datetime
import PySimpleGUI as sg
import os

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
    [sg.Text("カメラ設定"),sg.Button("設定変更",key="camera_setting"),sg.Text("FPS変更"),sg.InputText(key="FPS",size=(10,1)),sg.Button("FPS設定変更",key="FPS_change")],
    [sg.Radio("START",group_id="A",default=False,key="START",text_color="blue"),sg.Radio("STOP",group_id="A",default=True,key="STOP",text_color="red")],
    [sg.Image("",key="IMAGE")],
]

window = sg.Window("",layout=layout)

# VideoCapture を作成する。
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#解像度変更  
cap.set(cv2.CAP_PROP_FPS, 50) 
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
    
    
        
    if event == "camera_setting":
        cap.set(cv2.CAP_PROP_SETTINGS,0)
        
        
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    
    
    
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window["IMAGE"].update(imgbytes)
    
    writer.write(frame)
    
    
    
    if not ret:
        break  # 取得に失敗した場合
    
    if value["START"] == True:
        if ret == True:     
            writer.write(frame)  
            if (datetime.datetime.now() -d).seconds >= 60:
                writer.release()
                cv2.destroyAllWindows()
                ret, frame = cap.read()
                count+=1
                writer = cv2.VideoWriter(os.path.join(value["IN_DIR"],f"{count}__{date_name()}.mp4"), fourcc, fps, (width, height))
                
                d = datetime.datetime.now()
                #writer.write(frame)
                #cv2.waitKey(1)
                
                if event == "FPS_change":
                    
                    writer.release()
                    cap.release()
                    cap.set(cv2.CAP_PROP_FPS, int(value["FPS"])) 
                    writer = cv2.VideoWriter(os.path.join(value["IN_DIR"],f"{count}__{date_name()}.mp4"), fourcc, int(value["FPS"]), (width, height))
                    ret, frame = cap.read()
                    writer.wite(frame)
                
                continue
    
    
        
        
    
    
    
     
        
            
    
        
            
            
    
    
    
    
    
    

writer.release()
cap.release()