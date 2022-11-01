
import torch
import PySimpleGUI as sg
import cv2

lay = [
        [sg.Button("START",key="START")],
    ]


        
        

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

 #解像度の設定
cap.set(cv2.CAP_PROP_FPS, 60) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400) 


window =  sg.Window("",lay)

model = torch.hub.load("yolov5", "custom",path="periperi.pt" ,source="local")

#conf 信頼度を設定
model.conf = 0.7

while True:
    event,value = window.read(timeout=0)
    
    if event == None:
        break
    
    # ret = カメラ映像の取得有無 , frame = 取得した画像データ
    ret,frame = cap.read()
    
    #im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #if event == "OK":
    #    results = model(r"C:\Users\60837\Desktop\YoLo\gazou\pos_264.jpg")
    #    print(len(results.xyxy[0])) #or .show() .print() .save() .crop() .pandas()
        
    if event == "START":
        results = model(frame)
        
        #検出個数をコンソールに表示
        print(len(results.xyxy[0]))  #or .show() .print() .save() .crop() .pandas()
        
        # results.xyxy[0]で検出結果を取得
        # iに検出物の座標  confに信頼度を格納
        for *i, conf, cls in results.xyxy[0]:
            cv2.rectangle(
                frame,
                (int(i[0]),int(i[1])),
                (int(i[2]),int(i[3])),
                color = (0,0,255),
                thickness=2
            )
            
            #信頼度を小数点第二位に変換
            lav = "{:.2f}".format(float(conf))
            
            #信頼度を描画する文字枠を作成
            cv2.rectangle(frame, (int(i[0]), int(i[1])-20), (int(i[0])+len(lav)*10, int(i[1])), (0,0,255), -1)
            #信頼度の数値を描画
            cv2.putText(frame, lav, (int(i[0]), int(i[1])-5), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
            
        cv2.imshow("",frame)
        #imshow()のウィンドウをリサイズする　※解像度はそのまま
        #cv2.resizeWindow("",width=200,height=200)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break