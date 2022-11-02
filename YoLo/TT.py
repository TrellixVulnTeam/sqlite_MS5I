
import torch
import PySimpleGUI as sg
import cv2
import os

sg.theme("SystemDefault1")

lay = [
        [sg.Button("START",key="START")],
    ]

lay_1 = [
    [sg.Frame("動画",layout=[
        [sg.Image("",key="CAP",size=(300,200))],
    ])]
]

lay_2 = [
    [sg.Frame("画像",layout=[
        [sg.Image("",key="IMG",size=(300,200),right_click_menu=["",["画像を保存"]])],
    ])]
]

lay_3 = [
    [sg.Frame("情報",layout=[
    [sg.Text("検出数"),sg.InputText(size=(10,1), key="hit")],
    [sg.Button("画像取得",key="img_get")],
    
    ])]
]

layout = [lay,lay_1,[sg.Column(lay_2,vertical_alignment="t"),sg.Column(lay_3,vertical_alignment="t")]]
#Column()で列方向のレイアウトを揃える
#vertical_alignment="t"でレイアウトTop合わせにする
        

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

 #解像度の設定
cap.set(cv2.CAP_PROP_FPS, 60) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 750)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500) 


window =  sg.Window("",layout)

model = torch.hub.load("yolov5", "custom",path="periperi.pt" ,source="local")

#画像データを一時的に格納する
img_data = None

#conf 信頼度を設定
model.conf = 0.7

while True:
    event,value = window.read(timeout=0)
    
    if event == None:
        break
    
    
    # ret = カメラ映像の取得有無 , frame = 取得した画像データ
    ret,frame = cap.read()
    
    
    #画像処理を実行する
    def main():
        results = model(frame)
        
        #検出個数を検出
        hit_count= len(results.xyxy[0])
        #print(hit_count)  #or .show() .print() .save() .crop() .pandas()
        
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
        
        #画像を出力前にリサイズする
        h, w = frame.shape[:2]
        height = round(h * (300 / w))
        dst = cv2.resize(frame, dsize=(300, height))
            
        imgbytes = cv2.imencode('.png', dst)[1].tobytes()
        window["IMG"].update(imgbytes)
        window["hit"].update(hit_count)
        
        return frame
    
    
    
    
    
    
    #im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #if event == "OK":
    #    results = model(r"C:\Users\60837\Desktop\YoLo\gazou\pos_264.jpg")
    #    print(len(results.xyxy[0])) #or .show() .print() .save() .crop() .pandas()
    
    
    #動画を出力前にリサイズする
    h, w = frame.shape[:2]
    height = round(h * (500 / w))
    dst_cap = cv2.resize(frame, dsize=(500, height))
    
    #frameをエンコードしないとpysimpleguiに埋め込めない
    imgbytes = cv2.imencode('.png', dst_cap)[1].tobytes()
    window["CAP"].update(imgbytes)
    
    #cv2.imshow("TST",frame)
    
    
    
    if event == "START":
        
        UU = main()
        img_data = UU
        """
        results = model(frame)
        
        #検出個数を検出
        hit_count= len(results.xyxy[0])
        #print(hit_count)  #or .show() .print() .save() .crop() .pandas()
        
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
        
        #画像を出力前にリサイズする
        h, w = frame.shape[:2]
        height = round(h * (300 / w))
        dst = cv2.resize(frame, dsize=(300, height))
            
        imgbytes = cv2.imencode('.png', dst)[1].tobytes()
        window["IMG"].update(imgbytes)
        window["hit"].update(hit_count)
        
        
        
        #cv2.imshow("",frame)
        
        
        #imshow()のウィンドウをリサイズする　※解像度はそのまま
        #cv2.resizeWindow("",width=200,height=200)
    
        """
    
    #画像を保存する
    if event == "画像を保存":
        
        save_dir = sg.popup_get_folder("保存する場所を選択")
        file_name = sg.popup_get_text("ファイル名を入力")
        
        
        
        if save_dir or file_name == None:
            sg.popup_quick_message("画像の保存を中止しました")
            continue
        
        elif save_dir or file_name == "":
            sg.popup_quick_message("入力がありません　保存を中止しました")
            continue
            
        else:
            cv2.imwrite(f"{os.path.join(save_dir, file_name)}.jpg",img_data)
            sg.popup_quick_message("画像を保存しました")
    
    
    