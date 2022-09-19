import datetime
import PySimpleGUI as sg
import cv2

#参考サイト   https://teratail.com/questions/225414
#            https://pystyle.info/opencv-videoio/
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)

fps = int(cap.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video_{0}.mp4'.format(1), fourcc, fps, (w, h))

lay = [
    [sg.Image("",key="IMAGE")],
    [sg.Button("OK",key="OK")],
]

window = sg.Window("",lay)

def main(name,frame):
# 動画ファイル保存用の設定
    fps = int(cap.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter(r'C:\Users\60837\Desktop\syasin\video_{0}.mp4'.format(name), fourcc, fps, (w, h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    now = datetime.datetime.now()
    TEN=datetime.timedelta(minutes=1)
    while True:
        TT = datetime.datetime.now()
        ret, frame = cap.read()
        cv2.imshow("cap", frame)
        if TT > now + TEN:
            video.write(frame)
            break
 
count=0
while True:
    event,value = window.read(timeout=0)
    if event == None:
        break
    
    ret, frame = cap.read()
    
    if not ret:
        break
    
    imgbytes = cv2.imencode('.png', frame)[1].tobytes()
    window["IMAGE"].update(imgbytes)
    
    video.write(frame)
    
    #cv2.imshow("cap", frame)
    
    #main(count,frame)
    count +=1
    #video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
# 撮影用オブジェクトとウィンドウの解放
cap.release()
cv2.destroyAllWindows()