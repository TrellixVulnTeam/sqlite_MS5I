
import cv2
import datetime
import PySimpleGUI as sg
import os

count = 0

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
    [sg.Text("カメラ設定"),sg.Button("設定変更",key="camera_setting"),sg.Button("異常信号",key="Emergency",button_color=("white","red"),visible=False)],
    [sg.Button("START",button_color=("white","blue"),key="START")],
    #[sg.Radio("START",group_id="A",default=False,key="START",text_color="blue"),sg.Radio("STOP",group_id="A",default=True,key="STOP",text_color="red")],
    [sg.Image("",key="IMAGE")],
]

window = sg.Window("",layout=layout,finalize=True)

# VideoCapture を作成する。
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#解像度変更  
cap.set(cv2.CAP_PROP_FPS, 30) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100) 

def Write_cap ():
    global width,height,fps,fourcc,initial,dir_path
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # VideoWriter を作成する。
    #fourcc = cv2.VideoWriter_fourcc(*"XVID")
    
    fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
    writer = cv2.VideoWriter(f"{count}__{date_name()}.mp4", fourcc, fps, (width, height))
    if count == 0:
        dir_path = os.getcwd()
        initial = f"{count}__{date_name()}.mp4"
    
    return writer

writer = Write_cap()

d = datetime.datetime.now()

file_name = os.listdir()

time_count = 1

while True:
    event,value = window.read()
    if event == None:
        break
    
    
        
    if event == "camera_setting":
        cap.set(cv2.CAP_PROP_SETTINGS,0)
        
  

    
    
    if event =="START":
        
        if value["IN_DIR"] == "":
            sg.popup("保存フォルダを選択してください")
            continue
        
        else:
            while True:
                event,value = window.read(timeout=0)
                
                if event == None:
                    break
                
                if count == 0:
                    #初回ループのみ実施
                    if time_count == 1:
                        dir_first = date_name()
                        os.chdir(value["IN_DIR"])
                        os.mkdir(dir_first)
                        out_dir = os.path.join(os.getcwd(),dir_first)
                        os.chdir(out_dir)
                        time_count += 1
                
                #カメラ設定
                if event == "camera_setting":
                    cap.set(cv2.CAP_PROP_SETTINGS,0)
                    
                window["Emergency"].update(visible=True)
                
                # 1フレームずつ取得する。
                ret, frame = cap.read()
                
                
                
                imgbytes = cv2.imencode('.png', frame)[1].tobytes()
                window["IMAGE"].update(imgbytes)
            
                if not ret:
                    break  # 取得に失敗した場合
                
                
                if ret == True: 
                    
                    writer.write(frame)  
                    if (datetime.datetime.now() -d).seconds >= 6:
                        writer.release()
                        cv2.destroyAllWindows()
                        ret, frame = cap.read()
                        count+=1
                        
                        writer = Write_cap()
                        #writer = cv2.VideoWriter(f"{count}__{date_name()}.mp4", fourcc, fps, (width, height))
                        
                        d = datetime.datetime.now()
                        writer.write(frame)
                        cv2.waitKey(1)
                        
                    
                    #異常信号発生時
                    if event == "Emergency":
                        #os.chdir(value["IN_DIR"])
                        path = os.listdir()
                        #フォルダ内に'Error'フォルダが存在しない場合ディレクトリを作成
                        if "Error" not in path:
                            os.makedirs("Error")
                        
                        
                        
                        continue
            
        #writer.write(frame)
                
    

writer.release()
cap.release()


#最初に作成される動画ファイルを削除する
if (initial in file_name):
    os.chdir(dir_path)
    os.remove(initial)
    
