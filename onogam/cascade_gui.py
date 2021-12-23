import cv2
import numpy as np
import os
import PySimpleGUI as sg
import shutil

count = 0
#オプション設定
sg.set_options(use_ttk_buttons=True,
               dpi_awareness=True, #画面のぼやけを無くす
               font=("meiryo",10) #フォントを指定
              )
#テーマの設定
sg.theme("DarkGrey2")
#ユーザーセッティング
settings = sg.UserSettings(filename="set_path",path= os.path.split(__file__)[0])
settings.load()

#指定したフォルダ内のファイル名を取得
def get_path_pos(path):
    file_list = []
    #カレントディレクトリを移動する
    os.chdir(path)
    #ディレクトリ内のファイルを取得
    file_path = os.listdir(path)
    
    return file_path
        
#指定したフォルダ内のファイル名を絶対パスで取得
def get_path_neg(path):
    file_list = []
    #カレントディレクトリを移動する
    os.chdir(path)
    #ディレクトリ内のファイルを取得
    file_path = os.listdir(path)
    for i in file_path:
        #絶対パスで表示させる
        x = os.path.abspath(i)
        file_list.append(x)
    
    return file_list

#ベクトルファイル作成
def vec_make(path):
    os.chdir(path)
    sg.execute_command_subprocess("start","opencv_createsamples.exe -info pos/poslist.txt -vec vec/positive.vec -num 1000")
    



num = 1
def main(img_path):
    #写真データ読み込み
    img = cv2.imread(img_path)
    
    pt_1 = []
    pt_2 = [] 
    total = [] 
    num = [0]

    #マウスイベント関数        
    def event_mouse(event, x, y,a,b):
        global  count , aa , bb
        
        count = count

        if event == cv2.EVENT_LBUTTONDOWN:
            count += 1 #左クリックするとcountが1プラスされる
            
            #1クリック目のイベント処理
            if count == 1:
                pt_1.append((x,y))
                total.append(x)
                total.append(y)
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                
                cv2.imshow("",img)
                
            #2クリック目のイベント処理
            if count == 2:
                pt_2.append((x,y))
                total.append(x - pt_1[0][0])
                total.append(y - pt_1[0][1])
                cv2.circle(img, (x,y), 1,(255,0,0),thickness=2)
                cv2.rectangle(img, pt_1[0],pt_2[0],(0,0,255),thickness=3)
                cv2.imshow("",img)
                #print(pt_1,pt_2)
                #print(total)
            
                #リセットする
                count = 0
                pt_1.clear()
                pt_2.clear()
                num[0] += 1
                
    
                
        if event == cv2.EVENT_MOUSEMOVE:  # マウスが移動したときにx線とy線を更新する
            if count == 0:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.line(img2, (x, 0), (x, h - 1), (255, 0, 0))
                cv2.line(img2, (0, y), (w - 1, y), (255, 0, 0))
                cv2.imshow("", img2) 
                
            if count == 1:
                
                img2 = np.copy(img)
                h, w = img2.shape[0], img2.shape[1]
                cv2.rectangle(img2, pt_1[0], (x,y), (255,0,0),thickness=1)
                #cv2.line(img2, pt_1[0], (x, pt_1[0][1]), (255, 0, 0))
                #cv2.line(img2, pt_1[0], (pt_1[0][0], y), (255, 0, 0))
                cv2.imshow("", img2) 
                
    cv2.imshow("", img)

    #マウスイベント（コールバック関数）を定義
    cv2.setMouseCallback("", event_mouse,)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
    return {"total" :total , "num" :num[0]}

#ファイルを一括リネーム
def file_rename(path,cas_name):
    
    count = 1
    file = os.listdir(path)
    
    for zname in file:
        under_name = os.path.splitext(zname)[1] #拡張子取得
        new_name = os.path.join(path,zname) #取得したファイル名を絶対パスに変更
 
        os.rename(new_name,os.path.join(path,f"{cas_name}{count}{under_name}"))#リネーム
        count +=1





