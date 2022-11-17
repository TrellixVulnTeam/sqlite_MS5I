
import torch
import PySimpleGUI as sg
import cv2
import os
import sys
import time

os.environ['BLINKA_FT232H'] = '1'#環境変数設定

from board import *
import digitalio

sg.theme("SystemDefault1")

sg.set_options(use_ttk_buttons=True,dpi_awareness=True)

#IOピンの設定
SW = digitalio.DigitalInOut(D6)
SW.switch_to_input()


def main_act(FPS, width, height, pt_path, conf):

    lay = [
            [sg.Button("実行",key="GO",button_color=("white","red"))],
        ]

    lay_1 = [
        [sg.Frame("動画",layout=[
            [sg.Image("",key="CAP",size=(300,200))],
        ])]
    ]

    lay_2 = [
        [sg.Frame("画像",layout=[
            [sg.Image("",key="IMG",size=(300,200),right_click_menu=["",["画像を保存","画像を表示"]])],
        ])]
    ]

    lay_3 = [
        [sg.Frame("情報",layout=[
        [sg.Text("検出数"),sg.InputText(size=(10,1), key="hit")],
        [sg.Text("型開き信号"),sg.InputText(size=(10,1), key="kata")]
        
        
        ])]
    ]

    layout = [lay,lay_1,[sg.Column(lay_2,vertical_alignment="t"),sg.Column(lay_3,vertical_alignment="t")]]
    #Column()で列方向のレイアウトを揃える
    #vertical_alignment="t"でレイアウトTop合わせにする
            

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    #解像度の設定
    cap.set(cv2.CAP_PROP_FPS, FPS) 
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 


    window_main =  sg.Window("",layout)

    model = torch.hub.load("yolov5", "custom",path= pt_path ,source="local")

    #画像データを一時的に格納する
    img_data = None
    
    #conf 信頼度を設定
    model.conf = conf
    
    
    out_res = None

    while True:
        event,value = window_main.read(timeout=0)
        
        if event == (None) or (sg.WIN_CLOSED):
            break
        
        #型開き限の信号状態
        out_res = SW.value
        window_main["kata"].update(out_res)
        
        # ret = カメラ映像の取得有無 , frame = 取得した画像データ
        ret,frame = cap.read()
        
        
        
        
        #画像処理を実行する
        def main(Frame):
            results = model(Frame)
            
            
            
            #検出個数を検出
            hit_count= len(results.xyxy[0])
            label = results.names[0]
            print(label)
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
                
                val = "{:.2f}".format(float(conf))
                
                #信頼度を小数点第二位に変換
                lav = f"{label}:{val}"#:.2f
                
                #信頼度を描画する文字枠を作成
                cv2.rectangle(frame, (int(i[0]), int(i[1])-20), (int(i[0])+len(lav)*10, int(i[1])), (0,0,255), -1)
                #信頼度の数値を描画
                cv2.putText(frame, lav, (int(i[0]), int(i[1])-5), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, cv2.LINE_AA)
            
            #画像を出力前にリサイズする
            h, w = frame.shape[:2]
            height = round(h * (300 / w))
            dst = cv2.resize(frame, dsize=(300, height))
                
            imgbytes = cv2.imencode('.png', dst)[1].tobytes()
            window_main["IMG"].update(imgbytes)
            window_main["hit"].update(hit_count)
            
            
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
        window_main["CAP"].update(imgbytes)
        
        #型開き限信号　処理
        if SW.value == False:
            main(Frame=frame)
            
        
        
        
        if event == "GO":
            
            UU = main(Frame=frame)
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
            window_main["IMG"].update(imgbytes)
            window_main["hit"].update(hit_count)
            
            
            
            #cv2.imshow("",frame)
            
            
            #imshow()のウィンドウをリサイズする　※解像度はそのまま
            #cv2.resizeWindow_mainwindow_main("",width=200,height=200)
        
            """
            
        
        #画像を保存する
        if event == "画像を保存":
            
            save_dir = sg.popup_get_folder("保存する場所を選択")
            file_name = sg.popup_get_text("ファイル名を入力")
            
            
            
            if (save_dir or file_name) == None:
                
                sg.popup_quick_message("画像の保存を中止しました")
                continue
            
            elif (save_dir or file_name) == "":
                sg.popup_quick_message("入力がありません　保存を中止しました")
                continue
                
            else:
                cv2.imwrite(f"{os.path.join(save_dir, file_name)}.jpg",img_data)
                sg.popup_quick_message("画像を保存しました")
        
        #右クリックメニュー　画像を表示        
        if event == "画像を表示":
            cv2.imshow("cap", img_data)
        
    
    cap.release()#この記述が無いとリサイズ後プログラムが終わらない
            
    window_main.close()
            
        
    
    
            
    
    
    
    




def start_set():
    lay_1 = [
        
        [sg.Frame("解像度設定",layout=[
            [sg.Text("プレームレート(FPS)"),sg.InputText(default_text="60",size=(10,1), key="start_FPS")],
            [sg.Text("画面 幅(width)"),sg.InputText(default_text="750",size=(10,1),key="start_FRAME_WIDTH")],
            [sg.Text("画面 高さ(height)"),sg.InputText(default_text="500",size=(10,1),key="start_FRAME_HEIGHT")],
        ])], ]
    
    lay_2 = [
        [sg.Frame("パラメーター設定",layout=[
            
            [sg.Text("学習ファイルを選択(.pt)"),sg.InputText(key="start_pt",size=(30,1),background_color="yellow"),sg.FileBrowse("選択")],
            [sg.Text("信頼度(conf)"),sg.InputText(default_text="0.5",key="start_conf",size=(10,1))],
            
        ])]
        
    ]
    
    lay_3 = [
        
        [sg.Button("START",key="START",font=("meiryo",20),button_color=("white","blue"),pad=(300,0))],
        
    ],
    
    
    Start_layout =[[sg.Column(lay_1,vertical_alignment="t"),sg.Column(lay_2,vertical_alignment="t")],lay_3]
    
    window = sg.Window("初期設定",Start_layout)
    
    out_list = {}
    
    
    
    
    while True:
        event,value = window.read()
        if event == None:
            sys.exit()
            
        
        if event == "START":
            test_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            ret,frame = test_cap.read()
            
            if ret == False:
                sg.popup("カメラの入力がありません")
                continue
            
            
            if value["start_FPS"] == "":
                sg.popup("未入力の箇所があります")
                continue
            elif value["start_FRAME_WIDTH"] == "":
                sg.popup("未入力の箇所があります")
                continue
            elif value["start_FRAME_HEIGHT"] == "":
                sg.popup("未入力の箇所があります")
                continue
            elif value["start_pt"] == "":
                sg.popup("未入力の箇所があります")
                continue
            elif value["start_conf"] == "":
                sg.popup("未入力の箇所があります")
                continue
            
            
            else:
            
                out_list["FPS"] = int(value["start_FPS"])
                out_list["width"] = int(value["start_FRAME_WIDTH"])
                out_list["height"] = int(value["start_FRAME_HEIGHT"])
                out_list["pt_path"] = value["start_pt"]
                out_list["conf"] = float(value["start_conf"])
                        
            
                
                window.close() #ウィンドウを閉じる
                test_cap.release() #カメラオブジェクトを閉じる
                
                return out_list
            
            
        
                
        
    
init = start_set()    


main_act(FPS=int(init["FPS"]), width=int(init["width"]), height=int(init["height"]), pt_path=init["pt_path"], conf=float(init["conf"]))
