import datetime
from time import time
import cv2
import time


camera = cv2.VideoCapture(0)

def main(name,frame):
# 動画ファイル保存用の設定
    fps = int(camera.get(cv2.CAP_PROP_FPS))                    # カメラのFPSを取得
    w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter(r'C:\Users\60837\Desktop\syasin\video_{0}.mp4'.format(name), fourcc, fps, (w, h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    now = datetime.datetime.now()
    TEN=datetime.timedelta(minutes=1)
    while True:
        TT = datetime.datetime.now()
        ret, frame = camera.read()
        cv2.imshow("camera", frame)
        if TT > now + TEN:
            video.write(frame)
            break
 
count=0
while True:
    ret, frame = camera.read()
    cv2.imshow("camera", frame)
    
    main(count,frame)
    count +=1
    #video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
# 撮影用オブジェクトとウィンドウの解放
camera.release()
cv2.destroyAllWindows()