#各種設定ウィンドウ
def set():
    
    
    
    layout = [
        [sg.Text("➀作業フォルダを選択してください",text_color="#ff00ff")],
        [sg.InputText(key="input_path",default_text=settings["file_path"]),sg.FolderBrowse("選択")],
        [sg.Text("➁各種フォルダを作成",text_color="#ff00ff"),sg.Button("作成",key="make_bt")],
        [sg.Text("'cascade'フォルダを作成しました",visible=False,key="T_cascade",text_color="#00bfff")],
        [sg.Text("'neg'フォルダを作成しました",visible=False,key="T_neg",text_color="#00bfff")],
        [sg.Text("'pos'フォルダを作成しました",visible=False,key="T_pos",text_color="#00bfff")],
        [sg.Text("'vec'フォルダを作成しました",visible=False,key="T_vec",text_color="#00bfff")],
        [sg.Text("➂PATHの設定",text_color="#ff00ff")],
        [sg.Text("使用環境のbit数を選択して下さい")],
        [sg.Radio("64bit","A",text_color="#00bfff",key="64bit",enable_events=True),sg.Radio("32bit","A",text_color="#00bfff",key="32bit",enable_events=True)],
        [sg.pin(sg.Frame("64bit",layout=[
            [sg.Text("opencv_createsamples.exeのpathを選択"),sg.InputText(default_text=settings["createsamples_path"],key=("createsamples_path"),size=(20,10)),sg.FileBrowse("選択")],
            [sg.Text("opencv_traincascade.exeのpathを選択"),sg.InputText(default_text=settings["traincascade_path"],key=("traincascade_path"),size=(20,10)),sg.FileBrowse("選択")],
            [sg.Text("opencv_world3416.dllのpathを選択"),sg.InputText(settings["world3416_path"],key=("world3416_path"),size=(20,10)),sg.FileBrowse("選択")],
        ],title_color="#00bfff",visible=False,key="64bit_frame"))],
        
        [sg.pin(sg.Frame("32bit",layout=[
            [sg.Text("各種ファイルフォルダを選択"),sg.InputText(default_text=settings["32bit_path"],key="32bit_path",size=(20,10)),sg.FolderBrowse("選択")],
        ],title_color="#00bfff",visible=False,key="32bit_frame"))],
       
        [sg.Button("設定保存",key="save"),sg.Text("※フォルダ選択後設定保存を押してください",text_color="yellow")],
    ]
    
    window = sg.Window("環境設定",layout)
    
    while True:
        event,value = window.read()
        #初期設定フォルダを作成する関数
        def new_folder(path):
            os.chdir(path)
            file_list = os.listdir()
            #指定フォルダの中に["cascade","neg","pos","vec"のフォルダが無ければ新規作成する]
            cascade_j = "cascade" in file_list
            neg_j = "neg" in file_list
            pos_j = "pos" in file_list
            vec_j = "vec" in file_list
            if cascade_j == False:  
                os.mkdir(os.path.join(value["input_path"],"cascade"))
                
                window["T_cascade"].update(visible=True)
                
            if neg_j == False:
                os.mkdir(os.path.join(value["input_path"],"neg"))
                
                window["T_neg"].update(visible=True)
            if pos_j == False:
                os.mkdir(os.path.join(value["input_path"],"pos"))
                
                window["T_pos"].update(visible=True)
            if vec_j == False:
                os.mkdir(os.path.join(value["input_path"],"vec"))
                
                window["T_vec"].update(visible=True)
        
        #フォルダ作成ボタンを押したときの処理
        if event == "make_bt":
            if value["input_path"] == "":
                sg.popup("作業フォルダを選択してください")
                continue
            elif value["createsamples_path"] == "":
                sg.popup("opencv_createsamples.exeのpathを選択してください")
                continue
            elif value["traincascade_path"] == "":
                sg.popup("opencv_traincascade.exeのpathを選択してください")
                continue
            elif value["world3416_path"] == "":
                sg.popup("opencv_world3416.dllのpathを選択してください")
                continue
            new_folder(value["input_path"])
            
        #ラジオボタンでビット数選択した時の処理
        if event == "64bit":
            window["32bit_frame"].update(visible=False)
            window["64bit_frame"].update(visible=True)
            
            if event == "save":
                if value["input_path"] == "":
                    sg.popup("作業フォルダを選択してください")
                    continue
                elif value["createsamples_path"] == "":
                    sg.popup("opencv_createsamples.exeのpathを選択してください")
                    continue
                elif value["traincascade_path"] == "":
                    sg.popup("opencv_traincascade.exeのpathを選択してください")
                    continue
                elif value["world3416_path"] == "":
                    sg.popup("opencv_world3416.dllのpathを選択してください")
                    continue
                
                #設定の保存
                settings["file_path"] = value["input_path"]
                settings["createsamples_path"] = value["createsamples_path"]
                settings["traincascade_path"] = value["traincascade_path"]
                settings["world3416_path"] = value["world3416_path"]
                #作業フォルダにopencv_createsamples.exe, opencv_traincascade.exe, opencv_world3416.dllをコピーする
                shutil.copyfile(settings["createsamples_path"],os.path.join(settings["file_path"],os.path.split(settings["createsamples_path"])[1]))
                shutil.copyfile(settings["traincascade_path"],os.path.join(settings["file_path"],os.path.split(settings["traincascade_path"])[1]))
                shutil.copyfile(settings["world3416_path"],os.path.join(settings["file_path"],os.path.split(settings["world3416_path"])[1]))
        
        
        
        elif event == "32bit":
            window["64bit_frame"].update(visible=False)
            window["32bit_frame"].update(visible=True)
        #設定保存ボタンを押したときの処理
        if event == "save":
            if value["input_path"] == "":
                sg.popup("作業フォルダを選択してください")
                continue
        #    elif value["createsamples_path"] == "":
        #        sg.popup("opencv_createsamples.exeのpathを選択してください")
        #        continue
        #    elif value["traincascade_path"] == "":
        #        sg.popup("opencv_traincascade.exeのpathを選択してください")
        #        continue
        #   elif value["world3416_path"] == "":
        #        sg.popup("opencv_world3416.dllのpathを選択してください")
        #        continue
            
            settings["file_path"] = value["input_path"]
            settings["createsamples_path"] = value["createsamples_path"]
            settings["traincascade_path"] = value["traincascade_path"]
            settings["world3416_path"] = value["world3416_path"]
            settings["32bit_path"] = value["32bit_path"]
            #作業フォルダにopencv_createsamples.exe, opencv_traincascade.exe, opencv_world3416.dllをコピーする
            #shutil.copyfile(settings["createsamples_path"],os.path.join(settings["file_path"],os.path.split(settings["createsamples_path"])[1]))
            #shutil.copyfile(settings["traincascade_path"],os.path.join(settings["file_path"],os.path.split(settings["traincascade_path"])[1]))
            #shutil.copyfile(settings["world3416_path"],os.path.join(settings["file_path"],os.path.split(settings["world3416_path"])[1]))
            
            def bit32_file_get(f_path):#32bitファイルフォルダの中身を作業フォルダへコピーする
                file_path = os.listdir(f_path)
                
                for i in file_path:
                    shutil.copyfile(os.path.join(f_path,i),os.path.join(settings["file_path"],i))
                    
            #bit32_file_get(settings["32bit_path"])
        
            
                    
        
        
        
        if event == None:
            break


rename = sg.Tab("ステップ➀",[
    [sg.Frame("ファイルリネーム",layout=[
    [sg.Text("ファイル名一括リネームしたいフォルダを選択")],
    [sg.InputText(key="input_rename"), sg.FolderBrowse("選択")],
    [sg.Text("ファイル名:"),sg.InputText(default_text="pos_",key="file_name",size=(20,10))],
    [sg.Text("※ファイル名がpos_の場合pos_1,pos_2という様になります",text_color="yellow",)],
    [sg.Button("開始",key="bt_start_rename"),sg.Text("処理が完了しました",key="rename_end",text_color="#00bfff",visible=False)],
    ])],
    [sg.Frame("neglist作成",layout=[
        [sg.Text("画像ファイルが格納してあるフォルダを選択してください")],
        [sg.InputText(key="input_neg"), sg.FolderBrowse(button_text="選択")],
        [sg.Text("出力先のフォルダを選択してください")],
        [sg.InputText(key="output_neg"), sg.FolderBrowse(button_text="選択")],
        [sg.Text("出力ファイル名"),sg.InputText(default_text="neglist.txt",size=(20,10),key=("neg_name"))],
        [sg.Button("作成",key="bt_start_neg"),sg.Text("処理が完了しました",key="neg_end",text_color="#00bfff",visible=False)],
        []
    ])],
])

#レイアウト
pos_file = sg.Tab("ステップ➁",[
    [sg.Frame("poslist作成",layout=[
        [sg.Text("画像ファイルが格納してあるフォルダを選択してください")],
        [sg.InputText(key="input_pos"), sg.FolderBrowse(button_text="選択")],
        [sg.Text("出力先のフォルダを選択してください")],
        [sg.InputText(key="output_pos"), sg.FolderBrowse(button_text="選択")],
        [sg.Text("出力ファイル名"),sg.InputText(default_text="poslist.txt",size=(20,10),key=("pos_name"))],
        [sg.Button("作成",key="bt_start_pos"),sg.Text("処理が完了しました",key="pos_end",text_color="#00bfff",visible=False)],
        [sg.Menu(menu_definition=[["設定","環境設定"]],background_color="white")]],)],
    [sg.Frame("vecファイル作成",layout=[
        [sg.Text("poslistを選択してください")],
        [sg.InputText(key="poslist_path"),sg.FileBrowse("選択")],
        [sg.Button("作成",key="bt_start_vec"),sg.Text("処理が完了しました",key="vec_end",text_color="#00bfff",visible=False)]
    ])]
    
    
    
])

fin =[[ sg.TabGroup([[rename,pos_file]]),]]

window = sg.Window("画像　アノテーション　ツール",layout=fin,finalize=True,)

while True:
    event,value = window.read()
    
    if event == None:
        break
    
    if event == "環境設定":
        set()
    #リネーム処理
    if event == "bt_start_rename":
        if value["input_rename"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["file_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        print(settings["file_path"])
        file_rename(value["input_rename"],value["file_name"])
        window["rename_end"].update(visible = True)
        
    #neglist作成
    if event == "bt_start_neg":
        if value["input_neg"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["output_neg"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["neg_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        
        file_path = get_path_neg(value["input_neg"])
        #フォルダ内にテキストファイルがあるか判定しある場合は処理を中断する
        neg_file_name = ".txt" in f"{file_path}"
        if neg_file_name == True:
            sg.popup(".txtファイルが存在します")
            pass
        else: #テキストファイルが存在しなければ通常通り処理をする
            for i in file_path:
                
                #テキストファイルに書き込み
                file_name = os.path.join(value["output_neg"],value["neg_name"])
                f = open(file_name, "a")
                f.write(f"{i}\n")
                f.close()
                window["neg_end"].update(visible = True)
            
    
    #poslist作成    
    if event == "bt_start_pos":
        if value["input_pos"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["output_pos"] == "":
            sg.popup("選択されていない項目があります")
            continue
        if value["pos_name"] == "":
            sg.popup("選択されていない項目があります")
            continue
        file_path = get_path_pos(value["input_pos"])
        lec = ""
        #メイン
        for i in file_path:
            mes = main(i)
            total = mes["total"]
            num = mes["num"]
            for ff in total:
                lec = lec + f" {ff}"
            final = f"{num}",lec
            #テキストファイルに書き込み
            file_name = os.path.join(value["output_pos"],value["pos_name"])
            f = open(file_name, "a")
            f.write(f"{i} {final[0]}{final[1]}\n")
            f.close()
            #lecをクリア
            lec = ""
        window["pos_end"].update(visible = True)
        
    
    #ベクトルファイル作成
    if event == "bt_start_vec":
        
        vec_make(settings["file_path"])